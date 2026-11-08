"""
Práctica 15 · Ejercicio B5 - Climatización de un centro de datos
Nivel: básico
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio B5 - Climatización de un centro de datos
#
# La consigna de temperatura de cada sala del CPD solo puede estar entre **18 y 27 °C**. Nadie debe poder cambiarla «a mano» desde fuera del objeto. Crea la clase `Climatizador` aplicando las convenciones de nombres:
#
# - Atributos de clase `TEMP_MIN = 18` y `TEMP_MAX = 27`.
# - Constructor con `sala` (público) y `consigna` inicial. La consigna se guarda en el atributo **privado** `__consigna`, ya limitada al rango permitido. Crea también el atributo de **uso interno** `_historial`, una lista con la consigna inicial.
# - Método **de uso interno** `_limitar(valor)`: devuelve el valor ajustado al rango (si es menor que el mínimo, el mínimo; si es mayor que el máximo, el máximo).
# - Método `ajustar(grados)`: suma (o resta, si es negativo) los grados a la consigna, la limita con `_limitar`, la añade al historial y devuelve la nueva consigna.
# - Método `consigna()`: devuelve el valor actual.
# - `__str__`: `"Sala A · 22 °C · 3 cambios"` (los cambios son las entradas del historial menos la inicial).
# Responde en un comentario al final del archivo: ¿por qué `hasattr(sala_a, "__consigna")` devuelve `False` si el atributo existe?
#
# **Código de prueba:**
#
# ```python
# sala_a = Climatizador("A", 22)
# sala_b = Climatizador("B", 31)
# print(sala_a.ajustar(-3), sala_a.ajustar(-4), sala_a.ajustar(6))
# print(sala_a)
# print(sala_b)
# print(sala_a._historial)
# print(vars(sala_b))
# print(hasattr(sala_a, "__consigna"), hasattr(sala_a, "_Climatizador__consigna"))
# ```
#
# **Salida esperada:**
#
# ```plain text
# 19 18 24
# Sala A · 24 °C · 3 cambios
# Sala B · 27 °C · 0 cambios
# [22, 19, 18, 24]
# {'sala': 'B', '_Climatizador__consigna': 27, '_historial': [27]}
# False True
# ```

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
sala_a = Climatizador("A", 22)
sala_b = Climatizador("B", 31)
print(sala_a.ajustar(-3), sala_a.ajustar(-4), sala_a.ajustar(6))
print(sala_a)
print(sala_b)
print(sala_a._historial)
print(vars(sala_b))
print(hasattr(sala_a, "__consigna"), hasattr(sala_a, "_Climatizador__consigna"))

# ===== RESPUESTA (comentario al final del archivo) =====
# ¿Por qué hasattr(sala_a, "__consigna") devuelve False si el atributo existe?
# 
