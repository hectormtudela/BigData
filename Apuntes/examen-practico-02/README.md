# SQL Server 2025 — Apuntes y ejercicios resueltos

---

# 1. Conceptos y código

## 1.1. JOIN

Un `JOIN` permite combinar información de varias tablas utilizando una relación entre ellas.

### INNER JOIN

Devuelve únicamente las filas que tienen coincidencia en ambas tablas.

```sql
SELECT *
FROM clientes c
INNER JOIN facturas f
    ON f.cliente_id = c.cliente_id;
```

**Idea:**

```text
clientes        facturas
   ↓               ↓
   └── coinciden ──┘
```

Solo aparecen clientes que tienen facturas.

---

### LEFT JOIN

Conserva **todas las filas de la tabla de la izquierda**.

```sql
SELECT *
FROM clientes c
LEFT JOIN facturas f
    ON f.cliente_id = c.cliente_id;
```

Aquí:

- Todos los `clientes` aparecen.
- Si tienen facturas, se añaden.
- Si no tienen factura, las columnas de `facturas` aparecen como `NULL`.

### Regla para memorizar

```text
A LEFT JOIN B
```

→ **Todos los de A**, y los de B cuando coincidan.

Por eso:

```sql
FROM clientes c
LEFT JOIN facturas f
    ON f.cliente_id = c.cliente_id
```

se queda con **todos los clientes**, no solo con los que tienen factura.

---

## 1.2. Subconsulta escalar

Una subconsulta escalar devuelve **un único valor**.

Ejemplo:

```sql
SELECT *
FROM facturas
WHERE importe > (
    SELECT AVG(importe)
    FROM facturas
);
```

La subconsulta:

```sql
SELECT AVG(importe)
FROM facturas
```

calcula un único valor y la consulta exterior lo utiliza.

### Estructura

```sql
WHERE columna > (
    SELECT funcion(...)
    FROM tabla
)
```

---

## 1.3. Subconsulta con IN

`IN` sirve para comprobar si un valor pertenece al resultado de una subconsulta.

```sql
SELECT *
FROM facturas
WHERE cliente_id IN (
    SELECT cliente_id
    FROM clientes
    WHERE pais = 'ES'
);
```

Se puede leer:

> Dame las facturas cuyo `cliente_id` esté entre los clientes españoles.

---

## 1.4. Subconsultas anidadas

Una subconsulta puede contener otra subconsulta.

```sql
SELECT *
FROM cobros
WHERE factura_id IN (
    SELECT factura_id
    FROM facturas
    WHERE cliente_id IN (
        SELECT cliente_id
        FROM clientes
        WHERE gestor_id IN (
            SELECT empleado_id
            FROM empleados
            WHERE puesto = 'Comercial'
        )
    )
);
```

Aquí tenemos varios niveles:

```text
cobros
  ↓
facturas
  ↓
clientes
  ↓
empleados
```

---

## 1.5. EXISTS

`EXISTS` comprueba si una subconsulta devuelve **al menos una fila**.

```sql
SELECT *
FROM clientes c
WHERE EXISTS (
    SELECT 1
    FROM facturas f
    WHERE f.cliente_id = c.cliente_id
);
```

No importa qué devuelve el `SELECT` interno. Solo importa si existe alguna fila.

Por eso es habitual utilizar:

```sql
SELECT 1
```

---

## 1.6. NOT EXISTS

Es lo contrario:

```sql
SELECT *
FROM clientes c
WHERE NOT EXISTS (
    SELECT 1
    FROM facturas f
    WHERE f.cliente_id = c.cliente_id
);
```

Devuelve clientes **sin facturas**.

---

## 1.7. CTE

Una CTE permite crear temporalmente un resultado con nombre para utilizarlo en la consulta siguiente.

```sql
WITH cobros_por_factura AS (
    SELECT
        factura_id,
        SUM(importe) AS cobrado
    FROM cobros
    GROUP BY factura_id
)
SELECT *
FROM cobros_por_factura;
```

La CTE solo existe durante esa consulta.

### Estructura

```sql
WITH nombre_cte AS (
    SELECT ...
)
SELECT ...
FROM nombre_cte;
```

---

## 1.8. CTE encadenadas

Podemos tener varias CTE:

```sql
WITH facturas_t3 AS (
    SELECT *
    FROM facturas
    WHERE fecha_emision >= '2026-07-01'
      AND fecha_emision <= '2026-09-30'
),
enriquecidas AS (
    SELECT
        f.factura_id,
        f.importe,
        c.pais,
        c.segmento
    FROM facturas_t3 f
    INNER JOIN clientes c
        ON c.cliente_id = f.cliente_id
),
por_segmento AS (
    SELECT
        pais,
        segmento,
        COUNT(*) AS facturas,
        SUM(importe) AS importe
    FROM enriquecidas
    GROUP BY pais, segmento
)
SELECT *
FROM por_segmento;
```

