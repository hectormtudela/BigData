# Laboratorio 11 – Implement Lakeflow Jobs with Azure Databricks (DP-750)

> **Autor:** Héctor Miguel Tudela · **Máster Big Data & IA – Tajamar**
> **Laboratorio:** https://microsoftlearning.github.io/DP-750T00-Implement-Data-Engineering-Solutions-using-Azure-Databricks/Instructions/Labs/11-implement-lakeflow-jobs.html

---

## 1. Escenario

Somos ingenieros de datos en **TelConnect**, un operador de telecomunicaciones regional. Los **CDR** (Call Detail Records) deben recorrer una arquitectura medallion **Bronze → Silver → Gold** y automatizarse con **Lakeflow Jobs**.

| Requisito | Solución en el lab |
|---|---|
| Procesar CDRs por capas (bronce, plata, oro) | Notebook parametrizado con widget `processing_date` |
| Encadenar el procesado con un resumen SQL | Job con 2 tareas dependientes (`process_cdrs → summarize_gold`) |
| Ejecutar cuando llegan ficheros nuevos | Trigger **File arrival** sobre un Volume |
| Ejecución nocturna fija | Trigger **Scheduled** con cron `0 0 2 * * ?` (Europe/Amsterdam) |
| Enterarse de los fallos | Notificaciones por email, reintentos y timeout |

**Compute:** Serverless (notebook y SQL warehouse)

## 2. Objetivos

1. Ejecutar un notebook medallion parametrizado (Bronze, Silver, Gold).
2. Crear un Lakeflow Job con dos tareas dependientes.
3. Pasar un parámetro dinámico `processing_date`.
4. Configurar un trigger de llegada de ficheros y otro programado (cron).
5. Configurar notificaciones de fallo, reintentos y timeout.
6. Monitorizar una ejecución y revisar los *task values*.

## 3. Requisitos previos

- Workspace Azure Databricks **Premium** (Lab 00) con Unity Catalog.
- Permiso para crear catálogos y esquemas.
- PySpark y Spark SQL básicos.

> ⚠️ Si `telconnect_lab` ya existe en el metastore compartido y no eres su propietario (como pasó con `edu_dev` o `banking_lab`), usa `telconnect_lab_hmt` y sustitúyelo **en todo el lab** (notebook, consulta SQL y ruta del trigger).

> ⚠️ Si borraste `rg-dp750` tras el lab anterior, recrea el workspace antes de empezar (mismo procedimiento que en los labs 00 y 06).

---

## 4. Parte 1 – Ejecutar el notebook de la pipeline

### Task 1.1 – Importar el notebook

1. Barra lateral → **Workspace**.
2. Crea/abre una carpeta para el lab → menú **⋮** → **Import**.
3. Elige **URL** y pega:
   `https://raw.githubusercontent.com/MicrosoftLearning/DP-750T00-Implement-Data-Engineering-Solutions-using-Azure-Databricks/refs/heads/main/Allfiles/11-implement-lakeflow-jobs.ipynb`
4. **Import** → abre `11-implement-lakeflow-jobs`.
5. Arriba a la derecha conecta con compute **Serverless**.

> Usa la URL `raw.githubusercontent.com`, no la `github.com/.../blob/...`.

📸 **Captura:** notebook importado y abierto, con **Serverless** conectado.

### Task 1.2 – Ejercicios 1 a 5 del notebook

Ejecuta las celdas en orden. Qué hace cada ejercicio y qué debe verse:

| Ejercicio | Qué hace | Resultado esperado |
|---|---|---|
| **1 – Estructura UC** | Crea el widget `processing_date` (por defecto, hoy), localiza el storage root y crea el catálogo `telconnect_lab` con esquemas `bronze`, `silver`, `gold` | Fecha de proceso, ruta del storage root y mensajes de creación de catálogo y esquemas |
| **2 – Bronze** | Crea el volume `raw_uploads`, descarga `telecom_cdrs.csv`, lo lee con esquema explícito (14 columnas) y guarda `telconnect_lab.bronze.cdr_bronze` | DataFrame bruto y **recuento Bronze** |
| **3 – Silver** | Aplica 4 reglas de calidad y guarda `telconnect_lab.silver.cdr_silver` | Recuento Bronze, recuento Silver y **registros descartados** |
| **4 – Gold** | Agrupa por región y tipo de red y guarda `telconnect_lab.gold.network_summary` | Nº de filas Gold y la tabla resumen |
| **5 – Job-ready** | Publica `gold_row_count` como *task value* y termina con `dbutils.notebook.exit(...)` (JSON con estado, fecha y filas Gold) | Mensaje de finalización y payload de salida |

