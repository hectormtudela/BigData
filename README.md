### Ejercicio 1 — Clasifica las fuentes

Clasifica cada fuente como estructurada, semiestructurada o no estructurada y justifica tu respuesta:

1. Exportación diaria del ERP de compras en CSV -> **Estructurada porque encaja en un esquema fijo (filas/columnas).**
2. Lecturas de temperatura de las cámaras frigoríficas enviadas cada 30 segundos en JSON -> **Semiestructurada porque tiene una organización jerarquica pero no fijo.**
3. Grabaciones MP3 del servicio de atención al cliente ->** No estructurada porque no tiene sistema que lo pueda interpretar rápidamente**
4. Tabla `Empleados` de la base de datos de RRHH -> **Estructurada porque está estructurado en un esquema fijo (filas/columnas)**
5. Logs de acceso de la tienda online -> **Semiestructurada si estuviese organizada jerárquica o etiquetada, si no está de esa manera y es texto liso debería de ser no estructurada  **
6. Fotografías de los lineales tomadas por los reponedores -> **No estructurada porque no tiene sistema que lo pueda interpretar rápidamente**

### Ejercicio 2 — Elige el formato

Para cada escenario de Grupo Alimenta, elige el formato más adecuado y justifica la decisión:

1. Un proveedor pequeño nos envía cada semana su tarifa de precios y solo sabe trabajar con Excel. **CSV**
2. Almacenar 5 años de líneas de ticket para que los analistas estudien la estacionalidad de ventas por familia de producto. **Parquet**
3. Tabla de socios de fidelización que se actualiza a diario y sobre la que el delegado de protección de datos exige poder ver cómo estaba hace un mes. **Delta**
4. Flujo continuo de lecturas de temperatura de las cámaras frigoríficas. **JSON**
5. Recepción de pedidos de compra con un gran proveedor que usa EDI. **XML**


### Ejercicio 3 — OLTP u OLAP

Indica si cada necesidad corresponde a un sistema transaccional o analítico:

1. Aplicar un cupón de descuento en la caja. **OLTP**
2. Calcular la evolución de las ventas de productos ecológicos en los últimos 3 años. **OLAP**
3. Consultar si queda aceite de oliva en la tienda de Valencia ahora mismo. **OLTP**
4. Detectar qué tiendas tienen más roturas de stock los lunes. **OLAP**
5. Actualizar la dirección de entrega de un pedido online en curso. **OLTP**

### Ejercicio 4 — ¿Qué rol es responsable?

1. El informe de ventas lleva dos días sin actualizarse porque ha fallado la carga nocturna. **Ingeniero de Datos**
2. Hay que restaurar la base de datos de la tienda online tras un borrado accidental. **Administrador de la base de datos**
3. Dirección quiere un nuevo gráfico de margen por familia de producto en el cuadro de mando. **Analista de Datos**
4. Atención al cliente quiere un asistente que responda "¿cuándo llega mi pedido?". **Ingeniero de IA**
5. Hay que enmascarar los teléfonos de los socios antes de que lleguen a la capa analítica. **Ingeniero de datos**
6. Marketing quiere saber qué socios tienen mayor probabilidad de dejar de comprar en los próximos 3 meses. **Científico de datos**
7. Se debe decidir si la plataforma se construye en Fabric, en Databricks o combinando ambos. **Arquitecto de Datos**
8. Dos departamentos presentan en el comité cifras distintas de "venta neta" para el mismo mes. **Analísta de datos**


