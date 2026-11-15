"""Cálculos sobre rutas de reparto (funciones puras)."""


def distancia_total(tramos_km):
    return round(sum(tramos_km), 1)


def coste_ruta(vehiculo, tramos_km):
    return round(vehiculo.coste_por_km() * distancia_total(tramos_km), 2)
