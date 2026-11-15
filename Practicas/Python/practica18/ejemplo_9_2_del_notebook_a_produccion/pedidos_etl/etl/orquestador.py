"""Orquestador: une las tres etapas del pipeline en el orden correcto."""

from .extraccion import leer_lineas
from .transformacion import transformar
from .carga import ResumenVentas

def ejecutar_pipeline(texto):
    lineas = leer_lineas(texto)
    activos, rechazados, cancelados = transformar(lineas)
    resumen = ResumenVentas()
    resumen.cargar(activos)
    return {
        "leidos": len(lineas),
        "rechazados": rechazados,
        "cancelados": cancelados,
        "resumen": resumen,
    }
