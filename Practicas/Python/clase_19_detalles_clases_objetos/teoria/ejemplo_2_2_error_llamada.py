# Ejemplo 2.2 · Llamar a una función de la clase desde un objeto
# clase_19_detalles_clases_objetos/teoria/ejemplo_2_2_error_llamada.py

class Notificador:
    def __init__(self, canal):
        self.canal = canal

    def version():
        return "Notificador v2.4"

n = Notificador("email")
print(Notificador.version())
print(n.version())
