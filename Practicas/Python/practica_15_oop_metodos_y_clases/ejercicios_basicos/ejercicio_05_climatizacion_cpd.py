"""
Práctica 15 · Ejercicio B5 - Climatización de un centro de datos
Nivel: básico

Enunciado completo: ../practica_15_oop_metodos_y_clases.md
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

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

# ===== Salida esperada =====
# 19 18 24
# Sala A · 24 °C · 3 cambios
# Sala B · 27 °C · 0 cambios
# [22, 19, 18, 24]
# {'sala': 'B', '_Climatizador__consigna': 27, '_historial': [27]}
# False True
