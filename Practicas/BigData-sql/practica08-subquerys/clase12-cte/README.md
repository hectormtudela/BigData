# Práctica 08. CTE's (Clase 12)

> **Entorno:** SQL Server 2025 desde SSMS 22, base de datos `SonoraDB`.


# Parte 01 · Ejemplos

> Ejecuta los ejemplos que se muestran a continuación. Para cada ejemplo de CTE añade también su equivalente usando **subconsultas**.
> Todos los ejemplos y ejercicios asumen que la carga del Ejemplo 8 (Clase 11) ya se ha realizado.

## Ejemplo 9. CTE simple

> **Pregunta de negocio:** ¿Cuáles son las 3 canciones con más reproducciones válidas?

**Paso 1.** La CTE `validas` aplica la regla de negocio (canción y al menos 30 segundos).
**Paso 2.** La consulta final cuenta por canción y se queda con las 3 primeras.

**Con CTE:**

```sql
WITH validas AS (
    SELECT cancion_id
    FROM dbo.reproducciones
    WHERE tipo_contenido = N'Canción'
      AND segundos_escuchados >= 30
)
SELECT TOP (3) c.titulo, COUNT(*) AS reproducciones_validas
FROM validas AS v
JOIN dbo.canciones AS c ON c.cancion_id = v.cancion_id
GROUP BY c.titulo
ORDER BY reproducciones_validas DESC, c.titulo;
```

![ej9 cte](images/clase12/ej9-cte.png)

**Equivalente con subconsultas:**

```sql
SELECT TOP (3) c.titulo, COUNT(*) AS reproducciones_validas
FROM (
    SELECT cancion_id
    FROM dbo.reproducciones
    WHERE tipo_contenido = N'Canción'
      AND segundos_escuchados >= 30
) AS v
JOIN dbo.canciones AS c ON c.cancion_id = v.cancion_id
GROUP BY c.titulo
ORDER BY reproducciones_validas DESC, c.titulo;
```

![ej9 subconsulta](images/clase12/ej9-subconsulta.png)

## Ejemplo 10. CTE encadenadas como pipeline

> **Pregunta de negocio:** ¿Cuántos minutos válidos se han escuchado por género?



**Con CTE:**

```sql
WITH limpias AS (
    SELECT cancion_id, segundos_escuchados
    FROM dbo.reproducciones
    WHERE tipo_contenido = N'Canción'
      AND segundos_escuchados >= 30
),
enriquecidas AS (
    SELECT l.segundos_escuchados, g.nombre AS genero
    FROM limpias AS l
    JOIN dbo.canciones AS c ON c.cancion_id = l.cancion_id
    JOIN dbo.generos   AS g ON g.genero_id  = c.genero_id
),
agregadas AS (
    SELECT genero,
           COUNT(*) AS reproducciones,
           CAST(SUM(segundos_escuchados) / 60.0 AS decimal(6,1)) AS minutos
    FROM enriquecidas
    GROUP BY genero
)
SELECT genero, reproducciones, minutos
FROM agregadas
ORDER BY minutos DESC, genero;
```

![ej10 cte](images/clase12/ej10-cte.png)

> Para depurar un pipeline de CTE, cambia el `SELECT` final por `SELECT * FROM limpias` o `SELECT * FROM enriquecidas` y revisa cada paso por separado. Se divide en `60.0` y no en `60` para evitar la división entera.

**Equivalente con subconsultas:**

```sql
SELECT genero, reproducciones, minutos
FROM (
    SELECT genero,
           COUNT(*) AS reproducciones,
           CAST(SUM(segundos_escuchados) / 60.0 AS decimal(6,1)) AS minutos
    FROM (
        SELECT l.segundos_escuchados, g.nombre AS genero
        FROM (
            SELECT cancion_id, segundos_escuchados
            FROM dbo.reproducciones
            WHERE tipo_contenido = N'Canción'
              AND segundos_escuchados >= 30
        ) AS l
        JOIN dbo.canciones AS c ON c.cancion_id = l.cancion_id
        JOIN dbo.generos   AS g ON g.genero_id  = c.genero_id
    ) AS enriquecidas
    GROUP BY genero
) AS agregadas
ORDER BY minutos DESC, genero;
```

