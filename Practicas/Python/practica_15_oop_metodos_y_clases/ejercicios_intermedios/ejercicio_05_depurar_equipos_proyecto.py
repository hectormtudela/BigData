"""
Práctica 15 · Ejercicio I5 - Depura el registro de equipos de proyecto
Nivel: intermedio

Enunciado completo: ../practica_15_oop_metodos_y_clases.md
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

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

# Salida actual (incorrecta):
# Data Lake: ['Ana', 'Luis', 'Sara'] · 200 h
# Churn ML: ['Ana', 'Luis', 'Sara'] · 60 h
# 0 0
# True
# {'nombre': 'Data Lake', 'horas': 200, 'equipos_creados': 1, 'horas_empresa': 200}

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

# ===== Salida esperada del código corregido =====
# Data Lake: ['Ana', 'Luis'] · 200 h
# Churn ML: ['Sara'] · 60 h
# 2 260
# False
# {'nombre': 'Data Lake', 'horas': 200, 'miembros': ['Ana', 'Luis']}
