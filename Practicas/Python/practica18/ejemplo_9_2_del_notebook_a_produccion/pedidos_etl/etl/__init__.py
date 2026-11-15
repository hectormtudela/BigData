"""Pipeline ETL de pedidos online: extracción, transformación y carga."""

from .orquestador import ejecutar_pipeline

__all__ = ["ejecutar_pipeline"]
