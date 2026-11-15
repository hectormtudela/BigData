"""La clase Factura, que usa los otros módulos del paquete."""

from .modelos import Cliente, LineaFactura
from .calculos import base_imponible, descuento_por_volumen, cuota_iva

class Factura:
    _contador = 0

    def __init__(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Se esperaba un Cliente")
        Factura._contador += 1
        self.numero = f"F-{Factura._contador:04d}"
        self.cliente = cliente
        self.lineas = []

    def agregar_linea(self, concepto, unidades, precio_unitario):
        self.lineas.append(LineaFactura(concepto, unidades, precio_unitario))
        return self

    def total(self):
        base = base_imponible(self.lineas)
        base_neta = round(base - descuento_por_volumen(base), 2)
        return round(base_neta + cuota_iva(base_neta, self.cliente.tipo_iva), 2)

    def __str__(self):
        return (f"{self.numero} | {self.cliente.nombre} | "
                f"líneas: {len(self.lineas)} | total: {self.total()} €")
