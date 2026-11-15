# Ejercicio I5 - Depura el registro de equipos de proyecto
#
# La PMO de una consultora registra los equipos de proyecto y las horas asignadas. Se quiere:
#
# - Que cada equipo tenga **sus propios** miembros y **sus propias** horas.
# - Que la clase lleve la cuenta de **todos** los equipos creados (`equipos_creados`) y de las horas de **toda** la empresa (`horas_empresa`).
# El programador que escribió la clase cometió **tres errores** relacionados con los atributos de clase y de instancia:
#
# class EquipoProyecto:
#     miembros = []
#     horas_empresa = 0
#     equipos_creados = 0
#
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.horas = 0
#         self.equipos_creados += 1
#
#     def incorporar(self, persona, horas):
#         self.miembros.append(persona)
#         self.horas += horas
#         self.horas_empresa += horas
#
#     def __str__(self):
#         return f"{self.nombre}:{self.miembros} ·{self.horas} h"
#
# Al ejecutarlo con el código de prueba de abajo, la salida es esta (incorrecta):
#
# Data Lake: ['Ana', 'Luis', 'Sara'] · 200 h
# Churn ML: ['Ana', 'Luis', 'Sara'] · 60 h
# 0 0
# True
# {'nombre': 'Data Lake', 'horas': 200, 'equipos_creados': 1, 'horas_empresa': 200}
#
# Se pide:
#
# 1. **Antes de tocar nada**, escribe en un comentario al principio del archivo por qué cada línea de la salida es incorrecta.
# 2. Explica en el comentario por qué `vars(datos)` contiene `equipos_creados` y `horas_empresa` si están declarados como atributos **de clase**.
# 3. Corrige la clase para que el código de prueba produzca la salida esperada.

# DIAGNÓSTICO
#
# 1. Por qué es incorrecta cada línea de la salida:
#
#    - Línea 1: "Data Lake: ['Ana', 'Luis', 'Sara'] · 200 h". Sara no es de Data Lake.
#      `miembros = []` está declarado en el cuerpo de la clase, así que es un atributo
#      de CLASE: existe una sola lista, compartida por todos los equipos. Cuando ml
#      añade a Sara, la añade a esa lista común y Data Lake también la ve. Las horas
#      (200) sí son correctas, porque `self.horas` se crea en __init__ y es de instancia.
#    - Línea 2: "Churn ML: ['Ana', 'Luis', 'Sara'] · 60 h". Mismo error: Ana y Luis
#      tampoco son de Churn ML. Sus horas (60) sí son correctas.
#    - Línea 3: "0 0". Debería ser "2 260". `self.equipos_creados += 1` y
#      `self.horas_empresa += horas` no modifican la clase: Python lee el valor de la
#      clase (0), calcula 0 + 1 y guarda el resultado en un atributo NUEVO del objeto.
#      Los contadores de la clase se quedan en 0.
#    - Línea 4: "True". Debería ser False. `datos.miembros` y `ml.miembros` son el
#      mismo objeto lista (el de la clase), por eso `is` da True.
#    - Línea 5: el vars(datos) es incorrecto. Contiene `equipos_creados` y
#      `horas_empresa` (que no deberían ser de instancia) y NO contiene `miembros`
#      (que debería ser propio de cada equipo).
#
# 2. Por qué vars(datos) contiene equipos_creados y horas_empresa si son atributos de clase:
#
#    `self.equipos_creados += 1` equivale a `self.equipos_creados = self.equipos_creados + 1`.
#    Para leer, Python no encuentra el atributo en el objeto y lo toma de la clase (0).
#    Pero la ASIGNACIÓN siempre se hace sobre `self`, así que crea un atributo de
#    instancia nuevo (1) que "tapa" al de la clase. El de la clase no cambia nunca.
#    Por eso aparece en vars(datos), que solo muestra los atributos de la instancia.
#    Lo mismo ocurre con horas_empresa. Y `miembros` no aparece porque vive en la clase.
#
# Corrección: miembros pasa a ser un atributo de instancia (se crea en __init__) y los
# contadores se modifican a través de la clase: EquipoProyecto.equipos_creados += 1.

# Solución:

class EquipoProyecto:
    """Equipo de proyecto de la PMO, con contadores globales en la clase."""

    horas_empresa = 0
    equipos_creados = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.horas = 0
        self.miembros = []
        EquipoProyecto.equipos_creados += 1

    def incorporar(self, persona, horas):
        self.miembros.append(persona)
        self.horas += horas
        EquipoProyecto.horas_empresa += horas

    def __str__(self):
        return f"{self.nombre}: {self.miembros} · {self.horas} h"


# Código de prueba del enunciado
datos = EquipoProyecto("Data Lake")
ml = EquipoProyecto("Churn ML")
datos.incorporar("Ana", 120)
datos.incorporar("Luis", 80)
ml.incorporar("Sara", 60)
print(datos)
print(ml)
print(EquipoProyecto.equipos_creados, EquipoProyecto.horas_empresa)
print(datos.miembros is ml.miembros)
print(vars(datos))