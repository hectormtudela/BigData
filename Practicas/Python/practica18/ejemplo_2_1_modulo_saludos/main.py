# Forma 1: importar el módulo completo
import saludos

saludos.saludar()
objeto = saludos.Saludo()
objeto.saludar_persona("Ana")

print("-" * 40)

# Forma 2: importar solo la función y la clase
from saludos import Saludo

objeto = Saludo()
objeto.saludar_persona("Ana")
