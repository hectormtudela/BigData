# 03 · Capa Gold: esquema en estrella en `WH_Gold`

Esquema `gold`: `Dim_Date` (1462 filas), `Dim_Product` (SCD1), `Dim_Customer` (SCD2 sobre `City`), `Dim_Store`, `Fact_Sales` (grano = línea de pedido). Claves sustitutas, PK/FK `NOT ENFORCED`, dimensión degenerada `OrderNumber` expuesta con la vista `gold.Dim_Order`, y dimensión *role-playing* de fecha (`OrderDateKey` activa, `ShipDateKey` inactiva).

## Pasos y evidencias
### 3.1 DDL

![Cinco tablas creadas en el esquema gold.](img/03a-ddl-cinco-tablas.png)

📸 **Captura:** Cinco tablas creadas en el esquema gold.

### 3.2 Dim_Date

![Dim_Date con 1462 filas.](img/03b-dim-date-1462.png)

📸 **Captura:** Dim_Date con 1462 filas.

### 3.3 Dimensiones

![Recuento de filas de las dimensiones (10 / 4 / 7).](img/03c-dimensiones-10-4-7.png)

📸 **Captura:** Recuento de filas de las dimensiones (10 / 4 / 7).

### 3.4 Fact_Sales

![Fact_Sales con 1200 filas y 0 filas huérfanas en la auditoría.](img/03d-fact-1200-auditoria-0.png)

📸 **Captura:** Fact_Sales con 1200 filas y 0 filas huérfanas en la auditoría.

### 3.5 Constraints

![PK/FK definidas como NOT ENFORCED.](img/03e-constraints-not-enforced.png)

📸 **Captura:** PK/FK definidas como NOT ENFORCED.

### 3.6 Vista Dim_Order

![Vista gold.Dim_Order (dimensión degenerada).](img/03f-vista-dim-order.png)

📸 **Captura:** Vista gold.Dim_Order (dimensión degenerada).


## Errores
| # | Error | Causa | Solución |
|---|---|---|---|
| 3 | `Msg 156` al ejecutar `CREATE SCHEMA gold;` en un script con más sentencias | `CREATE SCHEMA/PROCEDURE/VIEW` deben ir solos en su lote | Ejecutar `CREATE SCHEMA` solo y después las tablas por separado |
| 4 | `Msg 15816` con `sys.procedures` | No soportado en modo de procesamiento distribuido | Usar `sys.objects WHERE type='P'` en una consulta independiente |
| 6 | `Msg 207 Invalid column name 'CustomerKey'` | La columna real es `Customer_SK` | Corregir el nombre |
