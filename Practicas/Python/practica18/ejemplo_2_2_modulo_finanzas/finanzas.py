"""Funciones financieras del departamento de ventas."""

IVA_GENERAL = 0.21
IVA_REDUCIDO = 0.10


def con_iva(importe, tipo=IVA_GENERAL):
    return round(importe * (1 + tipo), 2)


def aplicar_descuento(importe, porcentaje):
    return round(importe * (1 - porcentaje / 100), 2)


def margen(precio_venta, coste):
    return round((precio_venta - coste) / precio_venta * 100, 1)
