# Ejemplo 2.1 · Sistema de alertas de un pipeline
# clase_19_detalles_clases_objetos/teoria/ejemplo_2_1_funciones_y_metodos.py

def cabecera():                                   # función global
    print("=== Sistema de alertas ===")

class Notificador:
    def __init__(self, canal):
        self.canal = canal

    def enviar(self, mensaje):                    # método de instancia: recibe self
        cabecera()                                # llama a una función global
        print(f"[{self.canal}] {mensaje}")

    def version():                                # función de la clase: sin self
        cabecera()
        print("Notificador v2.4")

def procesar_alertas(notificador, alertas):       # función global
    Notificador.version()                         # llama a la función de la clase
    for alerta in alertas:
        notificador.enviar(alerta)                # llama al método de instancia

slack = Notificador("slack#datos")
procesar_alertas(slack, ["Carga de ventas retrasada", "Disco al 91 %"])
