# Ejemplo 4.2 · Referencias con objetos inmutables y mutables
# clase_19_detalles_clases_objetos/teoria/ejemplo_4_2_referencias.py

class Umbral:
    def __init__(self, valor):
        self.valor = valor

# Objetos inmutables: int
limite = 500
alias = limite
print(alias is limite)
alias = 800
print(limite, alias)
print(alias is limite)

# Objetos mutables: list
columnas = ["id", "fecha"]
mismas = columnas
mismas.append("importe")
print(columnas)
print(mismas is columnas)

# Dos objetos con los mismos datos
u1 = Umbral(0.05)
u2 = Umbral(0.05)
print(u1 is u2, id(u1) == id(u2))
u3 = u1
u3.valor = 0.10
print(u1.valor, u2.valor)
print(id(u3) == id(u1))
