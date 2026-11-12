# Laboratorio 08 — Cleanse, Transform and Load Data into Unity Catalog (DP-750)

> **Autor:** Héctor Miguel Tudela · **Máster Big Data & IA – Tajamar**
> **Teoría:** https://learn.microsoft.com/en-us/training/modules/cleanse-transform-load-data-into-unity-catalog/
> **Laboratorio:** https://microsoftlearning.github.io/DP-750T00-Implement-Data-Engineering-Solutions-using-Azure-Databricks/Instructions/Labs/08-cleanse-transform-load-data-into-unity-catalog.html

---

## 1. Objetivo

Escenario: ingeniero de datos en **Pristine Properties**, una inmobiliaria con presencia en las grandes ciudades de Países Bajos. Los listados llegan de varias oficinas con precios imprecisos, anuncios duplicados (versiones actualizadas), nulos en campos clave y estadísticas de mercado en formato ancho. Hay que limpiar, tipar y reorganizar los datos para dashboards de precios y modelos de análisis de mercado.

Objetivos del laboratorio:

- Perfilar datos con `ANALYZE TABLE`, `.describe()` y un **Data Profile** (Snapshot) en Catalog Explorer.
- Elegir tipos de datos correctos: `DECIMAL` vs `DOUBLE`, `TIMESTAMP` vs `TIMESTAMP_NTZ`, `ARRAY` / `MAP` / `STRUCT`.
- Detectar y resolver duplicados y nulos (SQL con `QUALIFY` y PySpark con `dropDuplicates`, `dropna`, `fillna`).
- Combinar tablas con joins (inner y left anti-pattern).
- Reorganizar datos con `PIVOT` y `UNPIVOT`.

## 2. Entorno

| Elemento | Valor |
|---|---|
| Resource group | `rg-dp750` |
| Workspace | `adb-dp750` (Premium) |
| Cómputo | Serverless |
| Catálogo | `realestate_lab_hmt` (el notebook usa `realestate_lab`; se sustituye con Find and replace) |
| Esquemas | `bronze`, `silver` |
| Volumen | `realestate_lab_hmt.bronze.raw_files` |
| Tablas bronze | `listings`, `agents`, `sales`, `market_stats` |

> El nombre `realestate_lab` puede existir ya en el metastore compartido (como pasó en el lab 06 con `banking_lab`). Por eso se usa el sufijo `_hmt` desde el principio.

## 3. Teoría resumida (módulo de Microsoft Learn)

| Unidad | Idea principal |
|---|---|
| Profile data | Estadísticas de resumen para evaluar calidad y forma del dataset |
| Choose column data types | Equilibrio entre almacenamiento e integridad (`DECIMAL`, `TIMESTAMP_NTZ`, tipos complejos) |
| Resolve duplicates and nulls | Detectar duplicados; eliminar o rellenar valores nulos |
| Filters and aggregations | `WHERE`, `GROUP BY`, `HAVING`, agregaciones |
| Joins and set operators | `INNER`/`LEFT` join, `UNION`, `INTERSECT`, `EXCEPT` |
| Denormalization and pivots | Aplanar datos, `PIVOT` y `UNPIVOT` |
| Load data | `INSERT`, `MERGE`, `append` y `overwrite` |

---

## Task 1 — Preparar el notebook

1. Workspace → carpeta del lab → menú **⋮** → **Import** → **URL**.
2. Pegar la URL del notebook:
   `https://raw.githubusercontent.com/MicrosoftLearning/DP-750T00-Implement-Data-Engineering-Solutions-using-Azure-Databricks/refs/heads/main/Allfiles/08-cleanse-transform-load-data-into-unity-catalog.ipynb`
3. Abrir el notebook y elegir cómputo **Serverless**.
4. **Find and replace** → *Replace all*: `realestate_lab` → `realestate_lab_hmt`.

📸 **Captura:** notebook abierto con **Serverless** conectado y el cuadro de Find and replace con `realestate_lab` → `realestate_lab_hmt` (o el resultado tras *Replace all*).