La segunda CTE puede utilizar la primera y la tercera puede utilizar la segunda.

---

## 1.9. CTE recursiva

Se utiliza para recorrer estructuras jerárquicas.

Ejemplo:

```sql
WITH jerarquia AS (
    -- Caso inicial
    SELECT
        unidad_id,
        nombre,
        unidad_padre_id,
        0 AS nivel
    FROM unidades
    WHERE unidad_padre_id IS NULL

    UNION ALL

    -- Parte recursiva
    SELECT
        u.unidad_id,
        u.nombre,
        u.unidad_padre_id,
        j.nivel + 1
    FROM unidades u
    INNER JOIN jerarquia j
        ON u.unidad_padre_id = j.unidad_id
)
SELECT *
FROM jerarquia;
```

La primera parte encuentra la raíz.

La segunda va buscando sus hijos.

```text
Nivel 0
   ↓
Nivel 1
   ↓
Nivel 2
   ↓
Nivel 3
```

---

## 1.10. Vistas

Una vista es una consulta guardada que se puede consultar como si fuera una tabla.

```sql
CREATE OR ALTER VIEW dbo.mi_vista
AS
SELECT
    cliente_id,
    razon_social
FROM clientes;
GO
```

Después:

```sql
SELECT *
FROM dbo.mi_vista;
```

### CREATE OR ALTER

Es muy útil en ejercicios porque permite ejecutar el script varias veces:

```sql
CREATE OR ALTER VIEW ...
```

---

## 1.11. SELECT INTO

En SQL Server, `SELECT INTO` permite crear una tabla a partir del resultado de una consulta.

```sql
SELECT
    factura_id,
    cliente_id,
    importe
INTO dbo.facturas_copia
FROM facturas;
```

La tabla se crea automáticamente.

Si queremos poder ejecutar el script varias veces:

```sql
DROP TABLE IF EXISTS dbo.facturas_copia;

SELECT ...
INTO dbo.facturas_copia
FROM facturas;
```

---

## 1.12. Tablas temporales

Una tabla temporal comienza por `#`.

```sql
CREATE TABLE #ventas (
    cliente_id int,
    importe decimal(12,2)
);
```

Solo existe durante la sesión.

También podemos crearla con `SELECT INTO`:

```sql
SELECT
    cliente_id,
    SUM(importe) AS importe
INTO #ventas
FROM facturas
GROUP BY cliente_id;
```

Cuando termina la sesión, desaparece.

---

## 1.13. COALESCE

Sirve para sustituir `NULL` por otro valor.

```sql
COALESCE(cobrado, 0)
```

Si `cobrado` es `NULL`, devuelve `0`.

Ejemplo:

```sql
SELECT
    cliente_id,
    COALESCE(SUM(importe), 0) AS importe
FROM cobros
GROUP BY cliente_id;
```

---

## 1.14. CASE

Permite crear condiciones.

```sql
CASE
    WHEN pendiente = 0 THEN 'Cobrada'
    WHEN cobrado = 0 THEN 'Sin cobro'
    ELSE 'Cobro parcial'
END
```

Se utiliza para transformar valores según una condición.

---

## 1.15. Fechas

Para el T3 de 2026:

```sql
WHERE fecha >= '2026-07-01'
  AND fecha <= '2026-09-30'
```

También se puede utilizar:

```sql
WHERE fecha BETWEEN '2026-07-01' AND '2026-09-30'
```

En esta práctica:

```text
Fecha de corte → 30/09/2026

T3 → 01/07/2026 - 30/09/2026
```

---

# 2. Ejercicios resueltos

> **Consejo de estudio:** intenta leer primero el enunciado y pensar qué técnica necesitas. Después comprueba la solución.

---

## Pregunta 1 — JOIN

### Enunciado

El equipo de Datos va a construir la tabla de hechos de ventas internacionales. Antes de automatizar la carga, Tomás te pide comprobar a mano que las facturas cruzan correctamente con sus tres dimensiones: cliente, unidad y cuenta.

Muestra las facturas emitidas en el **T3 de 2026** a clientes de **fuera de España** cuyo importe sea de **al menos 80.000 €**.

Columnas:

- `factura_id`
- `fecha_emision`
- `razon_social`
- `pais`
- `unidad`
- `cuenta`
- `importe`

Orden: de mayor a menor importe.

### Solución

