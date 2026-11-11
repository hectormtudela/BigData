r"""
Práctica 16 · Clase 20 · Ejercicio P4 (Polimorfismo)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

# Ejercicio P4: Polimorfismo en un sistema de procesamiento de datos

> 📖
## 📌 Enunciado

Una empresa de Ingeniería de Datos necesita desarrollar una aplicación que permita procesar archivos procedentes de diferentes fuentes.

Actualmente, la empresa trabaja con tres formatos de archivos: **CSV, JSON y TXT**.

Cada tipo de archivo requiere un procesamiento diferente, pero todos deben permitir ejecutar una misma acción: `procesar()`.

Debes desarrollar una solución utilizando **programación orientada a objetos, herencia simple y polimorfismo**, sin utilizar `super()` ni herencia múltiple.

## Parte A. Crear la superclase

Crea una clase llamada `ArchivoDatos` que contenga los siguientes atributos:

| Atributo | Descripción |
| --- | --- |
| `nombre` | Nombre del archivo. |
| `tamano` | Tamaño del archivo en MB. |

La clase debe implementar estos métodos:

- `mostrar_informacion()`: muestra el nombre y el tamaño del archivo.
- `procesar()`: muestra el mensaje `"Procesamiento genérico de archivo"`.
## Parte B. Crear las subclases

Crea tres clases hijas que hereden de `ArchivoDatos`.

Cada clase debe sobrescribir el método `procesar()` para mostrar un comportamiento diferente.

| Subclase | Comportamiento de `procesar()` |
| --- | --- |
| `ArchivoCSV` | Lee registros separados por comas y los transforma en filas. |
| `ArchivoJSON` | Interpreta objetos JSON y extrae sus propiedades. |
| `ArchivoTXT` | Lee las líneas de texto y realiza una limpieza básica. |

Cada clase hija debe utilizar los atributos heredados `nombre` y `tamano`.

## Parte C. Crear los objetos

Crea los siguientes objetos:

```python
archivo1 = ArchivoCSV("ventas.csv", 15)
archivo2 = ArchivoJSON("sensores.json", 8)
archivo3 = ArchivoTXT("logs.txt", 25)
```

## Parte D. Aplicar polimorfismo

Crea una función llamada `ejecutar_procesamiento()` que reciba un objeto de cualquiera de las tres subclases.

La función debe ejecutar los métodos:

```python
archivo.mostrar_informacion()
archivo.procesar()
```

**Importante:** La función no debe utilizar `if`, `elif`, `isinstance()` ni `type()` para determinar qué clase de archivo está procesando.

## Parte E. Procesar múltiples archivos

Crea una lista que contenga los tres objetos anteriores.

Recorre la lista utilizando un bucle `for` y llama a la función `ejecutar_procesamiento()` para cada objeto.

### Salida esperada

```plain text
Nombre: ventas.csv
Tamaño: 15 MB
Procesando archivo CSV: ventas.csv
Leyendo registros separados por comas...

Nombre: sensores.json
Tamaño: 8 MB
Procesando archivo JSON: sensores.json
Extrayendo propiedades de los objetos JSON...

Nombre: logs.txt
Tamaño: 25 MB
Procesando archivo TXT: logs.txt
Leyendo líneas y realizando limpieza básica...
```

## Parte F. Ampliación del sistema

La empresa comienza a recibir archivos de un nuevo formato: **XML**.

Debes incorporar una nueva clase llamada `ArchivoXML` que herede de `ArchivoDatos`.

Esta clase debe sobrescribir `procesar()` para mostrar:

```plain text
Procesando archivo XML: configuracion.xml
Analizando etiquetas y atributos XML...
```

Crea un objeto `ArchivoXML`, añádelo a la lista anterior y comprueba que puede procesarse correctamente.

**Condición importante:** No puedes modificar la función `ejecutar_procesamiento()` para incorporar el nuevo formato.

## Preguntas 

20. ¿Qué métodos heredan las clases hijas de `ArchivoDatos`?
21. ¿Por qué las subclases sobrescriben el método `procesar()`?
22. ¿Dónde se aplica exactamente el polimorfismo en este ejercicio?
23. ¿Por qué no necesitamos utilizar `if` o `elif` para identificar cada tipo de archivo?
24. ¿Qué ventaja ofrece el polimorfismo cuando incorporamos la clase `ArchivoXML`?
---

> **Restricciones del ejercicio:** se permite herencia simple, sobrescritura de métodos, listas de objetos y funciones que reciben objetos como argumentos. No se permite utilizar `super()`, herencia múltiple ni estructuras condicionales para seleccionar el comportamiento de cada subclase.

**Nota:** No es necesario leer archivos reales del disco. El procesamiento se simulará mostrando los mensajes correspondientes mediante `print()`.
"""

