"""
Práctica 15 · Ejercicio B1 - Ficha de empleado del equipo de datos
Nivel: básico
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio B1 - Ficha de empleado del equipo de datos
#
# El departamento de RR. HH. quiere dejar de gestionar las fichas de empleados con diccionarios sueltos. Crea la clase `Empleado`:
#
# - Constructor con `nombre`, `departamento` y `salario_bruto` (anual, en euros). Además crea el atributo `proyectos`, que empieza siendo una **lista vacía**.
# - Método `asignar_proyecto(proyecto)`: añade el proyecto a la lista **solo si no estaba ya asignado**.
# - Método `salario_neto_mensual(retencion=0.15)`: aplica la retención al salario bruto, lo reparte en **14 pagas** y lo devuelve redondeado a 2 decimales.
# - `__str__` con el formato `"Lucía Ortega (Data Platform) · 2 proyectos"`.
# **Código de prueba:**
#
# ```python
# lucia = Empleado("Lucía Ortega", "Data Platform", 42000)
# mario = Empleado("Mario Gil", "BI", 35000)
# lucia.asignar_proyecto("Migración a Lakehouse")
# lucia.asignar_proyecto("Catálogo de datos")
# lucia.asignar_proyecto("Migración a Lakehouse")
# print(lucia)
# print(mario)
# print(lucia.proyectos)
# print(lucia.salario_neto_mensual())
# print(lucia.salario_neto_mensual(0.20))
# print(mario.salario_neto_mensual())
# ```
#
# **Salida esperada:**
#
# ```plain text
# Lucía Ortega (Data Platform) · 2 proyectos
# Mario Gil (BI) · 0 proyectos
# ['Migración a Lakehouse', 'Catálogo de datos']
# 2550.0
# 2400.0
# 2125.0
# ```

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
