"""Conversión de importes en euros a otras divisas."""


class ConversorDivisas:
    def __init__(self, tasas):
        self.tasas = tasas

    def convertir(self, importe_eur, divisa):
        return round(importe_eur * self.tasas[divisa], 2)

    def convertir_lote(self, importes_eur, divisa):
        return [self.convertir(importe, divisa) for importe in importes_eur]

    def tabla(self, importe_eur):
        return {divisa: self.convertir(importe_eur, divisa) for divisa in self.tasas}


if __name__ == "__main__":
    prueba = ConversorDivisas({"USD": 1.10, "GBP": 0.85})
    print("Prueba convertir:", prueba.convertir(100, "USD") == 110.0)
    print("Prueba lote:     ", prueba.convertir_lote([10, 20], "GBP") == [8.5, 17.0])
    print("Prueba tabla:    ", prueba.tabla(100) == {"USD": 110.0, "GBP": 85.0})