![ej10 subconsulta](images/clase12/ej10-subconsulta.png)

## Ejemplo 11. CTE recursiva: árbol de géneros

> **Pregunta de negocio:** mostrar el árbol completo de géneros con su nivel de profundidad y su ruta.

**Paso 1. Ancla:** el género raíz, el que no tiene padre (`Música`), con nivel 0.
**Paso 2. Miembro recursivo:** los géneros cuyo padre ya está en la CTE, con nivel + 1 y la ruta ampliada.
**Paso 3.** La recursión termina cuando una vuelta no encuentra más hijos.

**Con CTE:**

```sql
WITH arbol AS (
    SELECT genero_id, nombre, genero_padre_id,
           0 AS nivel,
           CAST(nombre AS nvarchar(200)) AS ruta
    FROM dbo.generos
    WHERE genero_padre_id IS NULL

    UNION ALL

    SELECT g.genero_id, g.nombre, g.genero_padre_id,
           a.nivel + 1,
           CAST(a.ruta + N' > ' + g.nombre AS nvarchar(200))
    FROM dbo.generos AS g
    JOIN arbol AS a ON g.genero_padre_id = a.genero_id
)
SELECT genero_id, nombre, nivel, ruta
FROM arbol
ORDER BY ruta;
```

![ej11 cte](images/clase12/ej11-cte.png)

> Los dos `CAST(... AS nvarchar(200))` son obligatorios. Sin ellos, el ancla devuelve `nvarchar(50)` (el tipo de `nombre`) y el miembro recursivo un `nvarchar` más largo, y SQL Server lanza el error Msg 240 por tipos distintos.

**Equivalente con subconsultas:**

```sql

-- una CTE recursiva no se puede convertir en una subconsulta en el caso general. Una tabla derivada no puede referenciarse a sí misma-

```

![ej11 subconsulta](images/clase12/ej11-subconsulta.png)

## Ejemplo 12. CTE recursiva combinada con agregación

> **Pregunta de negocio:** ¿cuántas reproducciones válidas tiene cada género principal, **contando todos sus subgéneros**? Por ejemplo, Urbano debe sumar Reguetón, Trap, Hip Hop y también Dembow, que cuelga de Reguetón.

**Paso 1. Ancla:** los géneros principales (hijos directos de la raíz). Cada uno se guarda como su propia raíz (`raiz_id`).
**Paso 2. Miembro recursivo:** los descendientes heredan el `raiz_id` de su antepasado.
**Paso 3.** Se unen canciones y reproducciones y se agrupa por la raíz.

**Con CTE:**

```sql
WITH arbol AS (
    SELECT genero_id, genero_id AS raiz_id
    FROM dbo.generos
    WHERE genero_padre_id = (SELECT genero_id FROM dbo.generos WHERE genero_padre_id IS NULL)

    UNION ALL

    SELECT g.genero_id, a.raiz_id
    FROM dbo.generos AS g
    JOIN arbol AS a ON g.genero_padre_id = a.genero_id
)
SELECT gr.nombre AS genero_principal,
       COUNT(r.reproduccion_id) AS reproducciones_validas
FROM arbol AS a
JOIN dbo.generos AS gr ON gr.genero_id = a.raiz_id
LEFT JOIN dbo.canciones AS c ON c.genero_id = a.genero_id
LEFT JOIN dbo.reproducciones AS r
       ON r.cancion_id = c.cancion_id
      AND r.tipo_contenido = N'Canción'
      AND r.segundos_escuchados >= 30
GROUP BY gr.nombre
ORDER BY reproducciones_validas DESC;
```

![ej12 cte](images/clase12/ej12-cte.png)

> Fíjate en que el ancla combina una CTE con una subconsulta escalar para localizar la raíz sin escribir su id a mano.

**Nota sobre el equivalente con subconsultas:**

No existe una traducción directa y general a subconsultas para este patrón recursivo. La recursividad requiere una CTE; una tabla derivada no puede referenciarse a sí misma dentro de la misma consulta.

## Ejemplo 13. CTE recursiva para generar fechas y `MAXRECURSION`

> **Pregunta de negocio:** reproducciones de canciones por día entre el 14/09 y el 22/09, **incluidos los días sin actividad**.