---
## Ejercicio 5 : Investiga y arma un diagrama de arquitectura de capas (como el de la sección 8) con cada una de estas tecnologías:
**5.1. Databricks (sin Azure)**
- Fuentes: bases de datos, ficheros, apps SaaS, streaming (igual que en cualquier plataforma).
- Ingesta: Auto Loader (ingesta incremental de archivos), Lakeflow / Delta Live Tables (pipelines ETL declarativos).
- Almacenamiento: Delta Lake (formato de tablas open source) sobre S3, ADLS o GCS, según la nube.
- Procesamiento: Apache Spark + Photon (motor de ejecución rápido).
- Analítica / modelado: Databricks SQL (warehouses) y MLflow (machine learning).
- Consumo: dashboards de AI/BI, o conectores hacia Power BI / Tableau.
- Gobierno transversal: Unity Catalog (catálogo, linaje y permisos, igual función que Purview).


**5.2. Microsoft Fabric (100% Fabric, nada fuera)**
- Fuentes: on-premises, SaaS, IoT (conectadas vía gateway).
- Ingesta: Fabric Data Factory (pipelines, Dataflows Gen2) y Eventstreams (tiempo real).
- Almacenamiento: OneLake, el único lago de datos lógico de Fabric.
- Procesamiento: notebooks Spark de Fabric y Dataflows Gen2.
- Analítica / modelado: Lakehouse, Warehouse y Eventhouse (Real-Time Intelligence).
- Consumo: Power BI y Fabric IQ / Copilot (lenguaje natural).
- Gobierno transversal: Microsoft Purview, integrado dentro del mismo workspace.

  
**5.3. AWS**
- Fuentes: bases de datos on-prem, apps, IoT.
- Ingesta: AWS Glue (ETL serverless), AWS DMS (migración de BD), Kinesis (streaming).
- Almacenamiento: Amazon S3 como data lake central + Lake Formation para el gobierno de permisos.
- Procesamiento: Amazon EMR (Spark/Hadoop gestionado), Amazon Athena (SQL serverless sobre S3).
- Analítica / modelado: Amazon Redshift (data warehouse) y SageMaker (ML).
- Consumo: Amazon QuickSight.
- Gobierno transversal: Lake Formation + Glue Data Catalog.


**5.4. GCP**
- Fuentes: on-prem, SaaS, IoT.
- Ingesta: Pub/Sub (mensajería en tiempo real), Datastream (CDC).
- Almacenamiento: Cloud Storage + BigLake (une lake y warehouse).
- Procesamiento: Dataflow (Apache Beam gestionado), Dataproc (Spark/Hadoop gestionado).
- Analítica / modelado: BigQuery (con BigQuery ML) y Vertex AI.
- Consumo: Looker / Looker Studio.
- Gobierno transversal: Dataplex y Data Catalog.

  
**5.5. Herramientas Open Source (la más importante)**
- Fuentes: cualquier sistema.
- Ingesta: Debezium (CDC), Apache Kafka (streaming), Airbyte (conectores ELT).
- Almacenamiento: MinIO/HDFS + formatos abiertos como Apache Iceberg o Apache Hudi.
- Procesamiento: Apache Spark / Flink, dbt (transformación SQL), Apache Airflow (orquestación).
- Analítica: Trino/Presto (SQL federado) o ClickHouse.
- Consumo: Apache Superset, Metabase.
- Gobierno transversal: DataHub o Apache Atlas.

  
## 6, 7 y 8. ¿Y Snowflake, dbt y DuckDB?
No son comparables directamente porque no ocupan la misma capa:
 
| Tecnología | Qué es | Capa donde encaja | Con qué se combina |
|---|---|---|---|
| **Snowflake** | Plataforma de datos en la nube (SaaS), multicloud | Almacenamiento + Procesamiento + Analítica (todo en uno) | Fivetran/Airbyte para ingesta, dbt para transformar, Power BI/Tableau para consumo |
| **dbt** | Herramienta de transformación SQL, no guarda datos | Procesamiento / transformación | Snowflake, BigQuery, Databricks, Redshift, DuckDB (funciona sobre cualquiera) |
| **DuckDB** | Motor analítico embebido ("SQLite para analítica") | Procesamiento local / edge | Notebooks Python, dbt-duckdb, y MotherDuck (su versión en la nube) |