![Captura Task 1](images/lab08-01-notebook.png)

> ℹ️ El notebook sugiere usar **Genie Code** en cada celda. Es una ayuda opcional: revisa siempre lo que propone antes de ejecutarlo.
>
> Regla del lab (igual que en el 07): **SQL con `%sql` en la primera línea de la celda, PySpark sin magic**, y un solo magic por celda.

---

## Task 2 — Ejercicio 1: Plataforma Pristine Properties (celdas proporcionadas)

Se ejecutan en orden, sin modificar, las celdas que:

1. Obtienen el *Storage Root* del catálogo por defecto y crean el catálogo `realestate_lab_hmt` con `MANAGED LOCATION`.
2. Crean los esquemas `bronze` y `silver` y el volumen gestionado `raw_files`.
3. Escriben en el volumen 4 CSV: `property_listings.csv` (33 filas con duplicados y nulos), `real_estate_agents.csv` (8 agentes), `property_sales.csv` (3 ventas) y `market_stats_wide.csv` (7 ciudades × 12 meses).
4. Cargan los CSV como tablas Delta bronze: `listings`, `agents`, `sales`, `market_stats`.

Verificación (en celdas separadas):

```sql
%sql
SHOW TABLES IN realestate_lab_hmt.bronze;
```

```sql
%sql
SELECT COUNT(*) AS total_filas FROM realestate_lab_hmt.bronze.listings;
```

📸 **Captura:** salida de `CREATE CATALOG` / mensaje `CSV files written to volume.` y `All tables loaded successfully.`

📸 **Captura:** `SHOW TABLES` con las 4 tablas (`listings`, `agents`, `sales`, `market_stats`) y el `COUNT(*)` = **33**.

![Captura Ejercicio 1 – estructura](images/lab08-02-estructura.png)
![Captura Ejercicio 1 – tablas](images/lab08-03-tablas.png)

---

## Task 3 — Ejercicio 2: Perfilar los datos de `listings`

### Task 2.1 — Estadísticas de tabla

```sql
%sql
-- Task 1a: calcular estadísticas de todas las columnas
ANALYZE TABLE realestate_lab_hmt.bronze.listings COMPUTE STATISTICS FOR ALL COLUMNS;
```

```sql
%sql
-- Task 1b: ver las estadísticas recogidas
DESCRIBE TABLE EXTENDED realestate_lab_hmt.bronze.listings;
```

📸 **Captura:** `DESCRIBE TABLE EXTENDED` mostrando la sección de estadísticas (`Statistics`, nº de filas = 33 y tamaño en bytes).

![Captura Ejercicio 2.1](images/lab08-04-analyze.png)

### Task 2.2 — Resumen con PySpark

```python
# Task 2: cargar listings y ver estadísticas de resumen
df_listings = spark.table("realestate_lab_hmt.bronze.listings")
display(df_listings.describe())
```

Qué debe verse: `count` distinto entre columnas (`list_price` < 33, `bedrooms` < 33, etc.), lo que delata los nulos. `describe()` devuelve count, mean, stddev, min y max; `summary()` añade además percentiles (25 %, 50 %, 75 %).

📸 **Captura:** tabla de `describe()` con las filas `count`, `mean`, `stddev`, `min`, `max` y los recuentos menores de 33 en `list_price`, `bedrooms`, `bathrooms` y `status`.

![Captura Ejercicio 2.2](images/lab08-05-describe.png)

### Task 2.3 — Tarea fuera del notebook: Data Profile en Catalog Explorer

> La página del lab la sitúa tras el Ejercicio 1 y el notebook tras el Ejercicio 2. Vale con hacerla aquí, porque la tabla bronze ya existe.