Reglas de Silver: descartar duraciones negativas · descartar VOICE/DATA sin destinatario · descartar llamadas VOICE completadas con duración 0 · conservar solo tipos VOICE, DATA y SMS.

Métricas de Gold: total de llamadas, llamadas completadas, % de *drop rate*, duración media de voz (>0 s) y MB de datos totales.

> Si usas un catálogo con otro nombre (`telconnect_lab_hmt`), usa **Buscar y reemplazar** del notebook antes de ejecutar.

📸 **Captura 1:** Ejercicio 1 con el catálogo y los 3 esquemas creados.
📸 **Captura 2:** Ejercicio 2 con el recuento Bronze.
📸 **Captura 3:** Ejercicio 3 con Bronze / Silver / descartados.
📸 **Captura 4:** Ejercicio 4 con la tabla `network_summary`.
📸 **Captura 5:** Ejercicio 5 con el payload de `dbutils.notebook.exit`.
📸 **Captura 6:** **Catalog** → `telconnect_lab` desplegado con `bronze` (`cdr_bronze`, volume `raw_uploads`), `silver` (`cdr_silver`) y `gold` (`network_summary`).

---

## 5. Parte 2 – Lakeflow Jobs

### Exercise 1 – Crear el job

1. Barra lateral → **Jobs & Pipelines** → **Create** → **Job**.
2. Nombre del job: `TelConnect CDR Pipeline`.
3. Añade una tarea de tipo **Notebook**:
   - **Task name:** `process_cdrs`
   - **Path:** el notebook importado (`11-implement-lakeflow-jobs`)
   - **Compute:** Serverless
   - **Create task**
4. En **Job details** → **Parameters** añade:
   - **Key:** `processing_date`
   - **Value:** referencia dinámica a la fecha del trigger, p. ej. `{{job.trigger.time.iso_date}}` (elige el valor de la lista **Browse dynamic values** si el nombre difiere en tu interfaz).
5. Comprueba que el grafo tiene un solo nodo y pulsa **Run now**.
6. Abre la ejecución y confirma que todas las celdas terminan correctamente.

📸 **Captura 1:** configuración de la tarea `process_cdrs`.
📸 **Captura 2:** parámetro de job `processing_date` con su valor dinámico.
📸 **Captura 3:** la ejecución terminada en **Succeeded**.

### Exercise 2 – Tarea SQL descendente (`summarize_gold`)

**Paso 1 – Crear la consulta guardada.** En **SQL Editor** (warehouse **Serverless**), crea una consulta que seleccione región, tipo de red, total de llamadas y *drop rate* de `telconnect_lab.gold.network_summary`, ordenada por *drop rate* descendente. Usa la consulta que da la página del lab; si los nombres de columna no coinciden, comprueba los reales con `DESCRIBE TABLE telconnect_lab.gold.network_summary;` (paso añadido por mí, no viene del lab). Versión orientativa:

```sql
SELECT
  region,
  network_type,
  total_calls,
  drop_rate_pct
FROM telconnect_lab.gold.network_summary
ORDER BY drop_rate_pct DESC;
```

Renombra la consulta a `summarize_gold_query` y **guárdala**.

**Paso 2 – Añadir la tarea al job.**

1. Abre el job → **Tasks** → **Add task**.
2. **Task name:** `summarize_gold` · **Type:** **SQL** → *Query*.
3. **Query:** `summarize_gold_query` · **SQL warehouse:** Serverless.
4. **Depends on:** `process_cdrs` · condición **All succeeded**.
5. **Create task** y guarda.
6. Verifica el grafo: `process_cdrs → summarize_gold`.

> Si no hay SQL warehouse Serverless disponible en la suscripción, anótalo en el apartado de problemas y usa el *Starter Warehouse* si existe.

📸 **Captura 1:** consulta `summarize_gold_query` guardada con resultados.
📸 **Captura 2:** configuración de la tarea `summarize_gold` (consulta, warehouse y dependencia).
📸 **Captura 3:** grafo del job con las dos tareas conectadas.

### Exercise 3 – Trigger de llegada de ficheros

1. En el panel derecho del job → **Schedules & Triggers** → **Add trigger**.
2. **Trigger type:** **File arrival**.
3. **Storage location:** `/Volumes/telconnect_lab/bronze/raw_uploads/`
4. Despliega **Advanced options** y ahí fija **Wait after last change:** `60` segundos.
5. **Save**.

📸 **Captura:** trigger File arrival configurado y guardado.

