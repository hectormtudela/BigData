# Práctica 24 · Clase 27: Agregaciones, joins, ventanas y escritura de datos

**Alumno:** Héctor Miguel Tudela · Máster Big Data & IA (Tajamar)

## Contenido

| Fichero | Descripción |
| --- | --- |
| [`clase_27_pyspark_agregaciones.ipynb`](clase_27_pyspark_agregaciones.ipynb) | Los 23 ejercicios de la clase, con enunciado, código y salida |
| [`capturas/`](capturas/) | Capturas de la ejecución en Databricks |
| [`datos/`](datos/) | Copia de los ficheros de entrada del pipeline final (ejercicio 9.1) |

## Ejercicios

| Nº | Ejercicio | Qué se practica |
| --- | --- | --- |
| 1.1 | Resumen del día de unas ferreterías | `agg()`, `countDistinct()` |
| 1.2 | Nulos en las agregaciones | `count()`, `avg()`, `coalesce()` |
| 2.1 | Facturación por canal | `groupBy()` y `orderBy()` |
| 2.2 | Varias columnas y filtros | Equivalentes de `WHERE` y `HAVING` |
| 2.3 | Cartera de productos de un banco | `collect_list()`, `collect_set()`, `size()` |
| 3.1 | Informe de tickets de soporte | Agregaciones condicionales |
| 3.2 | Ventas trimestrales de ópticas | `pivot()`, `fillna()` |
| 4.1 | Plazos de cobro de facturas | `to_date()`, `date_add()`, `datediff()` |
| 4.2 | Reservas por mes y turno | `to_timestamp()`, `dayofweek()` |
| 5.1 | Pedidos y clientes | `inner join` |
| 5.2 | Catálogo y ventas | `inner`, `left`, `right`, `full` |
| 5.3 | Clientes sin facturas | `left_semi`, `left_anti` |
| 5.4 | La misma tabla dos veces | Alias y claves con distinto nombre |
| 5.5 | Tabla pequeña y agregación | `broadcast()` |
| 6.1 | Versión vigente de cada cliente | `row_number()` |
| 6.2 | Ranking con empates | `row_number()`, `rank()`, `dense_rank()` |
| 6.3 | Variación y acumulados | `lag()`, `rowsBetween()` |
| 7.1 | Ingresos por plan | `spark.sql()`, vistas temporales, `selectExpr()` |
| 7.2 | Saldo de cuentas | CTE y función de ventana en SQL |
| 8.1 | Parquet y CSV | Modos de escritura |
| 8.2 | Datos particionados | `partitionBy()` |
| 8.3 | Tarifas de envío | `saveAsTable()` y catálogo |
| 9.1 | Pipeline completo | De los ficheros a las tablas finales |

## Cómo ejecutarlo

1. Abrir el notebook en un entorno con PySpark 4.1 (Spark local, clúster Docker o Databricks).
2. Ejecutar primero la **celda de configuración**: define `spark`, `RUTA` (ficheros) y `BD` (base de datos de las tablas).
3. Ejecutar el resto de celdas en orden. Los ficheros de entrada se crean solos en `RUTA`.
4. En local y Docker, la última celda cierra la sesión: el catálogo de Hive (Derby) solo admite una sesión a la vez.

En local en Windows hacen falta además `winutils.exe` y `hadoop.dll` para escribir ficheros.

## Entorno de las salidas guardadas

Las salidas guardadas dentro del notebook son de PySpark 4.1.4 con Java 21, en modo local sobre Linux, con catálogo Hive (las pruebas del final son de Databricks). Se han quitado los mensajes de log de Spark (salida de error) para que se lea mejor.

## Ideas clave

- `filter()` antes de `groupBy()` filtra filas; después de `agg()` filtra grupos.
- `left_anti` sirve como control de integridad: muestra las filas sin pareja.
- Las funciones de ventana calculan por grupo sin perder las filas originales.
- Parquet conserva los tipos; CSV no.

## Pruebas de ejecución en Databricks

Ejecución en Databricks (Spark 4.2.0) de los 23 ejercicios.