1. **Catalog** → `realestate_lab_hmt` → `bronze` → `listings`.
2. Pestaña **Quality** → activar **Data Quality Monitoring**.
3. En **Data profiling** → configurar monitor → tipo de perfil **Snapshot**.
4. **Create** para generar el primer perfil.
5. Abrir el dashboard de monitorización y refrescar (**Update and refresh**).
6. Revisar nulos, valores distintos y distribución de `list_price`.

📸 **Captura:** pestaña **Quality** con el monitor **Snapshot** creado.

📸 **Captura:** dashboard del perfil con los recuentos de nulos (`list_price`, `bedrooms`, `bathrooms`, `status`) y el histograma de `list_price`.

![Captura Data Profile – monitor](images/lab08-06-monitor.png)
![Captura Data Profile – dashboard](images/lab08-07-profile.png)

---

## Task 4 — Ejercicio 3: Elegir los tipos de datos

### Task 3.1 — `DECIMAL` vs `DOUBLE`

Celda proporcionada (muestra la imprecisión de coma flotante):

```sql
%sql
SELECT
  CAST(0.1 AS DOUBLE) + CAST(0.2 AS DOUBLE) AS sum_double,
  CAST(0.1 AS DOUBLE) + CAST(0.2 AS DOUBLE) = CAST(0.3 AS DOUBLE) AS double_exact,   -- FALSE
  CAST(0.1 AS DECIMAL(2,1)) + CAST(0.2 AS DECIMAL(2,1)) AS sum_decimal,
  CAST(0.1 AS DECIMAL(2,1)) + CAST(0.2 AS DECIMAL(2,1)) = CAST(0.3 AS DECIMAL(2,1)) AS decimal_exact; -- TRUE
```

Tabla silver con tipos correctos (`list_price` como `DECIMAL(12,2)`):

```sql
%sql
CREATE OR REPLACE TABLE realestate_lab_hmt.silver.listings_typed AS
SELECT
  CAST(listing_id    AS INT)            AS listing_id,
  CAST(property_id   AS STRING)         AS property_id,
  CAST(agent_id      AS INT)            AS agent_id,
  CAST(city          AS STRING)         AS city,
  CAST(property_type AS STRING)         AS property_type,
  CAST(bedrooms      AS INT)            AS bedrooms,
  CAST(bathrooms     AS INT)            AS bathrooms,
  CAST(list_price    AS DECIMAL(12,2))  AS list_price,
  CAST(sqm           AS INT)            AS sqm,
  CAST(listing_date  AS DATE)           AS listing_date,
  CAST(last_updated  AS TIMESTAMP)      AS last_updated,
  CAST(status        AS STRING)         AS status
FROM realestate_lab_hmt.bronze.listings;
```

```sql
%sql
DESCRIBE TABLE realestate_lab_hmt.silver.listings_typed;
```

📸 **Captura:** resultado de la celda proporcionada (`double_exact = false`, `decimal_exact = true`).

📸 **Captura:** `DESCRIBE TABLE` de `listings_typed` con `list_price` como `decimal(12,2)`, `listing_date` como `date` y `last_updated` como `timestamp`.

![Captura 3.1 – DOUBLE vs DECIMAL](images/lab08-08-decimal.png)
![Captura 3.1 – listings_typed](images/lab08-09-listings-typed.png)

### Task 3.2 — `TIMESTAMP` vs `TIMESTAMP_NTZ`

Se ejecuta la celda proporcionada (vista temporal `viewing_appointments` + `SET TIME ZONE 'America/New_York'` + `SELECT`). La columna `TIMESTAMP` **se desplaza** al cambiar la zona horaria; la `TIMESTAMP_NTZ` **no cambia**. Después se restaura la zona:

```sql
%sql
SET TIME ZONE 'UTC';
```

📸 **Captura:** resultado con `viewing_time_ts` desplazado (p. ej. 09:00 → 03:00 de Nueva York) y `viewing_time_ntz` intacto (09:00).

![Captura 3.2](images/lab08-10-timestamp.png)

### Task 3.3 — `ARRAY`, `MAP` y `STRUCT`

**3a — Vista temporal con tipos complejos:**

