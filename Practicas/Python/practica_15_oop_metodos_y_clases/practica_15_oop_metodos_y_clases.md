# 🧗🏽‍♂️ Practica 15 - OOP -Métodos y Clases

## Instrucciones

- **Regla general: no está permitido usar herencia ni polimorfismo.** Ninguna clase hereda de otra (`class A(B):` está prohibido). Cuando una clase necesite a otra, usa **composición**: un objeto guarda otros objetos en sus atributos.
- Solo se usa la biblioteca estándar de Python (`math` y `random` cuando el ejercicio lo indique).
- Entregar solo el vínculo a tu repo de Github que tenga, además de esta practica,  los ejemplos resueltos de la clases 18 y 19
> 💡 No hay un número mínimo de ejercicios propuestos para entregar, haz los que quieras.

---

## Sección 1 - Nivel básico

### Ejercicio B1 - Ficha de empleado del equipo de datos

El departamento de RR. HH. quiere dejar de gestionar las fichas de empleados con diccionarios sueltos. Crea la clase `Empleado`:

- Constructor con `nombre`, `departamento` y `salario_bruto` (anual, en euros). Además crea el atributo `proyectos`, que empieza siendo una **lista vacía**.
- Método `asignar_proyecto(proyecto)`: añade el proyecto a la lista **solo si no estaba ya asignado**.
- Método `salario_neto_mensual(retencion=0.15)`: aplica la retención al salario bruto, lo reparte en **14 pagas** y lo devuelve redondeado a 2 decimales.
- `__str__` con el formato `"Lucía Ortega (Data Platform) · 2 proyectos"`.
**Código de prueba:**

```python
lucia = Empleado("Lucía Ortega", "Data Platform", 42000)
mario = Empleado("Mario Gil", "BI", 35000)
lucia.asignar_proyecto("Migración a Lakehouse")
lucia.asignar_proyecto("Catálogo de datos")
lucia.asignar_proyecto("Migración a Lakehouse")
print(lucia)
print(mario)
print(lucia.proyectos)
print(lucia.salario_neto_mensual())
print(lucia.salario_neto_mensual(0.20))
print(mario.salario_neto_mensual())
```

**Salida esperada:**

```plain text
Lucía Ortega (Data Platform) · 2 proyectos
Mario Gil (BI) · 0 proyectos
['Migración a Lakehouse', 'Catálogo de datos']
2550.0
2400.0
2125.0
```

---

### Ejercicio B2 - Pool de conexiones a una base de datos

El servidor PostgreSQL de producción solo admite **3 conexiones simultáneas** desde los procesos ETL. Crea la clase `ConexionBD`:

- Atributo de clase `MAX_CONEXIONES = 3` y atributo de clase `abiertas = 0`.
- Constructor con `servidor`. Cada conexión empieza con el atributo `activa = False`.
- Método `abrir()`:
- Si la conexión ya estaba activa, devuelve `"ya estaba abierta"`.
- Si se ha alcanzado el máximo de conexiones, devuelve `"rechazada: límite alcanzado"`.
- En otro caso la activa, suma 1 a `abiertas` **de la clase** y devuelve `"abierta"`.
- Método `cerrar()`: si estaba activa, la desactiva, resta 1 a `abiertas` y devuelve `"cerrada"`; si no, devuelve `"no estaba abierta"`.
- Método de clase `estado_pool()` (con `@classmethod`) que devuelve `"2/3 conexiones en uso"`.
**Código de prueba:**

```python
etl_ventas = ConexionBD("pg-prod-01")
etl_stock = ConexionBD("pg-prod-01")
etl_crm = ConexionBD("pg-prod-01")
etl_logs = ConexionBD("pg-prod-01")
print(etl_ventas.abrir(), "|", etl_stock.abrir(), "|", etl_crm.abrir())
print(etl_logs.abrir())
print(etl_ventas.abrir())
print(ConexionBD.estado_pool())
print(etl_stock.cerrar())
print(etl_logs.abrir())
print(etl_stock.cerrar())
print(ConexionBD.estado_pool())
```

**Salida esperada:**

```plain text
abierta | abierta | abierta
rechazada: límite alcanzado
ya estaba abierta
3/3 conexiones en uso
cerrada
abierta
no estaba abierta
3/3 conexiones en uso
```

---

### Ejercicio B3 - Plantilla de prompt reutilizable · IA Generativa

El equipo de atención al cliente de una cadena de electrónica usa un LLM para clasificar reseñas. Cada analista escribe el prompt a mano y los resultados son inconsistentes. Crea la clase `PlantillaPrompt` para que todos usen la misma estructura:

- Constructor con `rol`, `tarea` y `formato_salida` (por defecto `"texto libre"`). Crea también la lista `restricciones`, vacía.
- Método `agregar_restriccion(texto)`: añade una restricción a la lista.
- Método `construir(entrada)`: devuelve **un único texto** con varias líneas, en este orden:
1. `Actúa como <rol>.`
2. `Tarea: <tarea>`
3. Si hay restricciones, la línea `Restricciones:` y una línea `<restricción>` por cada una.
4. `Formato de salida: <formato_salida>`
5. `Entrada: """<entrada>"""`
- `__repr__` con el formato `PlantillaPrompt(rol='analista de experiencia de cliente', restricciones=2)`.
Pista: construye una lista de líneas y únelas con `"\n".join(lineas)`.

**Código de prueba:**

```python
clasificador = PlantillaPrompt(
    "analista de experiencia de cliente",
    "clasifica el sentimiento de la reseña como POSITIVO, NEUTRO o NEGATIVO",
    "JSON con las claves sentimiento y motivo",
)
clasificador.agregar_restriccion("No inventes información que no aparezca en la reseña")
clasificador.agregar_restriccion("El motivo debe tener como máximo 15 palabras")
print(repr(clasificador))
print(clasificador.construir("El portátil llegó en 24 h pero la batería dura la mitad de lo anunciado."))
print("---")
resumen = PlantillaPrompt("redactor técnico", "resume la incidencia en una frase")
print(resumen.construir("El TPV de la tienda 14 no imprime tickets desde las 10:00."))
```

**Salida esperada:**

```plain text
PlantillaPrompt(rol='analista de experiencia de cliente', restricciones=2)
Actúa como analista de experiencia de cliente.
Tarea: clasifica el sentimiento de la reseña como POSITIVO, NEUTRO o NEGATIVO
Restricciones:
- No inventes información que no aparezca en la reseña
- El motivo debe tener como máximo 15 palabras
Formato de salida: JSON con las claves sentimiento y motivo
Entrada: """El portátil llegó en 24 h pero la batería dura la mitad de lo anunciado."""
---
Actúa como redactor técnico.
Tarea: resume la incidencia en una frase
Formato de salida: texto libre
Entrada: """El TPV de la tienda 14 no imprime tickets desde las 10:00."""
```

---

### Ejercicio B4 - Coste de las llamadas a un LLM · IA Generativa

Finanzas quiere saber cuánto cuesta cada llamada al proveedor de modelos de lenguaje. El proveedor cobra en dólares **por cada millón de tokens**, con un precio distinto para los tokens de entrada y los de salida. Crea la clase `LlamadaLLM`:

- Atributo de clase `PRECIOS`, un diccionario `{modelo: (precio_entrada, precio_salida)}`:
| Modelo | Entrada (/M tokens) | Salida (/M tokens) |  |
| --- | --- | --- |
| `modelo-lite` | 0.20 | 0.80 |
| `modelo-pro` | 3.00 | 12.00 |

- Atributo de clase `total_llamadas = 0`, que se incrementa cada vez que se crea una llamada.
- Constructor con `modelo`, `tokens_entrada` y `tokens_salida`.
- Método `coste()`: devuelve el coste en dólares redondeado a **6 decimales**.
- Método `tokens_totales()`.
- `__repr__` con el formato `LlamadaLLM(modelo-lite, 1500 tokens, $0.00048)`.
**Código de prueba:**

```python
llamadas = [
    LlamadaLLM("modelo-lite", 1200, 300),
    LlamadaLLM("modelo-pro", 1200, 300),
    LlamadaLLM("modelo-lite", 8000, 1500),
    LlamadaLLM("modelo-pro", 25000, 4000),
]
for llamada in llamadas:
    print(llamada)
print("Llamadas registradas:", LlamadaLLM.total_llamadas)
print(f"Coste total: ${round(sum([l.coste() for l in llamadas]), 6)}")
coste_pro = sum([l.coste() for l in llamadas if l.modelo == "modelo-pro"])
print("Peso de modelo-pro:", round(100 * coste_pro / sum([l.coste() for l in llamadas]), 1), "%")
```