### Configuración del entorno

![Configuración del entorno](capturas/configuracion.png)

### Ejercicio 1.1 · Resumen del día de unas ferreterías

![Ejercicio 1.1 · Resumen del día de unas ferreterías](capturas/ejercicio-1-1.png)

### Ejercicio 1.2 · Nulos en las agregaciones

![Ejercicio 1.2 · Nulos en las agregaciones](capturas/ejercicio-1-2.png)

### Ejercicio 2.1 · Facturación por canal

![Ejercicio 2.1 · Facturación por canal](capturas/ejercicio-2-1.png)

### Ejercicio 2.2 · Varias columnas y filtros

![Ejercicio 2.2 · Varias columnas y filtros](capturas/ejercicio-2-2.png)

### Ejercicio 2.3 · Cartera de productos de un banco

![Ejercicio 2.3 · Cartera de productos de un banco](capturas/ejercicio-2-3.png)

### Ejercicio 3.1 · Informe de tickets de soporte

![Ejercicio 3.1 · Informe de tickets de soporte](capturas/ejercicio-3-1.png)

### Ejercicio 3.2 · Ventas trimestrales de ópticas

![Ejercicio 3.2 · Ventas trimestrales de ópticas](capturas/ejercicio-3-2.png)

### Ejercicio 4.1 · Plazos de cobro de facturas

![Ejercicio 4.1 · Plazos de cobro de facturas](capturas/ejercicio-4-1.png)

### Ejercicio 4.2 · Reservas por mes y turno

![Ejercicio 4.2 · Reservas por mes y turno](capturas/ejercicio-4-2.png)

### Ejercicio 5.1 · Pedidos y clientes

![Ejercicio 5.1 · Pedidos y clientes](capturas/ejercicio-5-1.png)

### Ejercicio 5.2 · Catálogo y ventas

![Ejercicio 5.2 · Catálogo y ventas](capturas/ejercicio-5-2.png)

### Ejercicio 5.3 · Clientes sin facturas

![Ejercicio 5.3 · Clientes sin facturas](capturas/ejercicio-5-3.png)

### Ejercicio 5.4 · La misma tabla dos veces

![Ejercicio 5.4 · La misma tabla dos veces](capturas/ejercicio-5-4.png)

### Ejercicio 5.5 · Tabla pequeña y agregación

![Ejercicio 5.5 · Tabla pequeña y agregación](capturas/ejercicio-5-5.png)

### Ejercicio 6.1 · Versión vigente de cada cliente

![Ejercicio 6.1 · Versión vigente de cada cliente](capturas/ejercicio-6-1.png)

### Ejercicio 6.2 · Ranking con empates

![Ejercicio 6.2 · Ranking con empates](capturas/ejercicio-6-2.png)

### Ejercicio 6.3 · Variación y acumulados

![Ejercicio 6.3 · Variación y acumulados](capturas/ejercicio-6-3.png)

### Ejercicio 7.1 · Ingresos por plan

![Ejercicio 7.1 · Ingresos por plan](capturas/ejercicio-7-1.png)

### Ejercicio 7.2 · Saldo de cuentas

![Ejercicio 7.2 · Saldo de cuentas](capturas/ejercicio-7-2.png)

### Ejercicio 8.1 · Parquet y CSV

![Ejercicio 8.1 · Parquet y CSV](capturas/ejercicio-8-1.png)

### Ejercicio 8.2 · Datos particionados

![Ejercicio 8.2 · Datos particionados](capturas/ejercicio-8-2.png)

### Ejercicio 8.3 · Tarifas de envío

![Ejercicio 8.3 · Tarifas de envío](capturas/ejercicio-8-3.png)

### Ejercicio 9.1 · Pipeline completo (código)

![Ejercicio 9.1 · Pipeline completo (código)](capturas/ejercicio-9-1-codigo.png)

### Ejercicio 9.1 · Pipeline completo (código y resultado)

![Ejercicio 9.1 · Pipeline completo (código y resultado)](capturas/ejercicio-9-1-resultado.png)
