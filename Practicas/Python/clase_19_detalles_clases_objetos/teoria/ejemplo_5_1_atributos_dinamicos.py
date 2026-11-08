# Ejemplo 5.1 · Evento de clic en una tienda online
# clase_19_detalles_clases_objetos/teoria/ejemplo_5_1_atributos_dinamicos.py

class EventoClic:
    pass

e = EventoClic()

# crear atributos sobre la marcha
e.usuario = "u_4471"
e.pagina = "/checkout"
e.dispositivo = "movil"
e.campania = "black_friday"
print(vars(e))

# modificar atributos
e.pagina = "/checkout/pago"
e.dispositivo = "tablet"

# eliminar un atributo
del e.campania

print(vars(e))
print(hasattr(e, "campania"))
print(e.pagina)
