# Ejemplo 3.4 · Operadores ya sobrecargados en los tipos nativos
# clase_19_detalles_clases_objetos/teoria/ejemplo_3_4_operadores_nativos.py

print(10 + 20)
print("data" + "_" + "lake")
print([1, 2] + [3, 4])
print((2026, 10) + (29,))

print("-" * 20)
print([0] * 5)

print(int.__add__(10, 20))
print(str.__add__("data", "_lake"))
print(list.__mul__([0], 5))

print("ventas" - "s")