**Salida esperada:**

```plain text
LlamadaLLM(modelo-lite, 1500 tokens, $0.00048)
LlamadaLLM(modelo-pro, 1500 tokens, $0.0072)
LlamadaLLM(modelo-lite, 9500 tokens, $0.0028)
LlamadaLLM(modelo-pro, 29000 tokens, $0.123)
Llamadas registradas: 4
Coste total: $0.13348
Peso de modelo-pro: 97.5 %
```

---

### Ejercicio B5 - Climatización de un centro de datos

La consigna de temperatura de cada sala del CPD solo puede estar entre **18 y 27 °C**. Nadie debe poder cambiarla «a mano» desde fuera del objeto. Crea la clase `Climatizador` aplicando las convenciones de nombres:

- Atributos de clase `TEMP_MIN = 18` y `TEMP_MAX = 27`.
- Constructor con `sala` (público) y `consigna` inicial. La consigna se guarda en el atributo **privado** `__consigna`, ya limitada al rango permitido. Crea también el atributo de **uso interno** `_historial`, una lista con la consigna inicial.
- Método **de uso interno** `_limitar(valor)`: devuelve el valor ajustado al rango (si es menor que el mínimo, el mínimo; si es mayor que el máximo, el máximo).
- Método `ajustar(grados)`: suma (o resta, si es negativo) los grados a la consigna, la limita con `_limitar`, la añade al historial y devuelve la nueva consigna.
- Método `consigna()`: devuelve el valor actual.
- `__str__`: `"Sala A · 22 °C · 3 cambios"` (los cambios son las entradas del historial menos la inicial).
Responde en un comentario al final del archivo: ¿por qué `hasattr(sala_a, "__consigna")` devuelve `False` si el atributo existe?

**Código de prueba:**

```python
sala_a = Climatizador("A", 22)
sala_b = Climatizador("B", 31)
print(sala_a.ajustar(-3), sala_a.ajustar(-4), sala_a.ajustar(6))
print(sala_a)
print(sala_b)
print(sala_a._historial)
print(vars(sala_b))
print(hasattr(sala_a, "__consigna"), hasattr(sala_a, "_Climatizador__consigna"))
```

**Salida esperada:**

```plain text
19 18 24
Sala A · 24 °C · 3 cambios
Sala B · 27 °C · 0 cambios
[22, 19, 18, 24]
{'sala': 'B', '_Climatizador__consigna': 27, '_historial': [27]}
False True
```

---

### Ejercicio B6 - Peso de los envíos de un almacén

El almacén de una empresa de e-commerce agrupa paquetes en palés y necesita sumar, comparar y ordenar pesos. Crea la clase `PesoEnvio`:

- Constructor con `gramos` (entero). Si llega un valor negativo, se guarda `0`.
- Sobrecarga `+` para que la suma de dos pesos devuelva un **objeto nuevo** `PesoEnvio`.
- Sobrecarga `==` y `<` comparando los gramos.
- `__str__`: si el peso es de 1000 g o más, se muestra en kilos con 2 decimales (`"1.25 kg"`); si no, en gramos (`"850 g"`).
- `__repr__`: `PesoEnvio(850)`.
**Código de prueba:**

```python
paquetes = [PesoEnvio(850), PesoEnvio(1250), PesoEnvio(400), PesoEnvio(-30), PesoEnvio(2300)]
print(paquetes[0] + paquetes[2])
print(paquetes[0] + paquetes[1])
pale = PesoEnvio(0)
for p in paquetes:
    pale = pale + p
print("Palé:", pale)
print(sorted(paquetes))
print("Más pesado:", max(paquetes))
print(PesoEnvio(1250) == paquetes[1], PesoEnvio(1250) is paquetes[1])
```

**Salida esperada:**

```plain text
1.25 kg
2.10 kg
Palé: 4.80 kg
[PesoEnvio(0), PesoEnvio(400), PesoEnvio(850), PesoEnvio(1250), PesoEnvio(2300)]
Más pesado: 2.30 kg
True False
```

---

### Ejercicio B7 - Valoraciones de clientes desde una encuesta

La herramienta de encuestas exporta las valoraciones como texto: `"4,5/5"`, `"3/5"`, `"0/5"` (el `0` significa *sin valorar*). Crea la clase `Valoracion`:

- El constructor recibe el texto, toma la parte anterior a la `/`, cambia la coma por punto y guarda el valor como `float` en el atributo **privado** `__nota`.
- `float(v)`: devuelve la nota.
- `int(v)`: devuelve la nota **redondeada** a entero.
- `bool(v)`: `False` si la nota es 0 (sin valorar).
- `str(v)`: tantas `★` como `int(v)` y tantas `☆` como falten hasta 5, seguido de la nota entre paréntesis: `"★★★★☆ (4.5)"`.
**Código de prueba:**

```python
respuestas = ["4,5/5", "3/5", "0/5", "2,4/5", "5/5", "0/5"]
valoraciones = [Valoracion(r) for r in respuestas]
for v in valoraciones:
    print(str(v), float(v), int(v), bool(v))
validas = [v for v in valoraciones if v]
print("Respuestas válidas:", len(validas), "de", len(valoraciones))
print("Media:", round(sum([float(v) for v in validas]) / len(validas), 2))
```

**Salida esperada:**

```plain text
★★★★☆ (4.5) 4.5 4 True
★★★☆☆ (3.0) 3.0 3 True
☆☆☆☆☆ (0.0) 0.0 0 False
★★☆☆☆ (2.4) 2.4 2 True
★★★★★ (5.0) 5.0 5 True
☆☆☆☆☆ (0.0) 0.0 0 False
Respuestas válidas: 4 de 6
Media: 3.73
```

---

## Sección 2 - Nivel intermedio

### Ejercicio I1 - Historial de conversación de un asistente · IA Generativa

Una aseguradora está construyendo un asistente para tramitar partes de siniestros. Las API de los LLM reciben el historial como una lista de diccionarios `{"role": ..., "content": ...}` y tienen una **ventana de contexto** limitada. Modela el historial con **dos clases relacionadas por composición**.

**Clase ****`Mensaje`**

- Atributo de clase `ROLES_VALIDOS = ("system", "user", "assistant")`.
- Constructor con `rol` y `contenido`.
- Método `tokens()`: estimación sencilla, **1 token por palabra** (`len(contenido.split())`).
- Método `a_dict()`: devuelve `{"role": rol, "content": contenido}`.
- `__str__`: `"[user] Quiero dar un parte de mi coche"`.
**Clase ****`Conversacion`**

- Constructor con `max_tokens`. Guarda los mensajes en una lista **privada** `__mensajes`.
- Método `agregar(rol, contenido)`: si el rol no está en `Mensaje.ROLES_VALIDOS`, no añade nada y devuelve `False`. Si es válido, crea el `Mensaje`, lo añade, llama a `_recortar()` y devuelve `True`.
- `+=` recibe una **tupla** `(rol, contenido)` y usa `agregar`.
- Método `tokens_totales()`.
- Método de uso interno `_recortar()`: mientras los tokens totales superen `max_tokens`, elimina el **mensaje más antiguo que no sea ****`system`** (el mensaje de sistema nunca se borra).
- `len(conv)`: número de mensajes. `palabra in conv`: `True` si la palabra aparece en algún mensaje, sin distinguir mayúsculas.
- Método `para_api()`: lista de diccionarios de todos los mensajes.
- `__str__`: un mensaje por línea.
**Código de prueba:**

```python
conv = Conversacion(max_tokens=30)
conv += ("system", "Eres el asistente de siniestros de Seguros Brisamar")
conv += ("user", "Quiero dar un parte de mi coche")
conv += ("assistant", "Claro, ¿cuál es la matrícula del vehículo?")
print(conv.agregar("cliente", "Hola"))
print(len(conv), conv.tokens_totales())
conv += ("user", "Es la 4821 KLM y el golpe fue en un parking")
print(len(conv), conv.tokens_totales())
print(conv)
print("matrícula" in conv, "COCHE" in conv)
print(conv.para_api()[0])
```

**Salida esperada:**

