r"""
Práctica 16 · Clase 20 · Ejercicio P1 (Empleados)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

# Ejercicio P1. Sistema de gestión de empleados

### Enunciado

> Una empresa tecnológica necesita desarrollar un programa para gestionar la información de sus empleados. Actualmente cuenta con tres tipos de trabajadores: desarrolladores, analistas de datos y administradores de sistemas.

Debes desarrollar una estructura de clases basada en herencia que permita representar a los distintos trabajadores sin repetir atributos ni métodos comunes.

### Requisitos

1. Crear una superclase `Empleado` con los atributos `id_empleado`, `nombre`, `salario_base` y `departamento`.
2. Implementar un método `mostrar_informacion()` que muestre los datos del empleado.
3. Crear tres subclases:
- `Desarrollador`: añadir los atributos `lenguaje_principal` y `nivel`.
- `AnalistaDatos`: añadir los atributos `herramienta_bi` y `especialidad`.
- `AdministradorSistemas`: añadir los atributos `sistema_operativo` y `certificacion`.
4. Sobrescribir `mostrar_informacion()` en las tres subclases para incluir sus atributos específicos.
5. Crear al menos dos objetos de cada subclase.
6. Almacenar los seis objetos en una única lista llamada `empleados`.
7. Recorrer la lista e imprimir la información de todos los empleados.
"""

class Empleado:
    """Superclase: atributos y comportamiento común a todos los empleados."""

    def __init__(self, id_empleado, nombre, salario_base, departamento):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.salario_base = salario_base
        self.departamento = departamento

    def mostrar_informacion(self):
        print(f"ID: {self.id_empleado}")
        print(f"Nombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Salario base: {self.salario_base} €")


class Desarrollador(Empleado):
    def __init__(self, id_empleado, nombre, salario_base, departamento,
                 lenguaje_principal, nivel):
        super().__init__(id_empleado, nombre, salario_base, departamento)
        self.lenguaje_principal = lenguaje_principal
        self.nivel = nivel

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje principal: {self.lenguaje_principal}")
        print(f"Nivel: {self.nivel}")


class AnalistaDatos(Empleado):
    def __init__(self, id_empleado, nombre, salario_base, departamento,
                 herramienta_bi, especialidad):
        super().__init__(id_empleado, nombre, salario_base, departamento)
        self.herramienta_bi = herramienta_bi
        self.especialidad = especialidad

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Herramienta BI: {self.herramienta_bi}")
        print(f"Especialidad: {self.especialidad}")


class AdministradorSistemas(Empleado):
    def __init__(self, id_empleado, nombre, salario_base, departamento,
                 sistema_operativo, certificacion):
        super().__init__(id_empleado, nombre, salario_base, departamento)
        self.sistema_operativo = sistema_operativo
        self.certificacion = certificacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Sistema operativo: {self.sistema_operativo}")
        print(f"Certificación: {self.certificacion}")


def main():
    empleados = [
        Desarrollador("E001", "Ana López", 2800, "Desarrollo",
                      "Python", "Senior"),
        AnalistaDatos("E002", "Carlos Pérez", 2600, "Datos",
                      "Power BI", "Análisis de ventas"),
        AdministradorSistemas("E003", "Laura Gómez", 2900, "Infraestructura",
                              "Linux", "AZ-104"),
        Desarrollador("E004", "Javier Ruiz", 2400, "Desarrollo",
                      "JavaScript", "Junior"),
        AnalistaDatos("E005", "Marta Sanz", 2700, "Datos",
                      "Tableau", "Machine Learning"),
        AdministradorSistemas("E006", "Pablo Díaz", 3000, "Infraestructura",
                              "Windows Server", "AZ-800"),
    ]

    for empleado in empleados:
        empleado.mostrar_informacion()
        print()


if __name__ == "__main__":
    main()
