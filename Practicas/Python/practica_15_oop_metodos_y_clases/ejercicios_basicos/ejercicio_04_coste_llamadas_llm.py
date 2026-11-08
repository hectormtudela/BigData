"""
Práctica 15 · Ejercicio B4 - Coste de las llamadas a un LLM · IA Generativa
Nivel: básico
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio B4 - Coste de las llamadas a un LLM · IA Generativa
#
# Finanzas quiere saber cuánto cuesta cada llamada al proveedor de modelos de lenguaje. El proveedor cobra en dólares **por cada millón de tokens**, con un precio distinto para los tokens de entrada y los de salida. Crea la clase `LlamadaLLM`:
#
# - Atributo de clase `PRECIOS`, un diccionario `{modelo: (precio_entrada, precio_salida)}`:
# | Modelo | Entrada (/M tokens) | Salida (/M tokens) |  |
# | --- | --- | --- |
# | `modelo-lite` | 0.20 | 0.80 |
# | `modelo-pro` | 3.00 | 12.00 |
#
# - Atributo de clase `total_llamadas = 0`, que se incrementa cada vez que se crea una llamada.
# - Constructor con `modelo`, `tokens_entrada` y `tokens_salida`.
# - Método `coste()`: devuelve el coste en dólares redondeado a **6 decimales**.
# - Método `tokens_totales()`.
# - `__repr__` con el formato `LlamadaLLM(modelo-lite, 1500 tokens, $0.00048)`.
# **Código de prueba:**
#
# ```python
# llamadas = [
#     LlamadaLLM("modelo-lite", 1200, 300),
#     LlamadaLLM("modelo-pro", 1200, 300),
#     LlamadaLLM("modelo-lite", 8000, 1500),
#     LlamadaLLM("modelo-pro", 25000, 4000),
# ]
# for llamada in llamadas:
#     print(llamada)
# print("Llamadas registradas:", LlamadaLLM.total_llamadas)
# print(f"Coste total: ${round(sum([l.coste() for l in llamadas]), 6)}")
# coste_pro = sum([l.coste() for l in llamadas if l.modelo == "modelo-pro"])
# print("Peso de modelo-pro:", round(100 * coste_pro / sum([l.coste() for l in llamadas]), 1), "%")
# ```
#
# **Salida esperada:**
#
# ```plain text
# LlamadaLLM(modelo-lite, 1500 tokens, $0.00048)
# LlamadaLLM(modelo-pro, 1500 tokens, $0.0072)
# LlamadaLLM(modelo-lite, 9500 tokens, $0.0028)
# LlamadaLLM(modelo-pro, 29000 tokens, $0.123)
# Llamadas registradas: 4
# Coste total: $0.13348
# Peso de modelo-pro: 97.5 %
# ```

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
