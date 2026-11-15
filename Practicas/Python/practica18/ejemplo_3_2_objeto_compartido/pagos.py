"""Cobros a clientes."""

from auditoria import registro


def cobrar(cliente, importe):
    registro.anotar("pagos", f"cobro de {importe} € a {cliente}")
    return round(importe, 2)
