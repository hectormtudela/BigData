# Ejemplo 5.2 · Convertir una línea de CSV en un objeto
# clase_19_detalles_clases_objetos/teoria/ejemplo_5_2_setattr_getattr.py

class Registro:
    pass

cabecera = "id_pedido,cliente,importe,canal"
linea = "PED-9001,C-188,149.90,web"

columnas = cabecera.split(",")
valores = linea.split(",")

r = Registro()
for i in range(len(columnas)):
    setattr(r, columnas[i], valores[i])

print(vars(r))
print(getattr(r, "cliente"))
print(getattr(r, "descuento", "sin descuento"))

setattr(r, "importe", float(r.importe))
delattr(r, "canal")
print(vars(r))
print(hasattr(r, "canal"))
