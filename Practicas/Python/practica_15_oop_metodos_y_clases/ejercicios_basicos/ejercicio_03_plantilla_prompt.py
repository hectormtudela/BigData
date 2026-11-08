"""
Práctica 15 · Ejercicio B3 - Plantilla de prompt reutilizable · IA Generativa
Nivel: básico
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio B3 - Plantilla de prompt reutilizable · IA Generativa
#
# El equipo de atención al cliente de una cadena de electrónica usa un LLM para clasificar reseñas. Cada analista escribe el prompt a mano y los resultados son inconsistentes. Crea la clase `PlantillaPrompt` para que todos usen la misma estructura:
#
# - Constructor con `rol`, `tarea` y `formato_salida` (por defecto `"texto libre"`). Crea también la lista `restricciones`, vacía.
# - Método `agregar_restriccion(texto)`: añade una restricción a la lista.
# - Método `construir(entrada)`: devuelve **un único texto** con varias líneas, en este orden:
# 1. `Actúa como <rol>.`
# 2. `Tarea: <tarea>`
# 3. Si hay restricciones, la línea `Restricciones:` y una línea `<restricción>` por cada una.
# 4. `Formato de salida: <formato_salida>`
# 5. `Entrada: """<entrada>"""`
# - `__repr__` con el formato `PlantillaPrompt(rol='analista de experiencia de cliente', restricciones=2)`.
# Pista: construye una lista de líneas y únelas con `"\n".join(lineas)`.
#
# **Código de prueba:**
#
# ```python
# clasificador = PlantillaPrompt(
#     "analista de experiencia de cliente",
#     "clasifica el sentimiento de la reseña como POSITIVO, NEUTRO o NEGATIVO",
#     "JSON con las claves sentimiento y motivo",
# )
# clasificador.agregar_restriccion("No inventes información que no aparezca en la reseña")
# clasificador.agregar_restriccion("El motivo debe tener como máximo 15 palabras")
# print(repr(clasificador))
# print(clasificador.construir("El portátil llegó en 24 h pero la batería dura la mitad de lo anunciado."))
# print("---")
# resumen = PlantillaPrompt("redactor técnico", "resume la incidencia en una frase")
# print(resumen.construir("El TPV de la tienda 14 no imprime tickets desde las 10:00."))
# ```
#
# **Salida esperada:**
#
# ```plain text
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
# ```

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
