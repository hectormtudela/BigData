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
 AYUDA EJERCICIO 5 - PREGINTAR AL PROFE MAÑANA
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


