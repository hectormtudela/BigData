# Ejemplo 7.1 · Referencias compartidas
# clase_18_clases_objetos/teoria/ejemplo_7_1_referencias.py

class ClienteFidelidad:
    def __init__(self, id_cliente, puntos=0):
        self.id_cliente = id_cliente
        self.puntos = puntos

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad

def aplicar_bono_bienvenida(cliente):
    cliente.sumar_puntos(200)

original = ClienteFidelidad("C-88", 100)
alias = original
alias.sumar_puntos(50)
print(original.puntos)
print(alias is original)

otro = ClienteFidelidad("C-88", 150)
print(otro is original)
print(otro.puntos == original.puntos)

aplicar_bono_bienvenida(otro)
print(otro.puntos)
print(original.puntos)
