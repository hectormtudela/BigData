# Práctica 08. Subqueries

## Ejemplo 1. Subconsulta escalar en `WHERE`

> **Pregunta de negocio:** ¿Qué canciones del catálogo duran más que la media?

**Paso 1.** Resolver la pregunta interna por separado:

```sql
SELECT AVG(duracion_seg) FROM dbo.canciones;
```

![paso1](images/clase11/ej1_paso1.png)

**Paso 2.** Usar ese valor dentro de la consulta principal:

```sql
SELECT titulo, duracion_seg
FROM dbo.canciones
WHERE duracion_seg > (SELECT AVG(duracion_seg) FROM dbo.canciones)
ORDER BY duracion_seg DESC;
```

![paso2](images/clase11/ej1-paso2.png)

## Ejemplo 2. Subconsulta escalar en `SELECT`

> **Pregunta de negocio:** para las canciones de Luna Roja (artista 1), ¿Cuánto se desvía su duración de la media del catálogo?

```sql
SELECT titulo,
       duracion_seg,
       (SELECT AVG(duracion_seg) FROM dbo.canciones) AS media_catalogo,
       duracion_seg - (SELECT AVG(duracion_seg) FROM dbo.canciones) AS diferencia
FROM dbo.canciones
WHERE artista_id = 1;
```

> Para obtener la media con decimales basta con forzar un tipo decimal: `AVG(duracion_seg * 1.0)` devuelve **232.200000**. En ingeniería de datos este truncamiento silencioso es una fuente clásica de errores en informes.

![ej2 paso1](images/clase11/ej2-paso1.png)

## Ejemplo 3. Subconsulta de lista con `IN` (y subconsultas anidadas)

**Pregunta de negocio:** Marketing quiere enviar una notificación a los usuarios que han escuchado alguna canción de **Nébula**.

**Paso 1.** La consulta más interna obtiene el `artista_id` de Nébula (5).
**Paso 2.** La siguiente obtiene las canciones de ese artista (108, 109, 114).
**Paso 3.** La siguiente obtiene los usuarios que han reproducido alguna de esas canciones.
**Paso 4.** La consulta externa muestra los datos de esos usuarios.

```sql
SELECT nombre_usuario, plan_suscripcion
FROM dbo.usuarios
WHERE usuario_id IN (
    SELECT usuario_id
    FROM dbo.reproducciones
    WHERE cancion_id IN (
        SELECT cancion_id
        FROM dbo.canciones
        WHERE artista_id = (SELECT artista_id FROM dbo.artistas WHERE nombre = N'Nébula')
    )
)
ORDER BY nombre_usuario;
```

![ej3 paso1_2_3_4](images/clase11/ej3-paso1-2-3-4.png)

> `IN` elimina duplicados de forma natural: alexbeats ha escuchado varias veces a Nébula, pero aparece una sola vez. Con un `JOIN` habría que añadir `DISTINCT`.

## Ejemplo 4. Tabla derivada en `FROM`

**Pregunta de negocio:** ¿qué usuarios han reproducido 5 o más canciones?

**Paso 1.** La tabla derivada `t` calcula cuántas canciones ha reproducido cada usuario.
**Paso 2.** La consulta externa trata `t` como una tabla más: la une con `usuarios` y filtra.

```sql
SELECT u.nombre_usuario, u.plan_suscripcion, t.num_reproducciones
FROM (
    SELECT usuario_id, COUNT(*) AS num_reproducciones
    FROM dbo.reproducciones
    WHERE tipo_contenido = N'Canción'
    GROUP BY usuario_id
) AS t
JOIN dbo.usuarios AS u ON u.usuario_id = t.usuario_id
WHERE t.num_reproducciones >= 5
ORDER BY t.num_reproducciones DESC, u.nombre_usuario;
```

![ej4](images/clase11/ej4.png)

## Ejemplo 5. Subconsulta correlacionada

**Pregunta de negocio:** Para cada usuario, ¿cuál fue su última reproducción?

**Paso 1.** Para cada fila `r` de la consulta externa, la subconsulta busca la fecha máxima **de ese mismo usuario** (`r2.usuario_id = r.usuario_id`).
**Paso 2.** Solo se quedan las filas cuya fecha coincide con esa fecha máxima.

```sql
SELECT u.nombre_usuario, r.fecha_hora, c.titulo
FROM dbo.reproducciones AS r
JOIN dbo.usuarios AS u ON u.usuario_id = r.usuario_id
LEFT JOIN dbo.canciones AS c ON c.cancion_id = r.cancion_id
WHERE r.fecha_hora = (
    SELECT MAX(r2.fecha_hora)
    FROM dbo.reproducciones AS r2
    WHERE r2.usuario_id = r.usuario_id
)
ORDER BY r.fecha_hora;
```

