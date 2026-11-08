"""
Práctica 15 · Ejercicio B7 - Valoraciones de clientes desde una encuesta
Nivel: básico

Enunciado completo: ../practica_15_oop_metodos_y_clases.md
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
respuestas = ["4,5/5", "3/5", "0/5", "2,4/5", "5/5", "0/5"]
valoraciones = [Valoracion(r) for r in respuestas]
for v in valoraciones:
    print(str(v), float(v), int(v), bool(v))
validas = [v for v in valoraciones if v]
print("Respuestas válidas:", len(validas), "de", len(valoraciones))
print("Media:", round(sum([float(v) for v in validas]) / len(validas), 2))

# ===== Salida esperada =====
# ★★★★☆ (4.5) 4.5 4 True
# ★★★☆☆ (3.0) 3.0 3 True
# ☆☆☆☆☆ (0.0) 0.0 0 False
# ★★☆☆☆ (2.4) 2.4 2 True
# ★★★★★ (5.0) 5.0 5 True
# ☆☆☆☆☆ (0.0) 0.0 0 False
# Respuestas válidas: 4 de 6
# Media: 3.73
