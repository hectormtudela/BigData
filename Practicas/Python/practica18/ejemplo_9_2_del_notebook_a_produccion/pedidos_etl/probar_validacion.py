"""Sección 5: probar una pieza del pipeline por separado."""

from etl.transformacion import parsear, es_valido

print(es_valido(parsear("P010,Rosa Vidal,bilbao,19.95,entregado")))
print(es_valido(parsear("P009,Rosa Vidal,bilbao,9,95,entregado")))
print(es_valido(parsear("P011,Iván Paz,bilbao,,entregado")))
