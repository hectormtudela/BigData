r"""
Práctica 16 · Clase 21 · Ejercicio propuesto P2 (Pedidos)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

# Ejercicio propuesto P2. Procesamiento de pedidos de una tienda online

### Enunciado

> 📖 Una tienda online almacena los pedidos recibidos durante una jornada en una lista de diccionarios. El departamento de análisis necesita seleccionar los pedidos completados, calcular su importe con impuestos y obtener el total de facturación correspondiente.
Desarrolla un programa en Python utilizando **funciones ****`lambda`**** y las funciones de orden superior ****`filter()`****, ****`map()`**** y ****`reduce()`**.

### Datos iniciales

```python
pedidos = [
    {"pedido_id": "P001", "cliente": "Ana", "importe": 120.0, "estado": "completado"},
    {"pedido_id": "P002", "cliente": "Luis", "importe": 80.0, "estado": "pendiente"},
    {"pedido_id": "P003", "cliente": "Marta", "importe": 250.0, "estado": "completado"},
    {"pedido_id": "P004", "cliente": "Pedro", "importe": 60.0, "estado": "cancelado"},
    {"pedido_id": "P005", "cliente": "Lucía", "importe": 150.0, "estado": "completado"},
]
```

### Actividades

39. **Filtrado con ****`filter()`**. Obtén una nueva lista que contenga únicamente los pedidos cuyo `estado` sea `"completado"`. Utiliza una función `lambda` como criterio de selección.
40. **Transformación con ****`map()`**. A partir de los pedidos completados, genera una nueva lista de diccionarios con los campos `pedido_id`, `cliente` e `importe_final`. El `importe_final` será el importe original más un **21 % de IVA**. Redondea el resultado a dos decimales. No modifiques los diccionarios originales.
41. **Acumulación con ****`reduce()`**. Calcula la suma de todos los `importe_final` de los pedidos completados. Usa un acumulador inicial de `0`.
42. **Función ****`lambda`**** independiente**. Define una función `lambda` que reciba un importe y devuelva `"Alto"` si es mayor o igual a 200 €, y `"Normal"` en caso contrario. Aplícala a los importes finales mediante `map()` para generar una lista de clasificaciones.
43. **Presentación**. Muestra los pedidos completados, los pedidos transformados, las clasificaciones y la facturación total.
### Requisitos

- Utiliza `lambda` al menos en las operaciones de filtrado, transformación y clasificación.
- Utiliza obligatoriamente `filter()`, `map()` y `reduce()`.
- Importa `reduce` desde `functools`.
- Convierte a lista los resultados de `filter()` y `map()` cuando necesites mostrarlos o reutilizarlos.
- Mantén sin cambios la lista original `pedidos`.
### Comprobaciones

Al ejecutar el programa, verifica que:

- Se seleccionan **3 pedidos completados**.
- Los importes finales son **145.20 €, 302.50 € y 181.50 €**, en el mismo orden que los pedidos originales.
- La facturación total con IVA es **629.20 €**.
- Las clasificaciones son **`["Normal", "Alto", "Normal"]`**.
---
"""

from functools import reduce

IVA = 0.21


def main():
    pedidos = [
        {"pedido_id": "P001", "cliente": "Ana", "importe": 120.0, "estado": "completado"},
        {"pedido_id": "P002", "cliente": "Luis", "importe": 80.0, "estado": "pendiente"},
        {"pedido_id": "P003", "cliente": "Marta", "importe": 250.0, "estado": "completado"},
        {"pedido_id": "P004", "cliente": "Pedro", "importe": 60.0, "estado": "cancelado"},
        {"pedido_id": "P005", "cliente": "Lucía", "importe": 150.0, "estado": "completado"},
    ]
    copia_original = [dict(pedido) for pedido in pedidos]

    completados = list(filter(lambda p: p["estado"] == "completado", pedidos))

    pedidos_con_iva = list(map(
        lambda p: {
            "pedido_id": p["pedido_id"],
            "cliente": p["cliente"],
            "importe_final": round(p["importe"] * (1 + IVA), 2),
        },
        completados,
    ))

    facturacion_total = reduce(
        lambda acumulado, pedido: acumulado + pedido["importe_final"],
        pedidos_con_iva,
        0,
    )

    clasificar_importe = lambda importe: "Alto" if importe >= 200 else "Normal"
    importes_finales = list(map(lambda p: p["importe_final"], pedidos_con_iva))
    clasificaciones = list(map(clasificar_importe, importes_finales))

    print("Pedidos completados:")
    for pedido in completados:
        print(f"  {pedido}")

    print("\nPedidos transformados (con IVA):")
    for pedido in pedidos_con_iva:
        print(f"  {pedido['pedido_id']} - {pedido['cliente']}: "
              f"{pedido['importe_final']:.2f} €")

    print(f"\nClasificaciones: {clasificaciones}")
    print(f"\nFacturación total con IVA: {facturacion_total:.2f} €")

    print("\n--- Comprobaciones ---")
    print(f"3 pedidos completados: {len(completados) == 3}")
    print(f"Importes finales correctos: "
          f"{importes_finales == [145.20, 302.50, 181.50]}")
    print(f"Facturación total = 629.20 €: {round(facturacion_total, 2) == 629.20}")
    print(f"Clasificaciones correctas: "
          f"{clasificaciones == ['Normal', 'Alto', 'Normal']}")
    print(f"Lista original sin cambios: {pedidos == copia_original}")


if __name__ == "__main__":
    main()
