-- Ejercicio 1
SELECT
    SERVERPROPERTY('ProductMajorVersion') AS VersionPrincipal,
    d.compatibility_level AS NivelCompatibilidad
FROM sys.databases AS d
WHERE d.name = 'SonoraDB';

-- Ejercicio 2 Lista los nombres de las tablas de usuario de SonoraDB usando la vista de catálogo sys.tables, ordenados alfabéticamente.

SELECT name
FROM sys.tables
ORDER BY name desc

-- Ejercicio 3 Usando `INFORMATION_SCHEMA.COLUMNS`, muestra las columnas de la tabla `reproducciones` con su tipo de dato, su longitud máxima y si admiten nulos, en el orden en que están definidas.

SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS as columns
WHERE columns.TABLE_NAME = 'reproducciones'
ORDER BY ORDINAL_POSITION

-- Ejercicio 4 Muestra el nombre de usuario, el plan y la fecha de alta de los usuarios de España (ES), del más antiguo al más reciente.
SELECT nombre_usuario, plan_suscripcion, fecha_alta
FROM stg_usuarios
WHERE pais = 'ES'

-- Ejercicio 5 El equipo editorial busca canciones lanzadas en 2026 que duren entre 170 y 200 segundos (ambos incluidos) para una playlist de radio. 
-- Muestra título, duración y fecha de lanzamiento, ordenadas por fecha. Filtra el año con un rango de fechas, sin aplicar funciones sobre la columna.

SELECT titulo, duracion_seg, fecha_lanzamiento
FROM canciones
WHERE duracion_seg >= 170 AND duracion_seg <= 200 AND fecha_lanzamiento >= '2026-01-01'
AND fecha_lanzamiento < '2027-01-01'
ORDER BY fecha_lanzamiento 

-- Ejercicio 6  Obtén los usuarios cuyo nombre de usuario contiene un guion bajo (`_`), ordenados alfabéticamente. 
-- Antes de escribir la solución correcta, prueba `LIKE '%_%'` y explica por qué devuelve los 8 usuarios.
SELECT nombre_usuario
FROM stg_usuarios
WHERE nombre_usuario LIKE '%[_]%'

-- Ejercicio 7 - ¿Desde qué dispositivos se han hecho reproducciones? Muestra cada dispositivo una sola vez, ordenado alfabéticamente.
SELECT DISTINCT dispositivo 
FROM stg_reproducciones
ORDER BY dispositivo ASC

-- Ejercicio 8

SELECT reproduccion_id, usuario_id, fecha_hora, cancion_id
FROM reproducciones
WHERE cancion_id IS NULL

-- La condición = NULL no devuelve nada porque en SQL, NULL no representa un valor normal. Tienes que usar IS NULL

-- Ejercicio 9

SELECT TOP 2 WITH TIES reproduccion_id, usuario_id, cancion_id, segundos_escuchados
FROM reproducciones
ORDER BY segundos_escuchados DESC

-- Ejercicio 10 : La app muestra el catálogo en páginas de 5 canciones ordenadas por título. Obtén los títulos de la **página 2** con `OFFSET ... FETCH`.



-- Ejercicio 11

-- Ejercicio 12


