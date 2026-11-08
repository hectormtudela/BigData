# Ejemplo 5.3 · La trampa de las listas como atributo de clase
# clase_18_clases_objetos/teoria/ejemplo_5_3_cola_mensajes_error.py

class ColaMensajes:
    mensajes = []          # atributo de clase mutable: compartido por todas las colas

    def __init__(self, topic):
        self.topic = topic

    def publicar(self, mensaje):
        self.mensajes.append(mensaje)

pedidos = ColaMensajes("pedidos")
pagos = ColaMensajes("pagos")
pedidos.publicar("pedido 501 creado")
pagos.publicar("pago 77 confirmado")

print(pedidos.topic, pedidos.mensajes)
print(pagos.topic, pagos.mensajes)
print(pedidos.mensajes is pagos.mensajes)
