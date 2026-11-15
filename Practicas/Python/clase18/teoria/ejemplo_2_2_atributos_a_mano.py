# Ejemplo 2.2 · Atributos añadidos a mano y el problema que generan
# clase_18_clases_objetos/teoria/ejemplo_2_2_atributos_a_mano.py

class Pedido:
    pass

pedido_a = Pedido()
pedido_a.codigo = "PED-1001"
pedido_a.importe = 149.90

pedido_b = Pedido()
pedido_b.codigo = "PED-1002"

print(pedido_a.codigo, pedido_a.importe)
print(pedido_b.codigo)
print(hasattr(pedido_a, "importe"))
print(hasattr(pedido_b, "importe"))
print(vars(pedido_a))
print(vars(pedido_b))
