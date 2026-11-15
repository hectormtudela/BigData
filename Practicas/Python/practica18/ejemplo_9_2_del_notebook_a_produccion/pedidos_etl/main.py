"""Punto de entrada del pipeline de pedidos."""

from etl import ejecutar_pipeline

DATOS = """id,cliente,ciudad,importe,estado
P001, Ana López ,madrid,45.50,entregado
P002,Luis Pérez,Sevilla,12.00,cancelado
P003,Marta Ruiz,MADRID,30.25,entregado
P004,Jorge Gil,valencia,,entregado
P005,Elena Sanz,sevilla,80.00,entregado
P006,Pablo Ríos,Valencia,22.40,en reparto
P007,Sara Mora,madrid,abc,entregado"""

def mostrar_informe(resultado):
    print("Pedidos leídos:", resultado["leidos"])
    print("Rechazados por datos erróneos:", resultado["rechazados"])
    print("Pedidos cancelados:", resultado["cancelados"])
    print("Pedidos procesados:", len(resultado["resumen"]))
    print("Ventas con IVA por ciudad:")
    for ciudad, total in resultado["resumen"].por_ciudad().items():
        print(f"  {ciudad:<9}{total:>8.2f} €")

def main():
    resultado = ejecutar_pipeline(DATOS)
    mostrar_informe(resultado)

if __name__ == "__main__":
    main()