```sql
SELECT
    f.factura_id,
    f.fecha_emision,
    c.razon_social,
    c.pais,
    u.nombre AS unidad,
    cu.nombre AS cuenta,
    f.importe
FROM facturas f
INNER JOIN clientes c
    ON c.cliente_id = f.cliente_id
INNER JOIN unidades u
    ON u.unidad_id = f.unidad_id
INNER JOIN cuentas cu
    ON cu.cuenta_id = f.cuenta_id
WHERE f.fecha_emision >= '2026-07-01'
  AND f.fecha_emision <= '2026-09-30'
  AND c.pais <> 'ES'
  AND f.importe >= 80000
ORDER BY f.importe DESC;
```

### Qué hay que recordar

```text
facturas
   ↓
clientes
unidades
cuentas
```

Y los filtros van en `WHERE`.

---

# Pregunta 2 — Subconsulta escalar

### Enunciado

Antes de publicar la facturación en la capa de consumo, el pipeline debe señalar los valores atípicos para que alguien los revise.

Con una **subconsulta escalar**, lista las facturas cuyo importe supera **el doble del importe medio** de todas las facturas.

Columnas:

- `factura_id`
- `razon_social`
- `fecha_emision`
- `importe`

Orden: de mayor a menor importe.

### Solución

```sql
SELECT
    f.factura_id,
    c.razon_social,
    f.fecha_emision,
    f.importe
FROM facturas f
INNER JOIN clientes c
    ON c.cliente_id = f.cliente_id
WHERE f.importe > (
    SELECT AVG(importe) * 2
    FROM facturas
)
ORDER BY f.importe DESC;
```

### Clave

La subconsulta devuelve **un único número**:

```sql
SELECT AVG(importe) * 2
FROM facturas
```

---

# Pregunta 3 — Subconsultas anidadas

### Enunciado

Riesgos sospecha que los cobros de la cartera que gestionan los empleados con puesto `Comercial` no están bien conciliados y pide una cifra de control antes de lanzar el proceso de conciliación.

**Sin usar `JOIN`**, con subconsultas anidadas a tres niveles, obtén por método de cobro:

- `metodo`
- número de `cobros`
- `importe_cobrado`

Solo se deben considerar facturas de clientes cuyo gestor tiene el puesto `Comercial`.

### Solución

```sql
SELECT
    co.metodo,
    COUNT(*) AS cobros,
    SUM(co.importe) AS importe_cobrado
FROM cobros co
WHERE co.factura_id IN (
    SELECT f.factura_id
    FROM facturas f
    WHERE f.cliente_id IN (
        SELECT c.cliente_id
        FROM clientes c
        WHERE c.gestor_id IN (
            SELECT e.empleado_id
            FROM empleados e
            WHERE e.puesto = 'Comercial'
        )
    )
)
GROUP BY co.metodo
ORDER BY importe_cobrado DESC;
```

### Esquema mental

```text
cobros
  ↓
facturas
  ↓
clientes
  ↓
empleados
```

---

# Pregunta 4 — CTE

### Enunciado

El cálculo «importe cobrado por factura» se va a reutilizar en varios procesos del equipo, así que conviene aislarlo como un paso con nombre.

Define una **CTE** que obtenga el importe cobrado de cada factura y úsala para listar las facturas con **cobro parcial**: han recibido algún cobro, pero no están totalmente cobradas.

Columnas:

- `factura_id`
- `razon_social`
- `importe`
- `cobrado`
- `pendiente`

Orden: de mayor a menor saldo pendiente y, en caso de empate, por `factura_id`.

### Solución

```sql
WITH cobros_por_factura AS (
    SELECT
        factura_id,
        SUM(importe) AS cobrado
    FROM cobros
    GROUP BY factura_id
)
SELECT
    f.factura_id,
    c.razon_social,
    f.importe,
    cpf.cobrado,
    f.importe - cpf.cobrado AS pendiente
FROM facturas f
INNER JOIN clientes c
    ON c.cliente_id = f.cliente_id
INNER JOIN cobros_por_factura cpf
    ON cpf.factura_id = f.factura_id
WHERE cpf.cobrado > 0
  AND cpf.cobrado < f.importe
ORDER BY pendiente DESC, f.factura_id;
```

---

# Pregunta 5 — CTE encadenadas

### Enunciado

El equipo comercial quiere saber en qué países y segmentos de cliente se concentró la facturación del T3.

Resuélvelo como un pipeline de **CTE encadenadas**:

1. `facturas_t3`: facturas del T3.
2. `enriquecidas`: añade país y segmento.
3. `por_segmento`: agrupa por país y segmento.

La consulta final debe mostrar las combinaciones que facturaron **200.000 € o más**.

### Solución

