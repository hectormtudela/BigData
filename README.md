# Práctica 3: Python — Héctor Miguel Tudela

## Descripción
Resolución de los 20 ejercicios de la Práctica 3 sobre listas, funciones y paquetes, NumPy, diccionarios y pandas, lógica y control de flujo, y bucles.

## Entorno
- Python 3.12
- JupyterLab
- NumPy
- pandas
- Dependencias en `requeriments.txt`

## Estructura del repositorio

| Carpeta | Contenido |
| --- | --- |
| `data/` | Ficheros CSV de partida |
| `notebooks/` | Notebook con la resolución |
| `src/` | Módulo de funciones auxiliares |
| `outputs/` | Ficheros generados durante la ejecución |

## Datos de partida

| Fichero | Filas | Descripción |
| --- | --- | --- |
| `ventas_retail.csv` | 420 | Pedidos de una cadena minorista (3 primeros trimestres de 2025) |
| `empleados.csv` | 180 | Plantilla de una empresa tecnológica |
| `sensores_planta.csv` | 600 | Telemetría de 4 máquinas de planta, muestreada cada 15 min |

Los tres ficheros están sin modificar en `data/`, tal como se entregaron.

## Contenido del notebook

El notebook `notebooks/practica3_python.ipynb` resuelve 20 ejercicios agrupados en:

1. **Listas** (ej. 1-4): slicing, listas anidadas, copias vs. referencias, colas.
2. **Funciones y paquetes** (ej. 5-7): funciones propias, módulo `src/utilidades.py`, NumPy y pandas.
3. **NumPy** (ej. 8-11): vectorización, máscaras booleanas, arrays 2D, estadística descriptiva.
4. **Diccionarios y pandas** (ej. 12-15): diccionarios anidados, `DataFrame`, `groupby`, exportación a CSV.
5. **Lógica y control de flujo** (ej. 16-18): operadores booleanos, `if/elif/else`, filtrado avanzado.
6. **Bucles** (ej. 19-20): `while`, `for`, `enumerate`, iteración sobre `DataFrame`.

## Cómo reproducir

1. Crear el entorno virtual:

```bash
python3.12 -m venv .venv
```

2. Activarlo:

En Linux / macOS:

```bash
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

3. Instalar las dependencias y abrir el notebook:

```bash
python -m pip install -r requeriments.txt
jupyter lab notebooks/practica3_python.ipynb
```