```plain text
False
3 22
3 26
[system] Eres el asistente de siniestros de Seguros Brisamar
[assistant] Claro, ¿cuál es la matrícula del vehículo?
[user] Es la 4821 KLM y el golpe fue en un parking
True False
{'role': 'system', 'content': 'Eres el asistente de siniestros de Seguros Brisamar'}
```

---

### Ejercicio I2 - Cuotas de tokens por equipo - IA Generativa

Una consultora da acceso a un LLM corporativo a varios equipos y cada uno tiene una **cuota mensual de tokens**. La plataforma debe rechazar las peticiones que superen la cuota y mostrar un panel de consumo. Crea la clase `CuotaEquipo`:

- Atributo de clase `peticiones_rechazadas = 0` (para **todos** los equipos).
- Constructor con `equipo` y `limite_tokens`. Guarda los consumos en una lista **privada** `__consumos`, donde cada consumo es una tupla `(caso_uso, tokens)`.
- Método `consumido()` y método `restante()`.
- Método `registrar(caso_uso, tokens)`: si cabe en lo que queda, guarda el consumo y devuelve `True`; si no, suma 1 a `peticiones_rechazadas` **de la clase** y devuelve `False`.
- Método `porcentaje()`: porcentaje de la cuota consumido, redondeado a 1 decimal.
- Método `top_caso_uso()`: el caso de uso que más tokens ha consumido (suma por caso de uso). Si no hay consumos, `None`.
- `bool(cuota)`: `True` mientras quede algún token disponible.
- `<` compara por porcentaje consumido (para poder ordenar el panel).
- `__str__`: nombre del equipo con ancho 10, una barra de 10 caracteres (`#` por cada 10 % consumido, redondeando hacia abajo, y `.` para el resto) y el porcentaje: `"Marketing [######....] 64.0 %"`.
**Código de prueba:**

```python
marketing = CuotaEquipo("Marketing", 50_000)
legal = CuotaEquipo("Legal", 20_000)
soporte = CuotaEquipo("Soporte", 80_000)

marketing.registrar("copys campaña", 18_000)
marketing.registrar("traducciones", 9_000)
marketing.registrar("copys campaña", 5_000)
legal.registrar("resumen contratos", 15_000)
print(legal.registrar("resumen contratos", 6_000))
print(legal.registrar("cláusulas", 5_000))
soporte.registrar("respuestas tickets", 12_000)

panel = sorted([marketing, legal, soporte])
panel.reverse()
for cuota in panel:
    print(cuota)
print("Restante Legal:", legal.restante(), "| ¿Puede seguir?", bool(legal))
print("Top Marketing:", marketing.top_caso_uso())
print("Rechazadas en total:", CuotaEquipo.peticiones_rechazadas)
print(CuotaEquipo("I+D", 10_000).top_caso_uso())
```

**Salida esperada:**

```plain text
False
True
Legal      [##########] 100.0 %
Marketing  [######....] 64.0 %
Soporte    [#.........] 15.0 %
Restante Legal: 0 | ¿Puede seguir? False
Top Marketing: copys campaña
Rechazadas en total: 1
None
```

---

### Ejercicio I3 - Control de calidad de un lote de ingesta - Ingeniería de Datos

Antes de cargar los pedidos en la capa *silver* del data lake, el equipo de Data Engineering quiere separar los registros válidos de los rechazados e informar del motivo. Implementa **dos clases relacionadas por composición**.

**Clase ****`ReglaCalidad`**

- Constructor con `columna`, `tipo` (texto: `"int"`, `"float"` o `"str"`), `obligatoria` (por defecto `True`) y `minimo` (por defecto `None`).
- Método `comprobar(registro)`: recibe un diccionario y devuelve un **texto con el error** o `None` si la regla se cumple. Comprueba en este orden:
1. Si la columna no está o vale `None`: si es obligatoria, `"<columna>: falta"`; si no es obligatoria, la regla se cumple.
2. Si `type(valor).__name__` no coincide con `tipo`: `"<columna>: se esperaba <tipo>"`.
3. Si hay mínimo y el valor es menor: `"<columna>: menor que <minimo>"`.
- `__repr__`: `Regla(importe:float>=0.01)` o, sin mínimo y opcional, `Regla(cupon:str?)` (`?` indica opcional).
**Clase ****`ValidadorLote`**

- Constructor con `nombre`. Guarda una lista **privada** de reglas y dos listas públicas vacías: `validos` y `rechazados`.
- `+=` añade una `ReglaCalidad`. `len(validador)` devuelve el número de reglas.
- Método `validar(registro)`: devuelve la lista de errores de **todas** las reglas.
- Método `procesar(lote)`: vacía `validos` y `rechazados` y recorre el lote. Los registros sin errores van a `validos`; los demás van a `rechazados` como tupla `(registro, errores)`.
- Método `tasa_calidad()`: porcentaje de válidos (1 decimal).
- `__str__`: informe con el formato de la salida esperada.
**Código de prueba:**

```python
validador = ValidadorLote("pedidos_silver")
validador += ReglaCalidad("id_pedido", "int")
validador += ReglaCalidad("cliente", "str")
validador += ReglaCalidad("importe", "float", minimo=0.01)
validador += ReglaCalidad("unidades", "int", minimo=1)
validador += ReglaCalidad("cupon", "str", obligatoria=False)

lote = [
    {"id_pedido": 5001, "cliente": "C-17", "importe": 89.9, "unidades": 2},
    {"id_pedido": 5002, "cliente": "C-03", "importe": "45,00", "unidades": 1},
    {"id_pedido": 5003, "importe": 12.5, "unidades": 0, "cupon": "BF26"},
    {"id_pedido": 5004, "cliente": "C-17", "importe": 230.0, "unidades": 4, "cupon": "BF26"},
    {"id_pedido": 5005, "cliente": "C-88", "importe": -5.0, "unidades": 1, "cupon": 10},
]
validador.procesar(lote)
print(validador)
print([r["id_pedido"] for r in validador.validos])
print(ReglaCalidad("importe", "float", minimo=0.01), ReglaCalidad("cupon", "str", obligatoria=False))
```

**Salida esperada:**

```plain text
Validador pedidos_silver · 5 reglas
Válidos: 2 | Rechazados: 3 | Calidad: 40.0 %
  - 5002: importe: se esperaba float
  - 5003: cliente: falta; unidades: menor que 1
  - 5005: importe: menor que 0.01; cupon: se esperaba str
[5001, 5004]
Regla(importe:float>=0.01) Regla(cupon:str?)
```

---

### Ejercicio I4 - Reservas de salas de reuniones

La oficina central de una empresa de logística tiene salas que se reservan por franjas horarias y continuamente hay reservas solapadas. Implementa:

**Clase ****`FranjaHoraria`**

- Constructor con `inicio` y `fin` como texto `"HH:MM"`. Internamente guarda los **minutos desde las 00:00** en dos atributos privados.
- Método de uso interno `_a_minutos(texto)` que hace esa conversión.
- `len(franja)`: duración en minutos.
- `"HH:MM" in franja`: `True` si la hora está dentro de la franja (incluye el inicio, **excluye** el fin).
- Método `solapa(otra)`: `True` si las dos franjas comparten algún minuto.
- `<` compara por hora de inicio.
- `__str__`: `"09:30-10:15"`.
**Clase ****`Sala`**

- Constructor con `nombre` y `capacidad`. Lista **privada** de reservas; cada reserva es una tupla `(franja, responsable, asistentes)`.
- Método `reservar(inicio, fin, responsable, asistentes)` que devuelve un texto:
- `"RECHAZADA: aforo"` si los asistentes superan la capacidad.
- `"RECHAZADA: solapa con <franja> (<responsable>)"` si choca con una reserva existente.
- `"OK <franja>"` si se guarda.
- Método `ocupada_a(hora)`: responsable de la reserva que ocupa la sala a esa hora, o `None`.
- Método `ocupacion(jornada_min=600)`: porcentaje de una jornada de 10 h reservado (1 decimal).
- Método `agenda()`: texto con las reservas **ordenadas por hora**, una por línea: `"09:00-10:00 · Ana (6 pers.)"`.
**Código de prueba:**

```python
sala = Sala("Atlas", 8)
print(sala.reservar("10:00", "11:30", "Ana", 6))
print(sala.reservar("09:00", "10:00", "Luis", 4))
print(sala.reservar("11:00", "12:00", "Marta", 5))
print(sala.reservar("12:00", "12:45", "Iker", 12))
print(sala.reservar("15:15", "16:00", "Iker", 7))
print(sala.agenda())
print(sala.ocupada_a("10:59"), sala.ocupada_a("11:30"), sala.ocupada_a("15:15"))
print("Ocupación:", sala.ocupacion(), "%")
f = FranjaHoraria("08:45", "09:20")
print(f, len(f), "09:20" in f)
```

