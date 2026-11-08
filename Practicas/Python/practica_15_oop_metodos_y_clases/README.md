# Práctica 15 · OOP: Métodos y Clases

**Alumno:** Héctor Miguel Tudela · **Máster:** Big Data & IA · Tajamar
**Entorno:** Windows 11 · Python 3.12 · VS Code · PowerShell

## Objetivo

Practicar programación orientada a objetos en Python: clases, métodos, atributos de clase e instancia, convenciones de nombres, sobrecarga de operadores, composición y conversión de tipos. Los enunciados completos están en [`practica_15_oop_metodos_y_clases.md`](practica_15_oop_metodos_y_clases.md).

## Reglas

- No se permite herencia ni polimorfismo: se usa **composición**.
- Solo biblioteca estándar de Python (`math` y `random` cuando el ejercicio lo indique).
- Cada `.py` debe ejecutarse sin errores y con una salida igual a la esperada.
- Se entrega el enlace al repositorio de GitHub con esta práctica y los ejemplos resueltos de las clases 18 y 19 (`clase_18_clases_objetos/teoria/` y `clase_19_detalles_clases_objetos/teoria/`).

## Estructura

```text
practica_15_oop_metodos_y_clases/
├── README.md                              ← este documento (progreso)
├── practica_15_oop_metodos_y_clases.md   ← enunciados de los ejercicios
├── ejercicios_basicos/                    ← B1 ... B7
├── ejercicios_intermedios/                ← I1 ... I6
├── ejercicios_avanzados/                  ← A1 ... A5
├── refactorizacion/                       ← R1 (código heredado + tu versión OOP)
└── juego/                                 ← J1
```

Cada `.py` trae su cabecera, un hueco para tu solución, el **código de prueba** del enunciado y la **salida esperada** en comentarios.

## Cómo trabajar cada ejercicio

1. Abre el `.py`, lee el enunciado en el `.md` y escribe tu solución en el hueco indicado.
2. Ejecútalo con ▶ (o `python nombre_archivo.py` desde su carpeta).
   📸 Captura: editor con tu código y terminal con la salida **igual** a la esperada.
3. Al terminar cada nivel, guarda y envía el trabajo desde `python_big_data_engineering`:
   ```powershell
   git add .
   git commit -m "practica 15: ejercicios basicos"
   git push
   ```
   📸 Captura: terminal con el `git push` correcto.

## Progreso

### Nivel básico (`ejercicios_basicos/`)

- [ ] B1 · Ficha de empleado del equipo de datos → `ejercicios_basicos/ejercicio_01_ficha_empleado.py`
- [ ] B2 · Pool de conexiones a una base de datos → `ejercicios_basicos/ejercicio_02_pool_conexiones.py`
- [ ] B3 · Plantilla de prompt reutilizable · IA Generativa → `ejercicios_basicos/ejercicio_03_plantilla_prompt.py`
- [ ] B4 · Coste de las llamadas a un LLM · IA Generativa → `ejercicios_basicos/ejercicio_04_coste_llamadas_llm.py`
- [ ] B5 · Climatización de un centro de datos → `ejercicios_basicos/ejercicio_05_climatizacion_cpd.py`
- [ ] B6 · Peso de los envíos de un almacén → `ejercicios_basicos/ejercicio_06_peso_envios.py`
- [ ] B7 · Valoraciones de clientes desde una encuesta → `ejercicios_basicos/ejercicio_07_valoraciones_encuesta.py`

### Nivel intermedio (`ejercicios_intermedios/`)

- [ ] I1 · Historial de conversación de un asistente · IA Generativa → `ejercicios_intermedios/ejercicio_01_historial_conversacion.py`
- [ ] I2 · Cuotas de tokens por equipo - IA Generativa → `ejercicios_intermedios/ejercicio_02_cuotas_tokens.py`
- [ ] I3 · Control de calidad de un lote de ingesta - Ingeniería de Datos → `ejercicios_intermedios/ejercicio_03_calidad_lote_ingesta.py`
- [ ] I4 · Reservas de salas de reuniones → `ejercicios_intermedios/ejercicio_04_reservas_salas.py`
- [ ] I5 · Depura el registro de equipos de proyecto → `ejercicios_intermedios/ejercicio_05_depurar_equipos_proyecto.py`
- [ ] I6 · Precios en varias divisas → `ejercicios_intermedios/ejercicio_06_precios_divisas.py`

### Nivel avanzado (`ejercicios_avanzados/`)

- [ ] A1 · Mini framework de pipelines ETL - Ingeniería de Datos → `ejercicios_avanzados/ejercicio_01_pipeline_etl.py`
- [ ] A2 · Simulador de MapReduce sobre logs web - Big Data → `ejercicios_avanzados/ejercicio_02_simulador_mapreduce.py`
- [ ] A3 · Regresión lineal desde cero - Machine Learning → `ejercicios_avanzados/ejercicio_03_regresion_lineal.py`
- [ ] A4 · Motor RAG mínimo para la base de conocimiento de RR. HH. - IA Generativa → `ejercicios_avanzados/ejercicio_04_motor_rag_minimo.py`
- [ ] A5 · Planificador de proyectos con dependencias → `ejercicios_avanzados/ejercicio_05_planificador_proyectos.py`

### Refactorización (`refactorizacion/`)

- [ ] R1 · Refactorizar el gestor de pedidos de una distribuidora → `refactorizacion/gestion_pedidos_oop.py` (código heredado en `refactorizacion/gestion_pedidos_original.py`)

Test de caracterización, desde la carpeta `refactorizacion/` en PowerShell (no debe mostrar nada):

```powershell
python gestion_pedidos_original.py > salida_original.txt
python gestion_pedidos_oop.py > salida_oop.txt
Compare-Object (Get-Content salida_original.txt) (Get-Content salida_oop.txt)
```

📸 Captura: los tres comandos y `Compare-Object` sin ninguna salida.

### Juego (`juego/`)

- [ ] J1 · Juego interactivo: Hundir la flota → `juego/hundir_la_flota.py`

📸 Captura: partida en curso (`mapa`, `flota`), pantalla final con el resumen y ejecución de `probar()`.

## Conclusiones

_(Rellena al terminar.)_
