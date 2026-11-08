"""
Práctica 15 · Ejercicio B7 - Valoraciones de clientes desde una encuesta
Nivel: básico
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio B7 - Valoraciones de clientes desde una encuesta
#
# La herramienta de encuestas exporta las valoraciones como texto: `"4,5/5"`, `"3/5"`, `"0/5"` (el `0` significa *sin valorar*). Crea la clase `Valoracion`:
#
# - El constructor recibe el texto, toma la parte anterior a la `/`, cambia la coma por punto y guarda el valor como `float` en el atributo **privado** `__nota`.
# - `float(v)`: devuelve la nota.
# - `int(v)`: devuelve la nota **redondeada** a entero.
# - `bool(v)`: `False` si la nota es 0 (sin valorar).
# - `str(v)`: tantas `★` como `int(v)` y tantas `☆` como falten hasta 5, seguido de la nota entre paréntesis: `"★★★★☆ (4.5)"`.
# **Código de prueba:**
#
# ```python
# respuestas = ["4,5/5", "3/5", "0/5", "2,4/5", "5/5", "0/5"]
# valoraciones = [Valoracion(r) for r in respuestas]
# for v in valoraciones:
#     print(str(v), float(v), int(v), bool(v))
# validas = [v for v in valoraciones if v]
# print("Respuestas válidas:", len(validas), "de", len(valoraciones))
# print("Media:", round(sum([float(v) for v in validas]) / len(validas), 2))
# ```
#
# **Salida esperada:**
#
# ```plain text
# ★★★★☆ (4.5) 4.5 4 True
# ★★★☆☆ (3.0) 3.0 3 True
# ☆☆☆☆☆ (0.0) 0.0 0 False
# ★★☆☆☆ (2.4) 2.4 2 True
# ★★★★★ (5.0) 5.0 5 True
# ☆☆☆☆☆ (0.0) 0.0 0 False
# Respuestas válidas: 4 de 6
# Media: 3.73
# ```

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
respuestas = ["4,5/5", "3/5", "0/5", "2,4/5", "5/5", "0/5"]
valoraciones = [Valoracion(r) for r in respuestas]
for v in valoraciones:
    print(str(v), float(v), int(v), bool(v))
validas = [v for v in valoraciones if v]
print("Respuestas válidas:", len(validas), "de", len(valoraciones))
print("Media:", round(sum([float(v) for v in validas]) / len(validas), 2))