```sql
%sql
CREATE OR REPLACE TEMP VIEW listings_enriched AS
SELECT * FROM VALUES
  ('PROP-001',
   ARRAY('Parking', 'Balcony', 'Storage'),
   MAP('energy_label', 'A', 'heating', 'central'),
   NAMED_STRUCT('street', 'Damrak 10', 'city', 'Amsterdam', 'postal_code', '1012 LG')),
  ('PROP-002',
   ARRAY('Garden', 'Garage'),
   MAP('energy_label', 'B', 'heating', 'district'),
   NAMED_STRUCT('street', 'Coolsingel 25', 'city', 'Rotterdam', 'postal_code', '3012 AB')),
  ('PROP-004',
   ARRAY('Pool', 'Parking', 'Garden'),
   MAP('energy_label', 'A', 'heating', 'heat pump'),
   NAMED_STRUCT('street', 'Oudegracht 5', 'city', 'Utrecht', 'postal_code', '3511 AA'))
AS t(property_id, amenities, features, address);
```

**3b — Acceso a los elementos:**

```sql
%sql
SELECT
  property_id,
  amenities[0]              AS first_amenity,
  features['energy_label']  AS energy_label,
  address.city              AS city
FROM listings_enriched;
```

📸 **Captura:** las 3 filas con `first_amenity` (Parking / Garden / Pool), `energy_label` (A / B / A) y `city` (Amsterdam / Rotterdam / Utrecht).

![Captura 3.3](images/lab08-11-complex-types.png)

---

## Task 5 — Ejercicio 4: Duplicados y valores nulos

### Task 4.1 — Identificar duplicados

```sql
%sql
SELECT property_id, COUNT(*) AS veces
FROM realestate_lab_hmt.bronze.listings
GROUP BY property_id
HAVING COUNT(*) > 1
ORDER BY property_id;
```

Resultado esperado: **3 propiedades** duplicadas (`PROP-001`, `PROP-002`, `PROP-003`), 2 apariciones cada una.

📸 **Captura:** las 3 filas de duplicados con `veces = 2`.

![Captura 4.1](images/lab08-12-duplicados.png)

### Task 4.2 — Quedarse con la última versión (`ROW_NUMBER` + `QUALIFY`)

```sql
%sql
SELECT *
FROM realestate_lab_hmt.bronze.listings
QUALIFY ROW_NUMBER() OVER (PARTITION BY property_id ORDER BY last_updated DESC) = 1
ORDER BY property_id;
```

Resultado esperado: **30 filas** (33 − 3 duplicados). Para `PROP-001` queda el precio **279000.00** (actualizado el 2026-03-01).

📸 **Captura:** resultado con 30 filas y la fila de `PROP-001` con `list_price = 279000.00` y `last_updated = 2026-03-01`.

![Captura 4.2](images/lab08-13-qualify.png)

### Task 4.3 — Deduplicar con PySpark

```python
from pyspark.sql import functions as F

df = spark.table("realestate_lab_hmt.bronze.listings")
print(f"Filas antes: {df.count()}")

df_dedup = (df.orderBy(F.col("last_updated").desc())
              .dropDuplicates(["property_id"]))
print(f"Filas después: {df_dedup.count()}")

display(df_dedup.orderBy("property_id"))
```

Resultado esperado: **33 → 30**.

> ⚠️ `dropDuplicates` no garantiza formalmente qué fila conserva tras un `orderBy` en un entorno distribuido. Para un resultado determinista es mejor `ROW_NUMBER() ... QUALIFY` (Task 4.2) o una ventana con `row_number()` en PySpark.

📸 **Captura:** salida con `Filas antes: 33` y `Filas después: 30`, más la tabla resultante.

![Captura 4.3](images/lab08-14-dropduplicates.png)

### Task 4.4 — Tratar nulos

Reglas: `list_price` nulo → **eliminar fila**; `bedrooms` → `0`; `bathrooms` → `1.0`; `status` → `'Unknown'`.