**Diagrama 1 — Todo en Snowflake**
Fuentes → Fivetran/Airbyte (ingesta) → Snowflake (almacenamiento + cómputo + analítica) → dbt (transforma dentro de Snowflake) → Tableau/Power BI (consumo).

**Diagrama 2 — dbt sobre distintos motores**
Fuentes → Fivetran/Airbyte → almacenamiento a elegir (Snowflake, BigQuery, Databricks o Redshift) → dbt transforma sobre cualquiera de ellos, orquestado por Airflow → BI.

**Diagrama 3 — DuckDB local y MotherDuck en la nube**
Archivos Parquet/CSV en local o S3 → DuckDB (corre embebido en Python/notebook/dbt) → si hace falta escalar, MotherDuck (versión serverless en la nube) → consumo en notebooks o BI.

## Sección 10: Caso práctico — Plataforma de datos de Grupo Alimenta

1. **Clasificación.** Clasifica cada fuente (estructurada, semiestructurada, no estructurada) e indica si es OLTP, fichero o stream.
TPV/ERP (Azure SQL Database)	Estructurado	OLTP
App de fidelización (Cosmos DB, JSON)	Semiestructurado	OLTP orientado a documentos
Sensores IoT cámaras	Semiestructurado	Stream
Tarifas proveedores (CSV/SFTP)	Estructurado	Fichero 
Facturas PDF	No estructurado	Fichero 
Meteorología/festivos (API)	Semiestructurado	Fichero/API batch diario (podría tratarSE1 como stream de baja frecuencia)

2. **Arquitectura.** Dibuja  una arquitectura con capas Bronze, Silver y Gold. Indica qué servicio de Azure usarías en cada paso y justifica si optas por Fabric, Databricks u otro stack
**Bronze (ingesta cruda):**
Azure SQL/ERP → Azure Data Factory / Fabric Data Pipelines con ingesta incremental (CDC) hacia el Lakehouse.
Cosmos DB → conector nativo de Data Factory o Change Feed de Cosmos DB.
IoT sensores → Azure IoT Hub / Event Hubs → Structured Streaming (Databricks) o Eventstream (Fabric) para landing en tiempo casi real.
CSV/SFTP → Data Factory con conexión SFTP programada.
PDFs → Data Factory + Azure AI Document Intelligence para OCR antes de aterrizar el texto extraído.
API meteo → Data Factory (copy activity) o Azure Function programada.
**Silver (limpieza y conformado):** normalización de esquemas, deduplicación, tipado correcto, resolución de IDs (cliente, producto, tienda), agregación de streaming IoT a intervalos útiles. Aquí se usa Databricks (PySpark/Spark SQL) o Fabric Notebooks
**Gold (negocio):** tablas agregadas y modeladas en esquema en estrella, listas para consumo BI y ML. Se publican como Power BI datasets / Fabric Lakehouse SQL endpoint.

**¿Fabric o Databricks?** Con este stack full-Azure y necesidad de BI integrado, Microsoft Fabric es mejor porque junta ingesta, Lakehouse, Power BI y gobierno en un solo SaaS. Databricks sería mejor si necesitaras más potencia de Spark, MLOps o multi-nube.

3. **Formatos.** Indica el formato de almacenamiento de cada capa y por qué.
**Bronze:** formato lo más fiel al origen — JSON crudo, Parquet simple, o Delta sin transformar. Objetivo: trazabilidad, no optimización.
**Silver:** Delta Lake / formato Delta (Parquet + log de transacciones). Da ACID, versionado (time travel) y esquema forzado.
**Gold:** también Delta, pero particionado y optimizado (Z-ORDER, compactación) para consultas analíticas rápidas desde Power BI/SQL endpoint.


4. **Modelo Gold.** Diseña el esquema en estrella de ventas: tabla de hechos, granularidad, medidas y al menos cuatro dimensiones.
**Tabla de hechos:** FactVentas

