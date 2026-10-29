# Clase 13. Vistas

> **Regla de negocio:** una reproducción es **válida** cuando es de tipo `Canción` y se han escuchado al menos **30 segundos**. Por debajo de 30 segundos es un salto (`skip`).
>
> En los ejemplos y ejercicios que modifican datos se usa `BEGIN TRAN` ... `ROLLBACK` para dejar `SonoraDB` como estaba. Ejecuta cada bloque separado por `GO` de uno en uno y no olvides el `ROLLBACK` final.


# Parte 01 · Ejemplos

## Ejemplo 1. Vista que centraliza una regla de negocio

> **Pregunta de negocio:** en la clase anterior escribimos `tipo_contenido = N'Canción' AND segundos_escuchados >= 30` en casi todas las consultas. Si mañana Producto decide que el umbral es de 35 segundos, habría que buscar y cambiar todas las copias. Queremos escribir la regla una sola vez.

**Paso 1.** Crear la vista con las columnas necesarias (nunca con `SELECT *`, lo veremos en el Ejemplo 8):

```sql
CREATE OR ALTER VIEW dbo.vw_reproducciones_validas AS
SELECT reproduccion_id, usuario_id, cancion_id, fecha_hora, segundos_escuchados, dispositivo
FROM dbo.reproducciones
WHERE tipo_contenido = N'Canción'
  AND segundos_escuchados >= 30;
GO
```

![ej1 paso1](images/clase13/ej1-paso1.png)

**Paso 2.** Usarla como si fuera una tabla:

```sql
SELECT (SELECT COUNT(*) FROM dbo.reproducciones) AS total_reproducciones,
       (SELECT COUNT(*) FROM dbo.vw_reproducciones_validas) AS reproducciones_validas;
```

![ej1 paso2](images/clase13/ej1-paso2.png)

**Paso 3.** Filtrar y ordenar desde fuera, como en cualquier tabla. Reproducciones válidas de sofi.trap (usuario 4):

```sql
SELECT reproduccion_id, cancion_id, fecha_hora, segundos_escuchados, dispositivo
FROM dbo.vw_reproducciones_validas
WHERE usuario_id = 4
ORDER BY fecha_hora;
```

![ej1 paso3](images/clase13/ej1-paso3.png)

> Quien consulta la vista no tiene que conocer la regla: la hereda.

## Ejemplo 2. Vista que oculta columnas sensibles

> **Pregunta de negocio:** el equipo de Atención al cliente necesita consultar usuarios, pero no debe ver el email (dato personal).

```sql
CREATE OR ALTER VIEW dbo.vw_usuarios_directorio AS
SELECT usuario_id, nombre_usuario, pais, plan_suscripcion, fecha_alta
FROM dbo.usuarios;
GO

SELECT usuario_id, nombre_usuario, plan_suscripcion, fecha_alta
FROM dbo.vw_usuarios_directorio
WHERE pais = 'ES'
ORDER BY fecha_alta;
```

![ej2](images/clase13/ej2.png)

> Una vista puede restringir **columnas** (seguridad vertical, como aquí) o **filas** con un `WHERE` (seguridad horizontal, lo veremos en el Ejemplo 9). Que la vista oculte el email no impide por sí sola que alguien consulte la tabla: para eso hace falta además gestionar permisos, que se estudian en la sesión de DCL.

## Ejemplo 3. Vista sobre vista: reproducciones enriquecidas

> **Pregunta de negocio:** casi todos los informes necesitan la reproducción válida junto con el usuario, la canción, el artista y el género. Son cuatro `JOIN` que todo el mundo repite.

**Paso 1.** Crear una vista que parte de `vw_reproducciones_validas` (una vista puede leer de otra vista) y añade el contexto:

```sql
CREATE OR ALTER VIEW dbo.vw_reproducciones_detalle AS
SELECT v.reproduccion_id, v.fecha_hora,
       u.usuario_id, u.nombre_usuario, u.pais AS pais_usuario, u.plan_suscripcion,
       c.titulo, a.nombre AS artista, g.nombre AS genero,
       v.dispositivo, v.segundos_escuchados
FROM dbo.vw_reproducciones_validas AS v
JOIN dbo.usuarios  AS u ON u.usuario_id  = v.usuario_id
JOIN dbo.canciones AS c ON c.cancion_id  = v.cancion_id
JOIN dbo.artistas  AS a ON a.artista_id  = c.artista_id
JOIN dbo.generos   AS g ON g.genero_id   = c.genero_id;
GO
```

![ej3 paso1](images/clase13/ej3-paso1.png)

**Paso 2.** Con la vista, una pregunta como *"¿qué artistas escuchan los usuarios de México?"* se resuelve sin ningún `JOIN`:

```sql
SELECT artista,
       COUNT(*) AS reproducciones,
       COUNT(DISTINCT usuario_id) AS oyentes
FROM dbo.vw_reproducciones_detalle
WHERE pais_usuario = 'MX'
GROUP BY artista
ORDER BY reproducciones DESC, artista;
```

![ej3 paso2](images/clase13/ej3-paso2.png)

> SQL Server **expande** las vistas antes de ejecutar: sustituye `vw_reproducciones_detalle` por su definición, que a su vez contiene la de `vw_reproducciones_validas`, y optimiza la consulta completa. El filtro `pais_usuario = 'MX'` se aplica directamente sobre `usuarios`; no se calcula primero la vista entera. Aun así, encadenar muchas vistas unas sobre otras hace los planes difíciles de leer: dos o tres niveles es un límite razonable.

## Ejemplo 4. Vista con agregación: indicadores por canción

> **Pregunta de negocio:** el equipo de catálogo consulta a diario los indicadores de cada canción. Deben aparecer **todas** las canciones, también las que no tienen ninguna reproducción válida.

**Paso 1.** Crear la vista con `LEFT JOIN` desde `canciones` y agregación:

```sql
CREATE OR ALTER VIEW dbo.vw_kpi_cancion AS
SELECT c.cancion_id, c.titulo, a.nombre AS artista, c.fecha_lanzamiento,
       COUNT(v.reproduccion_id) AS reproducciones_validas,
       COUNT(DISTINCT v.usuario_id) AS oyentes,
       CAST(COALESCE(SUM(v.segundos_escuchados), 0) / 60.0 AS decimal(6,1)) AS minutos
FROM dbo.canciones AS c
JOIN dbo.artistas AS a ON a.artista_id = c.artista_id
LEFT JOIN dbo.vw_reproducciones_validas AS v ON v.cancion_id = c.cancion_id
GROUP BY c.cancion_id, c.titulo, a.nombre, c.fecha_lanzamiento;
GO
```

![ej4 paso1](images/clase13/ej4-paso1.png)

**Paso 2.** Canciones sin ninguna reproducción válida:

```sql
SELECT titulo, artista, fecha_lanzamiento
FROM dbo.vw_kpi_cancion
WHERE reproducciones_validas = 0
ORDER BY titulo;
```

![ej4 paso2](images/clase13/ej4-paso2.png)

**Paso 3.** Las 3 canciones con más minutos escuchados:

```sql
SELECT TOP (3) titulo, artista, reproducciones_validas, oyentes, minutos
FROM dbo.vw_kpi_cancion
ORDER BY minutos DESC;
```

![ej4 paso3](images/clase13/ej4-paso3.png)

> En la pestaña Messages puede aparecer `Warning: Null value is eliminated by an aggregate or other SET operation.` Es normal: las canciones sin reproducciones aportan `NULL` a `COUNT(DISTINCT ...)` y `SUM(...)`. No es un error.

## Ejemplo 5. La trampa de `ORDER BY` en una vista

> **Pregunta de negocio:** queremos que el catálogo salga "siempre ordenado" por duración.

**Paso 1.** El primer intento:

```sql
CREATE OR ALTER VIEW dbo.vw_canciones_ordenadas AS
SELECT titulo, duracion_seg
FROM dbo.canciones
ORDER BY duracion_seg DESC;
GO
```

![ej5 paso1](images/clase13/ej5-paso1.png)

**Paso 2.** El "truco" que circula por internet: añadir `TOP (100) PERCENT`.