```sql
WITH facturas_t3 AS (
    SELECT *
    FROM facturas
    WHERE fecha_emision >= '2026-07-01'
      AND fecha_emision <= '2026-09-30'
),
enriquecidas AS (
    SELECT
        f.factura_id,
        f.importe,
        c.pais,
        c.segmento
    FROM facturas_t3 f
    INNER JOIN clientes c
        ON c.cliente_id = f.cliente_id
),
por_segmento AS (
    SELECT
        pais,
        segmento,
        COUNT(*) AS facturas,
        SUM(importe) AS importe
    FROM enriquecidas
    GROUP BY pais, segmento
)
SELECT
    pais,
    segmento,
    facturas,
    importe
FROM por_segmento
WHERE importe >= 200000
ORDER BY importe DESC;
```

---

# Pregunta 6 — CTE recursiva

### Enunciado

Para la dimensión organizativa del modelo analítico hay que aplanar la jerarquía que guarda `dbo.unidades`, de modo que cada unidad lleve su profundidad y su ruta completa.

Con una **CTE recursiva** que parta de la unidad raíz, devuelve todas las unidades con:

- `unidad_id`
- `nombre`
- `tipo`
- `nivel`
- `ruta`

La raíz es el nivel `0`.

La ruta debe separar los nombres con `>`.

Orden: por `ruta`.

### Solución

```sql
WITH jerarquia AS (
    SELECT
        unidad_id,
        nombre,
        tipo,
        unidad_padre_id,
        0 AS nivel,
        CAST(nombre AS nvarchar(1000)) AS ruta
    FROM unidades
    WHERE unidad_padre_id IS NULL

    UNION ALL

    SELECT
        u.unidad_id,
        u.nombre,
        u.tipo,
        u.unidad_padre_id,
        j.nivel + 1,
        CAST(j.ruta + N' > ' + u.nombre AS nvarchar(1000))
    FROM unidades u
    INNER JOIN jerarquia j
        ON u.unidad_padre_id = j.unidad_id
)
SELECT
    unidad_id,
    nombre,
    tipo,
    nivel,
    ruta
FROM jerarquia
ORDER BY ruta
OPTION (MAXRECURSION 100);
```

### Muy importante

En una CTE recursiva existen dos partes:

```sql
-- Ancla
SELECT ...

UNION ALL

-- Recursión
SELECT ...
```

---

# Pregunta 7 — Vista

### Enunciado

Hugo Barrios, **Financial Analyst**, monta cada trimestre la cuenta de resultados del grupo en su herramienta de BI. No debe consultar las tablas base ni conocer cómo se cruzan.

Crea la vista:

```text
dbo.vw_cuenta_resultados
```

Debe tener:

- `ejercicio`
- `trimestre`
- `tipo`
- `cuenta`
- `importe`

La vista reúne:

- facturas → ingresos
- gastos → gastos

Las facturas se fechan por `fecha_emision` y los gastos por `fecha`.

### Solución

```sql
CREATE OR ALTER VIEW dbo.vw_cuenta_resultados
AS

SELECT
    p.ejercicio,
    p.trimestre,
    c.tipo,
    c.nombre AS cuenta,
    SUM(f.importe) AS importe
FROM facturas f
INNER JOIN periodos p
    ON f.fecha_emision BETWEEN p.fecha_inicio AND p.fecha_fin
INNER JOIN cuentas c
    ON c.cuenta_id = f.cuenta_id
GROUP BY
    p.ejercicio,
    p.trimestre,
    c.tipo,
    c.nombre

UNION ALL

SELECT
    p.ejercicio,
    p.trimestre,
    c.tipo,
    c.nombre AS cuenta,
    SUM(g.importe) AS importe
FROM gastos g
INNER JOIN periodos p
    ON g.fecha BETWEEN p.fecha_inicio AND p.fecha_fin
INNER JOIN cuentas c
    ON c.cuenta_id = g.cuenta_id
GROUP BY
    p.ejercicio,
    p.trimestre,
    c.tipo,
    c.nombre;
GO
```

Para comprobarla:

```sql
SELECT
    trimestre,
    tipo,
    SUM(importe) AS importe
FROM dbo.vw_cuenta_resultados
GROUP BY trimestre, tipo
ORDER BY trimestre, tipo;
```

---

# Pregunta 8 — Vista + CTE

### Enunciado

Clara Mendiola, **Budget Analyst**, hace el seguimiento del presupuesto de gastos y necesita comparar cada línea presupuestada con lo realmente gastado.

Crea:

```text
dbo.vw_presupuesto_gastos
```

Columnas:

- `ejercicio`
- `trimestre`
- `unidad`
- `cuenta`
- `presupuesto`
- `gasto_real`
- `desviacion`

