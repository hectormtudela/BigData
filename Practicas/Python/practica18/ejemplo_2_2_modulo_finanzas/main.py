import finanzas

print(type(finanzas))
print(finanzas.__name__)
print(finanzas.__doc__)
print([nombre for nombre in dir(finanzas) if not nombre.startswith("_")])

print(finanzas.con_iva(100))
print(finanzas.con_iva(100, finanzas.IVA_REDUCIDO))
print(finanzas.aplicar_descuento(250, 15))
print(finanzas.margen(150, 90), "%")

precios = [120.0, 45.5, 80.0]
print(list(map(finanzas.con_iva, precios)))
