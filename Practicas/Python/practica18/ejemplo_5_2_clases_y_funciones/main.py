from tarificador import Tarificador
from politicas_precio import POLITICAS, crear_descuento

catalogo = {"Zapatillas": 89.90, "Mochila": 45.00, "Gorra": 19.50}

caja = Tarificador()
print("Normal:      ", caja.tarifar(catalogo))

caja.cambiar_politica("black_friday")
print("Black Friday:", caja.tarifar(catalogo))

caja.cambiar_politica("outlet")
print("Outlet:      ", caja.tarifar(catalogo))

caja.politica = crear_descuento(10)               # política creada al momento
print("Socios -10%: ", caja.tarifar(catalogo))

print("Políticas disponibles:", list(POLITICAS))