`gasto_real` debe ser `0` si no existen gastos.

La desviación es:

```text
gasto_real - presupuesto
```

### Solución

```sql
CREATE OR ALTER VIEW dbo.vw_presupuesto_gastos
AS

WITH gasto_real AS (
    SELECT
        g.periodo_id,
        g.unidad_id,
        g.cuenta_id,
        SUM(g.importe) AS gasto_real
    FROM (
        SELECT
            g.*,
            p.periodo_id
        FROM gastos g
        INNER JOIN periodos p
            ON g.fecha BETWEEN p.fecha_inicio AND p.fecha_fin
    ) g
    GROUP BY
        g.periodo_id,
        g.unidad_id,
        g.cuenta_id
)
SELECT
    p.ejercicio,
    p.trimestre,
    u.nombre AS unidad,
    c.nombre AS cuenta,
    pr.importe AS presupuesto,
    COALESCE(gr.gasto_real, 0) AS gasto_real,
    COALESCE(gr.gasto_real, 0) - pr.importe AS desviacion
FROM presupuestos pr
INNER JOIN periodos p
    ON p.periodo_id = pr.periodo_id
INNER JOIN unidades u
    ON u.unidad_id = pr.unidad_id
INNER JOIN cuentas c
    ON c.cuenta_id = pr.cuenta_id
LEFT JOIN gasto_real gr
    ON gr.periodo_id = pr.periodo_id
   AND gr.unidad_id = pr.unidad_id
   AND gr.cuenta_id = pr.cuenta_id
WHERE c.tipo = 'Gasto';
GO
```

Comprobación:

```sql
SELECT
    unidad,
    cuenta,
    presupuesto,
    gasto_real,
    desviacion
FROM dbo.vw_presupuesto_gastos
WHERE ejercicio = 2026
  AND trimestre = 3
  AND desviacion > 5000
ORDER BY desviacion DESC;
```

---

# Pregunta 9 — Vista de riesgo

### Enunciado

Iván Calvo, **Risk Analyst**, revisa cada semana la exposición de crédito de los clientes y necesita una única fuente fiable para su informe.

Crea:

```text
dbo.vw_riesgo_cliente
```

Debe haber una fila por cliente, **incluidos los clientes sin facturas**.

Columnas:

- `cliente_id`
- `razon_social`
- `rating`
- `limite_credito`
- `exposicion`
- `saldo_vencido`

La exposición es la suma de saldos pendientes.

El saldo vencido corresponde a facturas con saldo pendiente cuya fecha de vencimiento es anterior al `30/09/2026`.

### Solución

```sql
CREATE OR ALTER VIEW dbo.vw_riesgo_cliente
AS

WITH cobrado AS (
    SELECT
        factura_id,
        SUM(importe) AS cobrado
    FROM cobros
    GROUP BY factura_id
),
saldo_factura AS (
    SELECT
        f.factura_id,
        f.cliente_id,
        f.fecha_vencimiento,
        f.importe - COALESCE(c.cobrado, 0) AS pendiente
    FROM facturas f
    LEFT JOIN cobrado c
        ON c.factura_id = f.factura_id
)
SELECT
    cl.cliente_id,
    cl.razon_social,
    cl.rating,
    cl.limite_credito,
    COALESCE(SUM(sf.pendiente), 0) AS exposicion,
    COALESCE(
        SUM(
            CASE
                WHEN sf.fecha_vencimiento < '2026-09-30'
                 AND sf.pendiente > 0
                THEN sf.pendiente
                ELSE 0
            END
        ),
        0
    ) AS saldo_vencido
FROM clientes cl
LEFT JOIN saldo_factura sf
    ON sf.cliente_id = cl.cliente_id
GROUP BY
    cl.cliente_id,
    cl.razon_social,
    cl.rating,
    cl.limite_credito;
GO
```

Comprobación:

```sql
SELECT
    razon_social,
    rating,
    limite_credito,
    exposicion,
    saldo_vencido
FROM dbo.vw_riesgo_cliente
WHERE exposicion > limite_credito
ORDER BY exposicion DESC;
```

---

# Pregunta 10 — SELECT INTO

### Enunciado

El equipo de BI va a probar un cuadro de mando nuevo y necesita una copia estática de la facturación del T3 para no trabajar sobre `dbo.facturas`.

Con una instrucción **`SELECT ... INTO`**, crea:

```text
dbo.facturas_2026_t3
```

con las facturas emitidas en el T3 de 2026.

Columnas:

- `factura_id`
- `cliente_id`
- `fecha_emision`
- `fecha_vencimiento`
- `importe`

El script debe poder ejecutarse varias veces sin dar error.