```sql
CREATE OR ALTER VIEW dbo.vw_canciones_ordenadas AS
SELECT TOP (100) PERCENT titulo, duracion_seg
FROM dbo.canciones
ORDER BY duracion_seg DESC;
GO
```

![ej5 paso2](images/clase13/ej5-paso2.png)

**Paso 3.** La forma correcta: la vista no ordena; ordena quien la consulta.

```sql
DROP VIEW IF EXISTS dbo.vw_canciones_ordenadas;
GO

SELECT titulo, duracion_seg
FROM dbo.canciones
ORDER BY duracion_seg DESC;
```

![ej5 paso3](images/clase13/ej5-paso3.png)

> Una vista representa un conjunto de filas, y un conjunto no tiene orden. Esto es especialmente importante en BI: Power BI ignora el orden de origen y aplica el suyo.

## Ejemplo 6. Vista con CTE recursiva: género principal de cada subgénero

> **Pregunta de negocio:** cada subgénero, a cualquier profundidad, cuenta para su género principal (hijo directo de `Música`). La CTE recursiva que lo resuelve la hemos escrito varias veces. La guardamos como vista para no volver a escribirla.

**Paso 1.** Una vista puede contener CTE, incluidas las recursivas. La definición empieza directamente con `WITH`:

```sql
CREATE OR ALTER VIEW dbo.vw_genero_principal AS
WITH arbol AS (
    SELECT genero_id, genero_id AS raiz_id
    FROM dbo.generos
    WHERE genero_padre_id = (SELECT genero_id FROM dbo.generos WHERE genero_padre_id IS NULL)

    UNION ALL

    SELECT g.genero_id, a.raiz_id
    FROM dbo.generos AS g
    JOIN arbol AS a ON g.genero_padre_id = a.genero_id
)
SELECT a.genero_id, g.nombre AS genero, r.nombre AS genero_principal
FROM arbol AS a
JOIN dbo.generos AS g ON g.genero_id = a.genero_id
JOIN dbo.generos AS r ON r.genero_id = a.raiz_id;
GO

SELECT genero_id, genero, genero_principal
FROM dbo.vw_genero_principal
ORDER BY genero_principal, genero;
```

![ej6 paso1](images/clase13/ej6-paso1.png)

**Paso 2.** Ahora la pregunta *"reproducciones válidas por género principal"* combina dos vistas y una tabla:

```sql
SELECT gp.genero_principal,
       COUNT(*) AS reproducciones_validas,
       CAST(SUM(v.segundos_escuchados) / 60.0 AS decimal(6,1)) AS minutos
FROM dbo.vw_reproducciones_validas AS v
JOIN dbo.canciones AS c ON c.cancion_id = v.cancion_id
JOIN dbo.vw_genero_principal AS gp ON gp.genero_id = c.genero_id
GROUP BY gp.genero_principal
ORDER BY reproducciones_validas DESC;
```

![ej6 paso2](images/clase13/ej6-paso2.png)

> La cláusula `OPTION (MAXRECURSION n)` no se puede escribir dentro de la vista. Si una jerarquía necesitara más de 100 niveles, el `OPTION` se añade al final de la consulta que usa la vista.

## Ejemplo 7. Consultar las vistas que existen y sus dependencias

> **Contexto de ingeniería de datos:** antes de modificar una tabla hay que saber qué objetos dependen de ella. Es el **análisis de impacto**, y SQL Server guarda la información necesaria en sus vistas de catálogo.

**Paso 1.** Listar las vistas de la base de datos:

```sql
SELECT name AS vista
FROM sys.views
ORDER BY name;
```

![ej7 paso1](images/clase13/ej7-paso1.png)

**Paso 2.** Ver la definición de una vista:

```sql
EXEC sp_helptext N'dbo.vw_reproducciones_validas';
```

![ej7 paso2](images/clase13/ej7-paso2.png)

> En SSMS 22 también se obtiene con clic derecho sobre la vista → Script View as → CREATE To.

**Paso 3.** ¿Qué objetos dependen de la tabla `reproducciones`?

```sql
SELECT referencing_schema_name, referencing_entity_name
FROM sys.dm_sql_referencing_entities(N'dbo.reproducciones', N'OBJECT')
ORDER BY referencing_entity_name;
```

![ej7 paso3](images/clase13/ej7-paso3.png)

**Paso 4.** Solo aparecen las dependencias **directas**. Para seguir la cadena hay que preguntar por la vista:

```sql
SELECT referencing_schema_name, referencing_entity_name
FROM sys.dm_sql_referencing_entities(N'dbo.vw_reproducciones_validas', N'OBJECT')
ORDER BY referencing_entity_name;
```

![ej7 paso4](images/clase13/ej7-paso4.png)

## Ejemplo 8. La trampa de `SELECT *` en una vista

> **Contexto:** SQL Server guarda la lista de columnas de la vista en el momento de crearla. Si después cambia la tabla, la vista no se entera.

**Paso 1.** Preparar una copia de `artistas` para no tocar las tablas del caso y crear sobre ella una vista con `SELECT *`:

```sql
DROP VIEW IF EXISTS dbo.vw_demo_artistas;
DROP TABLE IF EXISTS dbo.demo_artistas;
CREATE TABLE dbo.demo_artistas (
    artista_id int NOT NULL,
    nombre nvarchar(100) NOT NULL,
    pais char(2) NOT NULL
);
INSERT INTO dbo.demo_artistas (artista_id, nombre, pais)
SELECT artista_id, nombre, pais FROM dbo.artistas;
GO

CREATE OR ALTER VIEW dbo.vw_demo_artistas AS
SELECT * FROM dbo.demo_artistas;
GO

SELECT * FROM dbo.vw_demo_artistas WHERE artista_id <= 2;
```

![ej8 paso1](images/clase13/ej8-paso1.png)

**Paso 2.** Añadir una columna a la tabla y volver a consultar la vista:

```sql
ALTER TABLE dbo.demo_artistas ADD sello nvarchar(50) NULL;
GO
UPDATE dbo.demo_artistas SET sello = N'Sello Norte' WHERE artista_id = 1;
SELECT * FROM dbo.vw_demo_artistas WHERE artista_id <= 2;
```

![ej8 paso2](images/clase13/ej8-paso2.png)

**Paso 3.** Refrescar los metadatos de la vista:

```sql
  EXEC sp_refreshview N'dbo.vw_demo_artistas';
  SELECT * FROM dbo.vw_demo_artistas WHERE artista_id <= 2;
```

![ej8 paso3](images/clase13/ej8-paso3.png)

**Paso 4.** Limpiar los objetos de la demostración:

```sql
DROP VIEW IF EXISTS dbo.vw_demo_artistas;
DROP TABLE IF EXISTS dbo.demo_artistas;
```

![ej8 paso4](images/clase13/ej8-paso4.png)

> Añadir una columna es el caso inofensivo. Si se elimina o se reordenan columnas de la tabla, una vista con `SELECT *` puede fallar o, peor, devolver datos bajo el nombre de otra columna sin dar ningún error. **Regla:** en una vista, siempre lista explícita de columnas.

## Ejemplo 9. Una vista de filas y el efecto de `WITH CHECK OPTION`

> **Pregunta de negocio:** el equipo de conversión trabaja solo con usuarios Free.

**Paso 1.** Crear la vista sin `CHECK OPTION` y consultarla:

```sql
CREATE OR ALTER VIEW dbo.vw_usuarios_free AS
SELECT usuario_id, nombre_usuario, pais, plan_suscripcion, fecha_alta
FROM dbo.usuarios
WHERE plan_suscripcion = N'Free';
GO

SELECT usuario_id, nombre_usuario, pais, plan_suscripcion
FROM dbo.vw_usuarios_free
ORDER BY usuario_id;
```

![ej9 paso1](images/clase13/ej9-paso1.png)

**Paso 2.** Cambiar el plan de nachox **a través de la vista**, dentro de una transacción:

```sql
BEGIN TRAN;
UPDATE dbo.vw_usuarios_free
SET plan_suscripcion = N'Premium'
WHERE nombre_usuario = N'nachox';

SELECT COUNT(*) AS usuarios_free FROM dbo.vw_usuarios_free;
SELECT nombre_usuario, plan_suscripcion FROM dbo.usuarios WHERE nombre_usuario = N'nachox';
ROLLBACK;
```

![ej9 paso2](images/clase13/ej9-paso2.png)

**Paso 3.** Añadir `WITH CHECK OPTION` y repetir el mismo `UPDATE`:

```sql
CREATE OR ALTER VIEW dbo.vw_usuarios_free AS
SELECT usuario_id, nombre_usuario, pais, plan_suscripcion, fecha_alta
FROM dbo.usuarios
WHERE plan_suscripcion = N'Free'
WITH CHECK OPTION;
GO

UPDATE dbo.vw_usuarios_free
SET plan_suscripcion = N'Premium'
WHERE nombre_usuario = N'nachox';
```

>La vista solo permite ver usuarios cuyo plan es Free. Al hacer el UPDATE y cambiar a Premium, nachox dejaría de cumplir la condición de la vista. Como tiene WITH CHECK OPTION, SQL Server impide cualquier modificación que haga que una fila deje de cumplir el filtro de la vista.

![ej9 paso3](images/clase13/ej9-paso3.png)

**Paso 4.** Los cambios que mantienen la fila dentro de la vista sí se permiten:

```sql
BEGIN TRAN;
UPDATE dbo.vw_usuarios_free SET pais = 'AR' WHERE nombre_usuario = N'nachox';
ROLLBACK;
```

![ej9 paso4](images/clase13/ej9-paso4.png)

> `WITH CHECK OPTION` convierte el filtro de la vista en una regla de escritura. Es la forma de dar a un equipo permiso para mantener "sus" filas sin que pueda sacarlas, por error, de su ámbito.

## Ejemplo 10. Cuándo una vista no es actualizable

**Paso 1.** Intentar renombrar una canción a través de `vw_kpi_cancion`, que tiene `GROUP BY`:

```sql
UPDATE dbo.vw_kpi_cancion
SET titulo = N'Perreo Lunar (Remix)'
WHERE titulo = N'Perreo Lunar';
```

> las vistas que contienen `GROUP BY` o funciones de agregación no se pueden modificar directamente mediante `UPDATE`.

![ej10 paso1](images/clase13/ej10-paso1.png)

**Paso 2.** Intentar cambiar a la vez el título (tabla `canciones`) y el artista (tabla `artistas`) a través de `vw_reproducciones_detalle`:

```sql
UPDATE dbo.vw_reproducciones_detalle
SET titulo = N'Perreo Lunar (Remix)', artista = N'MC Brisa & Nébula'
WHERE reproduccion_id = 1;
```

> Una vista con `JOIN` puede ser actualizable en algunos casos, pero no puedes modificar mediante ella columnas que pertenecen a varias tablas.

![ej10 paso2](images/clase13/ej10-paso2.png)

> Ninguna de las dos sentencias llega a ejecutarse: SQL Server las rechaza al compilarlas, así que no hace falta transacción. Que una vista tenga `JOIN` no la hace no actualizable: lo que no se permite es que **una misma sentencia** toque columnas de más de una tabla base.

## Ejemplo 11. Proteger una vista con `SCHEMABINDING`

> **Pregunta de negocio:** el catálogo que consume la app de los sellos no puede romperse porque alguien cambie una tabla sin avisar.

**Paso 1.** Primer intento, con `SELECT *`:

```sql
CREATE OR ALTER VIEW dbo.vw_catalogo_canciones
WITH SCHEMABINDING AS
SELECT * FROM dbo.canciones;
GO
```

> SCHEMABINDING exige que las dependencias de la vista estén definidas de forma explícita, por eso SELECT * no está permitido.

![ej11 paso1](images/clase13/ej11-paso1.png)

**Paso 2.** Segundo intento, con columnas explícitas pero el nombre de la tabla sin esquema:

```sql
CREATE OR ALTER VIEW dbo.vw_catalogo_canciones
WITH SCHEMABINDING AS
SELECT cancion_id, titulo
FROM canciones;
GO
```

> SCHEMABINDING exige que las tablas referenciadas estén especificadas con su esquema (dbo.tabla).

![ej11 paso2](images/clase13/ej11-paso2.png)

**Paso 3.** La versión correcta:

```sql
CREATE OR ALTER VIEW dbo.vw_catalogo_canciones
WITH SCHEMABINDING AS
SELECT c.cancion_id, c.titulo, a.nombre AS artista, c.duracion_seg, c.fecha_lanzamiento
FROM dbo.canciones AS c
JOIN dbo.artistas AS a ON a.artista_id = c.artista_id;
GO
```

![ej11 paso3](images/clase13/ej11-paso3.png)

**Paso 4.** Un compañero intenta ampliar la columna `titulo`:

```sql
ALTER TABLE dbo.canciones ALTER COLUMN titulo nvarchar(200) NOT NULL;
```

> SCHEMABINDING protege la estructura de las tablas utilizadas por la vista frente a cambios que puedan romperla.

![ej11 paso4](images/clase13/ej11-paso4.png)

> El cambio se bloquea **antes** de romper nada. Para hacerlo de forma controlada hay que: (1) quitar el `SCHEMABINDING` de la vista o eliminarla, (2) modificar la tabla, (3) volver a crear la vista. Añadir una columna nueva a `canciones` sí estaría permitido, porque la vista no la usa.

## Ejemplo 12. Vista materializada para el indicador más consultado

> **Pregunta de negocio:** el contador de reproducciones válidas por canción aparece en la app, en la web y en los informes de los sellos. Se consulta miles de veces al día y hoy se recalcula en cada consulta.

**Paso 1.** Crear la vista con los requisitos de una vista indexada (tabla base, nombres de dos partes, `COUNT_BIG(*)` y `SUM` sobre una columna `NOT NULL`):

```sql
DROP VIEW IF EXISTS dbo.vw_ix_consumo_cancion;
GO
CREATE VIEW dbo.vw_ix_consumo_cancion
WITH SCHEMABINDING AS
SELECT cancion_id,
       COUNT_BIG(*) AS reproducciones_validas,
       SUM(segundos_escuchados) AS segundos
FROM dbo.reproducciones
WHERE tipo_contenido = N'Canción'
  AND segundos_escuchados >= 30
GROUP BY cancion_id;
GO
```

![ej12 paso1](images/clase13/ej12-paso1.png)

**Paso 2.** Crear el índice clustered único. En este momento el resultado se calcula y se guarda:

```sql
CREATE UNIQUE CLUSTERED INDEX IX_vw_ix_consumo_cancion
ON dbo.vw_ix_consumo_cancion (cancion_id);
GO

SELECT COUNT(*) AS filas_guardadas
FROM dbo.vw_ix_consumo_cancion WITH (NOEXPAND);
```

![ej12 paso2](images/clase13/ej12-paso2.png)

**Paso 3.** Consultarla con `NOEXPAND`:

```sql
SELECT TOP (5) c.titulo, v.reproducciones_validas,
       CAST(v.segundos / 60.0 AS decimal(6,1)) AS minutos
FROM dbo.vw_ix_consumo_cancion AS v WITH (NOEXPAND)
JOIN dbo.canciones AS c ON c.cancion_id = v.cancion_id
ORDER BY v.reproducciones_validas DESC, v.segundos DESC;
```

![ej12 paso3](images/clase13/ej12-paso3.png)

> La media y los minutos no se guardan (`AVG` y las expresiones sobre agregados no están permitidos), pero se calculan al consultar: `segundos / 60.0` o `segundos * 1.0 / reproducciones_validas`. `WITH (NOEXPAND)` es una indicación para el optimizador que obliga a leer el resultado guardado. Sin la sugerencia, el optimizador puede decidir expandir la vista y recalcular desde `reproducciones`; en algunas ediciones de SQL Server nunca usa la vista indexada automáticamente, así que la práctica recomendada es indicar siempre `NOEXPAND`.

