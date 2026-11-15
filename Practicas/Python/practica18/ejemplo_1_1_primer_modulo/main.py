import tarifas

pedidos = [("A-101", 2.0, False), ("A-102", 7.5, True), ("A-103", 0.5, False)]
for codigo, peso, urgente in pedidos:
    print(f"{codigo}: {tarifas.coste_envio(peso, urgente)} €")

print("Tarifa base:", tarifas.TARIFA_BASE)
