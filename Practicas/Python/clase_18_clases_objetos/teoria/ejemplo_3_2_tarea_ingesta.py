# Ejemplo 3.2 · Valores por defecto y atributos de estado
# clase_18_clases_objetos/teoria/ejemplo_3_2_tarea_ingesta.py

class TareaIngesta:
    def __init__(self, nombre, origen, formato="csv", reintentos_max=3):
        self.nombre = nombre
        self.origen = origen
        self.formato = formato
        self.reintentos_max = reintentos_max
        self.estado = "pendiente"
        self.filas_cargadas = 0

t1 = TareaIngesta("ventas_diarias", "sftp_tiendas")
t2 = TareaIngesta("clics_web", "blob_logs", formato="json", reintentos_max=5)

for tarea in [t1, t2]:
    print(f"{tarea.nombre:<15} formato={tarea.formato:<5} reintentos={tarea.reintentos_max} "
          f"estado={tarea.estado} filas={tarea.filas_cargadas}")
