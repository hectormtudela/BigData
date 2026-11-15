"""Gestión del inventario de un almacén."""

from modelos import Producto

class Inventario:
    CRITERIOS = {
        "precio": lambda p: p.precio_venta(),
        "stock": lambda p: p.stock,
        "valor": lambda p: p.valor_stock,
    }

    def __init__(self):
        self._productos = []

    def agregar(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se admiten objetos Producto")
        self._productos.append(producto)

    def __len__(self):
        return len(self._productos)

    def __iter__(self):
        for producto in self._productos:
            yield producto

    def bajo_stock(self, umbral):
        return list(filter(lambda p: p.stock < umbral, self._productos))

    def valor_total(self):
        return round(sum(p.valor_stock for p in self._productos), 2)

    def ordenar_por(self, criterio, descendente=False):
        return sorted(self._productos, key=self.CRITERIOS[criterio], reverse=descendente)
