r"""
Práctica 16 · Clase 21 · Ejercicio propuesto P1 (Envíos)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

# Ejercicio Propuesto P1: **Sistema de análisis de envíos logísticos**

## Enunciado

> 📖 Una empresa de logística recibe diariamente pedidos de envío. Cada pedido tiene un identificador, un destino y un peso, pero **el coste de transporte depende del tipo de envío**.
El equipo de Ingeniería de Datos quiere analizar estos pedidos sin modificar los registros originales. Para ello, debes construir un programa que combine:

- **Programación orientada a objetos:** para representar los envíos.
- **Herencia y polimorfismo:** para calcular sus costes según el tipo.
- **Comprehensions:** para filtrar y transformar colecciones de objetos.
- **Programación funcional:** para pasar funciones como argumentos y crear funciones que devuelvan otras funciones.
El resultado será un pequeño informe con los envíos caros, los tipos de envío disponibles y los importes finales tras aplicar un descuento.

## Reglas del negocio

Todos los envíos incluyen los siguientes datos:

| Atributo | Descripción |
| --- | --- |
| `envio_id` | Identificador único, por ejemplo `E01` |
| `destino` | Ciudad de destino |
| `peso` | Peso del paquete en kilogramos |

Hay tres modalidades, con las siguientes tarifas:

| Tipo de envío | Regla para calcular el coste (€) |
| --- | --- |
| Nacional | `peso * 2 + 3` |
| Internacional | `peso * 2 + 15` |
| Urgente | `(peso * 2) * 1.5` |

> **Importante:** Las tarifas son ficticias y se utilizan únicamente con fines educativos. Los importes se expresan en euros.

## Parte A. Crear la jerarquía de clases

### A.1. Superclase `Envio`

Implementa una clase `Envio` que:

25. Reciba `envio_id`, `destino` y `peso` en su constructor.
26. Almacene esos datos como atributos de instancia.
27. Implemente `calcular_coste()` con la tarifa base `peso * 2`.
28. Implemente `mostrar_informacion()`, que devuelva un **string** con el identificador, el destino y el peso.
### A.2. Subclases

Crea tres clases hijas de `Envio`:

- `EnvioNacional`
- `EnvioInternacional`
- `EnvioUrgente`
Cada subclase debe sobrescribir `calcular_coste()` para aplicar su tarifa. **Usa ****`super().calcular_coste()`** para obtener el coste base, sin repetir el cálculo `peso * 2`.

No es necesario añadir atributos nuevos a estas subclases ni redefinir sus constructores.

![Imagen](images/practica-16-oop-y-programacion-funcional/image-002.png)

## Parte B. Crear objetos y aplicar polimorfismo

Una vez implementadas las clases, crea **exactamente estos siete objetos**, en el orden indicado:

```python
# Ejecuta este bloque después de definir las cuatro clases.
envios = [
    EnvioNacional("E01", "Madrid", 2),
    EnvioInternacional("E02", "París", 3),
    EnvioUrgente("E03", "Sevilla", 4),
    EnvioNacional("E04", "Valencia", 5),
    EnvioInternacional("E05", "Roma", 1),
    EnvioUrgente("E06", "Bilbao", 2),
    EnvioNacional("E07", "Málaga", 1),
]
```

Recorre la colección y muestra para cada objeto su identificador y su coste. Debes utilizar **la misma llamada ****`envio.calcular_coste()`** independientemente de la clase concreta del objeto.

**Pregunta para responder en un comentario de código:** ¿Por qué esta llamada ejecuta una versión diferente de `calcular_coste()` dependiendo del objeto?

## Parte C. Aplicar comprehensions

Resuelve los tres apartados **sin utilizar ****`for`**** convencionales para construir las colecciones**. Puedes usar `for` dentro de las comprehensions.

### C.1. List comprehension: envíos de coste elevado

Crea una lista `envios_caros` con los **identificadores** de los envíos cuyo coste sea **mayor o igual a 12 €**.

Usa `calcular_coste()` dentro de la condición.

### C.2. Set comprehension: modalidades utilizadas

Crea un conjunto `tipos_envio` con los nombres de las clases de los objetos que aparecen en `envios`.

Pista: puedes obtener el nombre de la clase de un objeto con `type(objeto).__name__`.

### C.3. Dictionary comprehension: costes por envío

Crea un diccionario `costes_por_envio` que relacione cada `envio_id` con su coste calculado. Incluye **todos** los envíos.

## Parte D. Aplicar programación funcional

### D.1. Funciones como argumentos

Implementa la siguiente función genérica:

```python
def aplicar_operacion(funcion, valor):
    # Completar
    pass
```

Debe recibir una función y un valor, ejecutar la función recibida sobre ese valor y devolver el resultado.

Después, crea una función `redondear_euros(importe)` que devuelva el importe redondeado a dos decimales.

Comprueba que puedes llamar a `aplicar_operacion(redondear_euros, 12.345)` y obtener `12.35`.

### D.2. Función que devuelve otra función

Implementa `crear_descuento(porcentaje)`. Esta función debe **devolver otra función** que reciba un importe y aplique el descuento indicado.

Ejemplo del comportamiento requerido:

```python
descontar_10 = crear_descuento(10)
print(descontar_10(100))  # 90.0
```

La función interna debe conservar el porcentaje recibido por la función externa.

### D.3. Combinación de programación funcional y dictionary comprehension

Construye `costes_con_descuento`, un nuevo diccionario que:

29. Incluya **solo** los envíos cuyo coste original sea mayor o igual a 12 €.
30. Use el identificador del envío como clave.
31. Use como valor el coste tras aplicar un **10 % de descuento**.
32. Calcule ese valor combinando `aplicar_operacion()`, la función creada con `crear_descuento(10)` y `redondear_euros()`.
33. No modifique ningún objeto ni el diccionario `costes_por_envio`.
> Puedes realizar las dos operaciones sobre el valor con llamadas anidadas a `aplicar_operacion()`.

## Parte E. Mostrar el informe final

El programa debe imprimir los siguientes apartados, en este orden:

34. Coste calculado de cada envío.
35. Identificadores de `envios_caros`.
36. Modalidades de `tipos_envio`.
37. Diccionario `costes_por_envio`.
38. Diccionario `costes_con_descuento`.
Para presentar `tipos_envio` de forma ordenada, utiliza `sorted(tipos_envio)`; el conjunto original no tiene un orden garantizado.
```

## 8. Restricciones

- Deben existir **cuatro clases**: una superclase y tres subclases.
- Las tres subclases deben usar **herencia, sobrescritura de métodos y ****`super()`**.
- El cálculo del coste debe realizarse mediante **polimorfismo**; evita cadenas de `if/elif` que comprueben el tipo de envío.
- Debes emplear al menos **una list comprehension, una set comprehension y dos dictionary comprehensions**.
- Debes incluir **una función que reciba otra función** y **una función que devuelva otra función**.
- No utilices `map()`, `filter()`, `reduce()`, Pandas ni bibliotecas externas: trabaja con los conceptos estudiados.
- Los objetos y los datos originales no deben modificarse durante la generación del informe.
---
"""