**Paso 4.** Comprobar que el resultado guardado se mantiene solo. Latido no tiene reproducciones válidas; insertamos una dentro de una transacción:

```sql
BEGIN TRAN;
INSERT INTO dbo.reproducciones
    (reproduccion_id, usuario_id, cancion_id, fecha_hora, segundos_escuchados, dispositivo, tipo_contenido)
VALUES (44, 8, 115, '2026-09-22 12:00', 330, N'Móvil', N'Canción');

SELECT cancion_id, reproducciones_validas, segundos
FROM dbo.vw_ix_consumo_cancion WITH (NOEXPAND)
WHERE cancion_id = 115;
ROLLBACK;
```

![ej12 paso4](images/clase13/ej12-paso4.png)

---

# Parte 02 · Ejercicios de refuerzo

> Todos los ejercicios se resuelven sobre `SonoraDB` con el entorno preparado al inicio de la clase (43 reproducciones y 10 usuarios) y las vistas de la teoría ya creadas. Recuerda: una reproducción es válida si es de tipo `Canción` y tiene al menos 30 segundos escuchados. Los ejercicios que modifican datos se hacen dentro de `BEGIN TRAN` ... `ROLLBACK`, ejecutando cada bloque separado por `GO` de uno en uno.

## Ejercicio 1

El equipo comercial vende los huecos publicitarios y quiere una vista `dbo.vw_anuncios` con las reproducciones de tipo `Anuncio`: identificador de reproducción, usuario, fecha y hora, y dispositivo. Después, consulta la vista para obtener cuántos anuncios se han emitido por dispositivo y a cuántos usuarios distintos. Ordena por número de anuncios descendente y por dispositivo.

```sql
CREATE VIEW dbo.vw_anuncios AS
SELECT reproducciones.reproduccion_id, usuarios.nombre_usuario, reproducciones.fecha_hora, reproducciones.dispositivo
FROM reproducciones
INNER JOIN usuarios ON usuarios.usuario_id = reproducciones.usuario_id
WHERE reproducciones.tipo_contenido = N'Anuncio';

SELECT dispositivo, COUNT(reproduccion_id) as anuncios_por_dispositivo, COUNT(DISTINCT nombre_usuario) as num_usuarios
FROM dbo.vw_anuncios
GROUP BY dispositivo
ORDER BY anuncios_por_dispositivo DESC, dispositivo;
```

![ejercicio 1](images/clase13/ejercicio1-paso1.png)
![ejercicio 1](images/clase13/ejercicio1-paso2.png)


## Ejercicio 2

Crea la vista `dbo.vw_usuarios_pago` con los usuarios de los planes `Premium` y `Familiar`, sin la columna `email`. Consulta la vista ordenando por fecha de alta.

```sql
CREATE VIEW dbo.vw_usuarios_pago AS
SELECT usuario_id, nombre_usuario, pais, plan_suscripcion, fecha_alta
FROM usuarios
WHERE plan_suscripcion = N'Premium' OR plan_suscripcion = N'Familiar';

SELECT * 
FROM dbo.vw_usuarios_pago
ORDER BY fecha_alta;
```

![ejercicio 2](images/clase13/ejercicio2.png)

## Ejercicio 3

Producto estudia por qué los usuarios saltan canciones. Crea la vista `dbo.vw_saltos` con las reproducciones de tipo `Canción` de menos de 30 segundos: identificador, usuario, canción, fecha y hora, y segundos escuchados. Después, consulta la vista uniéndola con `usuarios` y `canciones` para mostrar el nombre de usuario, el título, los segundos escuchados y la fecha y hora, ordenado por fecha y hora.

```sql
DROP VIEW IF EXISTS dbo.vw_saltos
GO

CREATE VIEW dbo.vw_saltos AS
SELECT reproduccion_id, usuario_id, cancion_id, fecha_hora, segundos_escuchados
FROM reproducciones
WHERE tipo_contenido = N'Canción' AND segundos_escuchados < 30;
GO

SELECT usuarios.nombre_usuario, canciones.titulo, vw_saltos.segundos_escuchados, vw_saltos.fecha_hora
FROM vw_saltos
INNER JOIN usuarios ON usuarios.usuario_id = vw_saltos.usuario_id
INNER JOIN canciones ON canciones.cancion_id = vw_saltos.cancion_id
ORDER BY vw_saltos.fecha_hora
GO
```

![ejercicio 3](images/clase13/ejercicio3.png)

## Ejercicio 4

El equipo editorial necesita una ficha de catálogo. Crea la vista `dbo.vw_catalogo_detalle` con el identificador y el título de la canción, el nombre del artista (`artista`), el país del artista (`pais_artista`), el nombre del género (`genero`), la duración en segundos (`duracion_seg`) y la duración en minutos con un decimal (`duracion_min`). Consulta las canciones de artistas españoles ordenadas por título. ¿Por qué no aparece Sara Cometa, que es española?

```sql
DROP VIEW IF EXISTS dbo.vw_catalogo_detalle
GO

CREATE VIEW dbo.vw_catalogo_detalle AS
SELECT canciones.cancion_id, canciones.titulo, artistas.nombre as artista, 
artistas.pais as pais_artista, generos.nombre as genero, canciones.duracion_seg, 
ROUND(duracion_seg / 60, 1) as duracion_min
FROM canciones 
INNER JOIN artistas ON artistas.artista_id = canciones.artista_id
INNER JOIN generos ON generos.genero_id = artistas.genero_id;
GO

SELECT *
FROM vw_catalogo_detalle
WHERE pais_artista = N'ES'
ORDER BY titulo
GO
```

**Explicación:**

Sara Cometa no aparece porque el INNER JOIN con generos elimina las canciones cuyo artista no tiene un género asociado. Con LEFT JOIN solucionamos el problema.

![ejercicio 4](images/clase13/ejercicio4.png)

## Ejercicio 5

Un compañero ha intentado crear esta vista para el equipo de producto y no consigue que funcione:

```sql
CREATE VIEW dbo.vw_canciones_por_dispositivo AS
SELECT dispositivo, COUNT(*)
FROM dbo.reproducciones
WHERE tipo_contenido = N'Canción'
GROUP BY dispositivo
ORDER BY COUNT(*) DESC;
```



**Explicación de los dos problemas:**

1. Falta ponerle alias a COUNT(*)
2. No se puede usar ORDER BY dentro de una vista así

**Vista corregida y consulta:**

```sql

CREATE VIEW dbo.vw_canciones_por_dispositivo AS
SELECT dispositivo, COUNT(*) as reproducciones
FROM dbo.reproducciones
WHERE tipo_contenido = N'Canción'
GROUP BY dispositivo;
```

![ejercicio 5](images/clase13/ejercicio5.png)

## Ejercicio 6

Crea la vista `dbo.vw_kpi_usuario` con una fila por usuario, **incluidos los que no tienen actividad**: identificador, nombre de usuario, plan, país, número de reproducciones válidas (`reproducciones_validas`), minutos escuchados con un decimal (`minutos`) y fecha y hora de su última reproducción válida (`ultima_reproduccion_valida`). Reutiliza `dbo.vw_reproducciones_validas`. Después, con dos consultas sobre la vista:

**Vista:**

```sql
CREATE OR ALTER VIEW dbo.vw_reproducciones_validas AS
SELECT reproduccion_id, usuario_id, cancion_id, fecha_hora, segundos_escuchados, dispositivo
FROM dbo.reproducciones
WHERE tipo_contenido = N'Canción'
  AND segundos_escuchados >= 30;
GO

CREATE VIEW dbo.vw_kpi_usuario AS
SELECT usuarios.usuario_id, usuarios.nombre_usuario, usuarios.pais, usuarios.plan_suscripcion, COUNT(vw_reproducciones_validas.reproduccion_id) as reproducciones_validas, 
ROUND(SUM(vw_reproducciones_validas.segundos_escuchados) / 60,1) as minutos, MAX(vw_reproducciones_validas.fecha_hora) as ultima_repro_valida
FROM usuarios
LEFT JOIN vw_reproducciones_validas ON vw_reproducciones_validas.usuario_id = usuarios.usuario_id
GROUP BY 
    usuarios.usuario_id,
    usuarios.nombre_usuario,
    usuarios.plan_suscripcion,
    usuarios.pais
GO
```

