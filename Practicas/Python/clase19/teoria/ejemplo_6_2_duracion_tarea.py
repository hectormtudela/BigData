# Ejemplo 6.2 · Duración de una tarea: de texto a objeto y de objeto a número
# clase_19_detalles_clases_objetos/teoria/ejemplo_6_2_duracion_tarea.py

class DuracionTarea:
    def __init__(self, texto="00:00:00"):            # conversión str -> DuracionTarea
        horas, minutos, segundos = texto.split(":")
        self.__segundos = int(horas) * 3600 + int(minutos) * 60 + int(segundos)

    def __int__(self):                                # DuracionTarea -> int
        return self.__segundos

    def __float__(self):                              # DuracionTarea -> float (horas)
        return round(self.__segundos / 3600, 2)

    def __bool__(self):                               # DuracionTarea -> bool
        return self.__segundos > 0

    def __str__(self):                                # DuracionTarea -> str
        return f"{self.__segundos // 60} min {self.__segundos % 60} s"

extraccion = DuracionTarea("00:12:40")
transformacion = DuracionTarea("01:05:00")
sin_ejecutar = DuracionTarea()

print(int(extraccion))
print(float(transformacion))
print(str(extraccion))
print(bool(transformacion), bool(sin_ejecutar))

total_segundos = sum([int(d) for d in [extraccion, transformacion, sin_ejecutar]])
print(total_segundos)

if not sin_ejecutar:
    print("Hay tareas que no han llegado a ejecutarse")
