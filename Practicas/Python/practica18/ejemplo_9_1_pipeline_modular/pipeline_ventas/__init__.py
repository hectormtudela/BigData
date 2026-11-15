"""Pipeline ETL de ventas: extracción, transformación y carga."""

from .orquestador import ejecutar_pipeline

__all__ = ["ejecutar_pipeline"]