![ejercicio 6 vista](images/clase13/ejercicio6-vista.png)

**a)** Obtén los usuarios sin ninguna reproducción válida.

```sql
SELECT *
FROM dbo.vw_kpi_usuario
WHERE reproducciones_validas = 0;
```

![ejercicio 6 a](images/clase13/ejercicio6-a.png)

**b)** Obtén los usuarios de pago ordenados por minutos de mayor a menor.

```sql
SELECT *
FROM dbo.vw_kpi_usuario
WHERE plan_suscripcion = N'Premium' OR plan_suscripcion = N'Familiar'
ORDER BY minutos DESC;
```

![ejercicio 6 b](images/clase13/ejercicio6-b.png)

## Ejercicio 7

  Recursos Humanos consulta el organigrama varias veces por semana. Guarda la CTE recursiva del organigrama en la vista `dbo.vw_organigrama` con el identificador, el nombre, el puesto, el nivel (el CEO es nivel 0) y la ruta desde el CEO (`Irene Salas > Tomás Vidal > ...`). Con la vista:
  
**Vista:**

```sql

CREATE VIEW dbo.vw_organigrama AS
WITH organigrama AS
(
    SELECT empleado_id, nombre, puesto, 0 as nivel, CAST(nombre as NVARCHAR(MAX)) AS ruta
    FROM empleados
    WHERE jefe_id IS NULL

    UNION ALL

    SELECT empleado.empleado_id, empleado.nombre, empleado.puesto, organigrama.nivel + 1 AS nivel, CONCAT(organigrama.ruta, N' > ',empleado.nombre) AS ruta
    FROM empleados as empleado
    INNER JOIN organigrama ON empleado.jefe_id = organigrama.empleado_id
)

SELECT empleado_id, nombre, puesto, nivel, ruta
FROM organigrama
GO
```

![ejercicio 7 vista](images/clase13/ejercicio7-vista.png)

**a)** Obtén las personas que dependen, directa o indirectamente, de Raúl Benet, ordenadas por nombre.

```sql
SELECT *
FROM dbo.vw_organigrama
WHERE ruta LIKE '%Raúl Benet%' 
ORDER BY nombre
```

![ejercicio 7 a](images/clase13/ejercicio7-a.png)

**b)** Obtén cuántos empleados hay en cada nivel.

```sql
SELECT nivel, COUNT(nombre)
FROM dbo.vw_organigrama
GROUP BY nivel
```

![ejercicio 7 b](images/clase13/ejercicio7-b.png)

## Ejercicio 8

El equipo de lanzamientos solo debe gestionar canciones publicadas en 2026. Crea la vista `dbo.vw_canciones_2026` con todas las columnas de `canciones` (escritas de forma explícita), filtrada por `fecha_lanzamiento >= '2026-01-01'` y con `WITH CHECK OPTION`. Antes de ejecutar las siguientes sentencias, **predice** el resultado de cada una. Después, ejecútalas una a una dentro de una transacción y deshaz los cambios al final.

```sql
-- a) UPDATE dbo.vw_canciones_2026 SET duracion_seg = 170 WHERE titulo = N'Humo Violeta';
-- b) UPDATE dbo.vw_canciones_2026 SET fecha_lanzamiento = '2025-12-15' WHERE titulo = N'Humo Violeta';
-- c) UPDATE dbo.vw_canciones_2026 SET duracion_seg = 210 WHERE titulo = N'Neón';
-- d) INSERT INTO dbo.vw_canciones_2026 (cancion_id, titulo, artista_id, genero_id, duracion_seg, fecha_lanzamiento)
--    VALUES (116, N'Eco Antiguo', 9, 2, 190, '2025-10-01');
-- e) INSERT INTO dbo.vw_canciones_2026 (cancion_id, titulo, artista_id, genero_id, duracion_seg, fecha_lanzamiento)
--    VALUES (117, N'Primer Vuelo', 9, 2, 195, '2026-10-02');
```

**Vista:**

```sql
CREATE VIEW dbo.vw_canciones_2026 AS
SELECT cancion_id, titulo, artista_id, genero_id, duracion_seg, fecha_lanzamiento
FROM canciones
WHERE fecha_lanzamiento >= '2026-01-01'
WITH CHECK OPTION;
GO
```

**Predicción de cada sentencia:**

| Sentencia | Predicción |
| --- | --- |
| a) | Se ejecuta correctamente. Cambia duracion_seg a 170. La fecha sigue siendo de 2026.|
| b) | Da error. Intenta cambiar la fecha a 2025 y la fila dejaría de cumplir la condición de la vista. WITH CHECK OPTION lo impide. |
| c) | Se ejecuta correctamente. Cambia duracion_seg a 210 y la canción sigue siendo de 2026.|
| d) | Da error. Intenta insertar una canción de 2025, que no cumple el WHERE de la vista.|
| e) | Se ejecuta correctamente. La canción es de 2026 y cumple la condición de la vista. |

**Ejecución dentro de una transacción:**

```sql
-- Tu transacción con ROLLBACK aquí
```

![ejercicio 8](images/clase13/ejercicio8.png)

**Comprobación tras el `ROLLBACK`:**

```sql
BEGIN TRANSACTION;
GO

-- a)
UPDATE dbo.vw_canciones_2026
SET duracion_seg = 170
WHERE titulo = N'Humo Violeta';
GO

-- b)
UPDATE dbo.vw_canciones_2026
SET fecha_lanzamiento = '2025-12-15'
WHERE titulo = N'Humo Violeta';
GO

-- c)
UPDATE dbo.vw_canciones_2026
SET duracion_seg = 210
WHERE titulo = N'Neón';
GO

-- d)
INSERT INTO dbo.vw_canciones_2026 
    (cancion_id, titulo, artista_id, genero_id, duracion_seg, fecha_lanzamiento)
VALUES 
    (116, N'Eco Antiguo', 9, 2, 190, '2025-10-01');
GO

-- e)
INSERT INTO dbo.vw_canciones_2026 
    (cancion_id, titulo, artista_id, genero_id, duracion_seg, fecha_lanzamiento)
VALUES 
    (117, N'Primer Vuelo', 9, 2, 195, '2026-10-02');
GO

-- Deshacemos TODOS los cambios realizados
ROLLBACK;
GO
```

![ejercicio 8 comprobación](images/clase13/ejercicio8-comprobacion.png)

## Ejercicio 9

Usando la vista `dbo.vw_catalogo_detalle` del Ejercicio 4, que une `canciones`, `artistas` y `generos`, **predice** qué ocurre con cada sentencia. Después ejecútalas una a una dentro de una transacción (separadas por `GO`) y, antes del `ROLLBACK`, consulta las canciones cuyo artista empiece por `Luna Roja`.

```sql
-- a) UPDATE dbo.vw_catalogo_detalle SET duracion_seg = 205 WHERE titulo = N'Neón';
-- b) UPDATE dbo.vw_catalogo_detalle SET titulo = N'Neón (Remix)', artista = N'Luna Roja & DJ Coral' WHERE titulo = N'Neón';
-- c) UPDATE dbo.vw_catalogo_detalle SET duracion_min = 3.5 WHERE titulo = N'Neón';
-- d) UPDATE dbo.vw_catalogo_detalle SET artista = N'Luna Roja Oficial' WHERE titulo = N'Neón';
```

**Predicción de cada sentencia:**

| Sentencia | Predicción |
| --- | --- |
| a) | Funciona, duracion_seg pertenece a canciones, y se puede modificar a través de la vista. |
| b) | Error porque inntenta modificar columnas de dos tablas diferentes (canciones.titulo y artistas.nombre) en el mismo UPDATE.|
| c) | Error porque duracion_min es una columna calculada/derivada, no una columna almacenada directamente en una tabla. |
| d) | Funciona, artista corresponde a artistas.nombre, y se puede modificar esa columna a través de la vista.|

**Ejecución dentro de una transacción:**

