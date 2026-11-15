"""Preparación de envíos."""

from auditoria import registro


def preparar_envio(cliente, articulos):
    registro.anotar("envios", f"{len(articulos)} artículos para {cliente}")
    return sorted(articulos, key=lambda articulo: articulo.lower())
