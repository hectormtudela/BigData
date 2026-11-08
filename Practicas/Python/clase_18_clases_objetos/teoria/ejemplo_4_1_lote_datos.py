# Ejemplo 4.1 · Lote de registros con métodos de consulta
# clase_18_clases_objetos/teoria/ejemplo_4_1_lote_datos.py

class LoteDatos:
    def __init__(self, id_lote):
        self.id_lote = id_lote
        self.registros = []

    def agregar(self, registro):
        self.registros.append(registro)

    def total_registros(self):
        return len(self.registros)

    def importe_total(self):
        total = 0
        for registro in self.registros:
            total += registro["importe"]
        return round(total, 2)

lote = LoteDatos("L-2026-10-26-01")
lote.agregar({"ticket": "T1", "importe": 23.50})
lote.agregar({"ticket": "T2", "importe": 8.75})
lote.agregar({"ticket": "T3", "importe": 112.00})

print(lote.id_lote)
print(lote.total_registros())
print(lote.importe_total())
print(LoteDatos.total_registros(lote))
