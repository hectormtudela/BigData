"""Orquestador: une las tres etapas del pipeline."""

from .extraccion import leer_registros
from .transformacion import transformar
from .carga import AlmacenVentas


def ejecutar_pipeline(texto):
    almacen = AlmacenVentas()
    almacen.cargar(transformar(leer_registros(texto)))
    return almacen
