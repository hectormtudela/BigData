"""
Práctica 15 · Ejercicio B3 - Plantilla de prompt reutilizable · IA Generativa
Nivel: básico

Enunciado completo: ../practica_15_oop_metodos_y_clases.md
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
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

# ===== Salida esperada =====
# PlantillaPrompt(rol='analista de experiencia de cliente', restricciones=2)
# Actúa como analista de experiencia de cliente.
# Tarea: clasifica el sentimiento de la reseña como POSITIVO, NEUTRO o NEGATIVO
# Restricciones:
# - No inventes información que no aparezca en la reseña
# - El motivo debe tener como máximo 15 palabras
# Formato de salida: JSON con las claves sentimiento y motivo
# Entrada: """El portátil llegó en 24 h pero la batería dura la mitad de lo anunciado."""
# ---
# Actúa como redactor técnico.
# Tarea: resume la incidencia en una frase
# Formato de salida: texto libre
# Entrada: """El TPV de la tienda 14 no imprime tickets desde las 10:00."""
