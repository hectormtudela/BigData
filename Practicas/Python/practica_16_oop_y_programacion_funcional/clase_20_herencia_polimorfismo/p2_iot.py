r"""
Práctica 16 · Clase 20 · Ejercicio P2 (Refactorización IoT)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

# Ejercicio P2. Refactorización de un sistema de dispositivos IoT

### Enunciado

> Una empresa especializada en soluciones de *Smart Agriculture* ha desarrollado un programa para gestionar los dispositivos IoT instalados en diferentes explotaciones agrícolas.
El programa funciona, pero presenta un problema de diseño: **todos los tipos de sensores se representan mediante una única clase**, que contiene atributos que no corresponden a todos los dispositivos.

Tu tarea consiste en **refactorizar el código utilizando herencia**, creando una superclase y cuatro clases hijas.

### Código original que debes refactorizar

```python
class DispositivoIoT:
    def __init__(
        self,
        device_id,
        nombre,
        ubicacion,
        tipo,
        valor,
        unidad,
        profundidad=None,
        calibracion=None,
        altitud=None,
        precision=None,
        orientacion=None,
        velocidad_maxima=None,
        capacidad=None,
        nivel_bateria=None
    ):
        self.device_id = device_id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tipo = tipo
        self.valor = valor
        self.unidad = unidad

        self.profundidad = profundidad
        self.calibracion = calibracion
        self.altitud = altitud
        self.precision = precision
        self.orientacion = orientacion
        self.velocidad_maxima = velocidad_maxima
        self.capacidad = capacidad
        self.nivel_bateria = nivel_bateria

    def mostrar_informacion(self):
        print("ID:", self.device_id)
        print("Nombre:", self.nombre)
        print("Ubicación:", self.ubicacion)
        print("Tipo:", self.tipo)
        print("Valor:", self.valor, self.unidad)

        if self.tipo == "HUMEDAD":
            print("Profundidad:", self.profundidad)
            print("Calibración:", self.calibracion)

        elif self.tipo == "TEMPERATURA":
            print("Altitud:", self.altitud)
            print("Precisión:", self.precision)

        elif self.tipo == "VIENTO":
            print("Orientación:", self.orientacion)
            print("Velocidad máxima:", self.velocidad_maxima)

        elif self.tipo == "TANQUE":
            print("Capacidad:", self.capacidad)
            print("Nivel de batería:", self.nivel_bateria)


sensor1 = DispositivoIoT(
    "DEV001", "Sensor de suelo", "Parcela A",
    "HUMEDAD", 45, "%",
    profundidad=30, calibracion="Automática"
)

sensor2 = DispositivoIoT(
    "DEV002", "Sensor ambiental", "Parcela B",
    "TEMPERATURA", 26, "°C",
    altitud=650, precision=0.5
)

sensor3 = DispositivoIoT(
    "DEV003", "Anemómetro", "Parcela C",
    "VIENTO", 18, "km/h",
    orientacion="Norte", velocidad_maxima=80
)

sensor4 = DispositivoIoT(
    "DEV004", "Tanque principal", "Parcela A",
    "TANQUE", 75, "%",
    capacidad=5000, nivel_bateria=90
)

dispositivos = [sensor1, sensor2, sensor3, sensor4]

for dispositivo in dispositivos:
    dispositivo.mostrar_informacion()
    print("-" * 40)
```

### Requisitos de refactorización

Debes transformar el programa original en una estructura de cinco clases:

![Imagen](images/practica-16-oop-y-programacion-funcional/image-001.png)

La clase `DispositivoIoT` debe contener únicamente los atributos compartidos por todos los dispositivos: `device_id`, `nombre`, `ubicacion`, `valor` y `unidad`.

También debe implementar el método `mostrar_informacion()`.

Cada subclase debe añadir exclusivamente los atributos que necesita:

| Subclase | Atributos adicionales |
| --- | --- |
| `SensorHumedad` | `profundidad`, `calibracion` |
| `SensorTemperatura` | `altitud`, `precision` |
| `SensorViento` | `orientacion`, `velocidad_maxima` |
| `SensorTanque` | `capacidad`, `nivel_bateria` |

Cada subclase debe sobrescribir el método `mostrar_informacion()` para mostrar los atributos comunes y los específicos de su dispositivo.

8. Crear al menos dos objetos de cada subclase, obteniendo un total de ocho dispositivos.
9. Almacenar todos los objetos en una única lista llamada `dispositivos`.
10. Recorrer la lista y ejecutar `mostrar_informacion()` para cada dispositivo.
11. Utilizar `isinstance()` para identificar el tipo de dispositivo y mostrar un mensaje personalizado.
12. Comprobar que los objetos no contienen atributos innecesarios utilizando `vars()`.
### Salida esperada (orientativa)

```plain text
ID: DEV001
Nombre: Sensor de suelo
Ubicación: Parcela A
Valor: 45 %
Profundidad: 30 cm
Calibración: Automática
Categoría: Sensor de humedad
----------------------------------------

ID: DEV002
Nombre: Sensor ambiental
Ubicación: Parcela B
Valor: 26 °C
Altitud: 650 m
Precisión: 0.5 °C
Categoría: Sensor de temperatura
----------------------------------------
```

**Resultado esperado:** El nuevo programa debe conservar la funcionalidad original, eliminar los atributos innecesarios y aprovechar la herencia para reducir la duplicación de código.
"""

