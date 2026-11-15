import os
import sys

print("Primera ruta de búsqueda:", os.path.basename(sys.path[0]))
print("Número de rutas > 1:", len(sys.path) > 1)

import random
print("random se ha cargado desde:", os.path.basename(random.__file__))
try:
    print(random.randint(1, 6))
except AttributeError as error:
    print("AttributeError:", error)

try:
    import tarifas_2027
except ModuleNotFoundError as error:
    print("ModuleNotFoundError:", error)