**Salida esperada:**

```plain text
OK 10:00-11:30
OK 09:00-10:00
RECHAZADA: solapa con 10:00-11:30 (Ana)
RECHAZADA: aforo
OK 15:15-16:00
09:00-10:00 · Luis (4 pers.)
10:00-11:30 · Ana (6 pers.)
15:15-16:00 · Iker (7 pers.)
Ana None Iker
Ocupación: 32.5 %
08:45-09:20 35 False
```

---

### Ejercicio I5 - Depura el registro de equipos de proyecto

La PMO de una consultora registra los equipos de proyecto y las horas asignadas. Se quiere:

- Que cada equipo tenga **sus propios** miembros y **sus propias** horas.
- Que la clase lleve la cuenta de **todos** los equipos creados (`equipos_creados`) y de las horas de **toda** la empresa (`horas_empresa`).
El programador que escribió la clase cometió **tres errores** relacionados con los atributos de clase y de instancia:

```python
class EquipoProyecto:
    miembros = []
    horas_empresa = 0
    equipos_creados = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.horas = 0
        self.equipos_creados += 1

    def incorporar(self, persona, horas):
        self.miembros.append(persona)
        self.horas += horas
        self.horas_empresa += horas

    def __str__(self):
        return f"{self.nombre}:{self.miembros} ·{self.horas} h"
```

Al ejecutarlo con el código de prueba de abajo, la salida es esta (incorrecta):

```plain text
Data Lake: ['Ana', 'Luis', 'Sara'] · 200 h
Churn ML: ['Ana', 'Luis', 'Sara'] · 60 h
0 0
True
{'nombre': 'Data Lake', 'horas': 200, 'equipos_creados': 1, 'horas_empresa': 200}
```

Se pide:

1. **Antes de tocar nada**, escribe en un comentario al principio del archivo por qué cada línea de la salida es incorrecta.
2. Explica en el comentario por qué `vars(datos)` contiene `equipos_creados` y `horas_empresa` si están declarados como atributos **de clase**.
3. Corrige la clase para que el código de prueba produzca la salida esperada.
**Código de prueba:**

```python
datos = EquipoProyecto("Data Lake")
ml = EquipoProyecto("Churn ML")
datos.incorporar("Ana", 120)
datos.incorporar("Luis", 80)
ml.incorporar("Sara", 60)
print(datos)
print(ml)
print(EquipoProyecto.equipos_creados, EquipoProyecto.horas_empresa)
print(datos.miembros is ml.miembros)
print(vars(datos))
```

**Salida esperada del código corregido:**

```plain text
Data Lake: ['Ana', 'Luis'] · 200 h
Churn ML: ['Sara'] · 60 h
2 260
False
{'nombre': 'Data Lake', 'horas': 200, 'miembros': ['Ana', 'Luis']}
```

---

### Ejercicio I6 - Precios en varias divisas

Un marketplace vende en euros, dólares y libras. Hasta ahora los precios se guardaban como `float` y se sumaban sin convertir, con resultados absurdos. Crea la clase `Precio`:

- Atributo de clase `TASAS_A_EUR = {"EUR": 1.0, "USD": 0.92, "GBP": 1.17}` (cuántos euros vale 1 unidad de cada divisa).
- Constructor con `cantidad` y `divisa` (por defecto `"EUR"`). La cantidad se guarda redondeada a 2 decimales.
- Método `en_euros()`: la cantidad convertida a euros (sin redondear).
- Método `convertir_a(divisa)`: devuelve un **`Precio`**** nuevo** en la divisa indicada, redondeado a 2 decimales.
- `+`: suma dos precios y devuelve el resultado **en la divisa del primero**.
- : multiplica un precio por un número.
- `==` y `<`: comparan el valor **en euros** (para `==`, redondeado a 2 decimales).
- `float(precio)`: el valor en euros redondeado a 2 decimales.
- Método de clase `actualizar_tasa(divisa, tasa)` con `@classmethod`.
- `__str__`: `"12.50 USD"` (siempre 2 decimales).
**Código de prueba:**

```python
auriculares = Precio(59.90)
cable = Precio(12.50, "USD")
funda = Precio(15, "GBP")
print(auriculares + cable)
print(cable + auriculares)
print(funda.convertir_a("EUR"), funda.convertir_a("USD"))
print(cable * 3)
print(Precio(9.20) == Precio(10, "USD"), Precio(9.20) is Precio(10, "USD"))
catalogo = [auriculares, cable, funda]
print("Más barato:", min(catalogo), "| Más caro:", max(catalogo))
print("Total en EUR:", round(sum([float(p) for p in catalogo]), 2))
Precio.actualizar_tasa("USD", 0.95)
print(cable.convertir_a("EUR"), float(cable))
```

**Salida esperada:**

```plain text
71.40 EUR
77.61 USD
17.55 EUR 19.08 USD
37.50 USD
True False
Más barato: 12.50 USD | Más caro: 59.90 EUR
Total en EUR: 88.95
11.88 EUR 11.88
```

---

## Sección 3 - Nivel avanzado

### Ejercicio A1 - Mini framework de pipelines ETL - Ingeniería de Datos

El equipo de datos de una cadena de supermercados quiere un pequeño framework propio para encadenar pasos de limpieza sobre registros (diccionarios) y medir cuántos registros entran y salen de cada paso. Aprovecha que **en Python las funciones son objetos**: se pueden guardar en atributos y llamar después.

**Clase ****`Etapa`**

- Atributo de clase `TIPOS = ("transformar", "filtrar")`.
- Constructor con `nombre`, `funcion` y `tipo` (por defecto `"transformar"`).
- En una etapa `transformar`, `funcion(registro)` devuelve el registro modificado.
- En una etapa `filtrar`, `funcion(registro)` devuelve `True` si el registro **se queda**.
- Método `aplicar(registros)`: recibe una lista y devuelve una lista **nueva**. Las transformaciones se aplican sobre una **copia** de cada registro (`dict(registro)`) para no modificar los datos de entrada.
- `__repr__`: `Etapa(limpiar_tienda, transformar)`.
**Clase ****`Pipeline`**

- Constructor con `nombre`. Lista **privada** de etapas y lista **privada** de métricas.
- `+=` añade una `Etapa`. Si se intenta añadir algo que no es `Etapa` (compruébalo con `type(x).__name__`), se ignora.
- `len(pipeline)`: número de etapas.
- Método `ejecutar(registros)`: aplica las etapas en orden, guarda en las métricas una tupla `(nombre_etapa, entrada, salida)` por etapa y devuelve el resultado final. Cada ejecución reinicia las métricas.
- Método `informe()`: texto con una línea por etapa y una línea final con los descartados en total (ver salida).
- `__str__`: `"Pipeline ventas_diarias: limpiar_tienda → solo_completados → importe_con_iva → solo_grandes"`.
**Código de prueba:**

```python
def limpiar_tienda(r):
    r["tienda"] = r["tienda"].strip().upper()
    return r

def es_completado(r):
    return r["estado"] == "completado"

def con_iva(r):
    r["importe_iva"] = round(r["importe"] * 1.21, 2)
    return r

def es_grande(r):
    return r["importe_iva"] >= 50

ventas = [
    {"id": 1, "tienda": " mad-01", "estado": "completado", "importe": 120.0},
    {"id": 2, "tienda": "bcn-02 ", "estado": "cancelado", "importe": 80.0},
    {"id": 3, "tienda": "mad-01", "estado": "completado", "importe": 35.5},
    {"id": 4, "tienda": " vlc-03 ", "estado": "completado", "importe": 41.4},
    {"id": 5, "tienda": "bcn-02", "estado": "devuelto", "importe": 15.0},
    {"id": 6, "tienda": "vlc-03", "estado": "completado", "importe": 260.0},
]

p = Pipeline("ventas_diarias")
p += Etapa("limpiar_tienda", limpiar_tienda)
p += Etapa("solo_completados", es_completado, "filtrar")
p += Etapa("importe_con_iva", con_iva)
p += Etapa("solo_grandes", es_grande, "filtrar")
p += "esto no es una etapa"
print(p, "|", len(p), "etapas")
resultado = p.ejecutar(ventas)
for r in resultado:
    print(r)
print(p.informe())
print(ventas[0])
print(type(limpiar_tienda).__name__, Etapa("x", con_iva))
```

