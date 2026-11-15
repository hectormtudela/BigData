"""Tarifas para envíos fuera de España."""

ZONA = "internacional"


def calcular_coste(peso_kg):
    return round(12.00 + peso_kg * 2.50, 2)
