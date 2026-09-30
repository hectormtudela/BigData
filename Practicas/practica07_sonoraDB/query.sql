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

-- Ejercicio 7

-- Ejercicio 8


-- Ejercicio 9

-- Ejercicio 10

-- Ejercicio 11

-- Ejercicio 12