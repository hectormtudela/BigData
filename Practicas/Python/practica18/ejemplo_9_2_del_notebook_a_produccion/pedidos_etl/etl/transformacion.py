"""Transformación: funciones puras que limpian, validan y convierten los datos."""

from .config import ESTADO_CANCELADO
from .modelos import Pedido

def parsear(linea):
    return [campo.strip() for campo in linea.split(",")]

def es_valido(campos):
    if len(campos) != 5:
        return False
    try:
        float(campos[3])
        return True
    except ValueError:
        return False

def a_pedido(campos):
    id_pedido, cliente, ciudad, importe, estado = campos
    return Pedido(id_pedido, cliente.title(), ciudad.title(), float(importe), estado.lower())

def transformar(lineas):
    registros = list(map(parsear, lineas))
    rechazados = [r[0] for r in registros if not es_valido(r)]
    pedidos = [a_pedido(r) for r in registros if es_valido(r)]
    cancelados = [p.id_pedido for p in pedidos if p.estado == ESTADO_CANCELADO]
    activos = list(filter(lambda p: p.estado != ESTADO_CANCELADO, pedidos))
    return activos, rechazados, cancelados
