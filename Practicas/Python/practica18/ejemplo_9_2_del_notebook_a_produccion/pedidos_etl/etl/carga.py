"""Carga: guarda los pedidos procesados y genera el resumen."""

class ResumenVentas:
    def __init__(self):
        self._pedidos = []

    def cargar(self, pedidos):
        self._pedidos.extend(pedidos)

    def __len__(self):
        return len(self._pedidos)

    def por_ciudad(self):
        totales = {}
        for pedido in self._pedidos:
            totales[pedido.ciudad] = round(totales.get(pedido.ciudad, 0) + pedido.total_con_iva, 2)
        return dict(sorted(totales.items(), key=lambda par: par[1], reverse=True))