**Salida esperada:**

```plain text
Pipeline ventas_diarias: limpiar_tienda → solo_completados → importe_con_iva → solo_grandes | 4 etapas
{'id': 1, 'tienda': 'MAD-01', 'estado': 'completado', 'importe': 120.0, 'importe_iva': 145.2}
{'id': 4, 'tienda': 'VLC-03', 'estado': 'completado', 'importe': 41.4, 'importe_iva': 50.09}
{'id': 6, 'tienda': 'VLC-03', 'estado': 'completado', 'importe': 260.0, 'importe_iva': 314.6}
Informe de ventas_diarias
  limpiar_tienda       6 →   6  (-0)
  solo_completados     6 →   4  (-2)
  importe_con_iva      4 →   4  (-0)
  solo_grandes         4 →   3  (-1)
  Descartados en total: 3
{'id': 1, 'tienda': ' mad-01', 'estado': 'completado', 'importe': 120.0}
function Etapa(x, transformar)
```

---

### Ejercicio A2 - Simulador de MapReduce sobre logs web - Big Data

Antes de lanzar trabajos en el clúster Spark, el equipo de Big Data de un e-commerce quiere que los nuevos ingenieros entiendan cómo funciona el modelo **MapReduce**: los datos se reparten en **particiones**, cada partición se procesa por separado (*map*), se agregan resultados parciales en cada nodo (*combiner*) y finalmente se fusionan (*reduce*). El tráfico de red del *shuffle* depende de cuántos pares viajan entre nodos.

Cada línea de log tiene 5 campos separados por espacios: `timestamp país endpoint estado bytes`.

**Clase ****`ConteoParcial`** (resultado agregado clave → valor)

- Constructor sin parámetros: crea un diccionario **privado** vacío.
- Método `sumar(clave, valor)`.
- Método `get(clave)`: valor de la clave o `0`.
- `+`: devuelve un `ConteoParcial` **nuevo** que fusiona los dos (sumando los valores de las claves comunes). No modifica los originales.
- `len()`: número de claves distintas. Método `total()`: suma de todos los valores.
- Método `top(n)`: lista de las `n` tuplas `(clave, valor)` con mayor valor; a igual valor, por orden alfabético de clave.
**Clase ****`Particion`**

- Constructor con `id_particion` y `lineas`. `len()` devuelve el número de líneas.
- Método `mapear(funcion_map)`: aplica la función a cada línea y devuelve **la lista de todos los pares** generados. La función de map devuelve una **lista** de pares `(clave, valor)` (vacía si la línea no es válida).
**Clase ****`TrabajoMapReduce`**

- Constructor con `nombre`, `funcion_map` y `usar_combinador` (por defecto `True`).
- Método `ejecutar(particiones)`:
- Para cada partición: obtiene los pares y los agrega en un `ConteoParcial` local.
- Pares enviados al shuffle por la partición: si hay combinador, el número de **claves** del parcial; si no, el número de **pares**.
- Fusiona todos los parciales con `+` y devuelve el `ConteoParcial` final.
- Guarda en una lista **privada** una tupla por partición `(id, lineas, pares, enviados)`.
- Método `estadisticas()`: texto como el de la salida esperada.
Escribe además tres **funciones globales de map** (las líneas mal formadas, que no tienen 5 campos, no generan pares):

- `peticiones_por_pais(linea)` → `[(pais, 1)]`.
- `bytes_ok_por_endpoint(linea)` → `[(endpoint, bytes)]` solo si el estado es `200`.
- `errores_por_endpoint(linea)` → `[(endpoint, 1)]` solo si el estado es `500` o superior.
**Código de prueba:**

```python
particiones = [
    Particion("p0", ["10:01 ES /home 200 5120", "10:01 ES /checkout 200 830",
                     "10:02 FR /home 200 4980", "10:02 ES /home 500 0"]),
    Particion("p1", ["10:03 ES /search 200 2210", "10:03 PT /home 200 5003",
                     "linea corrupta", "10:04 ES /checkout 503 0", "10:04 FR /search 200 1990"]),
    Particion("p2", ["10:05 ES /home 200 5120", "10:05 ES /home 200 5120",
                     "10:06 ES /home 200 5120", "10:06 FR /checkout 500 0"]),
]

paises = TrabajoMapReduce("peticiones_por_pais", peticiones_por_pais)
resultado = paises.ejecutar(particiones)
print(paises.estadisticas())
print("Top 2:", resultado.top(2), "| Total:", resultado.total(), "| PT:", resultado.get("PT"), "| IT:", resultado.get("IT"))

sin_comb = TrabajoMapReduce("peticiones_por_pais", peticiones_por_pais, usar_combinador=False)
resultado_2 = sin_comb.ejecutar(particiones)
print(sin_comb.estadisticas())
print("Mismo resultado:", resultado_2.top(10) == resultado.top(10))

volumen = TrabajoMapReduce("bytes_ok", bytes_ok_por_endpoint).ejecutar(particiones)
print("Bytes OK:", volumen.top(3))
errores = TrabajoMapReduce("errores", errores_por_endpoint).ejecutar(particiones)
print("Errores:", errores.top(5), "| endpoints con error:", len(errores))
```

**Salida esperada:**

```plain text
Trabajo peticiones_por_pais (con combinador)
  p0: 4 líneas → 4 pares → 2 enviados
  p1: 5 líneas → 4 pares → 3 enviados
  p2: 4 líneas → 4 pares → 2 enviados
  Shuffle total: 7 pares
Top 2: [('ES', 8), ('FR', 3)] | Total: 12 | PT: 1 | IT: 0
Trabajo peticiones_por_pais (sin combinador)
  p0: 4 líneas → 4 pares → 4 enviados
  p1: 5 líneas → 4 pares → 4 enviados
  p2: 4 líneas → 4 pares → 4 enviados
  Shuffle total: 12 pares
Mismo resultado: True
Bytes OK: [('/home', 30463), ('/search', 4200), ('/checkout', 830)]
Errores: [('/checkout', 2), ('/home', 1)] | endpoints con error: 2
```

---

### Ejercicio A3 - Regresión lineal desde cero - Machine Learning

El equipo de marketing de una cadena de gimnasios quiere estimar cuántas **altas mensuales** se consiguen según la **inversión en publicidad digital** (miles de euros). Antes de usar scikit-learn, vas a programar el modelo a mano para entender qué hay dentro de `fit()` y `predict()`.

Fórmulas de mínimos cuadrados para `y = pendiente · x + intercepto`:

- `pendiente = Σ (xᵢ − x̄)(yᵢ − ȳ) / Σ (xᵢ − x̄)²`
- `intercepto = ȳ − pendiente · x̄`
- `R² = 1 − Σ (yᵢ − ŷᵢ)² / Σ (yᵢ − ȳ)²`
- `MAE = Σ |yᵢ − ŷᵢ| / n`
**Clase ****`ConjuntoDatos`**

- Constructor con `x`, `y` (listas de igual longitud) y `nombre_x`, `nombre_y`.
- `len()`: número de observaciones.
- Método `dividir(proporcion_train=0.75)`: devuelve una tupla `(train, test)` de **dos objetos ****`ConjuntoDatos`**** nuevos**. Las primeras `int(len * proporcion)` observaciones van a train y el resto a test (sin desordenar, para que el resultado sea reproducible).
- `__repr__`: `ConjuntoDatos(inversion_k€ → altas, n=12)`.
**Clase ****`RegresionLinealSimple`**

- Constructor sin datos: `pendiente` e `intercepto` valen `None`. Atributo de clase `modelos_entrenados = 0`.
- Método `entrenar(datos)`: calcula pendiente e intercepto con las fórmulas, suma 1 a `modelos_entrenados` y **devuelve ****`self`** (así se puede escribir `modelo = RegresionLinealSimple().entrenar(train)`).
- Método `predecir(x)`: si `x` es una lista, devuelve la lista de predicciones; si es un número, una sola predicción. Redondea a 2 decimales. Comprueba el tipo con `type(x).__name__`.
- Métodos `r2(datos)` y `mae(datos)`, ambos redondeados a 3 decimales.
- `bool(modelo)`: `True` si el modelo está entrenado.
- `__str__`: `"altas = 18.42 · inversion_k€ + 31.05"` (2 decimales) o `"Modelo sin entrenar"`.
**Código de prueba:**

