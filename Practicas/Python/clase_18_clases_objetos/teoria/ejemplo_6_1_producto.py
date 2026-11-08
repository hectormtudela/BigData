# Ejemplo 6.1 · Producto de un catálogo
# clase_18_clases_objetos/teoria/ejemplo_6_1_producto.py

class Producto:
    def __init__(self, sku, nombre, precio):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} ({self.sku}) - {self.precio:.2f} €"

    def __repr__(self):
        return f"Producto(sku='{self.sku}', nombre='{self.nombre}', precio={self.precio})"

p = Producto("SKU-4471", "Auriculares BT", 59.9)

print(p)
print(str(p))
print(repr(p))
print(f"Producto destacado: {p}")

catalogo = [p, Producto("SKU-1020", "Cargador USB-C", 19.95)]
print(catalogo)
