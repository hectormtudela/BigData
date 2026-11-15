import sys

print("Inicio del programa")
import configuracion
import configuracion            # No se ejecuta
import informes                 # Al importar informes también importa configuracion por lo que import configuracion no se ejecuta (creo)
print("Fin de los import")

print("¿Está en sys.modules?", "configuracion" in sys.modules)
print("¿Es el mismo objeto?", informes.configuracion is configuracion)

print(informes.formatear(1234.7))
configuracion.CONFIG["moneda"] = "USD"
configuracion.CONFIG["decimales"] = 0
print(informes.formatear(1234.7))