```python
inversion = [2.0, 3.5, 1.0, 4.0, 5.5, 3.0, 6.0, 2.5, 4.5, 7.0, 5.0, 1.5]
altas = [68, 95, 49, 112, 133, 88, 150, 74, 120, 162, 128, 60]
datos = ConjuntoDatos(inversion, altas, "inversion_k€", "altas")
train, test = datos.dividir(0.75)
print(datos, train, test)

modelo = RegresionLinealSimple()
print(modelo, bool(modelo))
modelo = modelo.entrenar(train)
print(modelo, bool(modelo))
print("R² train:", modelo.r2(train), "| R² test:", modelo.r2(test))
print("MAE test:", modelo.mae(test), "altas")
print("Predicción test:", modelo.predecir(test.x), "| real:", test.y)
print("¿Y si invertimos 8 k€?", modelo.predecir(8.0))
completo = RegresionLinealSimple().entrenar(datos)
print(completo, "| modelos entrenados:", RegresionLinealSimple.modelos_entrenados)
```

**Salida esperada:**

```plain text
ConjuntoDatos(inversion_k€ → altas, n=12) ConjuntoDatos(inversion_k€ → altas, n=9) ConjuntoDatos(inversion_k€ → altas, n=3)
Modelo sin entrenar False
altas = 20.03 · inversion_k€ + 27.55 True
R² train: 0.991 | R² test: 0.993
MAE test: 2.82 altas
Predicción test: [167.77, 127.71, 57.6] | real: [162, 128, 60]
¿Y si invertimos 8 k€? 187.81
altas = 19.42 · inversion_k€ + 29.62 | modelos entrenados: 2
```

---

### Ejercicio A4 - Motor RAG mínimo para la base de conocimiento de RR. HH. - IA Generativa

Una empresa de 800 empleados quiere un asistente que responda dudas sobre sus políticas internas **sin inventar**. La técnica es **RAG** (*Retrieval-Augmented Generation*): antes de llamar al LLM se buscan los fragmentos más parecidos a la pregunta y se insertan en el prompt como contexto. En producción se usan *embeddings* y una base vectorial; aquí vas a construir una versión didáctica con **bolsa de palabras** y **similitud del coseno**.

**Clase ****`Documento`**

- Atributo de clase `STOPWORDS = {"el", "la", "los", "las", "de", "del", "en", "y", "a", "un", "una", "por", "para", "con", "que", "se", "al", "es", "lo", "mi", "tengo", "hay", "cuántos", "cuántas", "cuál", "cómo"}`.
- Constructor con `id_doc`, `titulo` y `texto`.
- Método `terminos()`: devuelve un diccionario `{palabra: frecuencia}` del texto en minúsculas, quitando los signos `.,;:¿?¡!()` y las stopwords.
- `__repr__`: `Documento(POL-01: Teletrabajo)`.
**Clase ****`IndiceDocumental`**

- Constructor sin parámetros. Diccionario **privado** `{id_doc: Documento}`.
- `+=` añade un `Documento`. `len()` y `id_doc in indice`.
- Función de la clase **sin ****`self`** `similitud(v1, v2)`: similitud del coseno entre dos diccionarios de frecuencias. Si alguno está vacío, devuelve `0.0`.
- `coseno = Σ v1[t]·v2[t] / (√Σ v1[t]² · √Σ v2[t]²)`. Usa `math.sqrt`.
- Método `buscar(consulta, k=2, umbral=0.1)`: convierte la consulta a términos **con la misma limpieza que los documentos** (pista: crea un `Documento` temporal), calcula la similitud con cada documento y devuelve una lista de tuplas `(documento, puntuacion)` ordenada de mayor a menor, con como máximo `k` resultados y solo los que superen el umbral. Redondea la puntuación a 3 decimales.
**Clase ****`AsistenteRAG`**

- Constructor con `indice` e `instrucciones` (texto del mensaje de sistema).
- Método `construir_prompt(pregunta, k=2)`:
- Si la búsqueda no devuelve nada, el prompt incluye `CONTEXTO: (sin documentos relevantes)` para que el modelo responda que no lo sabe.
- Si hay resultados, un bloque `[id_doc] texto` por documento.
- Formato completo en la salida esperada.
- Método `fuentes(pregunta, k=2)`: lista de los `id_doc` usados.
**Código de prueba:**

```python
indice = IndiceDocumental()
indice += Documento("POL-01", "Teletrabajo", "El teletrabajo se permite dos días por semana previa aprobación del responsable.")
indice += Documento("POL-02", "Vacaciones", "Cada empleado dispone de 23 días laborables de vacaciones al año. Las vacaciones se solicitan en el portal.")
indice += Documento("POL-03", "Gastos de viaje", "Los gastos de viaje se reembolsan con ticket. El límite de dieta es de 45 euros por día.")
indice += Documento("POL-04", "Formación", "La empresa financia certificaciones técnicas hasta 1500 euros al año.")
print(len(indice), "POL-03" in indice, "POL-99" in indice)
print(Documento("X", "", "¿Cuántos días de vacaciones tengo al año?").terminos())

for doc, puntuacion in indice.buscar("¿Cuántos días de vacaciones tengo al año?", k=3):
    print(doc, puntuacion)

asistente = AsistenteRAG(indice, "Responde solo con el contexto. Si no está, di que no lo sabes. Cita las fuentes.")
print(asistente.construir_prompt("¿Cuál es el límite de dieta en un viaje?", k=1))
print(asistente.fuentes("¿Cuántos días de vacaciones tengo al año?"))
print(asistente.construir_prompt("¿Hay parking gratuito?"))
print(IndiceDocumental.similitud({"a": 1}, {}))
```

**Salida esperada:**

```plain text
4 True False
{'días': 1, 'vacaciones': 1, 'año': 1}
Documento(POL-02: Vacaciones) 0.641
Documento(POL-01: Teletrabajo) 0.204
Documento(POL-04: Formación) 0.204
SISTEMA: Responde solo con el contexto. Si no está, di que no lo sabes. Cita las fuentes.
CONTEXTO:
[POL-03] Los gastos de viaje se reembolsan con ticket. El límite de dieta es de 45 euros por día.
PREGUNTA: ¿Cuál es el límite de dieta en un viaje?
['POL-02', 'POL-01']
SISTEMA: Responde solo con el contexto. Si no está, di que no lo sabes. Cita las fuentes.
CONTEXTO: (sin documentos relevantes)
PREGUNTA: ¿Hay parking gratuito?
0.0
```

---

### Ejercicio A5 - Planificador de proyectos con dependencias

Una constructora digitaliza la planificación de sus obras. Cada tarea dura un número de días y no puede empezar hasta que terminen sus **dependencias**. Hay que calcular un orden de ejecución válido, el día de inicio y fin de cada tarea y la duración total del proyecto.

**Clase ****`Tarea`**

- Constructor con `codigo`, `descripcion`, `duracion` (días) y `dependencias` (lista de códigos, por defecto vacía). Atención: **no uses ****`[]`**** como valor por defecto** del parámetro; usa `None` y crea la lista dentro.
- Atributos `inicio` y `fin`, que empiezan en `None`.
- `__repr__`: `Tarea(T3, 5d)`.
**Clase ****`Proyecto`**

- Constructor con `nombre`. Diccionario **privado** `{codigo: Tarea}`.
- `+=` añade una tarea. `len()` y `codigo in proyecto`.
- Método `dependencias_rotas()`: lista ordenada de textos `"T7 → T9"` para cada dependencia que apunta a una tarea que no existe.
- Método `orden_ejecucion()`: devuelve la lista de códigos en un orden válido. Algoritmo:
1. Mientras queden tareas pendientes, busca las que tengan **todas** sus dependencias ya colocadas.
2. De ellas, coloca **la de código menor** (orden alfabético) y repite.
3. Si en una vuelta ninguna tarea está lista, hay un **ciclo**: devuelve `None`.
- Método `planificar()`: recorre el orden y asigna a cada tarea `inicio` = mayor `fin` de sus dependencias (0 si no tiene) y `fin = inicio + duracion`. Devuelve `True` si pudo planificar o `False` si hay ciclo o dependencias rotas.
- Método `duracion_total()`: el mayor `fin`.
- Método `ruta_critica()`: empezando por la tarea que termina la última, va hacia atrás eligiendo en cada paso la dependencia cuyo `fin` coincide con el `inicio` de la tarea actual (si hay varias, la de código menor). Devuelve la lista de códigos desde el principio hasta el final.
- Método `diagrama()`: una línea por tarea, en orden de ejecución, con un diagrama de Gantt en texto (ver salida).
**Código de prueba:**

