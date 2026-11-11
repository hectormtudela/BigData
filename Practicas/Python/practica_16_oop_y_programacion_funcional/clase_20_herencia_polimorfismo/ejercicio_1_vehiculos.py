r"""
Práctica 16 · Clase 20 · Ejercicio 1 (Vehículos)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

> Ejercicio 1 . Tomando como referencia el ejemplo anterior crear una Superclase llamada Vehículo con sus respectivos atributos comunes. Luego crear al menos tres subclases (con sus atributos adicionales) del tipo: Coche, Moto, Camión, Autobús. Crear por lo menos un objeto de cada subclase y muestra en pantalla los resultados.
"""

class Vehiculo:
    """Superclase con los atributos y métodos comunes a todos los vehículos."""

    def __init__(self, marca, modelo, anio, velocidad_max_kmh):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad_max_kmh = velocidad_max_kmh

    def mostrar_informacion(self):
        """Muestra los datos comunes. Las subclases añaden los suyos."""
        print(f"Tipo: {type(self).__name__}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Velocidad máxima: {self.velocidad_max_kmh} km/h")


class Coche(Vehiculo):
    """Coche: añade número de puertas y tipo de combustible."""

    def __init__(self, marca, modelo, anio, velocidad_max_kmh,
                 num_puertas, combustible):
        # Reutilizamos el constructor de la superclase para los atributos comunes
        super().__init__(marca, modelo, anio, velocidad_max_kmh)
        self.num_puertas = num_puertas
        self.combustible = combustible

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de puertas: {self.num_puertas}")
        print(f"Combustible: {self.combustible}")


class Moto(Vehiculo):
    """Moto: añade cilindrada y tipo de moto."""

    def __init__(self, marca, modelo, anio, velocidad_max_kmh,
                 cilindrada_cc, tipo_moto):
        super().__init__(marca, modelo, anio, velocidad_max_kmh)
        self.cilindrada_cc = cilindrada_cc
        self.tipo_moto = tipo_moto

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada_cc} cc")
        print(f"Tipo de moto: {self.tipo_moto}")


class Camion(Vehiculo):
    """Camión: añade carga máxima y número de ejes."""

    def __init__(self, marca, modelo, anio, velocidad_max_kmh,
                 carga_max_kg, num_ejes):
        super().__init__(marca, modelo, anio, velocidad_max_kmh)
        self.carga_max_kg = carga_max_kg
        self.num_ejes = num_ejes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Carga máxima: {self.carga_max_kg} kg")
        print(f"Número de ejes: {self.num_ejes}")


class Autobus(Vehiculo):
    """Autobús: añade número de plazas y tipo de servicio."""

    def __init__(self, marca, modelo, anio, velocidad_max_kmh,
                 num_plazas, tipo_servicio):
        super().__init__(marca, modelo, anio, velocidad_max_kmh)
        self.num_plazas = num_plazas
        self.tipo_servicio = tipo_servicio

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de plazas: {self.num_plazas}")
        print(f"Tipo de servicio: {self.tipo_servicio}")


def main():
    # Un objeto de cada subclase
    vehiculos = [
        Coche("Seat", "León", 2022, 210, 5, "Gasolina"),
        Moto("Yamaha", "MT-07", 2021, 195, 689, "Naked"),
        Camion("Volvo", "FH16", 2020, 90, 24000, 3),
        Autobus("Mercedes-Benz", "Tourismo", 2019, 100, 55, "Interurbano"),
    ]

    for vehiculo in vehiculos:
        vehiculo.mostrar_informacion()
        print("-" * 40)


if __name__ == "__main__":
    main()
