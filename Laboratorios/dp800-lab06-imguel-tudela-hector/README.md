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
| Base de datos | AdventureWorksLT |
| Cliente | SQL Server Management Studio (SSMS) |
| Autenticación | _(completar: Microsoft Entra MFA / SQL Login)_ |
| Grupo de recursos | _(completar)_ |
| Región | _(completar)_ |

---

## Paso 1 – Aprovisionar la base de datos Azure SQL

**Qué hice:** _(describir)_

![Captura paso 1](capturas/01-crear-bd.png)

**Observaciones:** _(completar)_

---

## Paso 2 – Crear la carga de trabajo de prueba (`OrderHistory`)

**Qué hice:** conexión con SSMS, creación de la tabla `dbo.OrderHistory` con 80.000 filas.

**Verificación (`COUNT(*)`):** _(completar: debe dar 80.000)_

![Captura paso 2](capturas/02-orderhistory.png)

---

## Paso 3 – Habilitar y configurar Query Store

**Qué hice:** activación de Query Store, limpieza y verificación de `actual_state_desc`.

**Resultado de `actual_state_desc`:** _(completar: READ_WRITE)_

![Captura paso 3](capturas/03-query-store.png)

---

## Paso 4 – Analizar el plan de ejecución y añadir un índice que falta

| Medida | Antes del índice | Después del índice |
| --- | --- | --- |
| Operador sobre `OrderHistory` | _(Clustered Index Scan)_ | _(Index Seek)_ |
| Logical reads | _(completar)_ | _(completar)_ |
| % de mejora sugerido por el optimizador | _(completar)_ | – |

![Plan antes](capturas/04-plan-antes.png)
![Plan después](capturas/04-plan-despues.png)

**Conclusión:** _(completar)_

---

## Paso 5 – Usar DMVs para encontrar las consultas más costosas

**Top 5 por CPU media:** _(captura / resumen)_
**Índice recomendado por las DMVs de missing index:** _(completar)_

![Captura paso 5](capturas/05-dmvs.png)

---

## Paso 6 – Simular y detectar una regresión de plan con Query Store

### 6.1 Preparación del escenario
_(índice no cubriente, datos sesgados con CustomerID 1, procedimiento `dbo.GetCustomerOrders`)_

### 6.2 Provocar la regresión
_(plan Seek vs plan Scan al reutilizar la caché)_

### 6.3 Detectar y forzar el plan en el GUI de Query Store
![Top Resource Consuming Queries](capturas/06-top-resource.png)
![Force Plan](capturas/06-force-plan.png)
![Queries With Forced Plans](capturas/06-forced-plans.png)

### 6.4 Verificación con T-SQL
**`is_forced_plan`:** _(completar)_  **`force_failure_count`:** _(completar)_

**Conclusión:** _(completar)_

---

## Paso 7 – Aplicar un Query Store hint

| Dato | Valor |
| --- | --- |
| `query_id` | _(completar)_ |
| Plan sin hint | _(paralelo, Gather Streams)_ |
| Plan con `MAXDOP 1` | _(un solo hilo)_ |
| Tiempo sin hint / con hint | _(completar)_ |

![Plan paralelo](capturas/07-plan-paralelo.png)
![Plan MAXDOP 1](capturas/07-plan-maxdop1.png)

---

## Paso 8 – Identificar y resolver un bloqueo

| Dato | Valor |
| --- | --- |
| Sesión bloqueadora (head blocker) | _(completar)_ |
| `wait_type` de la sesión bloqueada | _(LCK_M_X)_ |
| Estado de la sesión bloqueadora | _(sleeping)_ |

![Bloqueo detectado](capturas/08-bloqueo.png)

**Resolución:** `ROLLBACK TRANSACTION` en la ventana 1.

---

## Paso 9 – Limpieza

- [ ] `DROP PROCEDURE` / `DROP TABLE`
- [ ] Planes desforzados y hints eliminados
- [ ] Recursos de Azure eliminados (grupo de recursos)

---

## Conclusiones generales

_(completar al terminar: qué aprendí sobre índices cubrientes, parameter sniffing, Query Store y bloqueos)_