```python
from pyspark.sql import functions as F

df = spark.table("realestate_lab_hmt.bronze.listings")
print(f"Filas originales: {df.count()}")

df_clean = (df.dropna(subset=["list_price"])
              .fillna({"bedrooms": 0, "bathrooms": 1.0, "status": "Unknown"}))
print(f"Filas limpias: {df_clean.count()}")

display(df_clean.orderBy("listing_id"))
```

Resultado esperado: **33 → 31** (se eliminan `PROP-023` y `PROP-029`, sin precio). Ya no quedan nulos en `bedrooms`, `bathrooms` ni `status`. Como `bedrooms` y `bathrooms` son enteros, el `1.0` se almacena como `1`.

Comprobación opcional:

```python
display(df_clean.select([F.sum(F.col(c).isNull().cast("int")).alias(c) for c in df_clean.columns]))
```

📸 **Captura:** `Filas originales: 33` / `Filas limpias: 31` y la comprobación de nulos a 0 en `list_price`, `bedrooms`, `bathrooms` y `status`.

![Captura 4.4](images/lab08-15-nulos.png)

---

## Task 6 — Ejercicio 5: Joins

```python
from pyspark.sql import functions as F

l = spark.table("realestate_lab_hmt.bronze.listings").alias("l")
a = spark.table("realestate_lab_hmt.bronze.agents").alias("a")
s = spark.table("realestate_lab_hmt.bronze.sales").alias("s")
```

> Tanto `listings` como `agents` tienen columna `city`: hay que usar los alias (`l.city`) para evitar `AMBIGUOUS_REFERENCE`.

### Task 5.1 — Inner join listings + agents

```python
df_inner = (l.join(a, F.col("l.agent_id") == F.col("a.agent_id"), "inner")
             .select("l.listing_id", "l.property_id", "l.city",
                     "l.list_price", "a.agent_name", "a.agency"))
display(df_inner)
```

Resultado esperado: **33 filas** (todos los listados tienen agente).

📸 **Captura:** DataFrame con las columnas `listing_id`, `property_id`, `city`, `list_price`, `agent_name`, `agency` (33 filas).

![Captura 5.1](images/lab08-16-inner-join.png)

### Task 5.2 — Agentes sin listados (left join + `IS NULL`)

```python
df_no_listings = (a.join(l, F.col("a.agent_id") == F.col("l.agent_id"), "left")
                   .filter(F.col("l.listing_id").isNull())
                   .select("a.agent_id", "a.agent_name", "a.agency"))
display(df_no_listings)
```

Resultado esperado: **1 fila** → agente `108`, Robert Mulder, Canal Ring Realty.

📸 **Captura:** una fila con el agente 108.

![Captura 5.2](images/lab08-17-agentes-sin-listados.png)

### Task 5.3 — Listados sin vender

```python
df_unsold = (l.join(s, F.col("l.property_id") == F.col("s.property_id"), "left")
              .filter(F.col("s.sale_id").isNull())
              .select("l.listing_id", "l.property_id", "l.city",
                      "l.property_type", "l.list_price", "l.listing_date"))
display(df_unsold)
```

Resultado esperado: **30 filas** (33 listados − 3 propiedades vendidas: `PROP-005`, `PROP-011`, `PROP-016`).

📸 **Captura:** resultado con 30 filas, sin ninguna de las tres propiedades vendidas.

![Captura 5.3](images/lab08-18-sin-vender.png)

---

## Task 7 — Ejercicio 6: Pivot y Unpivot

### Task 6.1 — `PIVOT`: listados activos por ciudad y tipo

```sql
%sql
SELECT *
FROM (
  SELECT city, property_type
  FROM realestate_lab_hmt.bronze.listings
  WHERE status = 'Active'
)
PIVOT (
  COUNT(*) FOR property_type IN ('Apartment', 'House', 'Studio', 'Villa')
)
ORDER BY city;
```

