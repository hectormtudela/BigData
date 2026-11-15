import math
import statistics
from collections import Counter
from datetime import date, timedelta
from functools import partial

tickets = [("café", 1.40), ("tostada", 2.10), ("café", 1.40), ("zumo", 2.80),
           ("café", 1.40), ("tostada", 2.10), ("croissant", 1.80)]

# collections: contar sin escribir el bucle
mas_vendidos = Counter(producto for producto, _ in tickets)
print("Más vendidos:", mas_vendidos.most_common(2))

# statistics: medidas estadísticas
importes = [precio for _, precio in tickets]
print("Ticket medio:", round(statistics.mean(importes), 2),
      "| mediana:", statistics.median(importes))

# math: funciones matemáticas
consumo_kg, saco_kg = 7.3, 2
print("Sacos de café a pedir:", math.ceil(consumo_kg / saco_kg))

# datetime: fechas
ultimo_pedido = date(2026, 11, 10)
proximo_pedido = ultimo_pedido + timedelta(days=7)
print("Próximo pedido:", proximo_pedido.isoformat())

# functools: fijar argumentos de una función ya existente
def con_iva(importe, tipo):
    return round(importe * (1 + tipo), 2)

con_iva_hosteleria = partial(con_iva, tipo=0.10)
print("Con IVA del 10 %:", list(map(con_iva_hosteleria, [1.40, 2.10, 2.80])))
