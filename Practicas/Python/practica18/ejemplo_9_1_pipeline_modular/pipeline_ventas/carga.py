"""Carga: almacena las ventas y ofrece consultas."""


class AlmacenVentas:
    def __init__(self):
        self._ventas = []

    def cargar(self, ventas):
        for venta in ventas:
            self._ventas.append(venta)

    def __len__(self):
        return len(self._ventas)

    def total_por_tienda(self):
        totales = {}
        for venta in self._ventas:
            totales[venta.tienda] = round(totales.get(venta.tienda, 0) + venta.importe, 2)
        return totales

    def top_productos(self, n):
        totales = {}
        for venta in self._ventas:
            totales[venta.producto] = round(totales.get(venta.producto, 0) + venta.importe, 2)
        return sorted(totales.items(), key=lambda par: par[1], reverse=True)[:n]