```python
obra = Proyecto("Nave logística Getafe")
obra += Tarea("T1", "Licencias", 4, ["T8"])
obra += Tarea("T2", "Cimentación", 6, ["T1"])
obra += Tarea("T3", "Estructura", 8, ["T2"])
obra += Tarea("T4", "Acometida eléctrica", 3, ["T1"])
obra += Tarea("T5", "Cubierta", 5, ["T3"])
obra += Tarea("T6", "Instalaciones", 7, ["T3", "T4"])
obra += Tarea("T7", "Acabados", 4, ["T5", "T6"])
obra += Tarea("T8", "Proyecto técnico", 3)
print(len(obra), "T6" in obra, obra.dependencias_rotas())
print(obra.orden_ejecucion())
print(obra.planificar())
print(obra.diagrama())
print("Duración total:", obra.duracion_total(), "días")
print("Ruta crítica:", " → ".join(obra.ruta_critica()))

ciclo = Proyecto("Con ciclo")
ciclo += Tarea("A", "Diseño", 2, ["C"])
ciclo += Tarea("B", "Revisión", 1, ["A"])
ciclo += Tarea("C", "Aprobación", 1, ["B"])
print(ciclo.orden_ejecucion(), ciclo.planificar())

roto = Proyecto("Incompleto")
roto += Tarea("X1", "Pedido", 2, ["X0", "X9"])
print(roto.dependencias_rotas(), roto.planificar())
print(Tarea("Z1", "Prueba", 1).dependencias is Tarea("Z2", "Prueba", 1).dependencias)
```

**Salida esperada:**

```plain text
8 True []
['T8', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7']
True
T8  Proyecto técnico     |███                             | 0-3
T1  Licencias            |   ████                         | 3-7
T2  Cimentación          |       ██████                   | 7-13
T3  Estructura           |             ████████           | 13-21
T4  Acometida eléctrica  |       ███                      | 7-10
T5  Cubierta             |                     █████      | 21-26
T6  Instalaciones        |                     ███████    | 21-28
T7  Acabados             |                            ████| 28-32
Duración total: 32 días
Ruta crítica: T8 → T1 → T2 → T3 → T6 → T7
None False
['X1 → X0', 'X1 → X9'] False
False
```

---

## Sección 4 - Refactorización a programación orientada a objetos

### Ejercicio R1 - Refactorizar el gestor de pedidos de una distribuidora

Una distribuidora de bebidas para hostelería (canal **horeca**) y supermercados (canal **retail**) factura con un script escrito en 2017 por un becario que ya no está en la empresa. «Funciona», pero nadie se atreve a tocarlo: cada vez que cambia una regla de descuento hay que buscar en varios sitios y siempre se rompe algo. Te encargan **reescribirlo con programación orientada a objetos sin cambiar su comportamiento**.

**Restricción: no está permitido usar herencia ni polimorfismo.** Toda la reutilización se consigue con **composición** (objetos que contienen o usan otros objetos).

**Código heredado:**

```python
# gestion_pedidos.py · versión heredada (2017). "Funciona, no tocar".
p_cod = ["AG-01", "RF-02", "ZM-03", "CV-04", "VN-05"]
p_nom = ["Agua 1,5L pack 6", "Refresco cola pack 12", "Zumo naranja 1L", "Cerveza pack 24", "Vino tinto crianza"]
p_pre = [3.20, 9.60, 1.85, 18.90, 7.45]
p_stk = [120, 40, 60, 15, 30]
c_cod = ["CL-1", "CL-2", "CL-3"]
c_nom = ["Bar El Puerto", "Hotel Mirador", "Supermercado Sol"]
c_tip = ["horeca", "horeca", "retail"]
c_vip = [False, True, False]
peds = [
    ["CL-1", [["AG-01", 10], ["CV-04", 4], ["VN-05", 6]]],
    ["CL-2", [["RF-02", 20], ["VN-05", 12], ["XX-99", 1]]],
    ["CL-3", [["AG-01", 100], ["ZM-03", 30], ["CV-04", 10]]],
    ["CL-9", [["AG-01", 1]]],
    ["CL-1", [["CV-04", 5], ["ZM-03", 12]]],
    ["CL-2", [["CV-04", 3]]],
]
tot_emp = 0
n_ok = 0
n_ko = 0
for i in range(len(peds)):
    ped = peds[i]
    ci = -1
    for j in range(len(c_cod)):
        if c_cod[j] == ped[0]:
            ci = j
    if ci == -1:
        print("Pedido " + str(i + 1) + ": cliente " + ped[0] + " desconocido")
        n_ko = n_ko + 1
    else:
        print("Pedido " + str(i + 1) + " - " + c_nom[ci])
        sub = 0
        for l in ped[1]:
            pi = -1
            for k in range(len(p_cod)):
                if p_cod[k] == l[0]:
                    pi = k
            if pi == -1:
                print("   ! producto " + l[0] + " no existe")
            else:
                if p_stk[pi] >= l[1]:
                    p_stk[pi] = p_stk[pi] - l[1]
                    imp = p_pre[pi] * l[1]
                    sub = sub + imp
                    print("   " + p_nom[pi] + " x" + str(l[1]) + " = " + str(round(imp, 2)))
                else:
                    print("   ! sin stock de " + p_nom[pi] + " (quedan " + str(p_stk[pi]) + ")")
        d = 0
        if c_tip[ci] == "horeca":
            if sub > 100:
                d = 0.05
            if c_vip[ci] == True:
                d = d + 0.05
        else:
            if sub > 300:
                d = 0.08
            if c_vip[ci] == True:
                d = d + 0.05
        desc = sub * d
        base = sub - desc
        iva = base * 0.21
        tot = base + iva
        if sub > 0:
            print("   Subtotal: " + str(round(sub, 2)) + " | Dto: " + str(round(desc, 2)) + " | IVA: " + str(round(iva, 2)) + " | Total: " + str(round(tot, 2)))
            tot_emp = tot_emp + tot
            n_ok = n_ok + 1
        else:
            print("   Pedido vacío")
            n_ko = n_ko + 1
print("==============================")
print("Pedidos facturados: " + str(n_ok) + " | Rechazados: " + str(n_ko))
print("Facturación total: " + str(round(tot_emp, 2)))
print("Stock bajo (<20):")
for k in range(len(p_cod)):
    if p_stk[k] < 20:
        print("   " + p_cod[k] + " " + p_nom[k] + ": " + str(p_stk[k]))
```

**Salida del código heredado:**

```plain text
Pedido 1 - Bar El Puerto
   Agua 1,5L pack 6 x10 = 32.0
   Cerveza pack 24 x4 = 75.6
   Vino tinto crianza x6 = 44.7
   Subtotal: 152.3 | Dto: 7.62 | IVA: 30.38 | Total: 175.07
Pedido 2 - Hotel Mirador
   Refresco cola pack 12 x20 = 192.0
   Vino tinto crianza x12 = 89.4
   ! producto XX-99 no existe
   Subtotal: 281.4 | Dto: 28.14 | IVA: 53.18 | Total: 306.44
Pedido 3 - Supermercado Sol
   Agua 1,5L pack 6 x100 = 320.0
   Zumo naranja 1L x30 = 55.5
   Cerveza pack 24 x10 = 189.0
   Subtotal: 564.5 | Dto: 45.16 | IVA: 109.06 | Total: 628.4
Pedido 4: cliente CL-9 desconocido
Pedido 5 - Bar El Puerto
   ! sin stock de Cerveza pack 24 (quedan 1)
   Zumo naranja 1L x12 = 22.2
   Subtotal: 22.2 | Dto: 0.0 | IVA: 4.66 | Total: 26.86
Pedido 6 - Hotel Mirador
   ! sin stock de Cerveza pack 24 (quedan 1)
   Pedido vacío
==============================
Pedidos facturados: 4 | Rechazados: 2
Facturación total: 1136.78
Stock bajo (<20):
   AG-01 Agua 1,5L pack 6: 10
   ZM-03 Zumo naranja 1L: 18
   CV-04 Cerveza pack 24: 1
   VN-05 Vino tinto crianza: 12
```

**Reglas de negocio que esconde el código** (descúbrelas tú también leyéndolo):

