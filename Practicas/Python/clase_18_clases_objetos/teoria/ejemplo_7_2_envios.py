# Ejemplo 7.2 · Procesar una lista de objetos
# clase_18_clases_objetos/teoria/ejemplo_7_2_envios.py

class Envio:
    def __init__(self, id_envio, destino, peso_kg, entregado):
        self.id_envio = id_envio
        self.destino = destino
        self.peso_kg = peso_kg
        self.entregado = entregado

    def __repr__(self):
        return f"Envio({self.id_envio}, {self.destino}, {self.peso_kg} kg)"

def obtener_peso(envio):
    return envio.peso_kg

envios = [
    Envio("E-01", "Madrid", 2.5, True),
    Envio("E-02", "Sevilla", 14.0, False),
    Envio("E-03", "Madrid", 0.8, True),
    Envio("E-04", "Bilbao", 7.2, False),
    Envio("E-05", "Sevilla", 3.1, True),
]

peso_total = sum([e.peso_kg for e in envios])
pendientes = [e.id_envio for e in envios if not e.entregado]

envios_por_destino = {}
for e in envios:
    envios_por_destino[e.destino] = envios_por_destino.get(e.destino, 0) + 1

mas_pesados = sorted(envios, key=obtener_peso, reverse=True)[:2]

print("Peso total:", round(peso_total, 2), "kg")
print("Pendientes:", pendientes)
print("Envíos por destino:", envios_por_destino)
print("Los 2 más pesados:", mas_pesados)