**Granularidad:** una fila por línea de ticket/venta (producto × tienda × fecha × transacción).
**Medidas:** unidades_vendidas, importe_venta, coste, margen, flag_rotura_stock.

**Dimensiones:**
DimProducto (SK, familia, categoría, marca, unidad de medida)
DimTienda (SK, nombre, región, formato de tienda)
DimFecha (SK, día, mes, trimestre, festivo sí/no — enlaza con la API de meteo/festivos)
DimCliente (SK, segmento de fidelización — viene de Cosmos DB)

5. Asignación de roles (7 roles)
| Rol | Responsabilidad en la arquitectura |
|---|---|
| Arquitecto de datos |	Diseña la arquitectura Bronze/Silver/Gold, elige Fabric/Databricks, define seguridad y gobierno global |
| Ingeniero de datos	| Construye pipelines de ingesta (Data Factory, Event Hubs, OCR de PDFs) y transformaciones Bronze→Silver | 
| Analytics engineer	| Modela la capa Gold (esquema en estrella), define métricas de negocio y tests de calidad |
| Analista de datos / BI	| Construye el cuadro de mando de ventas/margen/roturas en Power BI |
| Científico de datos	| Desarrolla el modelo de previsión de demanda de frescos |
| Ingeniero de IA/ML	| Construye y despliega el asistente conversacional en Azure AI Foundry |
| Data steward / gobierno |	Vela por la calidad y clasificación de datos personales (con apoyo de Purview) |

6. **Métricas.** Como analytics engineer, redacta la definición oficial de "rotura de stock" y dos pruebas de calidad que aplicarías a la tabla Gold.
**Definición oficial de "rotura de stock":**
Decimos que hay rotura de stock cuando un producto se queda a 0 unidades en una tienda durante horario de apertura, y además sabemos que ese día sí había demanda de ese producto (por ejemplo, porque en otras tiendas parecidas sí se vendió). Es decir, no basta con que el stock llegue a cero.
Ejemplo real: El Domingo día 20 de Septiembre tuve que trabajar en mi empleo de fines de semana en la empresa Ahorramas S.A. Este día justo había habría una tienda de Precocinados Mari al lado de la tienda, una apertura que trajo muchísima gente a comprar a Precocinados Mari su comida para ese domingo y que llevo gente a comprar el pan en mi tienda. Debido a esto, la panadería se quedó sin pan muy rápido y tuvimos una "rotura de stock" porque mucha gente se marchaba sin comprar el pan debido a que no había más para comprar.

Dos pruebas de calidad sobre la tabla Gold:

Test de completitud/no nulos: ninguna fila de ``FactVentas`` puede tener ``tienda_id`` o ``producto_id`` nulos, ni fechas fuera del rango operativo.
Test de consistencia referencial: todo ``producto_id`` y ``tienda_id`` en la tabla de hechos debe existir en ``DimProducto`` y ``DimTienda`` (evitar huérfanos), y margen nunca puede ser mayor que ``importe_venta``.

### Tareas

1. **Clasificación.** Clasifica cada fuente (estructurada, semiestructurada, no estructurada) e indica si es OLTP, fichero o stream.
2. **Arquitectura.** Dibuja  una arquitectura con capas Bronze, Silver y Gold. Indica qué servicio de Azure usarías en cada paso y justifica si optas por Fabric, Databricks u otro stack
3. **Formatos.** Indica el formato de almacenamiento de cada capa y por qué.
4. **Modelo Gold.** Diseña el esquema en estrella de ventas: tabla de hechos, granularidad, medidas y al menos cuatro dimensiones.
5. **Roles.** Asigna cada paso de la arquitectura a uno de los siete roles vistos, incluyendo arquitecto de datos, analytics engineer y científico de datos.
6. **Métricas.** Como analytics engineer, redacta la definición oficial de "rotura de stock" y dos pruebas de calidad que aplicarías a la tabla Gold.
7. **Ciencia de datos.** Indica qué tablas y variables necesitaría el científico de datos para el modelo de previsión de demanda y cómo escribirías sus predicciones de vuelta en la plataforma.
8. **Gobierno.** Los datos de socios incluyen nombre, teléfono y correo. Explica qué harías en cada capa y qué papel juega Purview.
9. **IA.** Explica qué datos necesitaría el ingeniero de IA para construir el asistente en Foundry y qué requisitos de calidad le exigirías como ingeniero de datos.

