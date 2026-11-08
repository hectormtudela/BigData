# Ejemplo 4.2 · Métodos que controlan el ciclo de vida de una tarea
# clase_18_clases_objetos/teoria/ejemplo_4_2_ciclo_vida_tarea.py

class TareaIngesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "pendiente"
        self.filas_cargadas = 0

    def iniciar(self):
        if self.estado != "pendiente":
            print(f"[{self.nombre}] No se puede iniciar: estado actual '{self.estado}'")
            return
        self.estado = "en_ejecucion"
        print(f"[{self.nombre}] Iniciada")

    def cargar(self, filas):
        if self.estado != "en_ejecucion":
            print(f"[{self.nombre}] Carga rechazada: la tarea no está en ejecución")
            return
        self.filas_cargadas += filas
        print(f"[{self.nombre}] +{filas} filas (acumulado: {self.filas_cargadas})")

    def finalizar(self):
        if self.estado == "en_ejecucion":
            self.estado = "completada"
        print(f"[{self.nombre}] Estado final: {self.estado} con {self.filas_cargadas} filas")

tarea = TareaIngesta("ventas_diarias")
tarea.cargar(500)
tarea.iniciar()
tarea.cargar(12000)
tarea.cargar(8500)
tarea.iniciar()
tarea.finalizar()
