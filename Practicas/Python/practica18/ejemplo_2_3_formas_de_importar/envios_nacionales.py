"""Tarifas para envíos dentro de España."""

ZONA = "nacional"


def calcular_coste(peso_kg):
    return round(4.00 + peso_kg * 0.60, 2)