### Solución

```sql
DROP TABLE IF EXISTS dbo.facturas_2026_t3;

SELECT
    factura_id,
    cliente_id,
    fecha_emision,
    fecha_vencimiento,
    importe
INTO dbo.facturas_2026_t3
FROM facturas
WHERE fecha_emision >= '2026-07-01'
  AND fecha_emision <= '2026-09-30';
```

Comprobación:

```sql
SELECT
    COUNT(*) AS facturas,
    SUM(importe) AS importe_total,
    MIN(fecha_emision) AS primera_emision,
    MAX(fecha_emision) AS ultima_emision
FROM dbo.facturas_2026_t3;
```

---

# Pregunta 11 — SELECT INTO + CASE

### Enunciado

La capa de consumo necesita una tabla de facturas con el cliente ya resuelto y el estado de cobro calculado.

Con **`SELECT ... INTO`**, crea:

```text
dbo.facturas_enriquecidas
```

Columnas:

- `factura_id`
- `razon_social`
- `pais`
- `fecha_emision`
- `importe`
- `cobrado`
- `pendiente`
- `estado_cobro`

Estados:

- `Sin cobro` → no ha recibido ningún cobro.
- `Cobro parcial` → ha recibido alguno pero queda saldo.
- `Cobrada` → no queda saldo.

### Solución

```sql
DROP TABLE IF EXISTS dbo.facturas_enriquecidas;

WITH cobros_por_factura AS (
    SELECT
        factura_id,
        SUM(importe) AS cobrado
    FROM cobros
    GROUP BY factura_id
)
SELECT
    f.factura_id,
    c.razon_social,
    c.pais,
    f.fecha_emision,
    f.importe,
    COALESCE(cpf.cobrado, 0) AS cobrado,
    f.importe - COALESCE(cpf.cobrado, 0) AS pendiente,
    CASE
        WHEN COALESCE(cpf.cobrado, 0) = 0
            THEN 'Sin cobro'
        WHEN cpf.cobrado < f.importe
            THEN 'Cobro parcial'
        ELSE 'Cobrada'
    END AS estado_cobro
INTO dbo.facturas_enriquecidas
FROM facturas f
INNER JOIN clientes c
    ON c.cliente_id = f.cliente_id
LEFT JOIN cobros_por_factura cpf
    ON cpf.factura_id = f.factura_id;
```

---

# Pregunta 12 — Tabla temporal

### Enunciado

Tesorería pide dos cifras sobre los cobros del T3.

Crea la tabla temporal:

```text
#cobros_t3
```

con:

- `cobro_id`
- `razon_social`
- `fecha_cobro`
- `importe`
- `metodo`

Después:

**Consulta A:** número de cobros e importe por método.

**Consulta B:** los tres clientes con mayor importe cobrado.

### Solución

```sql
DROP TABLE IF EXISTS #cobros_t3;

SELECT
    co.cobro_id,
    c.razon_social,
    co.fecha_cobro,
    co.importe,
    co.metodo
INTO #cobros_t3
FROM cobros co
INNER JOIN facturas f
    ON f.factura_id = co.factura_id
INNER JOIN clientes c
    ON c.cliente_id = f.cliente_id
WHERE co.fecha_cobro >= '2026-07-01'
  AND co.fecha_cobro <= '2026-09-30';
```

### Consulta A

```sql
SELECT
    metodo,
    COUNT(*) AS cobros,
    SUM(importe) AS importe_cobrado
FROM #cobros_t3
GROUP BY metodo
ORDER BY importe_cobrado DESC;
```

### Consulta B

```sql
SELECT TOP 3
    razon_social,
    SUM(importe) AS importe_cobrado
FROM #cobros_t3
GROUP BY razon_social
ORDER BY importe_cobrado DESC;
```

---

# Pregunta 13 — Tablas temporales + depuración

### Enunciado

El banco ha enviado el lote de cobros de principios de octubre, almacenado en:

```text
dbo.stg_cobros
```

En esta pregunta **no se carga nada** en `dbo.cobros`.

Hay que hacerlo en tres pasos:

1. `#lote_unico`: eliminar filas repetidas.
2. `#lote_valido`: quedarse con las filas que:
   - no existan todavía en `dbo.cobros`;
   - tengan una factura existente;
   - tengan importe mayor que `0`.
3. Hacer dos consultas:
   - Consulta A: número de filas en cada etapa.
   - Consulta B: contenido de `#lote_valido`.

### Solución

#### Paso 1 — Lote sin duplicados

```sql
DROP TABLE IF EXISTS #lote_unico;

SELECT DISTINCT
    cobro_id,
    factura_id,
    fecha_cobro,
    importe,
    metodo
INTO #lote_unico
FROM dbo.stg_cobros;
```

