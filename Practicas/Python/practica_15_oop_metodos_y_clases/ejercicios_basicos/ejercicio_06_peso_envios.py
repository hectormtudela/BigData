"""
Práctica 15 · Ejercicio B6 - Peso de los envíos de un almacén
Nivel: básico

Enunciado completo: ../practica_15_oop_metodos_y_clases.md
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

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

# ===== Salida esperada =====
# 1.25 kg
# 2.10 kg
# Palé: 4.80 kg
# [PesoEnvio(0), PesoEnvio(400), PesoEnvio(850), PesoEnvio(1250), PesoEnvio(2300)]
# Más pesado: 2.30 kg
# True False
