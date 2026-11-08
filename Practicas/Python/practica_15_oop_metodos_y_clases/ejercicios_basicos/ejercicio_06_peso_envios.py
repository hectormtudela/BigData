"""
Práctica 15 · Ejercicio B6 - Peso de los envíos de un almacén
Nivel: básico
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio B6 - Peso de los envíos de un almacén
#
# El almacén de una empresa de e-commerce agrupa paquetes en palés y necesita sumar, comparar y ordenar pesos. Crea la clase `PesoEnvio`:
#
# - Constructor con `gramos` (entero). Si llega un valor negativo, se guarda `0`.
# - Sobrecarga `+` para que la suma de dos pesos devuelva un **objeto nuevo** `PesoEnvio`.
# - Sobrecarga `==` y `<` comparando los gramos.
# - `__str__`: si el peso es de 1000 g o más, se muestra en kilos con 2 decimales (`"1.25 kg"`); si no, en gramos (`"850 g"`).
# - `__repr__`: `PesoEnvio(850)`.
# **Código de prueba:**
#
# ```python
# paquetes = [PesoEnvio(850), PesoEnvio(1250), PesoEnvio(400), PesoEnvio(-30), PesoEnvio(2300)]
# print(paquetes[0] + paquetes[2])
# print(paquetes[0] + paquetes[1])
# pale = PesoEnvio(0)
# for p in paquetes:
#     pale = pale + p
# print("Palé:", pale)
# print(sorted(paquetes))
# print("Más pesado:", max(paquetes))
# print(PesoEnvio(1250) == paquetes[1], PesoEnvio(1250) is paquetes[1])
# ```
#
# **Salida esperada:**
#
# ```plain text
# 1.25 kg
# 2.10 kg
# Palé: 4.80 kg
# [PesoEnvio(0), PesoEnvio(400), PesoEnvio(850), PesoEnvio(1250), PesoEnvio(2300)]
# Más pesado: 2.30 kg
# True False
# ```

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
paquetes = [PesoEnvio(850), PesoEnvio(1250), PesoEnvio(400), PesoEnvio(-30), PesoEnvio(2300)]
print(paquetes[0] + paquetes[2])
print(paquetes[0] + paquetes[1])
pale = PesoEnvio(0)
for p in paquetes:
    pale = pale + p
print("Palé:", pale)
print(sorted(paquetes))
print("Más pesado:", max(paquetes))
print(PesoEnvio(1250) == paquetes[1], PesoEnvio(1250) is paquetes[1])