Si agrupamos directamente la tabla `reproducciones`, los días sin datos no aparecen. La solución es generar primero la lista completa de días y después unirla con `LEFT JOIN`.

**Con CTE:**

```sql
WITH dias AS (
    SELECT CAST('2026-09-14' AS date) AS dia
    UNION ALL
    SELECT DATEADD(DAY, 1, dia)
    FROM dias
    WHERE dia < '2026-09-22'
)
SELECT d.dia, COUNT(r.reproduccion_id) AS reproducciones
FROM dias AS d
LEFT JOIN dbo.reproducciones AS r
       ON CAST(r.fecha_hora AS date) = d.dia
      AND r.tipo_contenido = N'Canción'
GROUP BY d.dia
ORDER BY d.dia
OPTION (MAXRECURSION 400);
```

![ej13 cte](images/clase12/ej13-cte.png)

> Aquí solo hay 8 recursiones, pero si generas un año completo (365 días) sin `OPTION (MAXRECURSION ...)`, la consulta falla con el error Msg 530 al llegar a 100. En las próximas sesiones veremos `GENERATE_SERIES`, que genera series sin recursión y es la opción preferente en SQL Server 2022 y 2025.

**Equivalente con subconsultas:**

```sql
SELECT d.dia, COUNT(r.reproduccion_id) AS reproducciones
FROM (
    SELECT DATEADD(DAY, s.value, CAST('2026-09-14' AS date)) AS dia
    FROM GENERATE_SERIES(0, DATEDIFF(DAY, '2026-09-14', '2026-09-22')) AS s
) AS d
LEFT JOIN dbo.reproducciones AS r
       ON CAST(r.fecha_hora AS date) = d.dia
      AND r.tipo_contenido = N'Canción'
GROUP BY d.dia
ORDER BY d.dia;
```

![ej13 subconsulta](images/clase12/ej13-subconsulta.png)

## Ejemplo 14. CTE frente a subconsulta: reutilizar un resultado

> **Pregunta de negocio:** ¿Qué usuarios han escuchado más segundos de música que la media de los usuarios?

La lógica "segundos totales por usuario" se necesita **dos veces**: para listar a cada usuario y para calcular la media. Con una CTE se escribe una sola vez.

**Con CTE:**

```sql
WITH totales AS (
    SELECT usuario_id, SUM(segundos_escuchados) AS segundos
    FROM dbo.reproducciones
    WHERE tipo_contenido = N'Canción'
    GROUP BY usuario_id
)
SELECT u.nombre_usuario,
       t.segundos,
       (SELECT AVG(segundos) FROM totales) AS media_usuarios
FROM totales AS t
JOIN dbo.usuarios AS u ON u.usuario_id = t.usuario_id
WHERE t.segundos > (SELECT AVG(segundos) FROM totales)
ORDER BY t.segundos DESC;
```

![ej14 cte](images/clase12/ej14-cte.png)

**Equivalente con tablas derivadas** (obliga a repetir el bloque de agregación en cada sitio donde se usa):

```sql
SELECT u.nombre_usuario, t.segundos
FROM (SELECT usuario_id, SUM(segundos_escuchados) AS segundos
      FROM dbo.reproducciones
      WHERE tipo_contenido = N'Canción'
      GROUP BY usuario_id) AS t
JOIN dbo.usuarios AS u ON u.usuario_id = t.usuario_id
WHERE t.segundos > (SELECT AVG(t2.segundos)
                    FROM (SELECT usuario_id, SUM(segundos_escuchados) AS segundos
                          FROM dbo.reproducciones
                          WHERE tipo_contenido = N'Canción'
                          GROUP BY usuario_id) AS t2)
ORDER BY t.segundos DESC;
```

![ej14 subconsulta](images/clase12/ej14-subconsulta.png)

| Criterio | Subconsulta / tabla derivada | CTE |
| --- | --- | --- |
| Legibilidad | Se lee de dentro hacia fuera | Se lee de arriba abajo, como una secuencia de pasos |
| Reutilización en la misma consulta | Hay que repetir el código | Se define una vez y se referencia varias veces |
| Recursividad | No | Sí |
| Rendimiento | Equivalente en la mayoría de casos | SQL Server **no materializa** la CTE: si se referencia dos veces, se calcula dos veces |
| Alcance | La instrucción donde se escribe | La instrucción que sigue al `WITH` |

