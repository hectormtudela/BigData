# Ejemplo 6.1 · Conversiones entre tipos nativos
# clase_19_detalles_clases_objetos/teoria/ejemplo_6_1_conversiones_nativas.py

print(int("250"))
print(float("19.99"))
print(int(9.99))
print(round(9.99))
print(str(2026))
print(bool(0), bool(""), bool("0"), bool([]))

print(list("CSV"))
print(tuple(["id", "fecha"]))
print(set(["madrid", "sevilla", "madrid"]) == {"madrid", "sevilla"})
print(dict([("csv", 12), ("json", 3)]))
print(list({"csv": 12, "json": 3}))
print(int("0x1F", 16))
