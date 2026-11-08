# Ejemplo 4.1 · El tipo de cada cosa
# clase_19_detalles_clases_objetos/teoria/ejemplo_4_1_todo_es_objeto.py

import math

class Proveedor:
    pass

def validar_fichero(ruta):
    return ruta.endswith(".csv")

valores = [
    250,
    19.99,
    3 + 2j,
    "Logística Sur",
    True,
    [10, 20, 30],
    (40.41, -3.70),
    {"csv", "json"},
    {"tienda": "T-07"},
    None,
    validar_fichero,
    Proveedor,
    Proveedor(),
    math,
]

for v in valores:
    print(type(v))