> Si un resultado intermedio se va a usar en varias instrucciones o es costoso de calcular, la opción correcta es materializarlo en una tabla temporal.

---

# Parte 02 · Ejercicios de refuerzo

> Todos los ejercicios se resuelven sobre `SonoraDB` con la carga del Ejemplo 8 ya aplicada (38 reproducciones). Recuerda: una reproducción es válida si es de tipo `Canción` y tiene al menos 30 segundos escuchados.

## Ejercicio 1

El sello de Luna Roja quiere saber qué canciones del catálogo duran más que la canción más larga de Luna Roja. Resuélvelo con una subconsulta escalar que obtenga esa duración máxima a partir del **nombre** del artista. Ordena de mayor a menor duración.

```sql
SELECT titulo, duracion_seg
FROM dbo.canciones
WHERE duracion_seg > (
    SELECT MAX(c.duracion_seg)
    FROM dbo.canciones AS c
    JOIN dbo.artistas AS a ON a.artista_id = c.artista_id
    WHERE a.nombre = N'Luna Roja'
)
ORDER BY duracion_seg DESC;
```

![ejercicio 1](images/clase12/ejercicio1.png)

## Ejercicio 2

El equipo de producto está diseñando una nueva interfaz para televisores. Obtén, con una subconsulta de lista (`IN`), los títulos de las canciones que se han reproducido alguna vez desde un dispositivo `Smart TV`. Ordena alfabéticamente.

```sql
SELECT c.titulo
FROM dbo.canciones AS c
WHERE c.cancion_id IN (
    SELECT r.cancion_id
    FROM dbo.reproducciones AS r
    WHERE r.dispositivo = N'Smart TV'
)
ORDER BY c.titulo ASC;
```

![ejercicio 2](images/clase12/ejercicio2.png)

## Ejercicio 3

El equipo de catálogo necesita detectar artistas fichados que todavía no tienen ninguna canción publicada. Resuélvelo con `NOT EXISTS`.

```sql
SELECT a.artista_id, a.nombre
FROM dbo.artistas AS a
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.canciones AS c
    WHERE c.artista_id = a.artista_id
);
```

![ejercicio 3](images/clase12/ejercicio3.png)

## Ejercicio 4

El equipo comercial quiere ofrecer un descuento en Premium a los usuarios que han escuchado al menos un anuncio. Obtén su nombre de usuario y su plan con `EXISTS`. Ordena por nombre de usuario.

```sql
SELECT u.nombre_usuario, u.plan_suscripcion
FROM dbo.usuarios AS u
WHERE EXISTS (
    SELECT 1
    FROM dbo.reproducciones AS r
    WHERE r.usuario_id = u.usuario_id
      AND r.tipo_contenido = N'Anuncio'
)
ORDER BY u.nombre_usuario ASC;
```

![ejercicio 4](images/clase12/ejercicio4.png)

## Ejercicio 5

Obtén los usuarios con 4 o más reproducciones válidas, mostrando cuántas tienen. Resuélvelo dos veces: primero con una tabla derivada en `FROM` y después reescríbelo con una CTE. Ordena por número de reproducciones descendente y, en caso de empate, por nombre de usuario.

**Con tabla derivada:**

```sql
SELECT u.nombre_usuario, t.reproducciones_validas
FROM (
    SELECT usuario_id, COUNT(*) AS reproducciones_validas
    FROM dbo.reproducciones
    WHERE tipo_contenido = N'Canción'
      AND segundos_escuchados >= 30
    GROUP BY usuario_id
) AS t
JOIN dbo.usuarios AS u ON u.usuario_id = t.usuario_id
WHERE t.reproducciones_validas >= 4
ORDER BY t.reproducciones_validas DESC, u.nombre_usuario;
```

![ejercicio 5 tabla derivada](images/clase12/ejercicio5-derivada.png)

**Con CTE:**