- Canal `horeca`: 5 % de descuento si el subtotal supera 100 €. Canal `retail`: 8 % si supera 300 €.
- Los clientes VIP suman un 5 % extra de descuento, en cualquier canal.
- El IVA es del 21 % sobre la base (subtotal − descuento).
- Si no hay stock suficiente de un producto, esa línea no se sirve. Si ninguna línea se sirve, el pedido es vacío y cuenta como rechazado.
**Se pide:**

4. **Diagnóstico.** Al principio de `gestion_pedidos_oop.py`, en un comentario, enumera **al menos 6 problemas** de diseño del código heredado (por ejemplo: listas paralelas, búsquedas repetidas, números mágicos…).
5. **Diseño.** Implementa como mínimo estas clases (los nombres de los métodos los decides tú):
| Clase | Responsabilidad |
| --- | --- |
| `Producto` | Código, nombre, precio y **stock privado**. Sabe si tiene stock suficiente y descuenta unidades. |
| `Cliente` | Código, nombre, canal y si es VIP. Sabe **qué porcentaje de descuento le corresponde** para un subtotal. Las reglas por canal son un **atributo de clase**. |
| `Pedido` | Cliente, líneas servidas o con incidencia, subtotal, descuento, IVA y total. El IVA es un **atributo de clase**. `bool(pedido)` indica si tiene algo facturable y `str(pedido)` produce su bloque de texto. |
| `Distribuidora` | Catálogo de productos y clientes (diccionarios **privados** por código), procesa pedidos, acumula la facturación y genera el informe final. |
6. **Prohibido** en tu versión: listas paralelas, variables globales que se modifiquen dentro de bucles, búsquedas con `for j in range(len(...))` para encontrar un elemento y números sueltos (`0.21`, `100`, `0.05`, `20`…) fuera de atributos de clase.
7. **Test de caracterización.** La salida de tu programa debe ser **idéntica carácter a carácter** a la del código heredado. Compruébalo en PowerShell:
```powershell
python gestion_pedidos_original.py > salida_original.txt
python gestion_pedidos_oop.py > salida_oop.txt
Compare-Object (Get-Content salida_original.txt) (Get-Content salida_oop.txt)
```

Si `Compare-Object` no muestra nada, las dos salidas son iguales.
8. **Prueba de extensibilidad.** Cuando termines, responde en un comentario: si mañana se crea el canal `online` (3 % de descuento a partir de 50 €), ¿cuántas líneas tienes que cambiar en tu versión? ¿Y en la original?
---

## Sección 5 - Juego interactivo

> 💡 Puedes hacer tu propio juego si quieres. No tiene que ser obligatoriamente el ejercicio J1

### Ejercicio J1  - Juego interactivo: Hundir la flota

Vas a programar una versión de un jugador de **Hundir la flota** que se juega en la terminal. El ordenador esconde una flota en un tablero de 6 × 6 y el jugador dispara escribiendo coordenadas como `B4` hasta hundir todos los barcos o quedarse sin munición.

**Restricción: no está permitido usar herencia ni polimorfismo.** El diseño se basa en clases independientes que colaboran por **composición**.

**Reglas del juego**

- Tablero de 6 × 6. Columnas `AF` y filas `16`.
- Flota (atributo de clase de `Partida`): `Destructor` (3 casillas), `Fragata` (2) y `Lancha` (2). Se colocan al azar, en horizontal o vertical, sin salirse del tablero y sin solaparse.
- El jugador tiene **20 disparos**.
- Resultados de un disparo: `Agua.`, `¡Tocado!` o `¡Hundido! Barco hundido: <nombre>.`
- Disparar a una casilla ya disparada **no gasta munición**. Una coordenada mal escrita tampoco.
- Comandos especiales: `mapa` (dibuja el tablero sin mostrar los barcos), `flota` (estado de cada barco) y `salir`.
- La partida termina al hundir toda la flota (victoria), al agotar la munición o al escribir `salir`. Al terminar se muestra un resumen con las estadísticas y el tablero con los barcos al descubierto.
- Símbolos del tablero: `·` desconocido, `~` agua, `X` tocado, `#` barco hundido, `B` barco (solo en el resumen final).
**Diseño obligatorio**

| Clase | Responsabilidad | Detalles mínimos |
| --- | --- | --- |
| `Barco` | Un barco de la flota | Nombre, tamaño, lista de posiciones `(fila, columna)` y un `set` **privado** de impactos. `ocupa(pos)`, `recibir_impacto(pos)`, `hundido()`, `len(barco)` y `__str__` (`"Fragata (2) · 1/2 impactos"` o `"Fragata (2) · hundido"`). |
| `Tablero` | La cuadrícula y los barcos | Tamaño, lista de barcos y diccionario **privado** de disparos. Los símbolos son **atributos de clase**. Coloca barcos al azar, procesa un disparo, sabe si toda la flota está hundida y se dibuja como texto. |
| `Jugador` | Estadísticas del jugador | Nombre, munición, disparos y aciertos. `precision()`, `bool(jugador)` (`True` si le queda munición) y `__str__`. |
| `Partida` | Coordina el juego | **Tiene** un `Tablero` y un `Jugador`. Convierte el texto `B4` en `(fila, columna)` con un método de uso interno, procesa un turno, sabe si la partida ha terminado y contiene el bucle con `input()`. |

**Requisitos técnicos**

9. El constructor de `Partida` recibe un parámetro opcional `semilla`. Crea con él un **objeto** generador de números aleatorios: `random.Random(semilla)`. Con la misma semilla los barcos quedan siempre en el mismo sitio, lo que permite probar el juego.
10. Separa la lógica de la interacción: el método `turno(texto)` recibe una coordenada y **devuelve** el mensaje (no hace `print` ni `input`). Solo `jugar()` usa `input()` y `print()`.
11. Al final del archivo, protege el arranque con `if __name__ == "__main__":`, pidiendo el nombre del jugador y creando la partida con `semilla=7`.
12. Añade un bloque de **pruebas sin teclado** (por ejemplo, en una función `probar()`) que cree una partida con `semilla=7` y `municion=3`, llame tres veces a `turno()` y compruebe que la partida termina.
**Ejemplo de partida** (con `semilla=7`; tu tablero puede ser diferente si colocas los barcos con otro algoritmo, pero el formato debe ser este):

```plain text
Nombre del jugador: Ana
HUNDIR LA FLOTA · tablero 6x6 · 3 barcos · 20 disparos
Comandos: coordenada (B4), 'mapa', 'flota', 'salir'
[20] Disparo: A1
Agua.
[19] Disparo: D2
¡Tocado!
[18] Disparo: D3
¡Tocado!
[17] Disparo: d4
¡Hundido! Barco hundido: Destructor.
[16] Disparo: D4
Ya habías disparado ahí. No gastas munición.
[16] Disparo: Z9
Coordenada no válida: 'Z9'. Usa letra + número, por ejemplo B4.
[16] Disparo: mapa
    A B C D E F
 1  ~ · · · · ·
 2  · · · # · ·
 3  · · · # · ·
 4  · · · # · ·
 5  · · · · · ·
 6  · · · · · ·
[16] Disparo: E3
¡Tocado!
[15] Disparo: F3
¡Hundido! Barco hundido: Lancha.
[14] Disparo: flota
  - Destructor hundido
  - Fragata a flote
  - Lancha hundido
[14] Disparo: E1
¡Tocado!
[13] Disparo: F1
¡Hundido! Barco hundido: Fragata.

=== FIN DE LA PARTIDA ===
¡Victoria, Ana! Flota enemiga hundida.
Ana · disparos: 8 · aciertos: 7 · precisión: 87.5 % · munición: 12
  - Destructor (3) · hundido
  - Fragata (2) · hundido
  - Lancha (2) · hundido
    A B C D E F
 1  ~ · · · # #
 2  · · · # · ·
 3  · · · # # #
 4  · · · # · ·
 5  · · · · · ·
 6  · · · · · ·
```

**Ampliaciones interesantes**:

- Impedir que dos barcos queden en casillas contiguas.
- Elegir el tamaño del tablero y la dificultad (munición) al empezar.
- Guardar un ranking de partidas en una lista de objetos `Jugador` ordenada por precisión (sobrecarga `<`).
- Modo «radar»: una vez por partida, el comando `radar B4` indica cuántas casillas con barco hay en el cuadrado 3 × 3 alrededor de la coordenada.

