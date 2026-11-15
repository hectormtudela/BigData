"""Transformación: funciones puras que limpian y convierten los registros."""

from .modelos import Venta


def parsear(linea):
    return [campo.strip() for campo in linea.split(",")]


def _es_decimal(texto):
    try:
        float(texto)
        return True
    except ValueError:
        return False


def es_valido(campos):
    return len(campos) == 4 and campos[2].isdigit() and _es_decimal(campos[3])


def a_venta(campos):
    tienda, producto, unidades, precio = campos
    return Venta(tienda.title(), producto.lower(), int(unidades), float(precio))


def transformar(lineas):
    campos = map(parsear, lineas)
    validos = filter(es_valido, campos)
    return map(a_venta, validos)
