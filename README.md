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
6. Marketing quiere saber qué socios tienen mayor probabilidad de dejar de comprar en los próximos 3 meses. **Analísta de datos**
7. Se debe decidir si la plataforma se construye en Fabric, en Databricks o combinando ambos. **Arquitecto de Datos**
8. Dos departamentos presentan en el comité cifras distintas de "venta neta" para el mismo mes. **Analísta de datos**


