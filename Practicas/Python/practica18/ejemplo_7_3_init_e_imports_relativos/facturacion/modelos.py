"""Clases de datos de la facturación."""

class Cliente:
    def __init__(self, nif, nombre, tipo_iva=0.21):
        self.nif = nif
        self.nombre = nombre
        self.tipo_iva = tipo_iva

class LineaFactura:
    def __init__(self, concepto, unidades, precio_unitario):
        self.concepto = concepto
        self.unidades = unidades
        self.precio_unitario = precio_unitario

    @property
    def importe(self):
        return round(self.unidades * self.precio_unitario, 2)
