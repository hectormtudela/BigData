import facturacion
from facturacion import Cliente, Factura

print("Versión del paquete:", facturacion.__version__)

hosteleria = Cliente("B12345678", "Hostelería Levante SL")
panaderia = Cliente("A87654321", "Panadería Ortiz", tipo_iva=0.10)

f1 = (Factura(hosteleria)
      .agregar_linea("Cafetera industrial", 2, 950.00)
      .agregar_linea("Molinillo", 1, 320.00)
      .agregar_linea("Mantenimiento anual", 1, 180.00))
f2 = Factura(panaderia).agregar_linea("Amasadora", 1, 640.00)

for factura in [f1, f2]:
    print(factura)

print(facturacion.__all__)
print(Factura.__module__)
