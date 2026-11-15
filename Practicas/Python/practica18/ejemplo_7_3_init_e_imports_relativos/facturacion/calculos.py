"""Funciones puras para calcular importes."""

from functools import reduce

TRAMOS_DESCUENTO = [(1000, 0.05), (5000, 0.10)]

def base_imponible(lineas):
    return round(sum(linea.importe for linea in lineas), 2)


def descuento_por_volumen(base):
    porcentaje = reduce(
        lambda actual, tramo: tramo[1] if base >= tramo[0] else actual,
        TRAMOS_DESCUENTO,
        0.0,
    )
    return round(base * porcentaje, 2)

def cuota_iva(base, tipo):
    return round(base * tipo, 2)
