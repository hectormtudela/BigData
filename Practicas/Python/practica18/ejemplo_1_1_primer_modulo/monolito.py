"""Versión ANTES de modularizar: todo en un único archivo."""

TARIFA_BASE = 3.50
PRECIO_POR_KG = 0.80
RECARGO_URGENTE = 0.25


def coste_envio(peso_kg, urgente=False):
    coste = TARIFA_BASE + peso_kg * PRECIO_POR_KG
    if urgente:
        coste = coste * (1 + RECARGO_URGENTE)
    return round(coste, 2)


pedidos = [("A-101", 2.0, False), ("A-102", 7.5, True), ("A-103", 0.5, False)]
for codigo, peso, urgente in pedidos:
    print(f"{codigo}: {coste_envio(peso, urgente)} €")