#### Paso 2 — Lote válido

```sql
DROP TABLE IF EXISTS #lote_valido;

SELECT
    l.cobro_id,
    l.factura_id,
    l.fecha_cobro,
    l.importe,
    l.metodo
INTO #lote_valido
FROM #lote_unico l
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.cobros c
    WHERE c.cobro_id = l.cobro_id
)
AND EXISTS (
    SELECT 1
    FROM dbo.facturas f
    WHERE f.factura_id = l.factura_id
)
AND l.importe > 0;
```

#### Consulta A

```sql
SELECT
    'stg_cobros' AS etapa,
    COUNT(*) AS filas
FROM dbo.stg_cobros

UNION ALL

SELECT
    '#lote_unico',
    COUNT(*)
FROM #lote_unico

UNION ALL

SELECT
    '#lote_valido',
    COUNT(*)
FROM #lote_valido

ORDER BY filas DESC;
```

#### Consulta B

```sql
SELECT *
FROM #lote_valido
ORDER BY cobro_id;
```

### Idea importante

Aquí aparecen varias técnicas juntas:

```text
DISTINCT
   ↓
NOT EXISTS
   ↓
EXISTS
   ↓
WHERE importe > 0
```

---

# Pregunta 14 — CTE recursiva de empleados

### Enunciado

El equipo de Datos va a restringir el acceso a la información financiera: solo podrán consultarla las personas que dependen, **directa o indirectamente**, del CFO, Álvaro Montes.

La consulta debe seguir funcionando aunque se añadan o eliminen niveles de mando.

Hay dos opciones:

- subconsultas;
- CTE recursiva.

Hay que elegir la técnica adecuada y obtener los empleados que dependen del CFO, sin incluir al CFO.

Columnas:

- `nombre`
- `puesto`
- `nivel`

Los empleados que dependen directamente del CFO tienen nivel `1`.

Orden:

```text
nivel
nombre
```

### Solución

La técnica correcta es una **CTE recursiva**, porque la profundidad de la jerarquía puede cambiar.

Una cadena fija de subconsultas tendría que conocer de antemano cuántos niveles existen.

```sql
WITH jerarquia AS (
    -- Empleados que dependen directamente del CFO
    SELECT
        e.empleado_id,
        e.nombre,
        e.puesto,
        e.jefe_id,
        1 AS nivel
    FROM empleados e
    WHERE e.jefe_id = (
        SELECT empleado_id
        FROM empleados
        WHERE puesto = 'CFO'
    )

    UNION ALL

    -- Empleados de niveles posteriores
    SELECT
        e.empleado_id,
        e.nombre,
        e.puesto,
        e.jefe_id,
        j.nivel + 1
    FROM empleados e
    INNER JOIN jerarquia j
        ON e.jefe_id = j.empleado_id
)
SELECT
    nombre,
    puesto,
    nivel
FROM jerarquia
ORDER BY nivel, nombre
OPTION (MAXRECURSION 100);
```

### Idea para el examen

Si aparece algo como:

> "directa o indirectamente"

> "jerarquía"

> "niveles"

piensa inmediatamente:

```text
CTE RECURSIVA
```

---

# Pregunta 15 — Elegir entre vista, SELECT INTO y tabla temporal

### Enunciado

Tesorería quiere conservar la **foto de cobros a cierre del T3**: el importe cobrado a cada cliente hasta el `30/09/2026`.

Requisitos:

1. La foto **no debe cambiar** cuando se carguen cobros nuevos.
2. Debe **seguir existiendo en enero**.
3. Cualquier analista debe poder consultarla desde su sesión.
4. Debe crearse y cargarse en **una sola instrucción**.

Las opciones son:

- vista;
- tabla creada con `SELECT INTO`;
- tabla temporal.

Hay que crear:

```text
cierre_cobros_2026_t3
```

Columnas:

- `cliente_id`
- `razon_social`
- `importe_cobrado`
- `fecha_foto`

### Solución

La opción correcta es:

```text
SELECT INTO
```

### ¿Por qué?

**Vista:**

No sirve porque una vista vuelve a ejecutar la consulta sobre los datos actuales. Si posteriormente se cargan nuevos cobros, la "foto" cambiaría.

**Tabla temporal:**

No sirve porque es temporal y no está pensada para permanecer hasta enero ni para que otros analistas la consulten desde sus sesiones.

**SELECT INTO:**

Sí sirve porque crea una tabla física con una **copia estática** de los datos en ese momento.

Además, permite crearla y cargarla en una única instrucción.

### Solución

