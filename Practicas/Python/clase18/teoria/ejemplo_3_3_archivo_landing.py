# Ejemplo 3.3 · Atributos calculados en el constructor
# clase_18_clases_objetos/teoria/ejemplo_3_3_archivo_landing.py

class ArchivoLanding:
    def __init__(self, ruta, tamano_bytes):
        self.ruta = ruta
        self.tamano_bytes = tamano_bytes
        self.nombre = ruta.split("/")[-1]
        self.extension = self.nombre.split(".")[-1].lower()
        self.tamano_mb = round(tamano_bytes / (1024 * 1024), 2)
        self.es_grande = self.tamano_mb > 100

archivo = ArchivoLanding("/landing/ventas/2026/10/ventas_tienda_07.CSV", 157_286_400)

print(archivo.nombre)
print(archivo.extension)
print(archivo.tamano_mb)
print(archivo.es_grande)
