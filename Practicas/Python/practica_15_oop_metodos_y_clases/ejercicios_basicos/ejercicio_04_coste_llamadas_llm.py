"""
Práctica 15 · Ejercicio B4 - Coste de las llamadas a un LLM · IA Generativa
Nivel: básico

Enunciado completo: ../practica_15_oop_metodos_y_clases.md
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
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

# ===== Salida esperada =====
# LlamadaLLM(modelo-lite, 1500 tokens, $0.00048)
# LlamadaLLM(modelo-pro, 1500 tokens, $0.0072)
# LlamadaLLM(modelo-lite, 9500 tokens, $0.0028)
# LlamadaLLM(modelo-pro, 29000 tokens, $0.123)
# Llamadas registradas: 4
# Coste total: $0.13348
# Peso de modelo-pro: 97.5 %