### Exercise 4 – Programación nocturna (cron)

1. **Elimina** el trigger File arrival.
2. **Add trigger** → comprueba que **Trigger Status** = **Active** → **Trigger type:** **Scheduled**.
3. Selecciona **Schedule** (no *Interval*) y **Show cron syntax**.
4. Cron (Quartz): `0 0 2 * * ?`
5. **Time zone:** `Europe/Amsterdam` → **Save**.
6. Verifica que solo queda el trigger programado, diario a las 02:00.

| Campo | Valor |
|---|---|
| Segundos / Minutos / Hora | `0 0 2` |
| Día mes / Mes / Día semana | `* * ?` (todos los días) |
| Zona horaria | Europe/Amsterdam |

📸 **Captura 1:** trigger Scheduled con la expresión cron y la zona horaria.
📸 **Captura 2:** panel del job con **un único trigger** (el programado) activo.

### Exercise 5 – Notificaciones

**Nivel de job:**

1. **Job notifications** → **Edit notifications** → **Add notification** → **Email** (tu correo de Tajamar) → evento **Failure**.
2. *(Opcional)* añade **Duration warning** a **30 minutos**.

**Nivel de tarea (`process_cdrs`):**

1. Abre la tarea → **Notifications** → **Add** → **Email** → evento **Failure**.
2. Marca **Mute notifications until the last retry**.
3. **Save task**.

📸 **Captura 1:** notificaciones a nivel de job.
📸 **Captura 2:** notificación de la tarea con *Mute notifications until the last retry* marcado.

### Exercise 6 – Reintentos y timeout

En la tarea `process_cdrs`:

1. **Retries** → **Add**: **2** reintentos, intervalo de **60** segundos.
2. **Metric thresholds** → **Run duration**:
   - **Warning:** 20 minutos
   - **Timeout:** 30 minutos
3. **Save task**.

📸 **Captura:** tarea `process_cdrs` con reintentos y umbrales de duración visibles.

### Exercise 7 – Ejecutar y monitorizar

1. Pulsa **Run now**.
2. Pestaña **Runs** → abre la ejecución activa.
3. Confirma que **`process_cdrs` se ejecuta antes que `summarize_gold`**.
4. En `process_cdrs`, revisa las salidas de celda, el valor de `processing_date` y los valores fijados con `dbutils.jobs.taskValues.set()` (`gold_row_count`).
5. Confirma que el estado final es **Succeeded**.

📸 **Captura 1:** vista de la ejecución con las dos tareas en verde y su orden.
📸 **Captura 2:** salida de `process_cdrs` mostrando `processing_date` y `gold_row_count`.
📸 **Captura 3:** pestaña **Runs** con estado **Succeeded**.

---

## 6. Resultados esperados (checklist)

- [ ] Catálogo `telconnect_lab` con `bronze`, `silver`, `gold` y las tablas `cdr_bronze`, `cdr_silver`, `network_summary`.
- [ ] Job `TelConnect CDR Pipeline` con 2 tareas dependientes (`process_cdrs → summarize_gold`).
- [ ] Parámetro dinámico `processing_date` en el job.
- [ ] Solo el trigger programado `0 0 2 * * ?` (Europe/Amsterdam) activo; el File arrival eliminado.
- [ ] Notificaciones de fallo (job y tarea) con *mute until last retry*.
- [ ] 2 reintentos de 60 s y timeout de 30 min en `process_cdrs`.
- [ ] Ejecución final en **Succeeded**.

## 7. Limpieza

Para evitar ejecuciones y costes, **pausa o elimina el job** (el trigger diario seguiría lanzándolo a las 02:00):

1. **Jobs & Pipelines** → `TelConnect CDR Pipeline` → **⋮** → **Delete** (o pausa el trigger).
2. Elimina la consulta guardada si quieres: `summarize_gold_query`.
3. Borra el catálogo:

```sql
DROP CATALOG IF EXISTS telconnect_lab CASCADE;
```

4. Comprueba en **Compute** que no queda ningún warehouse ni cluster en ejecución.
5. Si no vas a hacer más labs de Databricks:

```bash
az group delete --name rg-dp750 --yes --no-wait
```

> Haz la limpieza solo después de tener todas las capturas y el README entregados.

## 8. Problemas encontrados

| Error | Causa | Solución |
|---|---|---|
| _(rellenar si aparece alguno)_ | | |

## 9. Conclusiones

_(rellenar al terminar: qué aporta Lakeflow Jobs frente a ejecutar el notebook a mano, diferencia entre trigger por fichero y por cron, utilidad de reintentos y timeouts)_