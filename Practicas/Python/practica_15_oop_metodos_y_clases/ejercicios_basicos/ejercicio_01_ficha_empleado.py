"""
Práctica 15 · Ejercicio B1 - Ficha de empleado del equipo de datos
Nivel: básico

Enunciado completo: ../practica_15_oop_metodos_y_clases.md
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
lucia = Empleado("Lucía Ortega", "Data Platform", 42000)
mario = Empleado("Mario Gil", "BI", 35000)
lucia.asignar_proyecto("Migración a Lakehouse")
lucia.asignar_proyecto("Catálogo de datos")
lucia.asignar_proyecto("Migración a Lakehouse")
print(lucia)
print(mario)
print(lucia.proyectos)
print(lucia.salario_neto_mensual())
print(lucia.salario_neto_mensual(0.20))
print(mario.salario_neto_mensual())

# ===== Salida esperada =====
# Lucía Ortega (Data Platform) · 2 proyectos
# Mario Gil (BI) · 0 proyectos
# ['Migración a Lakehouse', 'Catálogo de datos']
# 2550.0
# 2400.0
# 2125.0