```sql
SELECT
    c.cliente_id,
    c.razon_social,
    COALESCE(SUM(co.importe), 0) AS importe_cobrado,
    CAST('2026-09-30' AS date) AS fecha_foto
INTO dbo.cierre_cobros_2026_t3
FROM clientes c
LEFT JOIN facturas f
    ON f.cliente_id = c.cliente_id
LEFT JOIN cobros co
    ON co.factura_id = f.factura_id
   AND co.fecha_cobro <= '2026-09-30'
GROUP BY
    c.cliente_id,
    c.razon_social;
```

Comprobación:

```sql
SELECT *
FROM dbo.cierre_cobros_2026_t3
ORDER BY importe_cobrado DESC;
```

---

# 3. Chuleta rápida para el examen

## ¿Qué técnica utilizo?

| Si el enunciado dice... | Piensa en... |
|---|---|
| "Combina tablas" | `JOIN` |
| "Solo coincidencias" | `INNER JOIN` |
| "Todos los clientes aunque no tengan..." | `LEFT JOIN` |
| "Mayor que la media" | Subconsulta escalar |
| "Pertenece a una lista" | `IN` |
| "Existe al menos uno" | `EXISTS` |
| "No existe ninguno" | `NOT EXISTS` |
| "Quiero poner nombre a una consulta" | `CTE` |
| "Varias etapas" | CTE encadenadas |
| "Directa o indirectamente" | CTE recursiva |
| "Guardar una consulta como objeto" | `VIEW` |
| "Copia física" | `SELECT INTO` |
| "Solo durante la sesión" | `#tabla_temporal` |
| "Clasificar según condiciones" | `CASE` |
| "Si es NULL, usa otro valor" | `COALESCE` |

---

## JOIN que debes memorizar

```sql
FROM A
INNER JOIN B
    ON A.id = B.id
```

→ Solo coincidencias.

```sql
FROM A
LEFT JOIN B
    ON A.id = B.id
```

→ Todos los de `A`.

---

## EXISTS

```sql
WHERE EXISTS (
    SELECT 1
    FROM ...
    WHERE ...
)
```

No importa qué devuelve el `SELECT 1`.

Solo pregunta:

> ¿Existe alguna fila?

---

## CTE

```sql
WITH nombre AS (
    SELECT ...
)
SELECT *
FROM nombre;
```

---

## CTE recursiva

```sql
WITH jerarquia AS (

    -- Ancla
    SELECT ...

    UNION ALL

    -- Recursión
    SELECT ...
    FROM tabla t
    JOIN jerarquia j
        ON ...
)
SELECT *
FROM jerarquia
OPTION (MAXRECURSION 100);
```

---

## Vista

```sql
CREATE OR ALTER VIEW dbo.nombre
AS
SELECT ...
GO
```

---

## SELECT INTO

```sql
DROP TABLE IF EXISTS dbo.nombre;

SELECT ...
INTO dbo.nombre
FROM ...;
```

---

## Tabla temporal

```sql
SELECT ...
INTO #nombre
FROM ...;
```

---

## NULL

Nunca:

```sql
WHERE columna = NULL
```

Correcto:

```sql
WHERE columna IS NULL
```

o:

```sql
WHERE columna IS NOT NULL
```

Para sustituirlo:

```sql
COALESCE(columna, 0)
```

---

## Fechas de esta práctica

```text
Fecha de corte:
30/09/2026

T3:
01/07/2026 → 30/09/2026
```

Consulta típica:

```sql
WHERE fecha >= '2026-07-01'
  AND fecha <= '2026-09-30'
```

---

# 4. Estrategia para resolver los ejercicios

Cuando veas un ejercicio en el examen:

### 1. Busca las tablas

Pregúntate:

```text
¿Qué información necesito?
¿En qué tabla está?
¿Cómo se relacionan?
```

### 2. Busca la palabra clave del enunciado

```text
"coinciden"        → JOIN
"todos"            → LEFT JOIN
"lista"            → IN
"existe"           → EXISTS
"no existe"        → NOT EXISTS
"media"            → subconsulta escalar
"CTE"              → WITH
"jerarquía"        → CTE recursiva
"vista"             → CREATE OR ALTER VIEW
"copia"             → SELECT INTO
"temporal"          → #
```

### 3. Haz primero la consulta base

Por ejemplo:

```sql
SELECT ...
FROM ...
JOIN ...
```

Después añade:

```text
WHERE
GROUP BY
HAVING
ORDER BY
```

### 4. Comprueba siempre

Si el ejercicio da una salida esperada, úsala para detectar errores.

Especialmente comprueba:

- número de filas;
- columnas;
- nombres;
- orden;
- `NULL`;
- duplicados;
- filtros de fechas.