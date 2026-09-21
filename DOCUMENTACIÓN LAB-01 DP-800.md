# DOCUMENTACIÓN LAB-01 DP-800

![image.png](image.png)

Se ha iniciado **SQL Server Management Studio (SSMS)** y se ha establecido la conexión con el entorno de SQL Server correspondiente. La herramienta queda preparada para continuar con las tareas de configuración, consulta o administración de la base de datos.

![image.png](image%201.png)

### Preparación del entorno

Se ha comprobado que los archivos del laboratorio estén disponibles en la carpeta **C:\LabFiles**. En mi caso no estaban presentes. He tenido que clonar el repositorio **mslearn-sql-developer** desde GitHub mediante Visual Studio Code, con la opción **Git: Clone.** Este laboratorio requiere **SQL Server 2025 o superior**, la cual tengo instalada.

![image.png](image%202.png)

### Conexión con SQL Server

Se ha iniciado **SQL Server Management Studio (SSMS)** y se ha establecido la conexión (**localhost**).

![image.png](image%203.png)

### Creación de la base de datos EcommerceDB

Desde SSMS, se selecciona la carpeta **Databases** y se abre una nueva consulta con **New Query**. En ella se ejecuta un script en T-SQL que crea la base de datos **EcommerceDB** y cambia la abre.

![image.png](image%204.png)

Para comprobar que se está trabajando sobre la base de datos correcta y con la versión adecuada del motor, se ejecuta la siguiente consulta:

![image.png](image%205.png)

#### Creación de las tablas principales con restricciones

Se han creado las tablas base del sistema de comercio electrónico: **Supplier**, **Category** y **Product**. En todas, la clave primaria es un identificador autonumérico (`IDENTITY(1,1)`).

Durante la ejecución se detectó una coma sobrante tras la última clave foránea, que provoca un error de sintaxis en T-SQL, y se eliminó antes de ejecutar el script.

![image.png](image%206.png)

![image.png](image%207.png)

También se han insertado unos datos de prueba:

![image.png](image%208.png)

![image.png](image%209.png)

#### Columnas JSON para metadatos

Se ha añadido a la tabla **Product** la columna **Metadata** de tipo `JSON` para guardar atributos variables según el tipo de producto, como color, tamaño o material. Para consultar por color de forma eficiente, se creó la columna calculada **MetadataColor**, que extrae ese valor con `JSON_VALUE`

Tras rellenar los metadatos de los dos productos, la consulta filtrando por color `blue` devuelve únicamente el **Wireless Mouse**, con su color, tamaño y material extraídos del JSON.

![image.png](image%2010.png)

![image.png](image%2011.png)

**Tabla de pedidos particionada**

Se ha creado la tabla **Order** particionada por fecha de pedido para mejorar el rendimiento de las consultas. Para ello se definió la función de partición **PF_OrderDate**, que divide los datos por trimestres de 2025 (`RANGE RIGHT`), y el esquema **PS_OrderDate**, que asigna todas las particiones al filegroup `PRIMARY`.

Tras insertar tres pedidos de ejemplo, la consulta con `$PARTITION` muestra cómo se reparten: dos en la partición 2 (enero y febrero) y uno en la partición 3 (junio).

![image.png](image%2012.png)

![image.png](image%2013.png)

![image.png](image%2014.png)

#### Detalle de pedidos con SEQUENCE

Se ha creado la secuencia **OrderLineSequence**, que genera números únicos de forma independiente de cualquier tabla, y la tabla **OrderDetail**, que guarda las líneas de cada pedido. Su identificador `OrderLineID` no es `IDENTITY`, sino que se rellena con `NEXT VALUE FOR OrderLineSequence`. La tabla se relaciona con **Order** (por `OrderID` y `OrderDate`) y con **Product** mediante claves foráneas, y `LineTotal` se calcula automáticamente.

![image.png](image%2015.png)

Tras insertar tres líneas de ejemplo, la consulta de verificación muestra los identificadores 1, 2 y 3 generados por la secuencia y el total calculado de cada línea.

![image.png](image%2016.png)

#### Verificación de los objetos de la base de datos

Se comprobó el correcto funcionamiento de las restricciones intentando insertar un producto con precio negativo. La operación falló con un error de violación de la restricción `CHECK` 

A continuación se ejecutaron consultas de verificación sobre el resto de objetos. La consulta JSON devuelve los dos productos con su color extraído de `Metadata`, la de particionado muestra los pedidos repartidos entre las particiones 2 y 3, y la de la tabla temporal devuelve el historial completo de precios, con la versión anterior (99.99) y la vigente (109.99).

![image.png](image%2017.png)

![image.png](image%2018.png)

#### Limpieza

Una vez finalizado el laboratorio, se eliminó la base de datos **EcommerceDB** desde SSMS (clic derecho → *Delete*), marcando la opción *Close existing connections* para cerrar posibles conexiones abiertas.

![image.png](image%2019.png)

![image.png](image%2020.png)