```sql
BEGIN TRANSACTION;
GO

-- a)
UPDATE dbo.vw_catalogo_detalle
SET duracion_seg = 205
WHERE titulo = N'Neón';
GO

-- b)
UPDATE dbo.vw_catalogo_detalle
SET titulo = N'Neón (Remix)',
    artista = N'Luna Roja & DJ Coral'
WHERE titulo = N'Neón';
GO

-- c)
UPDATE dbo.vw_catalogo_detalle
SET duracion_min = 3.5
WHERE titulo = N'Neón';
GO

-- d)
UPDATE dbo.vw_catalogo_detalle
SET artista = N'Luna Roja Oficial'
WHERE titulo = N'Neón';
GO

-- Consultamos ANTES de deshacer los cambios
SELECT *
FROM dbo.vw_catalogo_detalle
WHERE artista LIKE N'Luna Roja%';
GO

-- Deshacemos todos los cambios
ROLLBACK;
GO
```

![ejercicio 9](images/clase13/ejercicio9.png)

**Pregunta:** ¿Por qué ha cambiado también el artista de Verano en Bucle si el `UPDATE` filtraba por Neón?

_(escribe aquí tu respuesta)_

## Ejercicio 10

Un compañero quiere proteger la ficha de artistas con `SCHEMABINDING`, pero su vista no se crea:

```sql
CREATE OR ALTER VIEW dbo.vw_artistas_ficha
WITH SCHEMABINDING AS
SELECT *
FROM artistas AS a
JOIN dbo.generos AS g ON g.genero_id = a.genero_id;
```

**a)** Identifica los tres problemas y corrige la vista para que devuelva el identificador del artista, su nombre (`artista`), su país y el nombre de su género (`genero`). Consulta los artistas españoles ordenados por nombre.

**Los tres problemas:**
1. SELECT * no está permitido con SCHEMABINDING
2. Las tablas deben llevar el esquema, es decir tendría que ser FROM dbo.artistas AS a
3. Hay que dar nombres a las columnas de la vista cuando puedan producir ambigüedad.

**Vista corregida y consulta:**

```sql
CREATE OR ALTER VIEW dbo.vw_artistas_ficha
WITH SCHEMABINDING AS
SELECT
    a.artista_id,
    a.nombre AS artista,
    a.pais,
    g.nombre AS genero
FROM dbo.artistas AS a
INNER JOIN dbo.generos AS g
    ON g.genero_id = a.genero_id;
GO

SELECT
    artista_id,
    artista,
    pais,
    genero
FROM dbo.vw_artistas_ficha
WHERE pais = N'ES'
ORDER BY artista;
GO
```

![ejercicio 10 a](images/clase13/ejercicio10-a.png)

**b)** Intenta ampliar la columna `nombre` de `artistas` a `nvarchar(150)`. ¿Qué ocurre y por qué aparecen dos vistas en los mensajes?

```sql
-- Tu ALTER TABLE aquí
```

![ejercicio 10 b](images/clase13/ejercicio10-b.png)

**Explicación:**

No deja hacerlo porque existe una vista creada con WITH SCHEMABINDING que depende de esa columna

**c)** Con `sys.dm_sql_referencing_entities`, obtén las vistas que dependen directamente de `dbo.artistas`, ordenadas por nombre. ¿Cuáles de ellas impiden el cambio del apartado b) y cuáles no? ¿Por qué?

```sql
SELECT
    referencing_entity_name AS vista
FROM sys.dm_sql_referencing_entities('dbo.artistas', 'OBJECT')
ORDER BY referencing_entity_name;
```

![ejercicio 10 c](images/clase13/ejercicio10-c.png)

**Explicación:**

dbo.vw_artistas_ficha
dbo.vw_catalogo_detalle

Porque fueron creadas con schemabinding

## Ejercicio 11

El panel de dispositivos de Producto se refresca cada minuto. Un compañero ha preparado esta vista para materializarla, pero al crear el índice SQL Server la rechaza:

```sql
DROP VIEW IF EXISTS dbo.vw_ix_consumo_dispositivo;
GO
CREATE VIEW dbo.vw_ix_consumo_dispositivo
WITH SCHEMABINDING AS
SELECT dispositivo, AVG(segundos_escuchados) AS media_segundos
FROM dbo.reproducciones
WHERE tipo_contenido = N'Canción'
  AND segundos_escuchados >= 30
GROUP BY dispositivo;
GO
CREATE UNIQUE CLUSTERED INDEX IX_vw_ix_consumo_dispositivo
ON dbo.vw_ix_consumo_dispositivo (dispositivo);
```

**a)** Explica por qué falla y corrígela para que guarde el número de reproducciones válidas (`reproducciones_validas`) y los segundos totales (`segundos`) por dispositivo. Crea el índice.

**Explicación:**

Hay varios problemas:

1. AVG(segundos_escuchados) no está permitido directamente en una vista indexada.
2. Para una vista indexada con GROUP BY, SQL Server exige incluir un COUNT_BIG(*).
3. Para este ejercicio nos piden guardar:
- número de reproducciones válidas → COUNT_BIG(*)
- segundos totales → SUM(segundos_escuchados)
4. Además, para que la vista sea apta para indexación, conviene usar COUNT_BIG(*) exactamente como exige SQL Server.

**Vista corregida e índice:**

```sql
DROP VIEW IF EXISTS dbo.vw_ix_consumo_dispositivo;
GO

CREATE VIEW dbo.vw_ix_consumo_dispositivo
WITH SCHEMABINDING AS
SELECT
    dispositivo,
    COUNT_BIG(*) AS reproducciones_validas,
    SUM(segundos_escuchados) AS segundos
FROM dbo.reproducciones
WHERE tipo_contenido = N'Canción'
  AND segundos_escuchados >= 30
GROUP BY dispositivo;
GO

CREATE UNIQUE CLUSTERED INDEX IX_vw_ix_consumo_dispositivo
ON dbo.vw_ix_consumo_dispositivo (dispositivo);
GO
```

![ejercicio 11 a](images/clase13/ejercicio11-a.png)

**b)** Consulta la vista con `NOEXPAND` calculando los minutos y la media de segundos por reproducción, ambos con un decimal. Ordena por reproducciones descendente y por dispositivo.

```sql
SELECT
    dispositivo,
    reproducciones_validas,
    ROUND(segundos / 60.0, 1) AS minutos,
    ROUND(segundos * 1.0 / reproducciones_validas, 1) AS media_segundos
FROM dbo.vw_ix_consumo_dispositivo WITH (NOEXPAND)
ORDER BY reproducciones_validas DESC, dispositivo;
```

![ejercicio 11 b](images/clase13/ejercicio11-b.png)

**c)** Dentro de una transacción, inserta la reproducción 44 (usuario 6, canción 102, `'2026-09-22 21:00'`, 201 segundos, `Smart TV`, `Canción`), consulta la fila de `Smart TV` de la vista y deshaz el cambio.

```sql
BEGIN TRANSACTION;
GO

INSERT INTO dbo.reproducciones
    (reproduccion_id, usuario_id, cancion_id, fecha_hora,
     segundos_escuchados, dispositivo, tipo_contenido)
VALUES
    (44, 6, 102, '2026-09-22 21:00', 201, N'Smart TV', N'Canción');
GO

SELECT
    dispositivo,
    reproducciones_validas,
    ROUND(segundos / 60.0, 1) AS minutos,
    ROUND(segundos * 1.0 / reproducciones_validas, 1) AS media_segundos
FROM dbo.vw_ix_consumo_dispositivo WITH (NOEXPAND)
WHERE dispositivo = N'Smart TV';
GO

ROLLBACK;
GO
```

![ejercicio 11 c](images/clase13/ejercicio11-c.png)

---

# Parte 03 · Caso de estudio Sonora: las vistas para el cuadro de mando
 
## Contexto
 
El informe del martes funcionó. El comité de dirección de Sonora vio las cifras de la semana y tomó una decisión: a partir de ahora quiere un **cuadro de mando en Power BI** que se actualice solo, en lugar de pedir cifras por mensaje cada semana.
 
