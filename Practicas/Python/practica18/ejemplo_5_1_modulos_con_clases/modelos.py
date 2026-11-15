"""Clases del catálogo de productos."""


class Producto:
    def __init__(self, sku, nombre, precio, stock):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def valor_stock(self):
        return round(self.precio * self.stock, 2)

    def precio_venta(self):
        return self.precio

    def __repr__(self):
        return f"{type(self).__name__}({self.sku!r}, {self.nombre!r})"


class ProductoPerecedero(Producto):
    def __init__(self, sku, nombre, precio, stock, dias_para_caducar):
        super().__init__(sku, nombre, precio, stock)
        self.dias_para_caducar = dias_para_caducar

    def precio_venta(self):
        if self.dias_para_caducar <= 3:
            return round(self.precio * 0.70, 2)
        return self.precio