Columnas: `city`, `Apartment`, `House`, `Studio`, `Villa`.

> Sobre la tabla bronze **sin deduplicar**, Amsterdam da `Apartment = 3, House = 1, Studio = 2, Villa = 1` (`PROP-003` aparece dos veces). El ejemplo del enunciado muestra `Studio = 1`, que corresponde a datos ya deduplicados. Si quieres que coincida, sustituye la subconsulta por la del Task 4.2 (`QUALIFY ROW_NUMBER() ...`) antes de filtrar `Active`.

📸 **Captura:** tabla pivotada con una fila por ciudad (7 ciudades) y las 4 columnas de tipo de propiedad.

![Captura 6.1](images/lab08-19-pivot.png)

### Task 6.2 — `UNPIVOT`: estadísticas de mercado a formato largo

```sql
%sql
SELECT city, month, avg_price
FROM realestate_lab_hmt.bronze.market_stats
UNPIVOT (
  avg_price FOR month IN (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)
)
ORDER BY city;
```

Resultado esperado: **84 filas** (7 ciudades × 12 meses) con columnas `city`, `month`, `avg_price`.

📸 **Captura:** resultado con columnas `city`, `month`, `avg_price` (84 filas).

![Captura 6.2](images/lab08-20-unpivot.png)

---

## 8. Conceptos clave

- **`ANALYZE TABLE ... COMPUTE STATISTICS`:** recoge estadísticas (nº de filas, tamaño, distintos, nulos, mín/máx) que usa el optimizador de consultas.
- **`describe()` vs `summary()`:** `describe()` da count, mean, stddev, min y max; `summary()` añade percentiles.
- **`DECIMAL` vs `DOUBLE`:** `DOUBLE` es coma flotante binaria y produce errores de redondeo (`0.1 + 0.2 ≠ 0.3`); para importes se usa `DECIMAL(p,s)`.
- **`TIMESTAMP` vs `TIMESTAMP_NTZ`:** `TIMESTAMP` se guarda en UTC y se muestra según la zona de la sesión; `TIMESTAMP_NTZ` guarda el valor tal cual (citas locales).
- **`ARRAY` / `MAP` / `STRUCT`:** `amenities[0]`, `features['clave']`, `address.city`.
- **Duplicados:** `GROUP BY ... HAVING COUNT(*) > 1` para detectarlos; `ROW_NUMBER() ... QUALIFY` para conservar el último registro de forma determinista.
- **`dropna` / `fillna`:** eliminan filas con nulos en columnas clave o rellenan con valores por defecto.
- **Left join + `IS NULL`:** patrón para encontrar registros de una tabla sin correspondencia en otra (anti-join).
- **`PIVOT` / `UNPIVOT`:** filas a columnas y columnas a filas.
- **Carga (teoría):** `INSERT`, `MERGE` y `overwrite` para escribir los datos transformados en tablas de Unity Catalog.

## 9. Problemas encontrados

| Error | Causa | Solución |
|---|---|---|
| *(completar si aparece alguno)* | | |

Puntos donde es fácil tropezar en este lab:

- `[PARSE_SYNTAX_ERROR]` / `SyntaxError` por olvidar `%sql` o juntar dos magics en la misma celda.
- `[AMBIGUOUS_REFERENCE]` en los joins al seleccionar `city` sin alias (existe en `listings` y en `agents`).
- Sugerencias de Genie Code que cambian los nombres de tabla o de columnas: comprobar que usan `realestate_lab_hmt`.

## 10. Limpieza

No se elimina `rg-dp750`. Opcional, para borrar el catálogo del lab:

```sql
%sql
-- DROP CATALOG IF EXISTS realestate_lab_hmt CASCADE;
```

Si se ha cambiado la zona horaria de la sesión, restaurar con `SET TIME ZONE 'UTC';`.

📸 **Captura:** (opcional) celda de limpieza ejecutada y el catálogo ausente en Catalog Explorer.

![Captura limpieza](images/lab08-21-limpieza.png)