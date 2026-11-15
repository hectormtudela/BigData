# Ejemplo 3.3 · Asignación compuesta, `in` y `len()` en un lote de tickets
# clase_19_detalles_clases_objetos/teoria/ejemplo_3_3_lote_operadores.py

class LoteTickets:
    def __init__(self, tienda):
        self.tienda = tienda
        self.__tickets = []

    def __iadd__(self, ticket):
        self.__tickets.append(ticket)
        return self

    def __len__(self):
        return len(self.__tickets)

    def __contains__(self, id_ticket):
        return id_ticket in [t["id"] for t in self.__tickets]

    def __str__(self):
        return f"Lote {self.tienda}: {len(self)} tickets"

lote = LoteTickets("T-07")
print(lote)

lote += {"id": "A-100", "importe": 23.5}
lote += {"id": "A-101", "importe": 8.75}
lote += {"id": "A-102", "importe": 112.0}

print(lote)
print(len(lote))
print("A-101" in lote)
print("Z-999" in lote)
print("Z-999" not in lote)
