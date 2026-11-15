# Ejemplo 3.2 · Comparar versiones de un esquema de datos
# clase_19_detalles_clases_objetos/teoria/ejemplo_3_2_version_esquema.py

class VersionEsquema:
    def __init__(self, mayor, menor, parche):
        self.mayor = mayor
        self.menor = menor
        self.parche = parche

    def __eq__(self, otra):
        return (self.mayor, self.menor, self.parche) == (otra.mayor, otra.menor, otra.parche)

    def __lt__(self, otra):
        return (self.mayor, self.menor, self.parche) < (otra.mayor, otra.menor, otra.parche)

    def __gt__(self, otra):
        return (self.mayor, self.menor, self.parche) > (otra.mayor, otra.menor, otra.parche)

    def __repr__(self):
        return f"v{self.mayor}.{self.menor}.{self.parche}"

productor = VersionEsquema(2, 10, 0)
consumidor = VersionEsquema(2, 9, 3)
copia = VersionEsquema(2, 10, 0)

print(productor == copia)
print(productor is copia)
print(productor != consumidor)
print(consumidor < productor)
print(productor > consumidor)

historico = [VersionEsquema(1, 4, 2), VersionEsquema(2, 10, 0), VersionEsquema(2, 9, 3), VersionEsquema(1, 12, 0)]
print(sorted(historico))
print(max(historico))
