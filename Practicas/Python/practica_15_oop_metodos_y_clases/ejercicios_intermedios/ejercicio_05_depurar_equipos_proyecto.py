"""
Práctica 15 · Ejercicio I5 - Depura el registro de equipos de proyecto
Nivel: intermedio
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio I5 - Depura el registro de equipos de proyecto
#
# La PMO de una consultora registra los equipos de proyecto y las horas asignadas. Se quiere:
#
# - Que cada equipo tenga **sus propios** miembros y **sus propias** horas.
# - Que la clase lleve la cuenta de **todos** los equipos creados (`equipos_creados`) y de las horas de **toda** la empresa (`horas_empresa`).
# El programador que escribió la clase cometió **tres errores** relacionados con los atributos de clase y de instancia:
#
# ```python
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
# ```
#
# Al ejecutarlo con el código de prueba de abajo, la salida es esta (incorrecta):
#
# ```plain text
# Data Lake: ['Ana', 'Luis', 'Sara'] · 200 h
# Churn ML: ['Ana', 'Luis', 'Sara'] · 60 h
# 0 0
# True
# {'nombre': 'Data Lake', 'horas': 200, 'equipos_creados': 1, 'horas_empresa': 200}
# ```
#
# Se pide:
#
# 1. **Antes de tocar nada**, escribe en un comentario al principio del archivo por qué cada línea de la salida es incorrecta.
# 2. Explica en el comentario por qué `vars(datos)` contiene `equipos_creados` y `horas_empresa` si están declarados como atributos **de clase**.
# 3. Corrige la clase para que el código de prueba produzca la salida esperada.
# **Código de prueba:**
#
# ```python
# datos = EquipoProyecto("Data Lake")
# ml = EquipoProyecto("Churn ML")
# datos.incorporar("Ana", 120)
# datos.incorporar("Luis", 80)
# ml.incorporar("Sara", 60)
# print(datos)
# print(ml)
# print(EquipoProyecto.equipos_creados, EquipoProyecto.horas_empresa)
# print(datos.miembros is ml.miembros)
# print(vars(datos))
# ```
#
# **Salida esperada del código corregido:**
#
# ```plain text
# Data Lake: ['Ana', 'Luis'] · 200 h
# Churn ML: ['Sara'] · 60 h
# 2 260
# False
# {'nombre': 'Data Lake', 'horas': 200, 'miembros': ['Ana', 'Luis']}
# ```

# ===== DIAGNÓSTICO (escríbelo ANTES de tocar el código) =====
# 1. Por qué es incorrecta cada línea de la salida:
#    - 
#    - 
#    - 
#    - 
#    - 
# 2. Por qué vars(datos) contiene equipos_creados y horas_empresa si son atributos de clase:
#    - 

# ===== Clase del enunciado (con los 3 errores): CORRÍGELA =====
class EquipoProyecto:
    miembros = []
    horas_empresa = 0
    equipos_creados = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.horas = 0
        self.equipos_creados += 1

    def incorporar(self, persona, horas):
        self.miembros.append(persona)
        self.horas += horas
        self.horas_empresa += horas

    def __str__(self):
        return f"{self.nombre}: {self.miembros} · {self.horas} h"

# ===== Código de prueba del enunciado =====
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