```sql
WITH validas AS (
    SELECT usuario_id, COUNT(*) AS reproducciones_validas
    FROM dbo.reproducciones
    WHERE tipo_contenido = N'Canción'
      AND segundos_escuchados >= 30
    GROUP BY usuario_id
)
SELECT u.nombre_usuario, v.reproducciones_validas
FROM validas AS v
JOIN dbo.usuarios AS u ON u.usuario_id = v.usuario_id
WHERE v.reproducciones_validas >= 4
ORDER BY v.reproducciones_validas DESC, u.nombre_usuario;
```

![ejercicio 5 cte](images/clase12/ejercicio5-cte.png)

## Ejercicio 6

Para las canciones de Nébula y DJ Coral, muestra el título y el número total de reproducciones (válidas o no) de cada una, **incluidas las que no tienen ninguna**. Usa una subconsulta correlacionada en el `SELECT` para el conteo y una subconsulta de lista para filtrar los artistas por nombre. Ordena por número de reproducciones descendente y por título.

```sql
SELECT c.titulo,
       (SELECT COUNT(*)
        FROM dbo.reproducciones AS r
        WHERE r.cancion_id = c.cancion_id) AS total_reproducciones
FROM dbo.canciones AS c
WHERE c.artista_id IN (
    SELECT a.artista_id
    FROM dbo.artistas AS a
    WHERE a.nombre IN (N'Nébula', N'DJ Coral')
)
ORDER BY total_reproducciones DESC, c.titulo;
```

![ejercicio 6](images/clase12/ejercicio6.png)

## Ejercicio 7

Un compañero ha escrito esta consulta para encontrar las canciones que ningún usuario Free ha escuchado nunca, pero devuelve 0 filas:

```sql
SELECT titulo
FROM dbo.canciones
WHERE cancion_id NOT IN (
    SELECT r.cancion_id
    FROM dbo.reproducciones AS r
    JOIN dbo.usuarios AS u ON u.usuario_id = r.usuario_id
    WHERE u.plan_suscripcion = N'Free'
);
```

Explica por qué falla y reescríbela correctamente con `NOT EXISTS`. Ordena por título.

**Explicación:**

La consulta devuelve 0 filas por culpa de los valores NULL. Los usuarios Free han escuchado anuncios, y en esas reproducciones cancion_id es NULL, así que la subconsulta del NOT IN devuelve una lista que contiene un NULL. Como la condición completa nunca llega a ser TRUE, no se devuelve ninguna fila.

**Consulta corregida:**

```sql
SELECT c.titulo
FROM dbo.canciones AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.reproducciones AS r
    JOIN dbo.usuarios AS u ON u.usuario_id = r.usuario_id
    WHERE r.cancion_id = c.cancion_id
      AND u.plan_suscripcion = N'Free'
)
ORDER BY c.titulo;
```

![ejercicio 7](images/clase12/ejercicio7.png)

## Ejercicio 8

La tabla `stg_usuarios` contiene el último lote de altas. Algunos usuarios ya existen en `usuarios`. Primero, escribe la consulta que identifica los usuarios del staging que aún no están cargados. Después, conviértela en un `INSERT ... SELECT` idempotente y comprueba que una segunda ejecución no inserta nada.

**Paso 1.** Consulta que identifica los usuarios nuevos:

```sql
SELECT s.usuario_id, s.nombre_usuario, s.plan_suscripcion
FROM dbo.stg_usuarios AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.usuarios AS u
    WHERE u.usuario_id = s.usuario_id
)
ORDER BY s.usuario_id;
```

![ejercicio 8 paso 1](images/clase12/ejercicio8-paso1.png)

**Paso 2.** Carga con `INSERT ... SELECT`:

```sql
INSERT INTO dbo.usuarios
    (usuario_id, nombre_usuario, email, pais, plan_suscripcion, fecha_alta)
SELECT s.usuario_id, s.nombre_usuario, s.email, s.pais, s.plan_suscripcion, s.fecha_alta
FROM dbo.stg_usuarios AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.usuarios AS u
    WHERE u.usuario_id = s.usuario_id
);
```

![ejercicio 8 paso 2](images/clase12/ejercicio8-paso2.png)

**Paso 3.** Segunda ejecución de la misma carga:

![ejercicio 8 paso 3](images/clase12/ejercicio8-paso3.png)

## Ejercicio 9

