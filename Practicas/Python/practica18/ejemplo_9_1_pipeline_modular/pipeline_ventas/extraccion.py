"""Extracción: lee los registros en bruto sin cargarlos todos a la vez."""


def leer_registros(texto):
    lineas = texto.strip().split("\n")
    for linea in lineas[1:]:                  # se salta la cabecera
        yield linea
