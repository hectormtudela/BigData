"""Punto de entrada del pipeline de ventas."""

from pipeline_ventas import ejecutar_pipeline

DATOS = """tienda,producto,unidades,precio
madrid, Café Molido ,3,4.50
barcelona,té verde,2,3.20
madrid,café molido,1,4.50
valencia,cacao,dos,2.80
barcelona,Café Molido,4,4.50
sevilla,té verde,,3.20
valencia,cacao,5,2.80
"""

def main():
    almacen = ejecutar_pipeline(DATOS)
    print("Ventas cargadas:", len(almacen))
    print("Total por tienda:", almacen.total_por_tienda())
    print("Top 2 productos:", almacen.top_productos(2))

if __name__ == "__main__":
    main()