## Sección 12: Repaso de conceptos
1. Un fichero donde cada evento puede tener campos distintos y anidados es un ejemplo de dato:
a) Estructurado b) Semiestructurado c) No estructurado d) Binario -> **RESPUESTA: B**
2. ¿Qué formato almacena juntos los valores de cada columna y es el estándar de facto de los lakehouses?
a) Avro b) CSV c) Parquet d) XML -> **RESPUESTA: C**
3. ¿Qué aporta Delta Lake sobre Parquet?
a) Legibilidad humana b) Un registro de transacciones con ACID y versionado c) Almacenamiento orientado a filas d) Soporte exclusivo para imágenes **-> **RESPUESTA: B****
4. Si una transacción crea un pedido pero falla la reserva de stock y se deshace todo, se está garantizando la:
a) Durabilidad b) Atomicidad c) Consistencia d) Disponibilidad -> **RESPUESTA: B**
5. En el patrón ELT, las transformaciones se realizan:
a) Antes de extraer b) En un servidor intermedio c) En el sistema de destino d) En la aplicación de origen -> **RESPUESTA: C**
6. ¿Qué capa de la arquitectura medallón contiene datos limpios, deduplicados y con tipos estandarizados?
a) Bronze b) Silver c) Gold d) Platinum -> **RESPUESTA: B** 
7. ¿Qué rol es el responsable de monitorizar que los pipelines de carga se ejecutan correctamente?
a) DBA b) Analista de datos c) Ingeniero de datos d) Ingeniero de IA -> **RESPUESTA: C** 
8. ¿Qué característica de Azure Storage permite usarlo como data lake?
a) File shares b) Tables c) Espacio de nombres jerárquico sobre Blob d) Colas -> **RESPUESTA: C** 
9. ¿Cuál es la opción recomendada de orquestación cuando todo el trabajo de datos se realiza dentro de Microsoft Fabric?
a) Azure Data Factory b) Fabric Data Factory c) Azure Stream Analytics d) Azure Data Explorer -> **RESPUESTA: B** 
10. ¿Qué servicio usarías para trazar el linaje de un dato desde el TPV hasta un informe de Power BI?
a) Microsoft Foundry b) Azure Cosmos DB c) Microsoft Purview d) Azure Databricks  -> **RESPUESTA: C** 
11. Microsoft Fabric se ofrece como:
a) IaaS b) PaaS c) SaaS d) On-premises -> **RESPUESTA: C** 
12. Una empresa necesita detectar en tiempo real cámaras frigoríficas que superan un umbral de temperatura. ¿Qué servicio encaja mejor?
a) Power BI b) Azure Stream Analytics c) Azure SQL Managed Instance d) Microsoft Purview -> **RESPUESTA: B** 
13. ¿Qué rol es responsable de que la métrica "venta neta" tenga una única definición oficial, probada y documentada?
a) DBA b) Analytics engineer c) Ingeniero de IA d) Científico de datos -> **RESPUESTA: B** 
14. ¿Qué rol construiría un modelo para predecir qué clientes dejarán de comprar en los próximos meses?
a) Analista de datos b) Arquitecto de datos c) Científico de datos d) DBA -> **RESPUESTA: C** 
15. ¿Qué rol decide si la plataforma de la empresa se organiza por dominios y qué servicios se usan en cada capa?
a) Arquitecto de datos b) Analytics engineer c) Analista de datos d) Ingeniero de IA -> **RESPUESTA: A** 
