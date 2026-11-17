# Laboratorio 10 – Diseñar e implementar pipelines de datos con Azure Databricks

**Curso:** DP-750 – Implement Data Engineering Solutions using Azure Databricks
**Autor:** Héctor Miguel Tudela
**Laboratorio:** [Lab 10 – Microsoft Learning](https://microsoftlearning.github.io/DP-750T00-Implement-Data-Engineering-Solutions-using-Azure-Databricks/Instructions/Labs/10-design-implement-data-pipelines.html)

---

## Escenario

Data engineer en **GlobStay**, un grupo hotelero con cinco propiedades. Su pipeline batch nocturno ingiere reservas en bruto, las limpia y valida, y genera analítica de ingresos. En este laboratorio se construye un pipeline **Bronze → Silver → Gold** en Unity Catalog, se parametrizan notebooks, se añade gestión de errores y se orquesta todo con un **Lakeflow Job** con ramificación condicional.

## Requisitos

- Workspace de Azure Databricks Premium (Laboratorio 00).
- Permiso para crear catálogos y esquemas en Unity Catalog.
- Conocimientos básicos de PySpark y Spark SQL.

## Objetivos de aprendizaje

- Arquitectura medallion en Unity Catalog.
- Limpieza de datos y agregaciones Gold.
- Gestión de errores con `try/except` y valores de salida del notebook.
- Parametrización con widgets y paso de valores entre tareas con task values.
- Lakeflow Jobs: dependencias, reintentos, notificaciones y If/else.

## Estructura de objetos

| Capa | Objeto |
|---|---|
| Catálogo | `hospitality_lab_hector` |
| Bronze | `hospitality_lab_hector.bronze.bookings_bronze` |
| Silver | `hospitality_lab_hector.silver.bookings_silver` |
| Gold | `hospitality_lab_hector.gold.property_performance`, `hospitality_lab_hector.gold.channel_performance` |
| Job | `GlobStay Booking Pipeline` |

---

# PARTE 1 – Notebook

## Preparación: importar el notebook y ejecutar el setup

1. **Workspace → carpeta → Import → URL**:
   `https://raw.githubusercontent.com/MicrosoftLearning/DP-750T00-Implement-Data-Engineering-Solutions-using-Azure-Databricks/refs/heads/main/Allfiles/10-design-implement-data-pipelines.ipynb`
2. Abrir el notebook y seleccionar compute **Serverless**.
3. Ejecutar las celdas de setup, que crean el catálogo `hospitality_lab_hector` (esquemas `bronze`, `silver`, `gold`) y el DataFrame `raw_df` con **16 filas** (15 reservas únicas; B001 duplicada).

Problemas de calidad incluidos a propósito: B001 duplicada; B004 y B015 con `guest_email` nulo; B005 con `room_type` nulo; B006 con `check_out_date` anterior a `check_in_date`; B007 con tarifa -50; B012 con tarifa 0.

## Nota: nombre del catálogo

Al ejecutar la celda de setup con el nombre original `hospitality_lab` apareció el error `PERMISSION_DENIED: User does not have USE CATALOG on Catalog 'hospitality_lab'` (`UNAUTHORIZED_ACCESS`, SQLSTATE 42501): ese catálogo ya existe en el metastore compartido y no pertenece al alumno. Solución: usar un catálogo propio, `hospitality_lab_hector`, cambiando la línea `catalog = "hospitality_lab_hector"` en la celda de setup y utilizando ese nombre en todo el laboratorio.

![alt text](images/README-1794909950904.png)

![alt text](images/README-1794909939476.png)

## Ejercicio 1: Capa Bronze

```python
raw_df.write.format("delta").mode("overwrite") \
    .saveAsTable("hospitality_lab_hector.bronze.bookings_bronze")

print(spark.table("hospitality_lab_hector.bronze.bookings_bronze").count())
```

**Resultado esperado:** `16`. Se usa `overwrite` para poder re-ejecutar la celda.

📸 **Captura:** celda con el recuento `16`.

![Celda con el recuento `16`](images/README-1794909920102.png)

## Ejercicio 2: Capa Silver

Reglas: deduplicar por `booking_id`; eliminar `room_type` nulo; eliminar reservas con `check_out_date <= check_in_date`; eliminar `rate_per_night <= 0`.

```python
from pyspark.sql.functions import col, to_date, datediff

bronze_df = spark.table("hospitality_lab_hector.bronze.bookings_bronze")

silver_df = (
    bronze_df
    .dropDuplicates(["booking_id"])
    .filter(col("room_type").isNotNull())
    .filter(datediff(to_date("check_out_date"), to_date("check_in_date")) > 0)
    .filter(col("rate_per_night") > 0)
)

silver_df.write.format("delta").mode("overwrite") \
    .saveAsTable("hospitality_lab_hector.silver.bookings_silver")

print("Bronze:", bronze_df.count(), "| Silver:", silver_df.count())
```

**Resultado esperado:** Bronze `16`, Silver `11`.

| Filas eliminadas | Motivo |
|---|---|
| B001 (duplicada) | Deduplicación |
| B005 | `room_type` nulo |
| B006 | Fechas invertidas |
| B007 | Tarifa negativa |
| B012 | Tarifa 0 |

B004 y B015 (email nulo) y B014 (pending) se conservan.

![salida `Bronze: 16 | Silver: 11`](images/README-1794910049736.png)

## Ejercicio 3 (parte A): Gold – `property_performance`

```sql
CREATE OR REPLACE TABLE hospitality_lab_hector.gold.property_performance AS
SELECT
  property_id,
  property_name,
  COUNT(*) AS confirmed_bookings,
  SUM(DATEDIFF(check_out_date, check_in_date)) AS total_nights,
  SUM(DATEDIFF(check_out_date, check_in_date) * rate_per_night) AS total_revenue
FROM hospitality_lab_hector.silver.bookings_silver
WHERE booking_status = 'confirmed'
GROUP BY property_id, property_name
ORDER BY total_revenue DESC;

SELECT * FROM hospitality_lab_hector.gold.property_performance;
```

![resultado del `SELECT`](images/README-1794910183815.png)

## Ejercicio 3 (parte B): Gold – `channel_performance`

```sql
CREATE OR REPLACE TABLE hospitality_lab_hector.gold.channel_performance AS
SELECT
  channel,
  COUNT(*) AS booking_count,
  SUM(DATEDIFF(check_out_date, check_in_date) * rate_per_night) AS total_revenue,
  ROUND(AVG(DATEDIFF(check_out_date, check_in_date) * rate_per_night), 2) AS avg_revenue_per_booking
FROM hospitality_lab_hector.silver.bookings_silver
WHERE booking_status = 'confirmed'
GROUP BY channel
ORDER BY total_revenue DESC;

SELECT * FROM hospitality_lab_hector.gold.channel_performance;
```

![resultado del `SELECT`](images/README-1794910236401.png)

## Ejercicio 4 (parte A): Lectura segura de tablas

```python
from pyspark.errors import PySparkException

def safe_read_table(table_name):
    try:
        return spark.table(table_name)
    except PySparkException as e:
        print(f"Error leyendo {table_name}: {e.getErrorClass()}")
        return None

df_ok = safe_read_table("hospitality_lab_hector.silver.bookings_silver")
print("OK:", df_ok.count())

df_bad = safe_read_table("hospitality_lab_hector.silver.no_existe")
print("Resultado tabla inexistente:", df_bad)
```

**Resultado esperado:** recuento `11` para la tabla válida; para la inexistente, un mensaje con la clase de error (`TABLE_OR_VIEW_NOT_FOUND`) y `None`.

![salida con ambos casos](images/README-1794910320120.png)

## Ejercicio 4 (parte B): Informar el resultado al job

```python
def report_pipeline_outcome(table_name):
    try:
        n = spark.table(table_name).count()
        dbutils.notebook.exit(f"SUCCESS: Processed {n} records from {table_name}")
    except Exception as e:
        dbutils.notebook.exit(f"FAILED: {e}")

# report_pipeline_outcome("hospitality_lab_hector.silver.bookings_silver")  # comentada a propósito
```

> La llamada se deja **comentada** porque `dbutils.notebook.exit()` detiene el notebook.

![función definida y llamada comentada](images/README-1794910360654.png)

## Ejercicio 5 (parte A): Parámetro con widget

```python
dbutils.widgets.text("booking_status", "confirmed", "Booking Status Filter")

status = dbutils.widgets.get("booking_status")
filtered = spark.table("hospitality_lab_hector.silver.bookings_silver") \
    .filter(f"booking_status = '{status}'")

display(filtered)
print("Filas:", filtered.count())
```

![widget "Booking Status Filter" y tabla filtrada](images/README-1794910436663.png)

## Ejercicio 5 (parte B): Task values

```python
silver = spark.table("hospitality_lab_hector.silver.bookings_silver")
props = [r.property_id for r in silver.select("property_id").distinct().collect()]

dbutils.jobs.taskValues.set(key="silver_record_count", value=silver.count())
dbutils.jobs.taskValues.set(key="properties_processed", value=props)

print(silver.count(), props)
```

> Fuera de la ejecución de un job, `taskValues.set()` no hace nada y muestra un aviso. Es el comportamiento esperado.

![salida con el recuento y la lista de propiedades](images/README-1794910507381.png)

---

# PARTE 2 – Orquestación con Lakeflow Jobs

> El mismo notebook se reutiliza en las tres tareas con distintos parámetros, solo con fines demostrativos.

## Ejercicio 6: Crear un job multitarea (*Create a multi-task pipeline job*)

### 6.1 Crear el job y las tareas

1. **Jobs & Pipelines → Create → Job**. Nombre: `GlobStay Booking Pipeline`.
2. **Tarea 1 – `ingest_bronze`:** tipo Notebook, origen Workspace, notebook importado, compute Serverless.
3. **Tarea 2 – `clean_silver`:** mismo notebook y compute, dependiente de `ingest_bronze`, parámetro `layer = silver`, **reintentos: 2**, intervalo **60 s**.
4. **Tarea 3 – `aggregate_gold`:** mismo notebook y compute, dependiente de `clean_silver`, parámetro `layer = gold`.

| Tarea | Depende de | Parámetro | Reintentos |
|---|---|---|---|
| `ingest_bronze` | – | – | – |
| `clean_silver` | `ingest_bronze` | `layer=silver` | 2 (60 s) |
| `aggregate_gold` | `clean_silver` | `layer=gold` | – |

![alt text](images/README-1794911363377.png)
![alt text](images/README-1794911374281.png)

### 6.2 Notificaciones de fallo

1. Panel de detalles del job → **Job notifications → Edit**.
2. **Add notification → On failure** con el correo del alumno.
3. (Opcional) silenciar notificaciones hasta el último reintento.
4. Guardar.

![notificación *On failure* configurada.](images/README-1794918194675.png)

### 6.3 Ejecutar el job

1. Pulsar **Run now**.
2. En la pestaña **Runs**, comprobar el orden `ingest_bronze → clean_silver → aggregate_gold` y revisar salida, logs y duración de cada tarea.

![alt text](images/README-1794918932655.png)
![alt text](images/README-1794918938385.png)

## Ejercicio 7: Añadir un flujo condicional (*Add a conditional task flow*)

1. **Deseleccionar** `aggregate_gold` antes de añadir la nueva tarea, para que no herede una dependencia no deseada.
2. Añadir `check_quality` (Notebook), dependiente de `clean_silver`.
3. Añadir `quality_gate` (**If/else condition**), dependiente de `check_quality`, con operador `>` y umbral `5`.
4. Rama **true:** `alert_data_issues` (Notebook).
5. Rama **false:** `proceed_gold` (Notebook).

El valor a comparar no lo especifica el enunciado. Propuesta: que `check_quality` publique un task value `issue_count` y que la condición sea:

```
{{tasks.check_quality.values.issue_count}} > 5
```

![alt text](images/README-1794919012883.png)

📸 **Captura:** DAG final y configuración de la condición de `quality_gate`.

![alt text](images/README-1794919231687.png)

---

# Reflexión: `try/except` en el notebook vs. gestión de errores en el job

| | `try/except` en el notebook | Nivel de job |
|---|---|---|
| Cuándo | Fallos previsibles y recuperables dentro de una tarea (tabla inexistente, dato mal formado) | Fallos transitorios, avisos a personas y enrutado entre tareas |
| Mecanismos | Captura de excepciones, `dbutils.notebook.exit()` con mensaje | Reintentos, notificaciones, dependencias, If/else |
| Ventaja | Control fino y mensajes específicos | Visibilidad y orquestación sin tocar el código |

Lo habitual es combinarlos: el notebook detecta y reporta el problema, y el job decide qué ocurre después.

# Limpieza (opcional)

El laboratorio no incluye sección de limpieza. Solo tras tener capturas y README entregados:

```sql
DROP CATALOG IF EXISTS hospitality_lab_hector CASCADE;
```

# Conclusiones

- Se construyó un pipeline medallion completo (16 filas en Bronze → 11 en Silver → 2 tablas Gold) en Unity Catalog.
- Se añadió gestión de errores, parametrización con widgets y task values.
- Se orquestó con un Lakeflow Job con dependencias, reintentos, notificaciones y rama condicional.