Carmen Lozano (Data Analyst) se encargará del cuadro de mando. Antes de que conecte Power BI, Raúl Benet (Head of Data) envía este mensaje:
 
> *"Carmen va a conectar Power BI esta semana y no quiero que el cuadro de mando lea las tablas directamente. Prepárale un conjunto de vistas, todas con el prefijo `vw_bi_`, que sean lo único que use. Las reglas de negocio tienen que estar dentro de las vistas, no en Power BI, para que no haya dos versiones de 'reproducción válida'. Aprovecha también para resolver dos peticiones que tengo pendientes: Laura quiere que su equipo de LATAM pueda corregir datos de sus usuarios sin tocar los de España, y Hugo quiere ampliar un campo de `usuarios`. Todo en un script que se pueda ejecutar varias veces."*
 
Todo el trabajo se hace sobre `SonoraDB`
 
### Reglas de negocio de Sonora
 
- Una reproducción es **válida** cuando es de tipo `Canción` y se han escuchado al menos **30 segundos**. Por debajo es un salto.
- Los **géneros principales** son los hijos directos del género raíz `Música`. Cada subgénero, a cualquier profundidad, cuenta para su género principal.
- Los **mercados LATAM** son México (`MX`), Argentina (`AR`), Colombia (`CO`) y Puerto Rico (`PR`).
- La **semana de análisis** del cuadro de mando va del 16/09/2026 al 22/09/2026, ambos incluidos.

## Preparación
 
```sql
USE SonoraDB;
GO

INSERT INTO dbo.reproducciones
    (reproduccion_id, usuario_id, cancion_id, fecha_hora, segundos_escuchados, dispositivo, tipo_contenido)
SELECT s.reproduccion_id, s.usuario_id, s.cancion_id, s.fecha_hora,
       s.segundos_escuchados, s.dispositivo, s.tipo_contenido
FROM dbo.stg_reproducciones AS s
WHERE NOT EXISTS (SELECT 1 FROM dbo.reproducciones AS r WHERE r.reproduccion_id = s.reproduccion_id);
 
INSERT INTO dbo.usuarios (usuario_id, nombre_usuario, email, pais, plan_suscripcion, fecha_alta)
SELECT s.usuario_id, s.nombre_usuario, s.email, s.pais, s.plan_suscripcion, s.fecha_alta
FROM dbo.stg_usuarios AS s
WHERE NOT EXISTS (SELECT 1 FROM dbo.usuarios AS u WHERE u.usuario_id = s.usuario_id);
GO

DROP TABLE IF EXISTS dbo.stg_reproducciones_2209;
 
CREATE TABLE dbo.stg_reproducciones_2209 (
    reproduccion_id      int,
    usuario_id           int,
    cancion_id           int,
    fecha_hora           datetime2(0),
    segundos_escuchados  int,
    dispositivo          nvarchar(20),
    tipo_contenido       nvarchar(10)
);
 
INSERT INTO dbo.stg_reproducciones_2209
    (reproduccion_id, usuario_id, cancion_id, fecha_hora, segundos_escuchados, dispositivo, tipo_contenido) VALUES
(37, 5,  NULL, '2026-09-21 22:00', 30,  N'Móvil', N'Anuncio'),
(38, 5,  104,  '2026-09-21 22:01', 190, N'Móvil', N'Canción'),
(39, 8,  106,  '2026-09-22 07:30', 12,  N'Móvil', N'Canción'),
(40, 10, 103,  '2026-09-22 09:00', 176, N'Móvil', N'Canción'),
(41, 9,  NULL, '2026-09-22 09:10', 30,  N'Web',   N'Anuncio'),
(42, 9,  111,  '2026-09-22 09:11', 356, N'Web',   N'Canción'),
(43, 1,  114,  '2026-09-22 10:00', 25,  N'Móvil', N'Canción');
 
INSERT INTO dbo.reproducciones
    (reproduccion_id, usuario_id, cancion_id, fecha_hora, segundos_escuchados, dispositivo, tipo_contenido)
SELECT s.reproduccion_id, s.usuario_id, s.cancion_id, s.fecha_hora,
       s.segundos_escuchados, s.dispositivo, s.tipo_contenido
FROM dbo.stg_reproducciones_2209 AS s
WHERE NOT EXISTS (SELECT 1 FROM dbo.reproducciones AS r WHERE r.reproduccion_id = s.reproduccion_id);
GO

SELECT (SELECT COUNT(*) FROM dbo.reproducciones) AS reproducciones,
       (SELECT COUNT(*) FROM dbo.usuarios)       AS usuarios;
```
 ![CasoDeUso 1](images/clase13/caso1.png)

## Desarrollo
 
### Vistas para el cuadro de mando (6 vistas con prefijo `vw_bi_`)
 
**Requerimiento 1: Tabla de hechos** — Una fila por reproducción válida con contexto completo
 
```sql
DROP VIEW IF EXISTS dbo.vw_bi_hechos_reproduccion;
GO
 
CREATE VIEW dbo.vw_bi_hechos_reproduccion AS
WITH genero_principal AS (
    SELECT genero_id, genero_id AS raiz_id
    FROM dbo.generos
    WHERE genero_padre_id = (SELECT genero_id FROM dbo.generos WHERE genero_padre_id IS NULL)
    
    UNION ALL
    
    SELECT g.genero_id, gp.raiz_id
    FROM dbo.generos AS g
    JOIN genero_principal AS gp ON g.genero_padre_id = gp.genero_id
)
SELECT 
    r.reproduccion_id,
    CAST(r.fecha_hora AS DATE) AS fecha,
    r.fecha_hora,
    u.usuario_id,
    u.nombre_usuario,
    u.pais,
    u.plan_suscripcion,
    c.titulo AS cancion_titulo,
    a.nombre AS artista,
    g.nombre AS genero,
    gp_root.nombre AS genero_principal,
    r.dispositivo,
    r.segundos_escuchados
FROM dbo.reproducciones AS r
INNER JOIN dbo.usuarios AS u ON u.usuario_id = r.usuario_id
INNER JOIN dbo.canciones AS c ON c.cancion_id = r.cancion_id
INNER JOIN dbo.artistas AS a ON a.artista_id = c.artista_id
INNER JOIN dbo.generos AS g ON g.genero_id = c.genero_id
INNER JOIN genero_principal AS gp ON gp.genero_id = g.genero_id
INNER JOIN dbo.generos AS gp_root ON gp_root.genero_id = gp.raiz_id
WHERE r.tipo_contenido = N'Canción'
  AND r.segundos_escuchados >= 30;
GO

SELECT pais, COUNT(*) AS reproducciones, COUNT(DISTINCT usuario_id) AS oyentes_distintos,
       CAST(SUM(segundos_escuchados) / 60.0 AS DECIMAL(10,1)) AS minutos
FROM dbo.vw_bi_hechos_reproduccion
GROUP BY pais
ORDER BY reproducciones DESC;
```

![Caso de uso parte 2](caso2.png)

**Requerimiento 2: Evolución diaria** — KPI por día
 
```sql
DROP VIEW IF EXISTS dbo.vw_bi_kpi_diario;
GO
 
CREATE VIEW dbo.vw_bi_kpi_diario AS
SELECT 
    fecha,
    COUNT(*) AS reproducciones_validas,
    COUNT(DISTINCT usuario_id) AS oyentes_distintos,
    CAST(SUM(segundos_escuchados) / 60.0 AS DECIMAL(10,1)) AS minutos
FROM dbo.vw_bi_hechos_reproduccion
GROUP BY fecha;
GO

SELECT fecha, reproducciones_validas, oyentes_distintos, minutos
FROM dbo.vw_bi_kpi_diario
WHERE fecha BETWEEN '2026-09-16' AND '2026-09-22'
ORDER BY fecha;
```

![Caso de uso 3](caso3.png)

**Requerimiento 3: Indicadores por género principal** — Acumulado histórico
 