# Restricciones de este ejercicio: SIN super(), SIN herencia múltiple y
# SIN if/elif/isinstance/type para elegir el comportamiento.


# Parte A: superclase
class ArchivoDatos:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano  # en MB

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tamaño: {self.tamano} MB")

    def procesar(self):
        print("Procesamiento genérico de archivo")


# Parte B: subclases. No definen __init__: heredan el de ArchivoDatos,
# por eso no necesitamos super() y usan self.nombre y self.tamano.
class ArchivoCSV(ArchivoDatos):
    def procesar(self):
        print(f"Procesando archivo CSV: {self.nombre}")
        print("Leyendo registros separados por comas...")


class ArchivoJSON(ArchivoDatos):
    def procesar(self):
        print(f"Procesando archivo JSON: {self.nombre}")
        print("Extrayendo propiedades de los objetos JSON...")


class ArchivoTXT(ArchivoDatos):
    def procesar(self):
        print(f"Procesando archivo TXT: {self.nombre}")
        print("Leyendo líneas y realizando limpieza básica...")


# Parte D: función polimórfica. Recibe cualquier objeto con estos métodos.
def ejecutar_procesamiento(archivo):
    archivo.mostrar_informacion()
    archivo.procesar()


# Parte F: nueva clase XML. Se añade SIN tocar ejecutar_procesamiento().
class ArchivoXML(ArchivoDatos):
    def procesar(self):
        print(f"Procesando archivo XML: {self.nombre}")
        print("Analizando etiquetas y atributos XML...")


def main():
    # Parte C: objetos
    archivo1 = ArchivoCSV("ventas.csv", 15)
    archivo2 = ArchivoJSON("sensores.json", 8)
    archivo3 = ArchivoTXT("logs.txt", 25)

    # Parte E: lista y bucle
    archivos = [archivo1, archivo2, archivo3]
    for archivo in archivos:
        ejecutar_procesamiento(archivo)
        print()

    # Parte F: ampliación con XML
    print("--- Llega un nuevo formato: XML ---\n")
    archivo4 = ArchivoXML("configuracion.xml", 5)
    archivos.append(archivo4)
    ejecutar_procesamiento(archivo4)
    print()

    # Comprobación: la lista completa sigue funcionando con la misma función
    print("--- Procesando de nuevo TODA la lista (4 archivos) ---\n")
    for archivo in archivos:
        ejecutar_procesamiento(archivo)
        print()


if __name__ == "__main__":
    main()


# ===========================================================================
# RESPUESTAS A LAS PREGUNTAS
# ===========================================================================
# 20. ¿Qué métodos heredan las clases hijas de ArchivoDatos?
#     Heredan el constructor __init__ (y con él los atributos nombre y
#     tamano), mostrar_informacion() y procesar(). Este último lo heredan,
#     pero lo sobrescriben con su propia versión.
#
# 21. ¿Por qué las subclases sobrescriben procesar()?
#     Porque cada formato se procesa de forma distinta. La versión genérica
#     de la superclase solo sirve como comportamiento por defecto; cada
#     subclase la reemplaza con su lógica (mismo nombre, distinto cuerpo).
#
# 22. ¿Dónde se aplica exactamente el polimorfismo?
#     En la línea archivo.procesar() dentro de ejecutar_procesamiento().
#     La llamada es siempre la misma, pero Python ejecuta la versión de la
#     clase real del objeto (CSV, JSON, TXT o XML) en tiempo de ejecución.
#
# 23. ¿Por qué no necesitamos if o elif para identificar cada tipo?
#     Porque es el propio objeto quien sabe cómo procesarse. Python decide
#     qué versión del método ejecutar según la clase del objeto (enlace
#     dinámico), así que la función no tiene que preguntar de qué tipo es.
#
# 24. ¿Qué ventaja ofrece al incorporar ArchivoXML?
#     Basta con crear la nueva clase y añadir el objeto a la lista: no hay
#     que modificar ejecutar_procesamiento() ni el bucle. El sistema queda
#     abierto a ampliaciones y cerrado a modificaciones (principio
#     Open/Closed), con menos riesgo de introducir errores.
