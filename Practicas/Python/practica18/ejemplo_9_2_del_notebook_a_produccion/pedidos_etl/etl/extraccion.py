"""Extracción: obtiene las líneas de datos en bruto, sin la cabecera."""

def leer_lineas(texto):
    return texto.strip().split("\n")[1:]