```sql
DROP VIEW IF EXISTS dbo.vw_bi_kpi_genero_principal;
GO
 
CREATE VIEW dbo.vw_bi_kpi_genero_principal AS
SELECT 
    genero_principal,
    COUNT(*) AS reproducciones_validas,
    COUNT(DISTINCT usuario_id) AS oyentes_distintos,
    CAST(SUM(segundos_escuchados) / 60.0 AS DECIMAL(10,1)) AS minutos
FROM dbo.vw_bi_hechos_reproduccion
GROUP BY genero_principal;
GO

SELECT genero_principal, reproducciones_validas, oyentes_distintos, minutos
FROM dbo.vw_bi_kpi_genero_principal
ORDER BY reproducciones_validas DESC;
```
 
![Caso de uso 4](caso4.png)

**Requerimiento 4: Rendimiento de canciones** — Análisis de saltos
 
```sql
DROP VIEW IF EXISTS dbo.vw_bi_rendimiento_canciones;
GO
 
CREATE VIEW dbo.vw_bi_rendimiento_canciones AS
SELECT 
    c.cancion_id, c.titulo, a.nombre AS artista, c.fecha_lanzamiento,
    (SELECT COUNT(*) FROM dbo.reproducciones r WHERE r.cancion_id = c.cancion_id) AS reproducciones_totales,
    COALESCE((SELECT COUNT(*) FROM dbo.reproducciones r 
              WHERE r.cancion_id = c.cancion_id AND r.tipo_contenido = N'Canción' AND r.segundos_escuchados >= 30), 0) AS reproducciones_validas,
    COALESCE((SELECT COUNT(*) FROM dbo.reproducciones r 
              WHERE r.cancion_id = c.cancion_id AND r.tipo_contenido = N'Canción' AND r.segundos_escuchados < 30), 0) AS saltos,
    CASE 
        WHEN (SELECT COUNT(*) FROM dbo.reproducciones r WHERE r.cancion_id = c.cancion_id) = 0 THEN NULL
        ELSE CAST(COALESCE((SELECT COUNT(*) FROM dbo.reproducciones r 
                      WHERE r.cancion_id = c.cancion_id AND r.tipo_contenido = N'Canción' AND r.segundos_escuchados < 30), 0) * 100.0 /
            (SELECT COUNT(*) FROM dbo.reproducciones r WHERE r.cancion_id = c.cancion_id) AS DECIMAL(5,1))
    END AS tasa_salto_pct
FROM dbo.canciones AS c
JOIN dbo.artistas AS a ON a.artista_id = c.artista_id;
GO

SELECT titulo, artista, fecha_lanzamiento, reproducciones_totales, reproducciones_validas, saltos, tasa_salto_pct
FROM dbo.vw_bi_rendimiento_canciones
WHERE saltos > 0
ORDER BY tasa_salto_pct DESC;
```

![Caso de uso 5](caso5.png)

**Requerimiento 6: Consumo por país y plan** — Vista blindada con SCHEMABINDING
 
```sql
DROP VIEW IF EXISTS dbo.vw_bi_consumo_pais_plan;
GO
 
CREATE VIEW dbo.vw_bi_consumo_pais_plan
WITH SCHEMABINDING AS
SELECT 
    u.pais,
    u.plan_suscripcion,
    COUNT(*) AS reproducciones_validas,
    CAST(SUM(r.segundos_escuchados) / 60.0 AS DECIMAL(10,1)) AS minutos
FROM dbo.reproducciones AS r
INNER JOIN dbo.usuarios AS u ON u.usuario_id = r.usuario_id
WHERE r.tipo_contenido = N'Canción'
  AND r.segundos_escuchados >= 30
GROUP BY u.pais, u.plan_suscripcion;
GO

SELECT pais, plan_suscripcion, reproducciones_validas, minutos
FROM dbo.vw_bi_consumo_pais_plan
ORDER BY minutos DESC;
```

![Caso de uso 6](caso6.png)

### Petición de Laura (equipo LATAM)
 
**Vista con WITH CHECK OPTION** para proteger el ámbito LATAM:
 
```sql
DROP VIEW IF EXISTS dbo.vw_usuarios_latam;
GO
 
CREATE VIEW dbo.vw_usuarios_latam AS
SELECT usuario_id, nombre_usuario, pais, plan_suscripcion, fecha_alta
FROM dbo.usuarios
WHERE pais IN (N'MX', N'AR', N'CO', N'PR')
WITH CHECK OPTION;
GO
 

SELECT usuario_id, nombre_usuario, pais, plan_suscripcion, fecha_alta
FROM dbo.vw_usuarios_latam
ORDER BY pais, nombre_usuario;
GO

BEGIN TRAN;
GO

UPDATE dbo.vw_usuarios_latam
SET plan_suscripcion = N'Premium'
WHERE nombre_usuario = N'nachox';

UPDATE dbo.vw_usuarios_latam
SET pais = N'ES'
WHERE nombre_usuario = N'juanpi';

UPDATE dbo.vw_usuarios_latam
SET plan_suscripcion = N'Familiar'
WHERE nombre_usuario = N'marta_rock';
 
ROLLBACK;
GO
```

![Caso de uso 7](caso7.png)
 
### Petición de Hugo (ampliar un campo de `usuarios`)
 
**Ampliación de plan_suscripcion a nvarchar(30)** para "Premium Estudiante Anual":
 
```sql
DROP VIEW IF EXISTS dbo.vw_bi_consumo_pais_plan;
GO

ALTER TABLE dbo.usuarios
ALTER COLUMN plan_suscripcion nvarchar(30) NOT NULL;
GO


CREATE VIEW dbo.vw_bi_consumo_pais_plan
WITH SCHEMABINDING AS
SELECT 
    u.pais,
    u.plan_suscripcion,
    COUNT(*) AS reproducciones_validas,
    CAST(SUM(r.segundos_escuchados) / 60.0 AS DECIMAL(10,1)) AS minutos
FROM dbo.reproducciones AS r
INNER JOIN dbo.usuarios AS u ON u.usuario_id = r.usuario_id
WHERE r.tipo_contenido = N'Canción'
  AND r.segundos_escuchados >= 30
GROUP BY u.pais, u.plan_suscripcion;
GO

SELECT pais, plan_suscripcion, reproducciones_validas, minutos
FROM dbo.vw_bi_consumo_pais_plan
ORDER BY minutos DESC;
GO
```

![Caso de uso 8](caso8.png)

**Explicación:** Con `WITH SCHEMABINDING`, SQL Server protege la vista contra cambios accidentales en la estructura base:
- **No permite**: eliminar columnas, cambiar tipos a incompatibles, reordenar columnas
- **Sí permite**: ampliar columnas nvarchar(20) → nvarchar(30), agregar nuevas columnas
Para cambiar de forma segura:
1. Ampliar plan_suscripcion (la vista lo usa pero con espacio adicional)
2. Para eliminar/cambiar: DROP VIEW → ALTER TABLE → CREATE VIEW
### Script completo y re-ejecutable
 
El script completo está diseñado para ejecutarse varias veces sin errores (idempotente). Incluye:
- **Preparación de datos** (43 reproducciones, 10 usuarios)
- **6 vistas para Power BI** (prefijo `vw_bi_`)
- **1 vista de mantenimiento** para LATAM (sin prefijo)
- **Soluciones a peticiones** (Laura y Hugo)
- **Análisis de dependencias** (sys.dm_sql_referencing_entities)

### Requerimiento 7: Mapa de dependencias
 
Para conocer el impacto si cambia la regla de reproducción válida:
 
```sql
SELECT referencing_schema_name, referencing_entity_name
FROM sys.dm_sql_referencing_entities(N'dbo.reproducciones', N'OBJECT')
ORDER BY referencing_entity_name;
GO

SELECT referencing_schema_name, referencing_entity_name
FROM sys.dm_sql_referencing_entities(N'dbo.vw_bi_hechos_reproduccion', N'OBJECT')
ORDER BY referencing_entity_name;
GO
```

![Caso de uso 9](caso9.png)
 
**Conclusión:** Si cambia la regla (ej: 35 segundos en lugar de 30), solo hay que actualizar `vw_bi_hechos_reproduccion` y todas las vistas que dependen de ella se auto-actualizan automáticamente.