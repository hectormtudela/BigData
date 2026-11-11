r"""
Práctica 16 · Clase 20 · Ejercicio 2 (Duck typing)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

> 📖 Ejercicio 2. Crea 2 ejemplos de polimorfismo mediante ***duck typing***** .**
"""

import json

# ---------------------------------------------------------------------------
# Duck typing: "si camina como un pato y hace cuac como un pato, es un pato".
# A Python no le importa de qué CLASE es el objeto, sino si TIENE el método
# que le pedimos. Por eso aquí NO hay herencia ni superclase común.
# ---------------------------------------------------------------------------


# ===========================================================================
# EJEMPLO 1: exportadores de datos (todos tienen el método guardar())
# ===========================================================================
class ExportadorCSV:
    def guardar(self, datos):
        fila = ",".join(str(valor) for valor in datos.values())
        print(f"[CSV]  Guardando fila: {fila}")


class ExportadorJSON:
    def guardar(self, datos):
        texto = json.dumps(datos, ensure_ascii=False)
        print(f"[JSON] Guardando objeto: {texto}")


class BaseDatos:
    def guardar(self, datos):
        columnas = ", ".join(datos.keys())
        valores = ", ".join(repr(valor) for valor in datos.values())
        print(f"[SQL]  INSERT INTO clientes ({columnas}) VALUES ({valores});")


def exportar(destino, datos):
    """Funciona con CUALQUIER objeto que tenga un método guardar()."""
    destino.guardar(datos)


# ===========================================================================
# EJEMPLO 2: fuentes de lectura (todas tienen el método leer())
# ===========================================================================
class SensorReal:
    def __init__(self, nombre, lectura_fija):
        self.nombre = nombre
        self.lectura_fija = lectura_fija

    def leer(self):
        return self.lectura_fija


class SimuladorSensor:
    """Simula un sensor devolviendo valores de una secuencia, de forma cíclica."""

    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.posicion = 0

    def leer(self):
        valor = self.secuencia[self.posicion % len(self.secuencia)]
        self.posicion += 1
        return valor


class ArchivoLecturas:
    """Fuente que lee de una lista (simula un fichero ya cargado)."""

    def __init__(self, lecturas):
        self.lecturas = lecturas

    def leer(self):
        return self.lecturas[-1]  # devuelve la última lectura registrada


def calcular_media(fuentes):
    """Pide leer() a cada fuente sin saber de qué clase es."""
    lecturas = [fuente.leer() for fuente in fuentes]
    print(f"Lecturas obtenidas: {lecturas}")
    return sum(lecturas) / len(lecturas)


class Objeto:
    """Clase SIN método guardar() ni leer(): romperá el duck typing."""


def main():
    print("=== EJEMPLO 1: exportadores (método guardar) ===")
    cliente = {"id": 1, "nombre": "Ana", "ciudad": "Madrid"}
    for destino in [ExportadorCSV(), ExportadorJSON(), BaseDatos()]:
        exportar(destino, cliente)

    print("\n=== EJEMPLO 2: fuentes de lectura (método leer) ===")
    fuentes = [
        SensorReal("Temp. parcela A", 24.5),
        SimuladorSensor([21.0, 23.0, 25.0]),
        ArchivoLecturas([20.0, 22.0, 26.5]),
    ]
    media = calcular_media(fuentes)
    print(f"Media de las lecturas: {media:.2f}")

    print("\n=== Qué pasa si el objeto NO tiene el método ===")
    try:
        exportar(Objeto(), cliente)
    except AttributeError as error:
        print(f"AttributeError: {error}")


if __name__ == "__main__":
    main()
