# Ejemplo 2.1 · Crear objetos de una clase vacía
# clase_18_clases_objetos/teoria/ejemplo_2_1_crear_objetos.py

class Pedido:
    pass

pedido_a = Pedido()
pedido_b = Pedido()

print(type(pedido_a))
print(type(pedido_a).__name__)
print(isinstance(pedido_a, Pedido))
print(isinstance("PED-1001", Pedido))
print(pedido_a is pedido_b)
