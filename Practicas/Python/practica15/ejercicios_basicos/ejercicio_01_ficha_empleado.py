# Ejercicio B1 - Ficha de empleado del equipo de datos
#
# El departamento de RR. HH. quiere dejar de gestionar las fichas de empleados con diccionarios sueltos. Crea la clase `Empleado`:
#
# - Constructor con `nombre`, `departamento` y `salario_bruto` (anual, en euros). Además crea el atributo `proyectos`, que empieza siendo una **lista vacía**.
# - Método `asignar_proyecto(proyecto)`: añade el proyecto a la lista **solo si no estaba ya asignado**.
# - Método `salario_neto_mensual(retencion=0.15)`: aplica la retención al salario bruto, lo reparte en **14 pagas** y lo devuelve redondeado a 2 decimales.
# - `__str__` con el formato `"Lucía Ortega (Data Platform) · 2 proyectos"`.

# Solución:

class Empleado:
    """Ficha de un empleado del equipo de datos."""

    def __init__(self, nombre, departamento, salario_bruto):
        self.nombre = nombre
        self.departamento = departamento
        self.salario_bruto = salario_bruto
        self.proyectos = [] 

    def asignar_proyecto(self, proyecto):
        """Añade el proyecto solo si no estaba ya asignado."""
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)

    def salario_neto_mensual(self, retencion=0.15):
        """Bruto anual - retención, repartido en 14 pagas, con 2 decimales."""
        neto_anual = self.salario_bruto * (1 - retencion)
        return round(neto_anual / 14, 2)

    def __str__(self):
        return f"{self.nombre} ({self.departamento}) · {len(self.proyectos)} proyectos"



# Código de prueba del enunciado
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
