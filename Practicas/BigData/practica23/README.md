# Práctica 23 (opcional) · De los orígenes al informe: medallion + star schema en Microsoft Fabric

**Autor:** Héctor Miguel Tudela · Máster Big Data & IA (Tajamar) · Workspace `WS-DP600-Lab-Hector` (trial 60 días) · 27/11/2026

## Caso de estudio
Pipeline de datos de ventas de extremo a extremo: datos crudos con suciedad deliberada → **Bronze** (CSV en `LH_Bronze`) → **Silver** (Delta limpio en `LH_Silver`) → **Gold** (esquema en estrella T-SQL en `WH_Gold`) → modelo semántico Direct Lake `SM_Ventas` → informe. Se orquesta con `PL_Medallion`.

Conceptos demostrados: SCD1 (MERGE) y SCD2 (histórico de ciudad), claves sustitutas, dimensión degenerada, dimensión *role-playing* de fecha con `USERELATIONSHIP`, cargas idempotentes, time intelligence en DAX.

## Índice
| Fase | Carpeta | Estado |
|---|---|---|
| 1 Bronze | [01-bronze](01-bronze/README.md) | ✅ |
| 2 Silver | [02-silver](02-silver/README.md) | ✅ |
| 3 Gold (star schema) | [03-gold](03-gold/README.md) | ✅ |
| 4 Procedimientos + SCD2 | [04-procedimientos](04-procedimientos/README.md) | ✅ |
| 5 Pipeline | [05-pipeline](05-pipeline/README.md) | ✅ 7 de 7 actividades (Outlook incluido; Teams opcional no añadido) |
| 6 Modelo semántico | [06-semantic-model](06-semantic-model/README.md) | ✅ higiene 6.3 aplicada con cuaderno |
| 7 Informe | [07-informe](07-informe/README.md) | ✅ 3 páginas hechas, matriz y medida corregidas (maquetación mejorable) |
| Opcional datamarts | [opcional-datamarts](opcional-datamarts/README.md) | ✅ 3 esquemas + vistas ejecutados (1200/1200/8 filas) |
| Opcional tiempo real | [opcional-real-time](opcional-real-time/README.md) | ✅ Eventhouse + KQL + Real-Time Dashboard (sin Eventstream) |

Presentación: [`presentacion/Practica23_Fabric.pptx`](presentacion/Practica23_Fabric.pptx) · PDF: [`docs/Practica23_Fabric.pdf`](docs/Practica23_Fabric.pdf)

## Resultado verificado (Punto de control 7)
Ventas netas 1 537 141,92 · 3609 unidades · 1200 líneas · descuento ≈ 5 %, idénticos en `WH_Gold` y en `SM_Ventas`.

## Resumen de errores
| # | Error | Solución |
|---|---|---|
| 1 | Trial "no disponible" | Incógnito/Edge y crear un ítem directamente; workspace *Prueba de Fabric* |
| 2 | Nombre de workspace ocupado | `WS-DP600-Lab-Hector` y rutas abfss adaptadas |
| 3 | `Msg 156` CREATE SCHEMA en script | Ejecutar solo en su lote |
| 4 | `Msg 15816` sys.procedures | `sys.objects WHERE type='P'` |
| 5 | SCD2 con 0 filas por retraso del SQL endpoint | Esperar 1–2 min y re-ejecutar |
| 6 | `Msg 207` CustomerKey | Columna real `Customer_SK` |
| 7 | Botones equivocados en el ribbon | Ventana 1400×900 |
| 8 | Modelo en modo Visualización | Cambiar a Edición |
| 9 | Autoindentado de TMDL | Sangría relativa + Shift+Tab |
| 10 | Vista DAX en blanco | Recargar |
| 11 | Tabla `_Medidas` en Direct Lake | Medidas en `Fact_Sales` |
| 12 | Selector de conexión en blanco (SP activity) | Editar JSON del pipeline; guardar a menudo |
| 13 | Actividad Script añadida por error | Eliminar |
| 14 | Latencia / primer clic perdido | Repetir y esperar |
| 15 | Popup de "Crear informe" bloqueado | Clic manual del usuario |
| 16 | Conexión Power BI no creable desde el selector del pipeline | Crearla en Administrar conexiones y puertas de enlace |
| 17 | Matriz del informe: "no se pueden mostrar los datos" y arrastre de Canal a Columnas fallido | Resuelto: borrar y recrear la matriz marcando los campos |
| 19 | Medida Días Medios de Envío = 0,00 | Rehacerla con DATEDIFF sobre fechas construidas desde la clave yyyymmdd (ahora 4,05) |
| 20 | Msg 156 al crear esquema/vista en un script | Envolver cada CREATE en EXEC('...') |
| 21 | KQL: group key 'Store' es 'dynamic' | tostring() antes de agrupar |
| 18 | Campo Cuerpo de Outlook (iframe) no admite escritura automatizada | Pegar el texto manualmente |

## Limitaciones
Pendiente / no hecho: verificación visual de la higiene 6.3 (aplicada por código), actividad Teams del pipeline (requiere inicio de sesión del usuario), Eventstream real del caso en tiempo real, ordenar visualmente las páginas 2 y 3 del informe.