> `vale_indie` no aparece porque no tiene reproducciones. Conceptualmente, la subconsulta se evalúa una vez por cada fila externa; el optimizador suele reescribirla de forma eficiente, pero en tablas grandes conviene revisar el plan de ejecución (lo veremos en la Sesión 13).

![ej5](images/clase11/ej5.png)

## Ejemplo 6. `EXISTS`

**Pregunta de negocio:** ¿qué artistas han publicado al menos una canción en 2026?

```sql
SELECT a.nombre, a.pais
FROM dbo.artistas AS a
WHERE EXISTS (
    SELECT 1
    FROM dbo.canciones AS c
    WHERE c.artista_id = a.artista_id
      AND c.fecha_lanzamiento >= '2026-01-01'
)
ORDER BY a.nombre;
```

> `EXISTS` se detiene en cuanto encuentra la primera fila que cumple la condición. No le importa cuántas canciones haya: solo si hay alguna.

![ej6](images/clase11/ej6.png)

## Ejemplo 7. La trampa de `NOT IN` con valores `NULL`

**Pregunta de negocio:** ¿Qué canciones del catálogo no se han reproducido nunca?

**Paso 1.** El primer intento con `NOT IN`:

```sql
SELECT cancion_id, titulo
FROM dbo.canciones
WHERE cancion_id NOT IN (SELECT cancion_id FROM dbo.reproducciones);
```

![ej7_paso1](images/clase11/ej7-paso1.png)

**Paso 2.** Entender por qué. La subconsulta devuelve también los `NULL` de los anuncios. `NOT IN (101, 103, NULL, ...)` equivale a `cancion_id <> 101 AND cancion_id <> 103 AND cancion_id <> NULL ...`, y cualquier comparación con `NULL` da `UNKNOWN`. Como la condición completa nunca llega a ser `TRUE`, no se devuelve ninguna fila.

**Paso 3.** La versión correcta con `NOT EXISTS`, que no se ve afectada por los `NULL`:

```sql
SELECT c.cancion_id, c.titulo
FROM dbo.canciones AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.reproducciones AS r
    WHERE r.cancion_id = c.cancion_id
);
```

> **Regla práctica:** para “lo que no está en”, usa `NOT EXISTS`. Si usas `NOT IN`, filtra los nulos dentro de la subconsulta (`WHERE cancion_id IS NOT NULL`). Este fallo es especialmente peligroso en pipelines porque no rompe nada: simplemente deja de cargar datos.

![ej7_paso2](images/clase11/ej7-paso2.png)

## Ejemplo 8. `NOT EXISTS` como anti-join para la carga incremental

**Contexto de ingeniería de datos:** el lote del 21/09 está en `stg_reproducciones`. La app reenvía a veces filas que ya se cargaron (las 32 y 33). Hay que cargar solo las nuevas y que la carga pueda repetirse sin duplicar.

**Paso 1.** Identificar las filas del staging que aún no están en destino:

```sql
SELECT s.reproduccion_id, s.usuario_id, s.cancion_id, s.fecha_hora
FROM dbo.stg_reproducciones AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.reproducciones AS r
    WHERE r.reproduccion_id = s.reproduccion_id
)
ORDER BY s.reproduccion_id;
```

![ej8_paso1](images/clase11/ej8-paso1.png)

**Paso 2.** Convertir esa consulta en la carga:

```sql
INSERT INTO dbo.reproducciones
    (reproduccion_id, usuario_id, cancion_id, fecha_hora, segundos_escuchados, dispositivo, tipo_contenido)
SELECT s.reproduccion_id, s.usuario_id, s.cancion_id, s.fecha_hora,
       s.segundos_escuchados, s.dispositivo, s.tipo_contenido
FROM dbo.stg_reproducciones AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.reproducciones AS r
    WHERE r.reproduccion_id = s.reproduccion_id
);
```

![ej8_paso2](images/clase11/ej8-paso2.png)
**Paso 3.** Ejecutar la misma carga una segunda vez: `(0 rows affected)`. La carga es **idempotente**: repetirla no duplica datos. Este patrón es la base de la carga incremental que automatizaremos en las próximas sesiones.

![ej8_paso3](images/clase11/ej8-paso3.png)

> **A partir de aquí, todos los ejemplos y ejercicios asumen que esta carga ya se ha realizado**
