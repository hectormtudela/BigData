"""Clase que aplica una política de precios a un catálogo."""

from politicas_precio import POLITICAS, precio_normal

class Tarificador:
    def __init__(self, politica=precio_normal):
        self.politica = politica

    def cambiar_politica(self, nombre):
        self.politica = POLITICAS[nombre]

    def tarifar(self, catalogo):
        return {producto: self.politica(precio) for producto, precio in catalogo.items()}
