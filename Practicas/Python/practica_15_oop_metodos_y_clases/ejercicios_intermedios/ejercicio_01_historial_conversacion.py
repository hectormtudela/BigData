"""
Práctica 15 · Ejercicio I1 - Historial de conversación de un asistente · IA Generativa
Nivel: intermedio

Enunciado completo: ../practica_15_oop_metodos_y_clases.md
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

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

# ===== Salida esperada =====
# False
# 3 22
# 3 26
# [system] Eres el asistente de siniestros de Seguros Brisamar
# [assistant] Claro, ¿cuál es la matrícula del vehículo?
# [user] Es la 4821 KLM y el golpe fue en un parking
# True False
# {'role': 'system', 'content': 'Eres el asistente de siniestros de Seguros Brisamar'}
