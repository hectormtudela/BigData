r"""
Práctica 16 · Clase 21 · Ejercicio propuesto P3 (Pipelines ETL)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

# Ejercicio propuesto P3. Análisis de ejecuciones de pipelines de datos

> 📖
### Enunciado

Un equipo de ingeniería de datos registra la duración, el volumen procesado y el resultado de las ejecuciones de varios pipelines ETL. El objetivo es elaborar un pequeño informe con las ejecuciones correctas, los datos procesados y el consumo de tiempo de ejecución.

Desarrolla el procesamiento utilizando **`lambda`****, ****`filter()`****, ****`map()`****, ****`reduce()`**** y ****`sorted()`**, evitando modificar los registros originales.

### Datos iniciales

```python
ejecuciones = [
    {"pipeline": "ventas", "duracion_min": 18, "registros": 12000, "estado": "ok"},
    {"pipeline": "clientes", "duracion_min": 32, "registros": 8000, "estado": "ok"},
    {"pipeline": "inventario", "duracion_min": 12, "registros": 0, "estado": "error"},
    {"pipeline": "facturas", "duracion_min": 45, "registros": 15000, "estado": "ok"},
    {"pipeline": "devoluciones", "duracion_min": 26, "registros": 4000, "estado": "ok"},
    {"pipeline": "proveedores", "duracion_min": 15, "registros": 0, "estado": "error"},
]
```

### Actividades

44. **Filtrado de ejecuciones exitosas**. Usa `filter()` y una función `lambda` para obtener únicamente los registros cuyo `estado` sea `"ok"`.
45. **Detección de ejecuciones lentas**. A partir de las ejecuciones exitosas, crea otra lista con aquellas cuya duración sea **superior a 25 minutos**.
46. **Transformación de datos**. Utiliza `map()` y `lambda` para crear una nueva lista de diccionarios con estos campos:
- `pipeline`: nombre del pipeline.
- `duracion_min`: duración original.
- `duracion_seg`: duración convertida a segundos.
- `registros`: número de registros procesados.
47. **Total de registros procesados**. Utiliza `reduce()` con valor inicial `0` para sumar los registros de todas las ejecuciones exitosas.
48. **Tiempo total de procesamiento**. Utiliza otra llamada a `reduce()` para sumar la duración, en minutos, de las ejecuciones exitosas.
49. **Ordenación**. Ordena los pipelines exitosos de **mayor a menor duración** mediante `sorted()` y una función `lambda` aplicada al parámetro `key`.
50. **Informe final**. Muestra el número de ejecuciones exitosas, los pipelines lentos, la lista transformada, el total de registros, el tiempo acumulado y los nombres de los pipelines ordenados por duración.
### Requisitos

- Utiliza **al menos dos llamadas a ****`filter()`**, una a `map()`, dos a `reduce()` y una a `sorted()`.
- Emplea funciones `lambda` en las operaciones anteriores.
- Usa `list()` para materializar los resultados que corresponda.
- No utilices bibliotecas externas como `pandas` o `numpy`.
- No modifiques la lista original `ejecuciones`.
### Comprobaciones

Al ejecutar el programa, verifica que:

- Existen **4 ejecuciones exitosas**.
- Los pipelines lentos son **`clientes`****, ****`facturas`**** y ****`devoluciones`**.
- Se procesaron **39 000 registros** en las ejecuciones exitosas.
- El tiempo total de estas ejecuciones es **121 minutos**.
- El orden de mayor a menor duración es: **`facturas`****, ****`clientes`****, ****`devoluciones`****, ****`ventas`**.
---
"""

from functools import reduce

UMBRAL_LENTO_MIN = 25


def main():
    ejecuciones = [
        {"pipeline": "ventas", "duracion_min": 18, "registros": 12000, "estado": "ok"},
        {"pipeline": "clientes", "duracion_min": 32, "registros": 8000, "estado": "ok"},
        {"pipeline": "inventario", "duracion_min": 12, "registros": 0, "estado": "error"},
        {"pipeline": "facturas", "duracion_min": 45, "registros": 15000, "estado": "ok"},
        {"pipeline": "devoluciones", "duracion_min": 26, "registros": 4000, "estado": "ok"},
        {"pipeline": "proveedores", "duracion_min": 15, "registros": 0, "estado": "error"},
    ]
    copia_original = [dict(ejecucion) for ejecucion in ejecuciones]

    exitosas = list(filter(lambda e: e["estado"] == "ok", ejecuciones))

    lentas = list(filter(lambda e: e["duracion_min"] > UMBRAL_LENTO_MIN, exitosas))

    transformadas = list(map(
        lambda e: {
            "pipeline": e["pipeline"],
            "duracion_min": e["duracion_min"],
            "duracion_seg": e["duracion_min"] * 60,
            "registros": e["registros"],
        },
        exitosas,
    ))

    total_registros = reduce(lambda acc, e: acc + e["registros"], exitosas, 0)

    total_minutos = reduce(lambda acc, e: acc + e["duracion_min"], exitosas, 0)

    ordenadas = sorted(exitosas, key=lambda e: e["duracion_min"], reverse=True)

    print("===== INFORME DE PIPELINES ETL =====\n")
    print(f"Ejecuciones exitosas: {len(exitosas)}")
    print(f"Pipelines lentos (> {UMBRAL_LENTO_MIN} min): "
          f"{[e['pipeline'] for e in lentas]}")

    print("\nLista transformada:")
    for ejecucion in transformadas:
        print(f"  {ejecucion}")

    print(f"\nTotal de registros procesados: {total_registros:,}".replace(",", " "))
    print(f"Tiempo acumulado: {total_minutos} minutos")
    print(f"Orden por duración (mayor a menor): "
          f"{[e['pipeline'] for e in ordenadas]}")

    print("\n--- Comprobaciones ---")
    print(f"4 ejecuciones exitosas: {len(exitosas) == 4}")
    print(f"Lentos = clientes, facturas, devoluciones: "
          f"{[e['pipeline'] for e in lentas] == ['clientes', 'facturas', 'devoluciones']}")
    print(f"39 000 registros: {total_registros == 39000}")
    print(f"121 minutos: {total_minutos == 121}")
    print(f"Orden correcto: "
          f"{[e['pipeline'] for e in ordenadas] == ['facturas', 'clientes', 'devoluciones', 'ventas']}")
    print(f"Lista original sin cambios: {ejecuciones == copia_original}")


if __name__ == "__main__":
    main()
