# Ejemplo 4.3 · Métodos que llaman a otros métodos
# clase_18_clases_objetos/teoria/ejemplo_4_3_factura.py

class Factura:
    def __init__(self, numero, cliente, tipo_iva=0.21):
        self.numero = numero
        self.cliente = cliente
        self.tipo_iva = tipo_iva
        self.lineas = []

    def agregar_linea(self, concepto, cantidad, precio_unitario):
        self.lineas.append({"concepto": concepto, "cantidad": cantidad, "precio": precio_unitario})

    def subtotal(self):
        return round(sum([linea["cantidad"] * linea["precio"] for linea in self.lineas]), 2)

    def impuestos(self):
        return round(self.subtotal() * self.tipo_iva, 2)

    def total(self):
        return round(self.subtotal() + self.impuestos(), 2)

    def imprimir(self):
        print(f"Factura {self.numero} · Cliente: {self.cliente}")
        for linea in self.lineas:
            importe = linea["cantidad"] * linea["precio"]
            print(f"  {linea['concepto']:<22} {linea['cantidad']:>3} x {linea['precio']:>8.2f} = {importe:>9.2f}")
        print(f"  {'Subtotal':<38} {self.subtotal():>9.2f}")
        print(f"  {'IVA ' + str(int(self.tipo_iva * 100)) + '%':<38} {self.impuestos():>9.2f}")
        print(f"  {'TOTAL':<38} {self.total():>9.2f}")

factura = Factura("F-2026-0412", "Logística Iberia S.L.")
factura.agregar_linea("Licencia ETL (usuario)", 3, 49.90)
factura.agregar_linea("Soporte anual", 1, 1200.00)
factura.agregar_linea("Formación (jornada)", 2, 350.00)
factura.imprimir()