# PARTE A: jerarquía de clases (una superclase + tres subclases)
class Envio:
    """Superclase: datos comunes y tarifa base de un envío."""

    def __init__(self, envio_id, destino, peso):
        self.envio_id = envio_id
        self.destino = destino
        self.peso = peso

    def calcular_coste(self):
        """Tarifa base: peso * 2 (en float para que todos los costes sean homogéneos)."""
        return float(self.peso * 2)

    def mostrar_informacion(self):
        """Devuelve un string (no imprime) con los datos del envío."""
        return f"Envío {self.envio_id} -> {self.destino} ({self.peso} kg)"


class EnvioNacional(Envio):
    def calcular_coste(self):
        return super().calcular_coste() + 3


class EnvioInternacional(Envio):
    def calcular_coste(self):
        return super().calcular_coste() + 15


class EnvioUrgente(Envio):
    def calcular_coste(self):
        return super().calcular_coste() * 1.5


# PARTE D: programación funcional
def aplicar_operacion(funcion, valor):
    """D.1: recibe una función y un valor, y devuelve funcion(valor)."""
    return funcion(valor)


def redondear_euros(importe):
    """Redondea un importe a dos decimales."""
    return round(importe, 2)


def crear_descuento(porcentaje):
    """D.2: devuelve OTRA función (closure) que recuerda el porcentaje."""

    def aplicar_descuento(importe):
        return importe * (1 - porcentaje / 100)

    return aplicar_descuento


def main():
    # PARTE B: siete objetos y polimorfismo
    envios = [
        EnvioNacional("E01", "Madrid", 2),
        EnvioInternacional("E02", "París", 3),
        EnvioUrgente("E03", "Sevilla", 4),
        EnvioNacional("E04", "Valencia", 5),
        EnvioInternacional("E05", "Roma", 1),
        EnvioUrgente("E06", "Bilbao", 2),
        EnvioNacional("E07", "Málaga", 1),
    ]

    # ¿Por qué envio.calcular_coste() ejecuta una versión distinta según el objeto?
    # Porque Python decide en TIEMPO DE EJECUCIÓN qué método llamar mirando la
    # clase real del objeto (enlace dinámico). Cada subclase sobrescribe
    # calcular_coste(), así que EnvioNacional, EnvioInternacional y EnvioUrgente
    # aplican su propia tarifa con exactamente la misma llamada (polimorfismo).

    # PARTE C: comprehensions
    # C.1 list comprehension: ids de los envíos con coste >= 12 €
    envios_caros = [envio.envio_id for envio in envios
                    if envio.calcular_coste() >= 12]

    # C.2 set comprehension: nombres de las clases usadas (sin repetidos)
    tipos_envio = {type(envio).__name__ for envio in envios}

    # C.3 dict comprehension: id -> coste de TODOS los envíos
    costes_por_envio = {envio.envio_id: envio.calcular_coste()
                        for envio in envios}

    # D.3 dict comprehension: solo los >= 12 €, con 10 % de descuento
    descontar_10 = crear_descuento(10)
    costes_con_descuento = {
        envio_id: aplicar_operacion(
            redondear_euros,
            aplicar_operacion(descontar_10, coste),
        )
        for envio_id, coste in costes_por_envio.items()
        if coste >= 12
    }

    # PARTE E: informe final (en el orden pedido)
    for envio in envios:
        print(f"{envio.envio_id}: {envio.calcular_coste()} €")

    print(f"\nEnvíos caros: {envios_caros}")
    print(f"\nTipos de envío: {sorted(tipos_envio)}")
    print(f"\nCostes por envío: {costes_por_envio}")
    print(f"\nCostes con descuento: {costes_con_descuento}")

    # Comprobaciones extra de los apartados A y D
    print("\n--- Comprobaciones ---")
    print(envios[0].mostrar_informacion())
    print(f"aplicar_operacion(redondear_euros, 12.345) = "
          f"{aplicar_operacion(redondear_euros, 12.345)}")
    print(f"descontar_10(100) = {descontar_10(100)}")


if __name__ == "__main__":
    main()
