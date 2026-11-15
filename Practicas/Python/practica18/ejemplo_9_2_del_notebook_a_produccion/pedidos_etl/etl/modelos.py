"""Clases de datos del pipeline."""

from .config import IVA

class Pedido:
    def __init__(self, id_pedido, cliente, ciudad, importe, estado):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.ciudad = ciudad
        self.importe = importe
        self.estado = estado

    @property
    def total_con_iva(self):
        return round(self.importe * (1 + IVA), 2)

    def __repr__(self):
        return f"Pedido({self.id_pedido}, {self.ciudad}, {self.total_con_iva})"
