"""Tarifas de envío de la empresa de paquetería."""

TARIFA_BASE = 3.50
PRECIO_POR_KG = 0.80
RECARGO_URGENTE = 0.25


def coste_envio(peso_kg, urgente=False):
    coste = TARIFA_BASE + peso_kg * PRECIO_POR_KG
    if urgente:
        coste = coste * (1 + RECARGO_URGENTE)
    return round(coste, 2)
