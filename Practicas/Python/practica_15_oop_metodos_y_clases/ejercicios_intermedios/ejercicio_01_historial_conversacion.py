"""
Práctica 15 · Ejercicio I1 - Historial de conversación de un asistente · IA Generativa
Nivel: intermedio
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio I1 - Historial de conversación de un asistente · IA Generativa
#
# Una aseguradora está construyendo un asistente para tramitar partes de siniestros. Las API de los LLM reciben el historial como una lista de diccionarios `{"role": ..., "content": ...}` y tienen una **ventana de contexto** limitada. Modela el historial con **dos clases relacionadas por composición**.
#
# **Clase ****`Mensaje`**
#
# - Atributo de clase `ROLES_VALIDOS = ("system", "user", "assistant")`.
# - Constructor con `rol` y `contenido`.
# - Método `tokens()`: estimación sencilla, **1 token por palabra** (`len(contenido.split())`).
# - Método `a_dict()`: devuelve `{"role": rol, "content": contenido}`.
# - `__str__`: `"[user] Quiero dar un parte de mi coche"`.
# **Clase ****`Conversacion`**
#
# - Constructor con `max_tokens`. Guarda los mensajes en una lista **privada** `__mensajes`.
# - Método `agregar(rol, contenido)`: si el rol no está en `Mensaje.ROLES_VALIDOS`, no añade nada y devuelve `False`. Si es válido, crea el `Mensaje`, lo añade, llama a `_recortar()` y devuelve `True`.
# - `+=` recibe una **tupla** `(rol, contenido)` y usa `agregar`.
# - Método `tokens_totales()`.
# - Método de uso interno `_recortar()`: mientras los tokens totales superen `max_tokens`, elimina el **mensaje más antiguo que no sea ****`system`** (el mensaje de sistema nunca se borra).
# - `len(conv)`: número de mensajes. `palabra in conv`: `True` si la palabra aparece en algún mensaje, sin distinguir mayúsculas.
# - Método `para_api()`: lista de diccionarios de todos los mensajes.
# - `__str__`: un mensaje por línea.
# **Código de prueba:**
#
# ```python
# conv = Conversacion(max_tokens=30)
# conv += ("system", "Eres el asistente de siniestros de Seguros Brisamar")
# conv += ("user", "Quiero dar un parte de mi coche")
# conv += ("assistant", "Claro, ¿cuál es la matrícula del vehículo?")
# print(conv.agregar("cliente", "Hola"))
# print(len(conv), conv.tokens_totales())
# conv += ("user", "Es la 4821 KLM y el golpe fue en un parking")
# print(len(conv), conv.tokens_totales())
# print(conv)
# print("matrícula" in conv, "COCHE" in conv)
# print(conv.para_api()[0])
# ```
#
# **Salida esperada:**
#
# ```plain text
# False
# 3 22
# 3 26
# [system] Eres el asistente de siniestros de Seguros Brisamar
# [assistant] Claro, ¿cuál es la matrícula del vehículo?
# [user] Es la 4821 KLM y el golpe fue en un parking
# True False
# {'role': 'system', 'content': 'Eres el asistente de siniestros de Seguros Brisamar'}
# ```

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
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
