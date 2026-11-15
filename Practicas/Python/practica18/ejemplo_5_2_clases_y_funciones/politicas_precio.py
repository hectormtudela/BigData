"""Políticas de precio: funciones puras que reciben un precio y devuelven otro."""

from functools import reduce

def precio_normal(precio):
    return precio

def redondeo_comercial(precio):
    return int(precio) + 0.99

def crear_descuento(porcentaje):
    def descontar(precio):
        return round(precio * (1 - porcentaje / 100), 2)
    return descontar

def componer(*politicas):
    return lambda precio: reduce(lambda acumulado, f: f(acumulado), politicas, precio)

POLITICAS = {
    "normal": precio_normal,
    "rebajas": crear_descuento(20),
    "black_friday": crear_descuento(35),
    "outlet": componer(crear_descuento(40), redondeo_comercial),
}
