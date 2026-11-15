# 1. import modulo
import envios_nacionales
print("1.", envios_nacionales.ZONA, envios_nacionales.calcular_coste(4))

# 2. import modulo as alias
import envios_internacionales as intl
print("2.", intl.ZONA, intl.calcular_coste(4))

# 3. from modulo import nombre
from envios_nacionales import calcular_coste
print("3.", calcular_coste(4))

# 4. from modulo import nombre as alias
from envios_internacionales import calcular_coste as coste_intl
print("4.", coste_intl(4))

# 5. Conflicto: se importa otro nombre igual al que ya existía
from envios_internacionales import calcular_coste
print("5.", calcular_coste(4))
print("   ¿De qué módulo viene ahora?", calcular_coste.__module__)
