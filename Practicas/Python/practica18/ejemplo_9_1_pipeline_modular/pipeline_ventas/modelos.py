"""Clases de datos del pipeline."""


class Venta:
    def __init__(self, tienda, producto, unidades, precio):
        self.tienda = tienda
        self.producto = producto
        self.unidades = unidades
        self.precio = precio

    @property
    def importe(self):
        return round(self.unidades * self.precio, 2)

    def __repr__(self):
        return f"Venta({self.tienda}, {self.producto}, {self.importe})"
