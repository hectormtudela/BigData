# Forma 1: importar el módulo completo

import saludos

# Llamar a la función del módulo
saludos.saludar()

# Crear un objeto de la clase
objeto = saludos.Saludo()

# Llamar al método del objeto
objeto.saludar_persona("Ana")

print("-" * 40)

# Forma 2: importar solo la función y la clase

from saludos import Saludo

objeto = Saludo()

objeto.saludar_persona("Ana")