El equipo de finanzas quiere saber cuánta música válida se consume según el país del usuario y su plan. Escribe un pipeline de tres CTE encadenadas (**limpiar → enriquecer → agregar**) que devuelva el país, el plan, el número de reproducciones válidas y los minutos escuchados con un decimal. Ordena por minutos de mayor a menor.

```sql
WITH limpias AS (
    SELECT usuario_id, segundos_escuchados
    FROM dbo.reproducciones
    WHERE tipo_contenido = N'Canción'
      AND segundos_escuchados >= 30
),
enriquecidas AS (
    SELECT u.pais, u.plan_suscripcion, l.segundos_escuchados
    FROM limpias AS l
    JOIN dbo.usuarios AS u ON u.usuario_id = l.usuario_id
),
agregadas AS (
    SELECT pais,
           plan_suscripcion,
           COUNT(*) AS reproducciones,
           CAST(SUM(segundos_escuchados) / 60.0 AS decimal(6,1)) AS minutos
    FROM enriquecidas
    GROUP BY pais, plan_suscripcion
)
SELECT pais, plan_suscripcion, reproducciones, minutos
FROM agregadas
ORDER BY minutos DESC;
```

![ejercicio 9](images/clase12/ejercicio9.png)

## Ejercicio 10

Recursos Humanos necesita el organigrama completo de Sonora. Con una CTE recursiva sobre `empleados`, muestra el nombre, el puesto, el nivel (el CEO es nivel 0) y la ruta desde el CEO con el formato `Irene Salas > Tomás Vidal > ...`. Ordena por la ruta.

```sql
WITH organigrama AS (
    SELECT empleado_id, nombre, puesto, jefe_id,
           0 AS nivel,
           CAST(nombre AS nvarchar(200)) AS ruta
    FROM dbo.empleados
    WHERE jefe_id IS NULL

    UNION ALL

    SELECT e.empleado_id, e.nombre, e.puesto, e.jefe_id,
           o.nivel + 1,
           CAST(o.ruta + N' > ' + e.nombre AS nvarchar(200))
    FROM dbo.empleados AS e
    JOIN organigrama AS o ON e.jefe_id = o.empleado_id
)
SELECT nombre, puesto, nivel, ruta
FROM organigrama
ORDER BY ruta;
```

![ejercicio 10](images/clase12/ejercicio10.png)

## Ejercicio 11

El equipo editorial prepara una playlist "Todo Urbano". Obtén todas las canciones del género `Urbano` y de **cualquiera de sus subgéneros**, a cualquier profundidad, con su género concreto y su artista. La CTE recursiva debe partir del nombre del género, no de su id. Ordena por género y título.

```sql
WITH subgeneros AS (
    SELECT genero_id, nombre
    FROM dbo.generos
    WHERE nombre = N'Urbano'

    UNION ALL

    SELECT g.genero_id, g.nombre
    FROM dbo.generos AS g
    JOIN subgeneros AS s ON g.genero_padre_id = s.genero_id
)
SELECT c.titulo, s.nombre AS genero, a.nombre AS artista
FROM subgeneros AS s
JOIN dbo.canciones AS c ON c.genero_id = s.genero_id
JOIN dbo.artistas AS a ON a.artista_id = c.artista_id
ORDER BY s.nombre, c.titulo;
```

![ejercicio 11](images/clase12/ejercicio11.png)

## Ejercicio 12

El CTO, Tomás Vidal, quiere saber quién forma parte de su área, directa o indirectamente. Con una CTE recursiva que parta de Tomás Vidal, muestra el nombre, el puesto y el nivel relativo (sus subordinados directos son nivel 1). No incluyas al propio CTO. Ordena por nivel y nombre.

```sql
WITH area_cto AS (
    SELECT empleado_id, nombre, puesto, 0 AS nivel
    FROM dbo.empleados
    WHERE nombre = N'Tomás Vidal'

    UNION ALL

    SELECT e.empleado_id, e.nombre, e.puesto, a.nivel + 1
    FROM dbo.empleados AS e
    JOIN area_cto AS a ON e.jefe_id = a.empleado_id
)
SELECT nombre, puesto, nivel
FROM area_cto
WHERE nivel > 0
ORDER BY nivel, nombre;
```

![ejercicio 12](images/clase12/ejercicio12.png)