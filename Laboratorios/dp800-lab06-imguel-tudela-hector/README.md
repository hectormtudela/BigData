# Laboratorio 06 – Optimizar el rendimiento de consultas (Azure SQL Database)

**Autor:** Héctor Miguel Tudela
**Fecha:** 07/10/2026
**Laboratorio:** [06 – Optimize query performance](https://microsoftlearning.github.io/mslearn-sql-developer/Instructions/Labs/06-optimize-database-performance.html)

---

## Objetivo

Investigar consultas lentas en Azure SQL Database usando **planes de ejecución**, **DMVs** y **Query Store**:

1. Detectar un índice que falta mediante el plan de ejecución.
2. Localizar las consultas más costosas con DMVs.
3. Simular y corregir una regresión por *parameter sniffing* forzando un plan en Query Store.
4. Aplicar un *Query Store hint* (`MAXDOP 1`).
5. Diagnosticar y resolver un escenario de bloqueo entre dos escrituras.

## Entorno

| Elemento | Valor |
| --- | --- |
| Servicio | Azure SQL Database (Hyperscale serverless / Free offer) |
| Base de datos | AdventureWorksLT (datos de ejemplo del esquema `SalesLT`) |
| Cliente | SQL Server Management Studio (SSMS) |
| Autenticación | SQL Server Authentication (inicio de sesión de administrador del servidor: `hectormtudela06`) |
| Servidor | `rg-lab06-sql.database.windows.net` |
| Grupo de recursos | `rg-lab06-sql` |
| Suscripción | Azure for Students |
| Región | Spain |

---

## Paso 1 – Aprovisionar la base de datos Azure SQL

**Qué hice:** desde el portal de Azure (Azure SQL hub) creé una base de datos Azure SQL llamada `AdventureWorksLT`, con un servidor nuevo en el grupo de recursos `rg-lab06-sql`. Configuré el entorno de desarrollo con cómputo serverless, redundancia de copia de seguridad local y conectividad por punto de conexión público. En el firewall activé el acceso de los servicios de Azure y añadí mi IP de cliente, y en la pestaña de configuración adicional elegí cargar los **datos de ejemplo**, para que la base de datos se creara con AdventureWorksLT.

El despliegue terminó correctamente el 07/10/2026 y creó cinco recursos: el servidor, la base de datos, la cadena de conexión por defecto y las dos reglas de firewall (`ClientIp-2026-10-7_21-14-20` y `AllowAllWindowsAzureIps`).

![crear bbdd](image.png)
![crear bbdd 2](image-1.png)
![crear bbdd 3](image-2.png)
![crear bbdd 4](image-3.png)

**Observaciones:** al ser una base de datos serverless con pausa automática, se suspende tras un periodo de inactividad. La primera conexión tras la pausa puede fallar con un error de tiempo de espera durante la fase previa al inicio de sesión; basta con esperar un minuto y volver a conectar, sin pérdida de datos.

---

## Paso 2 – Crear la carga de trabajo de prueba (`OrderHistory`)

**Qué hice:** me conecté con SSMS al servidor `rg-lab06-sql.database.windows.net` con la base de datos `AdventureWorksLT` y ejecuté el script que crea la tabla `dbo.OrderHistory` y la rellena con 80.000 filas. Los pedidos combinan clientes y productos reales de `SalesLT.Customer` y `SalesLT.Product`, con fechas aleatorias del último año, cantidades entre 1 y 10 y cuatro estados posibles (`Pending`, `Processing`, `Shipped`, `Delivered`). La columna `TotalAmount` es una columna calculada y persistida (`Quantity * UnitPrice`).

**Verificación (`COUNT(*)`):** `SELECT COUNT(*) FROM dbo.OrderHistory` devolvió **80.000** filas.

![Captura paso 2](image-4.png)
![Comprobacion Paso 2](image-5.png)

---

## Paso 3 – Habilitar y configurar Query Store

**Qué hice:** activación de Query Store, limpieza y verificación de `actual_state_desc`.

**Resultado de `actual_state_desc`:** _(completar: READ_WRITE)_

![Captura paso 3](image-6.png)
![Comprobacion paso 3](image-7.png)

---

## Paso 4 – Analizar el plan de ejecución y añadir un índice que falta
 
| Medida | Antes del índice | Después del índice |
| --- | --- | --- |
| Operador sobre `OrderHistory` | Clustered Index Scan (87 % del coste) | Index Seek sobre `IX_OrderHistory_CustomerDate` (8 % del coste) |
| Logical reads (`OrderHistory`) | 897 | 3 |
| % de mejora sugerido por el optimizador | 95,05 % | – |

![Leer el plan](image-9.png)

![plan después](image-10.png)

**Conclusión:** Sin índice, la consulta recorría toda la tabla (897 lecturas lógicas para devolver solo 19 filas). Con el índice cubriente en `(CustomerID, OrderDate DESC)` más `INCLUDE`, el motor hace un Index Seek directo y lee solo 3 páginas, una reducción de casi el 99,7 %. El plan sigue mostrando un operador Sort tras el Hash Match, porque el join no conserva el orden del índice, pero ahora ordena solo 19 filas.

---

## Paso 5 – Usar DMVs para encontrar las consultas más costosas
 
**Top 5 por CPU media:** la consulta más cara fue la propia consulta de DMVs (5516 µs de CPU media, 108 lecturas lógicas). Le siguen consultas internas de SSMS sobre metadatos (`udf.name`, `clmns.name`). La consulta de pedidos de `OrderHistory` aparece con 1253 µs de CPU media y solo 8 lecturas lógicas (5 de `Product` y 3 de `OrderHistory`), gracias al índice creado en el paso anterior.
 
**Índice recomendado por las DMVs de missing index** (tras ejecutar 5 veces la consulta por `Status` y `OrderDate`):
 
| Equality columns | Inequality columns | Included columns | improvement_measure |
| --- | --- | --- | --- |
| `ProductID`, `Status` | `OrderDate` | `Quantity`, `TotalAmount` | 326,35 |
| `Status` | `OrderDate` | `ProductID`, `Quantity`, `TotalAmount` | 241,97 |
 
Las dos filas son variantes del mismo problema: la consulta filtra por `Status` y `OrderDate`, y el índice actual (`CustomerID`, `OrderDate`) no sirve para ese filtro. No se crea ninguno, porque son recomendaciones y habría que probar su efecto en lecturas y escrituras antes de llevarlos a producción.

![paso5_1](image-12.png)
![paso5_2](image-13.png)
![paso5_3](image-14.png)

---

## Paso 6 – Simular y detectar una regresión de plan con Query Store

### 6.1 Preparación del escenario
 
Se limpió Query Store y se cambió `QUERY_CAPTURE_MODE` a `ALL`, para registrar todas las ejecuciones del procedimiento. Después:
 
1. Se sustituyó el índice cubriente por uno **sin `INCLUDE`**: `IX_OrderHistory_CustomerDate (CustomerID, OrderDate DESC)`. Así el optimizador debe elegir entre un Index Seek con Key Lookups y un scan completo, y eso hace posible el parameter sniffing.
2. Se insertaron **50.000 pedidos** para el `CustomerID = 1`, que pasó de 80 a **50.080** pedidos, mientras el resto de clientes tiene menos de 100.
3. Se actualizaron las estadísticas (`UPDATE STATISTICS`).
4. Se creó el procedimiento `dbo.GetCustomerOrders @CustomerID INT`.
Nota: en un primer intento el procedimiento no se llegó a crear y el `EXEC` falló con *Could not find stored procedure*. Se resolvió ejecutando de nuevo la preparación completa en un único script, con un `GO` entre cada bloque.
 
![Preparación del escenario](06-preparacion.png)


### 6.2 Provocar la regresión
 
Con el plan de ejecución real activado (Ctrl+M):
 
| Bloque | Qué se ejecutó | Plan obtenido |
| --- | --- | --- |
| A | Limpiar caché y `EXEC ... @CustomerID = 29485` (×10) | **Index Seek** + Key Lookup (el Key Lookup supone el 87 % del coste, con 99 filas) |
| B | Limpiar caché y `EXEC ... @CustomerID = 1` | **Clustered Index Scan** en paralelo (50.080 filas) |
| C | `EXEC ... @CustomerID = 29485` (×10) **sin limpiar la caché** | **Clustered Index Scan**: se reutiliza el plan de B |
 
La regresión se ve en el bloque C. Para el cliente 29485 el plan sigue siendo el scan en paralelo: el optimizador estima 48.957 filas y en realidad se devuelven solo 99, y el operador `SELECT` muestra un triángulo de aviso. El plan se compiló para el cliente 1 (50.080 filas) y se reutiliza con un cliente que solo necesita unas pocas filas. El mismo cliente, con el plan del bloque A, usaba un Index Seek.
 
Por último se ejecutó `sp_query_store_flush_db` para volcar los datos de Query Store a disco y que el asistente gráfico los muestre al momento.
 
![Bloque A: Index Seek](06-plan-seek.png)
![Bloque B: Clustered Index Scan, cliente 1](06-plan-scan-cliente1.png)
![Bloque C: Clustered Index Scan reutilizado, cliente 29485](06-plan-scan.png)

### 6.3 Detectar y forzar el plan en el GUI de Query Store
![top resource](image-15.png)
![Forced Plans](image-16.png)

### 6.4 Verificación con T-SQL
![Verificacion plan forzado](image-17.png)
![Plan](image-19.png)

![Limpieza](image-20.png)

**Conclusión:** La consulta a sys.query_store_plan confirmó que el plan quedó forzado: is_forced_plan vale 1 y force_failure_count vale 0, porque el índice IX_OrderHistory_CustomerDate sigue existiendo y el plan forzado se puede ejecutar sin problemas.

Al ejecutar dbo.GetCustomerOrders con @CustomerID = 29485 y con @CustomerID = 1, ambos usan el plan forzado con Index Seek, sin importar el parámetro. Esto elimina la regresión del cliente pequeño, que antes reutilizaba un Clustered Index Scan para leer solo 99 filas. La contrapartida está en el cliente 1: con más de 50.000 filas, el seek con Key Lookups no es el plan óptimo, y se ve en el plan con un posible derrame a disco en el Sort. En el cliente 29485 puede aparecer un aviso de exceso de memoria concedida en el SELECT.

Forzar el plan es una medida rápida que no requiere modificar el código de la aplicación ni del procedimiento, pero conviene tratarla como una mitigación temporal. Una solución más duradera sería reescribir la consulta, añadir un índice cubriente o usar una pista como OPTION (RECOMPILE), para que cada parámetro obtenga el plan que mejor le encaja.

---

## Paso 7 – Aplicar un Query Store hint

| Dato | Valor |
| --- | --- |
| `query_id` | 65 |
| Plan sin hint | Paralelo: flechas amarillas de paralelismo y operador Gather Streams |
| Plan con `MAXDOP 1` | Un solo hilo: sin flechas de paralelismo ni Gather Streams |
| Tiempo sin hint / con hint | 00:00:05 / 00:00:03 |

Se ejecutó la consulta de agregación pesada (`GROUP BY` por cliente, producto, categoría y estado, con tres funciones de ventana con distinto `PARTITION BY`). El optimizador eligió un plan paralelo porque su coste supera el umbral de paralelismo.

![Primera consulta](image-21.png)
![Plan de ejecución de la primera consulta: paralelo con Gather Streams](image-22.png)

Después se buscó el `query_id` de la consulta en Query Store, que resultó ser **65**.

![Query ID: búsqueda del número](image-23.png)

Se aplicó el hint `OPTION (MAXDOP 1)` a esa consulta con `sp_query_store_set_hints`, sin modificar el código de la consulta.

![Query con el número de la Query ID](image-24.png)

Al repetir la consulta, el plan pasó a ejecutarse en un solo hilo: desaparecieron las flechas de paralelismo y el Gather Streams.

![Repetir la consulta del punto 1](image-26.png)
![Plan de ejecución con MAXDOP 1](image-25.png)

Por último se eliminó el hint con `sp_query_store_clear_hints`.

![Quitar hint](image-27.png)

**Conclusión:** el hint `MAXDOP 1` permitió cambiar el comportamiento de la consulta (de plan paralelo a plan de un solo hilo) sin tocar el código de la aplicación. Con el hint, la consulta tardó ⏱ X s frente a ⏱ Y s sin él. El plan paralelo suele ser más rápido en tiempo de reloj, porque reparte la agregación y las ventanas entre varios hilos, mientras que el de un solo hilo consume menos CPU en total. Es un compromiso que `MAXDOP` permite controlar, útil cuando el paralelismo cuesta más de lo que aporta o se quiere reducir la CPU en un servidor compartido. Conviene documentar qué consultas llevan hint y retirarlo cuando ya no haga falta.
---

## Paso 8 – Identificar y resolver un bloqueo

| Dato | Valor |
| --- | --- |
| Sesión bloqueadora (head blocker) | sesión número 72 |
| `wait_type` de la sesión bloqueada | `LCK_M_X` (espera de un bloqueo exclusivo) |
| Estado de la sesión bloqueadora | `sleeping` (inactiva, con una transacción abierta) |

En Azure SQL Database el aislamiento RCSI está activado por defecto, así que las lecturas no bloquean a las escrituras. Sin embargo, dos escrituras sobre la misma fila sí se bloquean entre sí. Para comprobarlo se usaron tres ventanas de consulta conectadas a `AdventureWorksLT`.

**Ventana 1.** Se abrió una transacción con `BEGIN TRANSACTION` y un `UPDATE` sobre `OrderID = 1` (estado `Cancelled`), sin hacer commit. Simula una aplicación del almacén que se detiene a mitad de una transacción y deja la fila bloqueada.

![Consulta en ventana 1](image-28.png)

**Ventana 2.** Se intentó modificar la misma fila (estado `Shipped`). La consulta se quedó colgada, bloqueada por el bloqueo exclusivo de la ventana 1.

![Consulta colgada ventana 2](image-29.png)

**Ventana 3.** Con `sys.dm_exec_requests` se identificó la cadena de bloqueo: la sesión bloqueada espera con `LCK_M_X`, y la columna `head_blocker` indica qué sesión la bloquea. `wait_resource` apunta a la fila exacta.

![Encontrar bloqueo](image-30.png)

Después se investigó al bloqueador con `sys.dm_exec_sessions` y `sys.dm_exec_connections`. Su estado es `sleeping`: ejecutó su `UPDATE`, está inactiva y mantiene la transacción abierta. Es uno de los patrones de bloqueo más habituales.

![Investigar el bloqueador](image-31.png)

**Resolución.** Se ejecutó `ROLLBACK TRANSACTION` en la ventana 1, lo que liberó el bloqueo.

![Rollback transaction](image-32.png)

La ventana 2 pudo completar su `UPDATE` inmediatamente después.

![Update hecho](image-33.png)

**Conclusión:** un bloqueo no siempre lo causa una consulta lenta, sino una transacción abierta e inactiva. En producción conviene mantener las transacciones cortas, usar `TRY...CATCH` con `ROLLBACK` en el `CATCH`, activar `SET XACT_ABORT ON` en los procedimientos que abren transacciones y, si hay una sesión huérfana bloqueando a otras, terminarla con `KILL <session_id>`.

---

## Paso 9 – Limpieza

Al terminar el laboratorio se dejó la base de datos y Azure en su estado inicial.

**1. Objetos de prueba.** Se eliminaron el procedimiento `dbo.GetCustomerOrders` (si seguía existiendo) y la tabla `dbo.OrderHistory`, junto con sus índices.

![Borrar objetos de prueba](image-34.png)

**2. Planes forzados.** Se ejecutó el script que recorre `sys.query_store_plan` y llama a `sp_query_store_unforce_plan` por cada plan con `is_forced_plan = 1`, para quitar el plan forzado del paso 6.

![Desforzar los planes que quedan](image-35.png)

**3. Hints de Query Store.** Se consultó `sys.query_store_query_hints` para comprobar que no quedaba ningún hint activo. El hint `MAXDOP 1` del paso 7 (`query_id` 65) ya se había eliminado con `sp_query_store_clear_hints`.

![Comprobar que no quedan hints](image-36.png)

**4. Query Store en modo normal.** En el paso 6 se había cambiado `QUERY_CAPTURE_MODE` a `ALL` para registrar todas las ejecuciones. Se devolvió a `AUTO`, que es el valor recomendado en producción porque ignora las consultas más triviales.

![Query Store en modo normal](image-37.png)

**5. Recursos de Azure.** Se eliminó el grupo de recursos `rg-lab06-sql` desde el portal de Azure, con el servidor y la base de datos, para no consumir crédito.

![Recursos de Azure limpios](image-38.png)

---

## Conclusiones generales

En este laboratorio recorrí el flujo completo de diagnóstico de rendimiento en Azure SQL Database, desde la consulta lenta hasta el bloqueo.

**Índices cubrientes y planes de ejecución.** Leer el plan permite ver por qué una consulta es lenta. Sin índice, la consulta de pedidos hacía un Clustered Index Scan con **897 lecturas lógicas** para devolver solo 19 filas. Con un índice en `(CustomerID, OrderDate DESC)` más `INCLUDE`, pasó a un Index Seek con **3 lecturas lógicas**, una mejora de casi el 99,7 %. Las recomendaciones de missing index (en el plan y en las DMVs) son un buen punto de partida, pero hay que revisarlas y probarlas antes de aplicarlas, porque cada índice añade coste a las escrituras.

**DMVs.** Dan una visión global de la carga de trabajo: qué consultas consumen más CPU y qué índices echa en falta el optimizador. También conviene saber filtrar el ruido, porque entre los resultados aparecieron consultas internas de SSMS.

**Parameter sniffing y Query Store.** Con datos muy sesgados (el cliente 1 con más de 50.000 pedidos frente a menos de 100 en el resto), el plan compilado para un parámetro se reutilizó con otro y se produjo la regresión: un scan completo para devolver 99 filas. Query Store permitió ver los dos planes, compararlos y forzar el bueno sin tocar el código. Aun así, forzar un plan es una **mitigación temporal**, porque beneficia a unos parámetros y perjudica a otros. La solución duradera pasa por reescribir la consulta, mejorar los índices o recompilar por parámetro.

**Query Store hints.** Con `MAXDOP 1` cambié el grado de paralelismo de una consulta sin modificar la aplicación. Es una herramienta potente, pero hay que usarla con cuidado: el paralelismo suele ganar en tiempo de reloj y perder en CPU total, y los hints conviene documentarlos y retirarlos cuando ya no hagan falta.

**Bloqueos.** Una transacción abierta e inactiva (sesión `sleeping`) puede bloquear a otras sesiones aunque no ejecute nada. Las DMVs permiten encontrar al bloqueador (`head_blocker`) y ver qué espera la sesión bloqueada (`LCK_M_X`). Para evitarlo: transacciones cortas, `TRY...CATCH` con `ROLLBACK`, `SET XACT_ABORT ON` y `KILL` solo como último recurso.

**Lección general.** Medir antes y después (lecturas lógicas, planes, tiempos) y limpiar al terminar es tan importante como la optimización en sí.


