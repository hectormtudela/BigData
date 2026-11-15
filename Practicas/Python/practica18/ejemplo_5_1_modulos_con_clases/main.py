from modelos import Producto, ProductoPerecedero
from inventario import Inventario

almacen = Inventario()
almacen.agregar(Producto("SKU-01", "Aceite 1L", 6.40, 120))
almacen.agregar(ProductoPerecedero("SKU-02", "Yogur pack 4", 2.20, 15, dias_para_caducar=2))
almacen.agregar(Producto("SKU-03", "Arroz 1kg", 1.35, 8))
almacen.agregar(ProductoPerecedero("SKU-04", "Queso curado", 9.90, 30, dias_para_caducar=40))

print("Productos en almacén:", len(almacen))
for p in almacen:
    print(f"  {p.nombre:<14} precio venta: {p.precio_venta():>5}")

print("Bajo stock (<20):", almacen.bajo_stock(20))
print("Valor total:", almacen.valor_total())
print("Por valor:", [p.sku for p in almacen.ordenar_por("valor", descendente=True)])

try:
    almacen.agregar("Leche")
except TypeError as error:
    print("TypeError:", error)
