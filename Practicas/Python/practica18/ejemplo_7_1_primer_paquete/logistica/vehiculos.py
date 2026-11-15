"""Vehículos de la flota."""


class Vehiculo:
    def __init__(self, matricula, capacidad_kg):
        self.matricula = matricula
        self.capacidad_kg = capacidad_kg

    def coste_por_km(self):
        return 0.0

    def puede_cargar(self, kg):
        return kg <= self.capacidad_kg

    def __str__(self):
        return f"{type(self).__name__} {self.matricula}"


class Furgoneta(Vehiculo):
    def coste_por_km(self):
        return 0.35


class Camion(Vehiculo):
    def coste_por_km(self):
        return 0.90
