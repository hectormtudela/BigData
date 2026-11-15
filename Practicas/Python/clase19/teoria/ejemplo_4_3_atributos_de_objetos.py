# Ejemplo 4.3 · Los atributos de los objetos nativos
# clase_19_detalles_clases_objetos/teoria/ejemplo_4_3_atributos_de_objetos.py

def validar_fichero(ruta):
    return ruta.endswith(".csv")

print("__add__" in dir(55))
print("__abs__" in dir(-5.67))
print("__call__" in dir(validar_fichero))
print("upper" in dir("texto"))

print((55).__add__(45))
print((-5.67).__abs__())
print("ventas".__len__())
print(validar_fichero.__call__("ventas_07.csv"))
print(validar_fichero.__name__)

funcion = globals()["validar_fichero"]
print(funcion("clientes.json"))
