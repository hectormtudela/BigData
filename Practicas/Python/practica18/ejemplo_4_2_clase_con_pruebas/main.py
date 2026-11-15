from conversor import ConversorDivisas

tasas_hoy = {"USD": 1.08, "GBP": 0.86, "JPY": 162.5}
conversor = ConversorDivisas(tasas_hoy)

facturas = [("F-01", 1200.0), ("F-02", 349.9), ("F-03", 75.0)]

print("100 € equivalen a:", conversor.tabla(100))

en_usd = conversor.convertir_lote([importe for _, importe in facturas], "USD")
print("Facturas en USD:", en_usd)

grandes_gbp = {numero: conversor.convertir(importe, "GBP")
               for numero, importe in facturas if importe > 100}
print("Mayores de 100 € en GBP:", grandes_gbp)

numeros = [numero for numero, _ in facturas]
superan_300_usd = list(filter(lambda par: par[1] > 300, zip(numeros, en_usd)))
print("Superan 300 USD:", superan_300_usd)