class DispositivoIoT:
    """Superclase: SOLO los atributos compartidos por todos los dispositivos."""

    def __init__(self, device_id, nombre, ubicacion, valor, unidad):
        self.device_id = device_id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.valor = valor
        self.unidad = unidad

    def mostrar_informacion(self):
        print(f"ID: {self.device_id}")
        print(f"Nombre: {self.nombre}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Valor: {self.valor} {self.unidad}")


class SensorHumedad(DispositivoIoT):
    def __init__(self, device_id, nombre, ubicacion, valor, unidad,
                 profundidad, calibracion):
        super().__init__(device_id, nombre, ubicacion, valor, unidad)
        self.profundidad = profundidad
        self.calibracion = calibracion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Profundidad: {self.profundidad} cm")
        print(f"Calibración: {self.calibracion}")


class SensorTemperatura(DispositivoIoT):
    def __init__(self, device_id, nombre, ubicacion, valor, unidad,
                 altitud, precision):
        super().__init__(device_id, nombre, ubicacion, valor, unidad)
        self.altitud = altitud
        self.precision = precision

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Altitud: {self.altitud} m")
        # La precisión se expresa en la misma unidad que la medida (°C)
        print(f"Precisión: {self.precision} {self.unidad}")


class SensorViento(DispositivoIoT):
    def __init__(self, device_id, nombre, ubicacion, valor, unidad,
                 orientacion, velocidad_maxima):
        super().__init__(device_id, nombre, ubicacion, valor, unidad)
        self.orientacion = orientacion
        self.velocidad_maxima = velocidad_maxima

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Orientación: {self.orientacion}")
        print(f"Velocidad máxima: {self.velocidad_maxima} {self.unidad}")


class SensorTanque(DispositivoIoT):
    def __init__(self, device_id, nombre, ubicacion, valor, unidad,
                 capacidad, nivel_bateria):
        super().__init__(device_id, nombre, ubicacion, valor, unidad)
        self.capacidad = capacidad
        self.nivel_bateria = nivel_bateria

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Capacidad: {self.capacidad} L")
        print(f"Nivel de batería: {self.nivel_bateria} %")


def obtener_categoria(dispositivo):
    """Devuelve un mensaje personalizado según el tipo (usa isinstance)."""
    if isinstance(dispositivo, SensorHumedad):
        return "Sensor de humedad"
    if isinstance(dispositivo, SensorTemperatura):
        return "Sensor de temperatura"
    if isinstance(dispositivo, SensorViento):
        return "Sensor de viento"
    if isinstance(dispositivo, SensorTanque):
        return "Sensor de tanque"
    return "Dispositivo genérico"


def main():
    # Ocho dispositivos: dos de cada subclase
    dispositivos = [
        SensorHumedad("DEV001", "Sensor de suelo", "Parcela A",
                      45, "%", 30, "Automática"),
        SensorTemperatura("DEV002", "Sensor ambiental", "Parcela B",
                          26, "°C", 650, 0.5),
        SensorViento("DEV003", "Anemómetro", "Parcela C",
                     18, "km/h", "Norte", 80),
        SensorTanque("DEV004", "Tanque principal", "Parcela A",
                     75, "%", 5000, 90),
        SensorHumedad("DEV005", "Sensor de suelo 2", "Parcela B",
                      38, "%", 20, "Manual"),
        SensorTemperatura("DEV006", "Sensor invernadero", "Parcela C",
                          31, "°C", 640, 0.2),
        SensorViento("DEV007", "Anemómetro 2", "Parcela A",
                     12, "km/h", "Suroeste", 75),
        SensorTanque("DEV008", "Tanque auxiliar", "Parcela B",
                     40, "%", 2000, 85),
    ]

    # Información + categoría (isinstance)
    for dispositivo in dispositivos:
        dispositivo.mostrar_informacion()
        print(f"Categoría: {obtener_categoria(dispositivo)}")
        print("-" * 40)

    # Comprobación con vars(): solo atributos necesarios, ninguno a None
    print("\nComprobación con vars():")
    for dispositivo in dispositivos:
        atributos = vars(dispositivo)
        sin_none = all(valor is not None for valor in atributos.values())
        print(f"{dispositivo.device_id}: {len(atributos)} atributos "
              f"-> sin atributos vacíos: {sin_none}")
        print(f"   {atributos}")


if __name__ == "__main__":
    main()
