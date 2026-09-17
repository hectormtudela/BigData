# 📘 Manual completo de repaso — Python, SQL y Scala

> Examen práctico del 18/09. Este documento no resume: explica cada cosa como si la vieras por primera vez. Cada palabra técnica (slicing, casting, booleano, mutable, etc.) se define la primera vez que aparece, entre paréntesis o en su propio párrafo.

---

## ÍNDICE

1. Python — fundamentos absolutos
2. Python — listas
3. Python — diccionarios
4. Python — funciones y paquetes
5. Python — NumPy
6. Python — Pandas
7. Python — lógica y control de flujo
8. Python — bucles
9. Python — programación orientada a objetos (POO) y conceptos avanzados
10. SQL — fundamentos
11. SQL — agregación
12. SQL — combinación de tablas (JOINs)
13. SQL — operadores de conjunto
14. SQL — subconsultas y CTE
15. SQL — funciones de ventana
16. SQL — fechas, texto y pivotado
17. Scala — fundamentos
18. Scala — funciones
19. Scala — colecciones (Array y List)
20. Scala — control de flujo y estilo funcional
21. Índice de ejercicios del profesor
22. Temario de los cursos de DataCamp

---

# 1. PYTHON — FUNDAMENTOS ABSOLUTOS

## 1.1 ¿Qué es una variable?

```python
edad = 25
```

Aquí `edad` es el nombre de la variable y `25` es el valor que se guarda. A partir de ahora, cada vez que escribas `edad` en tu código, Python lo sustituye por `25`.

## 1.2 Tipos de datos básicos

Cada valor en Python tiene un "tipo", que es la categoría de dato que es. Los cuatro tipos básicos que necesitas para el examen son:

```python
x = 5          # int
y = 3.14       # float
s = "texto"    # string
b = True       # boolean
```

Puedes comprobar el tipo de cualquier variable con la función `type()`:

```python
type(x)   # devuelve <class 'int'>
```

## 1.3 Operadores aritméticos (cómo sumar, restar, multiplicar y dividir)

Aritmética básica en Python:

```python
5 + 3    # suma -> 8
5 - 3    # resta -> 2
5 * 3    # multiplicación -> 15
5 / 3    # división -> 1.6666666666666667 (SIEMPRE devuelve un float, aunque la división sea exacta)
5 // 3   # división ENTERA -> 1 (se queda solo con la parte entera del resultado, descarta el resto)
5 % 3    # módulo (el RESTO de la división entera) -> 2, porque 5 = 3*1 + 2
5 ** 3   # potencia -> 125, es decir 5 elevado a 3 (5*5*5)
```
ç

Para sumar directamente y guardar el resultado en la misma variable, puedes hacer `a = a + 1` o, de forma abreviada, `a += 1` (esto quiere decir "coge el valor actual de `a`, súmale 1 y guárdalo de nuevo en `a`"). Existen también `-=`, `*=`, `/=` con la misma lógica.

## 1.4 Conversión de tipos (casting)

"Casting" significa convertir un dato de un tipo a otro. Por ejemplo, convertir el texto `"5"` (que es un `str`) en el número `5` (que es un `int`), para poder hacer operaciones matemáticas con él (con texto no se puede sumar como si fuera número).

```python
str(5)        # convierte el int 5 al texto "5"
int("5")      # convierte el texto "5" al int 5
float("3.14") # convierte el texto "3.14" al float 3.14
bool(0)       # convierte 0 a False (cualquier número distinto de 0 se convierte en True)
```

⚠️ Si intentas convertir un texto que no es un número a `int` o `float` (por ejemplo `int("hola")`), Python da un error, porque no sabe qué número representa "hola".

## 1.5 Comportamientos curiosos que suelen aparecer en examen

```python
True + True + False
```
Esto da `2`. ¿Por qué? Porque en Python los booleanos son en realidad un caso especial de los enteros: `True` vale internamente `1` y `False` vale `0`. Así que sumar `True + True + False` es lo mismo que sumar `1 + 1 + 0 = 2`.

```python
3 != 3.0
```
Esto da `False`. El símbolo `!=` significa "distinto de". Python compara el *valor*, no el tipo exacto, así que el entero `3` y el float `3.0` se consideran iguales.

```python
"Zapatilla" > "Mochila"
```
Esto da `True`. Cuando comparas texto con `>` o `<`, Python compara letra por letra usando el orden alfabético (más exactamente, el orden del código de cada carácter). Como la "Z" va después de la "M" en el alfabeto, `"Zapatilla"` se considera "mayor" que `"Mochila"`.

```python
"Norte" == "norte"
```
Esto da `False`. Python distingue mayúsculas de minúsculas (esto se llama "case-sensitive"), así que `"Norte"` y `"norte"` son cadenas de texto diferentes aunque signifiquen lo mismo para una persona.

---

# 2. PYTHON — LISTAS

## 2.1 ¿Qué es una lista?

Una lista es una colección ordenada de valores, que se escribe entre corchetes `[ ]` separando los elementos por comas. Puede contener números, textos, booleanos, e incluso mezclarlos:

```python
catalogo = ["Auriculares BT", 59.90, "Smartwatch S2", 149.00]
```

## 2.2 Índices (indexing) — cómo acceder a un elemento

Un "índice" es la posición de un elemento dentro de la lista. **En Python, la numeración empieza en 0, no en 1.** Es decir, el primer elemento tiene índice `0`, el segundo tiene índice `1`, y así sucesivamente.

```python
lista = [10, 20, 30, 40]
lista[0]   # 10 (el primer elemento)
lista[1]   # 20 (el segundo elemento)
lista[3]   # 40 (el cuarto y último elemento)
```

También existen los **índices negativos**, que cuentan desde el final de la lista hacia atrás: `-1` es el último elemento, `-2` el penúltimo, etc.

```python
lista[-1]  # 40 (el último)
lista[-2]  # 30 (el penúltimo)
```

## 2.3 Slicing (segmentación) — cómo extraer un trozo de la lista

"Slicing" (en español a veces se traduce como "rebanado" o "segmentación", pero en clase normalmente se usa la palabra en inglés) es la técnica para extraer varios elementos seguidos de una lista de golpe, en vez de uno solo. La sintaxis es:

```python
lista[inicio:fin]
```

Esto te da todos los elementos desde la posición `inicio` (incluida) hasta la posición `fin` (**sin incluir esa posición**, esto es muy importante: el final del slicing nunca se incluye).

```python
lista = [10, 20, 30, 40, 50]
lista[1:3]     # [20, 30]  -> coge la posición 1 y la posición 2, NO la posición 3
lista[0:2]     # [10, 20]
lista[:2]      # [10, 20]  -> si no pones "inicio", empieza desde el principio (posición 0)
lista[2:]      # [30, 40, 50]  -> si no pones "fin", llega hasta el final de la lista
```

El slicing también admite un tercer número, el **paso** (step), que indica de cuántos en cuántos elementos vas saltando. Se escribe así: `lista[inicio:fin:paso]`.

```python
lista = [10, 20, 30, 40, 50, 60]
lista[::2]     # [10, 30, 50]  -> empieza en el principio, va hasta el final, saltando de 2 en 2 (posiciones pares: 0, 2, 4)
lista[1::2]    # [20, 40, 60]  -> empieza en la posición 1, salta de 2 en 2 (posiciones impares: 1, 3, 5)
```

Si el paso es negativo, recorres la lista hacia atrás. Un truco muy usado para invertir una lista sin usar ningún método especial es:

```python
lista[::-1]    # [60, 50, 40, 30, 20, 10]  -> recorre toda la lista de atrás hacia adelante
```

## 2.4 Listas anidadas (una lista dentro de otra)

Una "lista anidada" es una lista cuyos elementos son, a su vez, otras listas. Se usa por ejemplo para representar una tabla, donde cada fila es una sublista:

```python
inventario = [
    ["ALM-NORTE", "Robot Aspirador", 34, 201.50],
    ["ALM-SUR", "Silla Ergonomica", 12, 178.90],
]
```

Para acceder a un dato concreto necesitas dos índices: el primero para elegir la sublista (la fila) y el segundo para elegir el elemento dentro de esa sublista (la columna). Esto se llama "doble indexación":

```python
inventario[0]        # ["ALM-NORTE", "Robot Aspirador", 34, 201.50]  -> la fila completa
inventario[0][1]     # "Robot Aspirador"  -> dentro de la fila 0, el elemento en la posición 1
```

## 2.5 Métodos para modificar listas

Un "método" es una función que pertenece a un objeto concreto y se llama poniendo un punto detrás del objeto: `objeto.metodo()`. Aquí tienes los métodos de lista más importantes:

```python
lista = [1, 2, 3]

lista.append(4)       # añade 4 al FINAL de la lista. La lista queda [1, 2, 3, 4]
```
`.append()` modifica la lista directamente (esto se llama modificar "in situ" o "in-place", es decir, cambia la lista original en vez de crear una nueva) y no devuelve nada útil (devuelve `None`, que en Python representa "ningún valor").

```python
lista.extend([5, 6])  # añade VARIOS elementos al final. La lista queda [1, 2, 3, 4, 5, 6]
```
Si usaras `.append([5, 6])` en vez de `.extend([5, 6])`, añadiría la lista `[5, 6]` como un único elemento (quedaría `[1, 2, 3, [5, 6]]`), que normalmente no es lo que quieres.

```python
lista.insert(2, "nuevo")  # inserta "nuevo" en la posición 2, desplazando el resto hacia la derecha
```

```python
lista.remove(3)       # elimina la PRIMERA aparición del VALOR 3 (no de la posición 3, del valor 3)
```

```python
valor = lista.pop(1)  # elimina el elemento de la posición 1 y además lo DEVUELVE, guardándolo en "valor"
lista.pop()            # sin argumento, elimina y devuelve el ÚLTIMO elemento
```

```python
del lista[0]           # elimina el elemento de la posición 0. A diferencia de .pop(), no devuelve nada
```

```python
lista.index("Robot Aspirador")  # te dice en qué posición está la primera vez que aparece ese valor
lista.count(3)                   # cuenta cuántas veces aparece el valor 3 en la lista
```

```python
lista.sort()              # ordena la lista de menor a mayor, MODIFICÁNDOLA (in-place), y no devuelve nada
lista.sort(reverse=True)  # ordena de mayor a menor
```

```python
nueva = sorted(lista)     # crea una lista NUEVA ordenada, sin tocar la lista original
```
La diferencia clave: `.sort()` es un método que cambia la lista original y no te devuelve nada que puedas guardar en otra variable (si haces `x = lista.sort()`, `x` será `None`). `sorted(lista)` es una función que no toca la lista original, sino que te devuelve una lista nueva ya ordenada.

```python
lista.reverse()  # invierte el orden de la lista, modificándola directamente (in-place)
```

## 2.6 Copiar una lista — el error más común y más caro de depurar

Esto es muy importante porque es un error clásico de examen. Cuando haces esto:

```python
lista_a = [1, 2, 3]
lista_b = lista_a
```

**NO estás copiando la lista.** Lo que ocurre es que `lista_b` pasa a apuntar exactamente al mismo objeto en memoria que `lista_a` (esto se llama trabajar por "referencia": una variable de lista no contiene los datos directamente, contiene una especie de "dirección" que apunta a donde están los datos reales). Esto significa que si modificas `lista_b`, también estás modificando `lista_a`, porque en realidad son el mismo objeto con dos nombres distintos.

```python
lista_a = [1, 2, 3]
lista_b = lista_a
lista_b[0] = 99
print(lista_a)   # [99, 2, 3]  -> ¡lista_a también cambió, aunque no la tocaste directamente!
```

Para hacer una copia real e independiente (de forma que modificar una no afecte a la otra), hay dos formas:

```python
copia1 = list(lista_a)   # usando la función list()
copia2 = lista_a[:]       # usando slicing completo (sin inicio ni fin, coge todo, pero crea un objeto nuevo)
```

Puedes comprobar que ahora son objetos distintos con la función `id()`, que te da un identificador único de cada objeto en memoria:

```python
id(lista_a) == id(copia1)   # False, son objetos distintos
```

⚠️ Nota adicional: si la lista tiene listas dentro (anidadas), `list()` y `[:]` solo copian el primer nivel (esto se llama copia "superficial" o *shallow copy*); las sublistas de dentro seguirían siendo las mismas referencias. Para una copia completa de todos los niveles haría falta `copy.deepcopy()`, aunque para el nivel del examen normalmente basta con saber la diferencia entre `=` (referencia) y `list()`/`[:]` (copia).

## 2.7 Métodos de texto (strings) que se combinan con listas

```python
texto = "  Hola Mundo  "
texto.strip()     # quita los espacios en blanco al principio y al final -> "Hola Mundo"
texto.upper()      # convierte todo a mayúsculas -> "  HOLA MUNDO  "
texto.lower()      # convierte todo a minúsculas
texto.replace("Hola", "Adiós")  # sustituye un trozo de texto por otro
texto.split("-")   # divide el texto en una LISTA de trozos, cortando por el carácter indicado
```

⚠️ Muy importante: `.strip()`, `.upper()`, `.lower()`, `.replace()` y `.split()` **no modifican la cadena original**, porque en Python el texto (`str`) es "inmutable" (no se puede cambiar una vez creado). Lo que hacen es **devolver una cadena nueva**. Por eso hay que guardarlas en una variable: `texto_limpio = texto.strip()`.

```python
"|".join(["a", "b", "c"])   # une los elementos de una lista en un único texto, separados por "|" -> "a|b|c"
```

---

# 3. PYTHON — DICCIONARIOS

## 3.1 ¿Qué es un diccionario?

Un diccionario es una colección de pares "clave-valor" (en inglés *key-value*). Se parece a un diccionario de verdad: buscas una "palabra" (la clave) y obtienes su "significado" (el valor). Se escribe entre llaves `{ }`:

```python
tarifas = {"Norte": 4.95, "Sur": 5.50, "Este": 5.20}
```

Aquí `"Norte"`, `"Sur"` y `"Este"` son las claves, y `4.95`, `5.50`, `5.20` son sus valores asociados.

## 3.2 Operaciones básicas

```python
tarifas["Norte"]           # accede al valor asociado a la clave "Norte" -> 4.95
tarifas["Insular"] = 9.80  # si la clave no existe, la CREA con ese valor
tarifas["Oeste"] = 5.95    # si la clave YA existe, ACTUALIZA su valor
del tarifas["Sur"]         # elimina la clave "Sur" (y su valor) del diccionario
"Norte" in tarifas          # comprueba si "Norte" es una clave del diccionario -> True o False
```

## 3.3 Recorrer un diccionario

```python
for clave, valor in tarifas.items():
    print(clave, "->", valor)
```

El método `.items()` te da, en cada vuelta del bucle, una pareja (clave, valor). ⚠️ Si haces `for clave in tarifas:` sin `.items()`, solo obtienes las claves, no los valores.

## 3.4 Diccionarios anidados (un diccionario dentro de otro)

```python
red_logistica = {
    "Norte": {"almacen": "ALM-NORTE", "tarifa": 4.95, "entrega_h": 24},
    "Este":  {"almacen": "ALM-ESTE", "tarifa": 5.20, "entrega_h": 48},
}
```

Aquí cada clave del diccionario principal (`"Norte"`, `"Este"`) tiene como valor otro diccionario más pequeño. Para acceder a un dato concreto, encadenas dos claves (esto se llama "doble clave" o acceso anidado):

```python
red_logistica["Este"]["entrega_h"]   # 48
```

## 3.5 ¿Cuándo usar un diccionario en vez de una lista?

Una lista se accede por posición (índice numérico), mientras que un diccionario se accede por un nombre significativo (la clave). Si tus datos tienen una etiqueta natural que tiene sentido usar para buscarlos (un nombre de región, un código de producto, un DNI), un diccionario es más claro y más rápido de consultar que recorrer una lista buscando esa etiqueta.

---

# 4. PYTHON — FUNCIONES Y PAQUETES

## 4.1 ¿Qué es una función?

Una función es un bloque de código con un nombre, que recibe unos datos de entrada (llamados "parámetros" o "argumentos"), hace algo con ellos, y opcionalmente devuelve un resultado. Sirve para no tener que repetir el mismo código muchas veces.

```python
def calcular_importe(unidades, precio_unitario, descuento_pct=0):
    """Devuelve el importe neto redondeado a dos decimales."""
    bruto = unidades * precio_unitario
    neto = bruto * (1 - descuento_pct / 100)
    return round(neto, 2)
```

Desglosando esto:
- `def` es la palabra clave que indica "voy a definir una función".
- `calcular_importe` es el nombre que le damos a la función.
- `(unidades, precio_unitario, descuento_pct=0)` son los parámetros que la función espera recibir. `descuento_pct=0` significa que ese parámetro tiene un **valor por defecto**: si al llamar a la función no le pasas ese dato, se usará automáticamente `0`.
- El texto entre comillas triples justo debajo de la definición es el **docstring**: una descripción de qué hace la función, pensada para que otra persona (o tú mismo dentro de unos meses) entienda qué hace sin tener que leer todo el código. Puedes verlo con `help(calcular_importe)`.
- `return` es la palabra clave que indica qué valor debe devolver la función cuando se la llama. En cuanto se ejecuta un `return`, la función termina ahí.

Para usar (o "llamar a") la función:

```python
calcular_importe(3, 59.90, 10)   # 161.73
```

Aquí `3` se asigna a `unidades`, `59.90` a `precio_unitario` y `10` a `descuento_pct`, en ese orden (esto se llama pasar argumentos "posicionales", porque el orden importa).

## 4.2 Argumentos por palabra clave (keyword arguments)

En vez de depender del orden, puedes indicar explícitamente a qué parámetro corresponde cada valor, escribiendo `nombre_del_parametro=valor`:

```python
calcular_importe(precio_unitario=59.90, unidades=3, descuento_pct=10)
```

Esto da el mismo resultado que antes, pero ahora el orden no importa porque cada valor lleva escrito a qué parámetro pertenece. Esto se llama "argumentos por palabra clave" o *keyword arguments* (a veces abreviado *kwargs*).

## 4.3 Funciones que devuelven varios valores (tuplas) y desempaquetado

Una función puede devolver varios valores a la vez separados por comas; en realidad Python los agrupa automáticamente en una **tupla** (una tupla es como una lista, pero no se puede modificar después de creada, es decir, es "inmutable"; se escribe con paréntesis `( )` en vez de corchetes):

```python
def resumen_pedido(unidades, precio_unitario, descuento_pct=0):
    bruto = unidades * precio_unitario
    neto = calcular_importe(unidades, precio_unitario, descuento_pct)
    ahorro = round(bruto - neto, 2)
    return bruto, ahorro, neto   # esto crea una tupla (bruto, ahorro, neto)
```

Para separar esos tres valores en tres variables distintas de golpe, se hace lo que se llama "desempaquetado" (unpacking):

```python
bruto, ahorro, neto = resumen_pedido(unidades=3, precio_unitario=59.90, descuento_pct=10)
```

Ahora `bruto`, `ahorro` y `neto` son tres variables independientes con cada uno de los tres valores devueltos.

## 4.4 Funciones integradas (built-in) más usadas

Estas funciones ya vienen con Python, no hace falta importarlas:

```python
len(lista)      # cuenta cuántos elementos tiene una lista, texto, diccionario, etc.
max(lista)       # el valor más grande
min(lista)       # el valor más pequeño
sorted(lista)    # una lista nueva, ordenada, sin tocar la original
round(3.14159, 2)  # redondea a 2 decimales -> 3.14
sum(lista)       # suma todos los elementos numéricos de la lista
type(x)           # te dice el tipo de dato de x
```

## 4.5 Paquetes y módulos (import)

Un "módulo" es un archivo de Python con funciones ya escritas que puedes reutilizar. Un "paquete" es, básicamente, una colección organizada de módulos. Para poder usar las funciones de un módulo o paquete, primero tienes que "importarlo":

```python
import math
math.sqrt(2809)     # usa la función sqrt (raíz cuadrada) del módulo math -> 53.0
```

Aquí tienes que escribir `math.` delante de cada función porque has importado *todo* el módulo con su nombre.

```python
from math import pi, ceil
```

Esto importa **solamente** `pi` (el número π) y `ceil` (la función que redondea siempre hacia arriba, "ceiling" = techo) directamente, así que ya no hace falta escribir `math.` delante, puedes usar `pi` y `ceil(x)` directamente.

```python
import numpy as np
import pandas as pd
```

Esto importa los paquetes `numpy` y `pandas`, pero les da un **alias** (un nombre corto alternativo) para no tener que escribir el nombre completo cada vez. Por convención casi universal, `numpy` se importa como `np` y `pandas` como `pd`.

```python
import random
random.seed(42)
valoraciones = [random.randint(1, 5) for _ in range(10)]
```

`random.seed(42)` fija la "semilla" del generador de números aleatorios. Los ordenadores no generan números realmente aleatorios, usan un algoritmo que parte de un número inicial (la semilla) para generar la secuencia. Si tú y el profesor usáis la misma semilla, obtendréis exactamente la misma secuencia de números "aleatorios", lo cual permite que el resultado sea reproducible (que se pueda repetir exactamente igual otra vez).

## 4.6 Importar tu propio módulo

Si has guardado funciones tuyas en un archivo, por ejemplo `src/utilidades.py`, y tu notebook está en otra carpeta (por ejemplo `notebooks/`), Python no sabe automáticamente dónde buscar ese archivo. Para decírselo:

```python
import sys
sys.path.append("../src")   # añade la carpeta "../src" a los sitios donde Python busca módulos

from utilidades import calcular_importe, clasificar_ticket
```

`sys` es el módulo que te permite interactuar con cosas del propio sistema/intérprete de Python, y `sys.path` es la lista de carpetas donde Python busca módulos al hacer `import`. `"../src"` significa "sube una carpeta desde donde estoy y entra en la carpeta src".

---

# 5. PYTHON — NUMPY

## 5.1 ¿Qué es NumPy y por qué no basta con listas?

NumPy es un paquete para trabajar con números de forma mucho más rápida y cómoda que con listas normales de Python. La estructura principal de NumPy es el **array** (que en español a veces se llama "arreglo" o "matriz" si tiene más de una dimensión), que se parece a una lista pero con una diferencia clave: los arrays de NumPy permiten hacer operaciones matemáticas sobre **todos los elementos a la vez**, sin necesidad de bucles.

```python
import numpy as np

lista = [1, 2, 3]
lista * 2          # [1, 2, 3, 1, 2, 3]  -> ¡esto DUPLICA la lista, no multiplica cada número por 2!

array = np.array([1, 2, 3])
array * 2           # [2, 4, 6]  -> esto SÍ multiplica cada número por 2
```

Esta operación de aplicar una operación a todos los elementos de golpe se llama **vectorización**. La ventaja es doble: el código es más corto (no hace falta escribir un bucle `for` para recorrer elemento por elemento) y es mucho más rápido internamente, porque NumPy está optimizado para hacer estos cálculos de forma masiva.

## 5.2 Crear y describir un array

```python
arr = np.array([1, 2, 3])

arr.dtype   # el tipo de dato que contiene el array (por ejemplo int64, float64...). "dtype" = data type
arr.shape    # la forma del array: para un array 1D de 3 elementos, sería (3,)
arr.ndim     # el número de dimensiones (1 para un array simple, 2 para una matriz, etc.)
arr.size     # el número total de elementos
```

## 5.3 Arrays de dos dimensiones (matrices)

Un array 2D es como una tabla, con filas y columnas.

```python
m = np.array([[1, 2], [3, 4]])
m.shape   # (2, 2) -> 2 filas, 2 columnas
```

Para acceder a un elemento concreto, se usa `[fila, columna]` (con una sola pareja de corchetes y una coma dentro, a diferencia de las listas anidadas de Python normal, que necesitan `[fila][columna]`):

```python
m[0, 1]    # elemento en la fila 0, columna 1 -> 2
m[:, 0]    # el símbolo ":" solo significa "todas". Aquí: todas las filas, columna 0 -> array([1, 3])
m[0, :]    # fila 0, todas las columnas -> array([1, 2])
```

Para apilar (juntar) arrays:

```python
np.vstack([m, [5, 6]])       # añade una fila nueva al final ("v" de vertical stack, apilar verticalmente)
np.column_stack([a, b])        # junta dos arrays 1D como si fueran dos columnas de una tabla
```

## 5.4 Máscaras booleanas (boolean masks) — filtrar arrays

Una "máscara booleana" es un array del mismo tamaño que el original, pero lleno de `True` y `False`, que indica qué posiciones cumplen una condición. Se usa para quedarte solo con los elementos que te interesan.

```python
precios = np.array([50, 150, 30, 200])
caros = precios > 100          # array([False, True, False, True])  -> esta es la máscara
precios[caros]                  # array([150, 200])  -> usando la máscara como "filtro" dentro de los corchetes
```

Puedes contar cuántos elementos cumplen la condición sumando la máscara, porque, igual que vimos antes con los booleanos en Python puro, `True` vale `1` y `False` vale `0` a efectos de suma:

```python
caros.sum()   # 2 -> hay 2 elementos que cumplen precios > 100
```

`np.where(caros)` te da las posiciones (los índices) donde la máscara es `True`, en vez de los valores.

Para combinar varias condiciones a la vez, en NumPy **no se usan las palabras `and` / `or`** (eso daría error), se usan los símbolos `&` (y) y `|` (o), y cada condición individual tiene que ir entre paréntesis, porque si no, Python intenta evaluar `&` antes que `>` y el resultado es incorrecto o da error:

```python
seleccion = (precios > 100) & (precios < 250)   # True donde se cumplen AMBAS condiciones
```

## 5.5 Funciones estadísticas

```python
np.mean(arr)        # la media (promedio)
np.median(arr)        # la mediana (el valor central si ordenas todos los datos)
np.std(arr)           # la desviación típica (cuánto se dispersan los datos respecto a la media)
np.percentile(arr, 25)  # el percentil 25 (el valor por debajo del cual está el 25% de los datos)
np.corrcoef(a, b)      # la matriz de correlación entre dos variables (mide si suben y bajan juntas)
np.argmax(arr)          # la POSICIÓN (índice) del valor más alto, no el valor en sí
```

Para generar números aleatorios de forma reproducible (con semilla) usando la sintaxis moderna de NumPy:

```python
rng = np.random.default_rng(42)      # crea un "generador" con semilla 42
rng.normal(68, 6.5, 500)               # 500 números siguiendo una distribución normal (media 68, desviación 6.5)
```

## 5.6 Un array con tipos mezclados

Si metes en un mismo array valores de distinto tipo, por ejemplo `[1, "dos", 3.0, True]`, NumPy no puede mantener cada uno con su tipo original (a diferencia de una lista de Python, que sí admite tipos mezclados). NumPy exige que **todos los elementos de un array tengan el mismo tipo** (esto se llama que el array es "homogéneo"), así que convierte automáticamente todos los elementos al tipo más general posible; en este caso, como hay un texto, todo se convierte a texto (`str`).

---

# 6. PYTHON — PANDAS

## 6.1 ¿Qué es Pandas?

Pandas es el paquete para trabajar con datos en forma de tabla (como una hoja de Excel o una tabla de base de datos), dentro de Python. La estructura principal se llama **DataFrame**, que es una tabla con filas y columnas, donde cada columna puede tener su propio nombre y tipo de dato. Una sola columna extraída de un DataFrame se llama **Serie** (Series).

## 6.2 Crear y cargar un DataFrame

```python
import pandas as pd

datos = {"nombre": ["Ana", "Luis"], "nota": [8, 4]}
df = pd.DataFrame(datos)   # convierte un diccionario en una tabla
```

Aquí cada clave del diccionario se convierte en el nombre de una columna, y su lista de valores se convierte en los datos de esa columna.

```python
df = pd.read_csv("archivo.csv")                     # carga un archivo CSV como DataFrame
df = pd.read_csv("archivo.csv", index_col="id")      # además, usa la columna "id" como índice de las filas
```

Un archivo CSV (Comma-Separated Values, "valores separados por comas") es un archivo de texto donde cada línea es una fila de la tabla y los valores de cada columna van separados por comas.

## 6.3 Explorar un DataFrame

```python
df.head(8)    # muestra las primeras 8 filas
df.tail(3)     # muestra las últimas 3 filas
df.shape       # una tupla (número_de_filas, número_de_columnas)
df.info()       # muestra, para cada columna: cuántos valores no nulos tiene y de qué tipo es
df.isna().sum()  # cuenta, por columna, cuántos valores son nulos (NaN, "Not a Number", es decir, un hueco vacío)
```

## 6.4 Seleccionar datos: corchetes, `.loc` y `.iloc`

```python
df["nota"]        # selecciona la columna "nota" como una SERIE (una sola columna)
df[["nota", "nombre"]]  # selecciona VARIAS columnas a la vez como un DataFrame (nota los dobles corchetes)
```

`.loc` selecciona por **etiqueta**, es decir, por el nombre real de la fila o columna (el índice o el nombre de columna, tal como aparecen):

```python
df.loc["EMP-1042"]                    # la fila cuyo índice se llama exactamente "EMP-1042"
df.loc["EMP-1042", "departamento"]    # el valor de la columna "departamento" en esa fila
df.loc[:, ["nombre", "bonus_pct"]]    # todas las filas (":"), solo esas dos columnas
```

`.iloc` selecciona por **posición numérica**, igual que los índices de las listas, sin importar cómo se llame la fila o columna:

```python
df.iloc[0]           # la primera fila, sea cual sea su nombre de índice
df.iloc[0:3, 1:3]    # las tres primeras filas (posiciones 0,1,2) y las columnas en posición 1 y 2
```

La diferencia clave para recordar: **`loc` = nombre/etiqueta, `iloc` = posición/número**, igual que la diferencia entre buscar una palabra en un diccionario por su nombre (`loc`) o por "la palabra número 5 de la página" (`iloc`).

## 6.5 Crear columnas nuevas (columnas calculadas)

```python
df["importe_bruto"] = df["unidades"] * df["precio_unitario"]
```

Esto crea una columna nueva llamada `importe_bruto`, calculada multiplicando, fila por fila, los valores de `unidades` y `precio_unitario`. Esto es vectorización otra vez: no hace falta ningún bucle, pandas aplica la operación a todas las filas de golpe.

## 6.6 Agrupar y agregar datos (`groupby`)

"Agrupar" significa juntar todas las filas que comparten un mismo valor en una columna, para después calcular algo sobre cada grupo (una suma, una media, un conteo...). Esto se llama "agregación".

```python
df.groupby("region")["importe_neto"].sum()
```

Esto dice: "agrupa todas las filas por el valor de la columna `region` (todas las filas de 'Norte' juntas, todas las de 'Sur' juntas, etc.), y para cada grupo, suma la columna `importe_neto`". El resultado es una tabla con una fila por cada región distinta y su suma total.

```python
df.groupby(["categoria", "canal"]).agg({"importe_neto": "mean", "unidades": "sum"})
```

Aquí se agrupa por dos columnas a la vez (categoría y canal), y `.agg()` (de "aggregate", agregar) permite aplicar una función distinta a cada columna: la media (`mean`) para `importe_neto` y la suma (`sum`) para `unidades`.

```python
df.groupby("producto")["importe_neto"].sum().nlargest(5)
```

`.nlargest(5)` te da los 5 valores más grandes del resultado, es decir, en este caso, el top 5 de productos por facturación.

## 6.7 Filtrar filas de un DataFrame

Filtrar significa quedarte solo con las filas que cumplen una condición.

```python
df[df["importe_neto"] > 500]                      # filas donde importe_neto es mayor que 500
df[df["region"].isin(["Norte", "Centro"])]          # filas donde la región está DENTRO de esa lista
df[df["descuento_pct"].between(10, 20)]              # filas donde el descuento está entre 10 y 20, ambos incluidos
```

Para combinar varias condiciones, igual que en NumPy, se usan `&` (y) y `|` (o) en vez de `and`/`or`, con cada condición entre paréntesis:

```python
df[(df["categoria"] == "Electronica") & (df["unidades"] > 2) & (df["descuento_pct"] != 0)]
```

Para invertir una condición (quedarte con lo que NO cumple), se usa `~`:

```python
df[~(df["categoria"] == "Oficina")]   # todas las filas cuya categoría NO sea "Oficina"
```

También existe una forma alternativa, más legible, usando `.query()`, donde escribes la condición como si fuera texto normal:

```python
df.query("importe_neto > 500 and canal == 'Online'")
```

## 6.8 Aplicar una función a una columna (`.apply()`)

```python
def clasificar_ticket(importe):
    if importe < 100:
        return "Bajo"
    elif importe < 400:
        return "Medio"
    return "Alto"

df["segmento"] = df["importe_neto"].apply(clasificar_ticket)
```

`.apply()` ejecuta la función que le pasas sobre cada valor de la columna, uno por uno, y guarda los resultados en la nueva columna. ⚠️ Fíjate en que se escribe `df["importe_neto"].apply(clasificar_ticket)`, **sin paréntesis después del nombre de la función**. Si escribieras `clasificar_ticket()` con paréntesis, estarías llamando a la función inmediatamente (y fallaría, porque no le estás pasando ningún valor); sin paréntesis, le estás pasando la función en sí, para que sea pandas quien la llame internamente sobre cada dato.

## 6.9 Rellenar valores nulos

```python
df["satisfaccion"] = df["satisfaccion"].fillna(df["satisfaccion"].median())   # rellena huecos con la mediana
df["canal"] = df["canal"].fillna("Desconocido")                                # rellena huecos con un texto fijo
```

## 6.10 El accesor de texto en columnas (`.str`)

Cuando una columna contiene texto, puedes usar `.str` para aplicar operaciones de texto a toda la columna de golpe (vectorizado, igual que con números):

```python
df["region"].str[:3].str.upper()
```

Esto coge, para cada valor de la columna `region`, los primeros 3 caracteres (usando slicing, como en las listas) y los convierte a mayúsculas.

## 6.11 Recorrer un DataFrame fila por fila (`.iterrows()`)

```python
for etiqueta, fila in df.iterrows():
    print(fila["region"], fila["importe_neto"])
```

`.iterrows()` te devuelve, en cada vuelta del bucle, dos cosas: la etiqueta (el nombre del índice de esa fila) y la fila completa (que se comporta como si fuera un diccionario, donde puedes acceder a cada columna por su nombre).

## 6.12 Exportar un DataFrame

```python
df.to_csv("../outputs/resultado.csv")
```

Esto guarda el DataFrame como un archivo CSV en la ruta indicada.

---

# 7. PYTHON — LÓGICA Y CONTROL DE FLUJO

## 7.1 Operadores de comparación

Estos operadores comparan dos valores y devuelven un booleano (`True` o `False`):

```python
5 == 5    # igual a -> True
5 != 3    # distinto de -> True
5 > 3     # mayor que -> True
5 < 3     # menor que -> False
5 >= 5    # mayor o igual que -> True
5 <= 4    # menor o igual que -> False
```

⚠️ Ojo: `==` (dos signos igual) se usa para **comparar**; `=` (un solo signo igual) se usa para **asignar** un valor a una variable. Son cosas completamente distintas y confundirlas es un error muy común.

## 7.2 Operadores lógicos

Sirven para combinar varias condiciones booleanas:

```python
True and False   # "y": solo es True si AMBAS partes son True -> False
True or False    # "o": es True si AL MENOS UNA parte es True -> True
not True          # invierte el valor -> False
```

Ejemplo aplicado:

```python
unidades = 6
descuento = 15
(unidades > 4) and (descuento >= 10)   # True, porque se cumplen las dos condiciones
```

⚠️ Importante: `and`, `or` y `not` funcionan con valores individuales (un solo booleano cada vez). **No funcionan igual sobre arrays de NumPy ni columnas (Series) de pandas**: ahí hay que usar `&`, `|`, `~`, como se explicó en las secciones de NumPy y Pandas, porque si intentas usar `and`/`or` sobre un array entero, Python no sabe cómo convertir un array completo en un único `True`/`False`, y da un error (`ValueError`).

## 7.3 `if`, `elif`, `else` — tomar decisiones en el código

Esta estructura permite que el programa ejecute un bloque de código u otro dependiendo de si se cumple una condición.

```python
def nivel_riesgo(temperatura):
    if temperatura > 85:
        return "CRÍTICO"
    elif temperatura > 76:
        return "ALTO"
    elif temperatura > 70:
        return "MEDIO"
    else:
        return "BAJO"
```

Cómo se lee esto: "si la temperatura es mayor que 85, devuelve 'CRÍTICO'. Si no (pero es mayor que 76), devuelve 'ALTO'. Si no (pero es mayor que 70), devuelve 'MEDIO'. Si ninguna de las anteriores se cumplió, devuelve 'BAJO'." `elif` es la forma abreviada de escribir "else if" (si no, si..."), y puedes poner tantos `elif` como necesites entre el `if` inicial y el `else` final. El `else` es opcional, y captura todos los casos que no cumplieron ninguna condición anterior.

**Es fundamental fijarse en la indentación** (los espacios en blanco al principio de cada línea): en Python, la indentación no es solo estética, es lo que le dice al intérprete qué líneas pertenecen a cada bloque (`if`, `elif`, `else`, funciones, bucles...). Si la indentación está mal, el código falla o hace algo distinto de lo que querías.

---

# 8. PYTHON — BUCLES

Un bucle sirve para repetir un bloque de código varias veces, sin tener que copiarlo y pegarlo a mano.

## 8.1 Bucle `while`

`while` repite el bloque de código **mientras** se siga cumpliendo una condición. Hay que tener cuidado de que, en algún momento, la condición deje de cumplirse, o el bucle se repetiría para siempre (bucle infinito).

```python
stock = 12
lote = 0

while stock < 60:
    lote = lote + 1
    stock = stock + 8
    print("Lote", lote, "-> stock:", stock)
```

Aquí, mientras `stock` sea menor que 60, se ejecuta el bloque: se suma 1 a `lote`, se suman 8 unidades a `stock`, y se imprime el estado. En cuanto `stock` llega a 60 o más, la condición `stock < 60` deja de cumplirse y el bucle termina.

## 8.2 Bucle `for` — recorrer una secuencia

`for` recorre, uno por uno, todos los elementos de algo que se pueda recorrer (una lista, un texto, un rango de números, las claves de un diccionario, las filas de un DataFrame...).

```python
regiones = ["Norte", "Sur", "Este"]
for region in regiones:
    print(region.upper())
```

En cada vuelta del bucle, la variable `region` toma el valor del siguiente elemento de la lista, hasta que se recorren todos.

## 8.3 `enumerate` — recorrer con el número de posición

Si además de cada elemento necesitas saber en qué posición está, se usa `enumerate()`:

```python
for i, region in enumerate(regiones, start=1):
    print(f"Región {i}: {region}")
```

`enumerate(regiones, start=1)` va dando, en cada vuelta, una pareja (posición, elemento). `start=1` hace que la cuenta empiece en 1 en vez de en 0 (por defecto `enumerate` empezaría a contar desde 0, como los índices normales de Python).

## 8.4 Recorrer listas anidadas con desempaquetado

```python
for almacen, producto, unidades, coste in inventario:
    print(almacen, producto, unidades * coste)
```

Como cada elemento de `inventario` es una sublista de 4 valores, puedes "desempaquetarla" directamente en la cabecera del bucle, dándole un nombre a cada uno de los 4 valores de golpe.

## 8.5 Recorrer un diccionario

```python
for region, tarifa in tarifas.items():
    print(region, "->", tarifa)
```

## 8.6 Recorrer un DataFrame de pandas

```python
for etiqueta, fila in df.iterrows():
    print(fila["producto"], fila["importe_neto"])
```

---

# 9. PYTHON — PROGRAMACIÓN ORIENTADA A OBJETOS (POO) Y CONCEPTOS AVANZADOS

*(Estos conceptos vienen de los cursos "Introduction/Intermediate to Python for Developers" que también estás siguiendo. No aparecen en los ejercicios de práctica que me has pasado, pero los incluyo por si el examen los toca.)*

## 9.1 Clases y objetos

Una "clase" es como un molde o plantilla para crear objetos que comparten una misma estructura. Un "objeto" (o "instancia") es cada elemento concreto creado a partir de esa clase.

```python
class Jugador:
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

    def mostrar(self):
        print(f"{self.nombre}: {self.puntuacion} puntos")
```

`__init__` es el "constructor": una función especial que se ejecuta automáticamente cada vez que creas un objeto nuevo de esa clase, y sirve para darle sus valores iniciales. `self` es una referencia al propio objeto que se está creando o usando (siempre es el primer parámetro de los métodos de una clase).

```python
jugador1 = Jugador("Ana", 10)   # crea un objeto (instancia) de la clase Jugador
jugador1.mostrar()               # llama a un método del objeto -> "Ana: 10 puntos"
```

## 9.2 Herencia

Una clase puede "heredar" de otra, es decir, reutilizar y ampliar su comportamiento sin tener que reescribirlo todo:

```python
class JugadorVIP(Jugador):
    def __init__(self, nombre, puntuacion, descuento):
        super().__init__(nombre, puntuacion)   # reutiliza el constructor de la clase padre
        self.descuento = descuento
```

`super()` te permite llamar a métodos de la clase "padre" (de la que hereda) desde la clase "hija".

## 9.3 Tuplas y sets

Una **tupla** es como una lista pero inmutable (no se puede modificar después de creada), se escribe con paréntesis: `(1, 2, 3)`.

Un **set** (conjunto) es una colección de elementos sin orden y **sin duplicados** (si añades un valor que ya está, no se repite), se escribe con llaves: `{1, 2, 3}`. Sirve, por ejemplo, para eliminar duplicados de una lista rápidamente: `set([1, 2, 2, 3])` da `{1, 2, 3}`.

## 9.4 Manejo de errores (`try` / `except`)

Sirve para evitar que el programa se pare en seco cuando ocurre un error esperado (como dividir por cero, o convertir un texto no numérico a número):

```python
try:
    resultado = int("abc")
except ValueError:
    print("Ese texto no se puede convertir a número")
```

Python intenta ejecutar el bloque `try`; si ocurre un error del tipo indicado en `except`, en vez de detener el programa, ejecuta el bloque `except`.

## 9.5 Lectura y escritura de archivos

```python
with open("archivo.txt", "r") as f:
    contenido = f.read()
```

`with open(...) as f:` abre el archivo y se asegura de cerrarlo automáticamente al terminar el bloque, aunque ocurra un error en medio. `"r"` significa modo lectura (*read*); `"w"` sería modo escritura (*write*, y borraría el contenido anterior).

## 9.6 `*args` y `**kwargs`

Permiten que una función acepte un número variable de argumentos, sin saber de antemano cuántos van a ser.

```python
def sumar_todos(*args):
    return sum(args)

sumar_todos(1, 2, 3, 4)   # 10, "args" recoge todos los argumentos posicionales en una tupla
```

`**kwargs` hace lo mismo pero para argumentos por palabra clave, agrupándolos en un diccionario.

## 9.7 Funciones lambda

Una función "lambda" es una función corta, escrita en una sola línea, sin necesidad de `def` ni nombre (aunque se le puede dar un nombre si se quiere):

```python
doble = lambda x: x * 2
doble(5)   # 10
```

Se usan mucho junto a `map()` (aplica una función a todos los elementos de una lista) y `filter()` (se queda solo con los elementos que cumplen una condición):

```python
list(map(lambda x: x * 2, [1, 2, 3]))       # [2, 4, 6]
list(filter(lambda x: x > 1, [1, 2, 3]))     # [2, 3]
```

## 9.8 Generadores (`yield`)

Un generador es una función especial que, en vez de calcular y devolver todos los resultados de golpe (lo cual puede ocupar mucha memoria si son muchos datos), va "produciendo" un valor cada vez que se le pide, usando `yield` en vez de `return`.

```python
def contador(hasta):
    i = 0
    while i < hasta:
        yield i
        i += 1
```

## 9.9 Decoradores

Un decorador es una función que "envuelve" a otra función para añadirle comportamiento extra (por ejemplo, medir cuánto tarda en ejecutarse) sin tener que modificar el código original de esa función. Se aplican con el símbolo `@` justo encima de la función:

```python
@mi_decorador
def mi_funcion():
    ...
```

---

# 10. SQL — FUNDAMENTOS

## 10.1 ¿Qué es SQL?

SQL (Structured Query Language, "lenguaje de consulta estructurado") es el lenguaje que se usa para pedirle datos a una base de datos relacional (una base de datos organizada en tablas, con filas y columnas, como una hoja de cálculo pero mucho más potente y con relaciones entre tablas). Este documento usa la sintaxis de **PostgreSQL** concretamente (no SQL Server), que es la que has practicado.

## 10.2 La estructura básica: SELECT, FROM, WHERE, ORDER BY, LIMIT

```sql
SELECT nombre, precio
FROM productos
WHERE precio > 10
ORDER BY precio DESC
LIMIT 5;
```

- `SELECT` indica **qué columnas** quieres ver en el resultado. `SELECT *` significa "todas las columnas".
- `FROM` indica **de qué tabla** quieres sacar los datos.
- `WHERE` indica una **condición de filtrado**: solo aparecerán en el resultado las filas que cumplan esa condición.
- `ORDER BY` indica **cómo ordenar** el resultado. `DESC` significa descendente (de mayor a menor); `ASC` (que es el valor por defecto si no escribes nada) significa ascendente (de menor a mayor).
- `LIMIT` indica cuántas filas como máximo quieres que te devuelva la consulta.

Puedes dar un nombre alternativo (un "alias") a una columna en el resultado usando `AS`:

```sql
SELECT nombre AS producto, precio AS precio_venta
FROM productos;
```

## 10.3 Condiciones más habituales en `WHERE`

```sql
WHERE precio BETWEEN 10 AND 50    -- el valor está entre 10 y 50, AMBOS incluidos
WHERE pais IN ('Italia', 'Francia', 'España')   -- el valor está DENTRO de esa lista de opciones
WHERE nombre LIKE 'A%'             -- el texto empieza por "A". El símbolo % significa "cualquier cosa aquí"
WHERE columna IS NULL               -- la columna NO tiene ningún valor (está vacía)
WHERE columna IS NOT NULL           -- la columna SÍ tiene un valor
```

⚠️ Un detalle importante sobre los valores `NULL` (que representan "sin dato", no es lo mismo que cero o texto vacío): cuando comparas algo con `NULL` usando `=` o `!=`, el resultado nunca es verdadero ni falso, es también `NULL`, y esa fila simplemente desaparece del resultado sin ningún aviso de error. Por eso hace falta usar específicamente `IS NULL` / `IS NOT NULL` para comprobar si algo está vacío.

---

# 11. SQL — AGREGACIÓN

## 11.1 Funciones de agregación

Una función de agregación toma muchas filas y las resume en un único valor.

```sql
COUNT(*)             -- cuenta cuántas filas hay
COUNT(columna)        -- cuenta cuántas filas tienen esa columna CON valor (ignora los NULL)
COUNT(DISTINCT columna)  -- cuenta cuántos valores DIFERENTES hay en esa columna (sin repetir)
SUM(columna)           -- suma todos los valores de esa columna
AVG(columna)           -- calcula la media (promedio)
MIN(columna)            -- el valor más pequeño
MAX(columna)            -- el valor más grande
```

⚠️ La diferencia entre `COUNT(*)` y `COUNT(columna)` es clave: `COUNT(*)` cuenta filas sin mirar si hay `NULL` o no; `COUNT(columna)` solo cuenta las filas donde esa columna concreta tiene un valor real (no nulo).

## 11.2 `GROUP BY` — agrupar filas

`GROUP BY` junta todas las filas que comparten el mismo valor en una columna (o combinación de columnas), para poder aplicar una función de agregación a cada grupo por separado.

```sql
SELECT pais, COUNT(*) AS num_clientes
FROM clientes
GROUP BY pais;
```

Esto da una fila por cada país distinto, con el número de clientes de ese país.

## 11.3 `HAVING` — filtrar sobre los grupos ya agregados

```sql
SELECT pais, COUNT(*) AS num_clientes
FROM clientes
GROUP BY pais
HAVING COUNT(*) >= 5;
```

Aquí está la diferencia clave que suele salir en examen: **`WHERE` filtra filas individuales antes de agrupar**; **`HAVING` filtra los grupos ya calculados, después de agregar**. Por eso, si quieres filtrar por el resultado de un `COUNT()`, `SUM()`, etc., tienes que usar `HAVING`, porque en el momento en el que se evalúa el `WHERE`, esos totales todavía no existen (WHERE se ejecuta antes de que se calculen las agregaciones).

---

# 12. SQL — COMBINACIÓN DE TABLAS (JOINs)

## 12.1 ¿Qué es un JOIN?

Un "JOIN" (unión, aunque en SQL "unión" también significa otra cosa distinta con `UNION`, así que mejor pensarlo como "combinación" o "cruce" de tablas) sirve para juntar datos de dos tablas distintas que están relacionadas entre sí mediante una columna en común (normalmente un identificador, como `cliente_id`).

## 12.2 `INNER JOIN` — solo las coincidencias

`INNER JOIN` devuelve **únicamente** las filas donde hay coincidencia en ambas tablas. Si una fila de una tabla no tiene pareja en la otra, no aparece en el resultado.

```sql
SELECT p.nombre AS producto, c.nombre AS categoria
FROM productos p
INNER JOIN categorias c ON p.categoria_id = c.id;
```

`p` y `c` son alias (nombres cortos) para las tablas `productos` y `categorias`, para no tener que escribir el nombre completo cada vez. La condición después de `ON` indica cómo se relacionan ambas tablas: la columna `categoria_id` de `productos` tiene que coincidir con la columna `id` de `categorias`.

Si el nombre de la columna de unión es exactamente igual en las dos tablas, puedes usar `USING` en vez de `ON`, que además evita que esa columna salga duplicada en el resultado:

```sql
SELECT *
FROM pedidos
INNER JOIN detalle_pedidos USING(pedido_id);
```

## 12.3 `LEFT JOIN` — todas las de la izquierda, tengan pareja o no

`LEFT JOIN` devuelve **todas** las filas de la tabla de la izquierda (la que va justo después de `FROM`), aunque no tengan ninguna coincidencia en la tabla de la derecha. Cuando no hay coincidencia, las columnas de la tabla derecha aparecen como `NULL`.

```sql
SELECT c.nombre, COUNT(p.id) AS num_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.nombre;
```

Esto sirve, por ejemplo, para encontrar clientes que **nunca** han hecho un pedido: como se conserva la fila del cliente aunque no tenga ningún pedido asociado, ese cliente sigue apareciendo en el resultado.

⚠️ Aquí es clave la diferencia entre `COUNT(*)` y `COUNT(p.id)` que vimos antes: si usas `COUNT(*)`, un cliente sin pedidos contaría como si tuviera 1 pedido (porque `COUNT(*)` cuenta la fila entera, aunque esté rellena de `NULL` por el `LEFT JOIN`). Si usas `COUNT(p.id)`, como `p.id` sería `NULL` para ese cliente, `COUNT` lo ignora y da correctamente 0.

## 12.4 `RIGHT JOIN` y `FULL JOIN`

`RIGHT JOIN` es exactamente igual que `LEFT JOIN` pero al revés: conserva todas las filas de la tabla de la derecha. En la práctica casi nunca hace falta, porque cualquier `RIGHT JOIN` se puede escribir como un `LEFT JOIN` cambiando el orden de las tablas.

`FULL JOIN` conserva **todas** las filas de **ambas** tablas, tengan coincidencia o no. Donde no hay coincidencia por un lado, esos campos salen como `NULL`.

```sql
SELECT COALESCE(a.pais, b.pais) AS pais, a.num_clientes, b.num_proveedores
FROM clientes_por_pais a
FULL JOIN proveedores_por_pais b ON a.pais = b.pais;
```

`COALESCE(valor1, valor2, ...)` es una función que devuelve el **primer valor que no sea `NULL`** de la lista que le pases. Aquí se usa porque, en un `FULL JOIN`, la columna de país puede venir vacía por el lado `a` o por el lado `b` según el caso, así que `COALESCE` coge el que sí tenga valor.

## 12.5 `SELF JOIN` — una tabla unida consigo misma

Un `SELF JOIN` es cuando unes una tabla consigo misma, algo útil, por ejemplo, cuando una tabla de empleados tiene una columna `jefe_id` que apunta a otro empleado de la misma tabla (el jefe).

```sql
SELECT e.nombre AS empleado, j.nombre AS jefe
FROM empleados e
LEFT JOIN empleados j ON e.jefe_id = j.id;
```

Aquí la tabla `empleados` aparece dos veces en la consulta, una vez con el alias `e` (representando al empleado) y otra con el alias `j` (representando a su jefe). Como es literalmente la misma tabla física, los alias dejan de ser opcionales: sin ellos, SQL no sabría a cuál de las dos "copias" te refieres en cada columna.

## 12.6 `CROSS JOIN` — todas las combinaciones posibles

`CROSS JOIN` combina cada fila de una tabla con **todas** las filas de la otra tabla, generando el llamado "producto cartesiano" (todas las combinaciones posibles entre ambos conjuntos). Se usa, por ejemplo, para construir una "rejilla" completa de categoría × año, de forma que aunque una categoría no haya vendido nada en un año concreto, esa combinación exista igualmente (con un 0), en vez de faltar directamente en el resultado.

```sql
SELECT cat.nombre, a.anio, COALESCE(v.total, 0) AS facturacion
FROM categorias cat
CROSS JOIN anios a
LEFT JOIN ventas v ON v.categoria_id = cat.id AND v.anio = a.anio;
```

El patrón típico es: primero un `CROSS JOIN` para generar el "esqueleto" con todas las combinaciones posibles, y después un `LEFT JOIN` para "colgar" los datos reales sobre ese esqueleto. Si lo haces al revés, las combinaciones sin datos reales nunca llegarían a aparecer.

---

# 13. SQL — OPERADORES DE CONJUNTO

Estos operadores combinan el resultado de dos consultas `SELECT` completas, en vez de combinar tablas por una columna en común como hacen los JOIN. Para poder usarlos, ambas consultas tienen que devolver el mismo número de columnas, en el mismo orden y con tipos compatibles.

```sql
SELECT nombre FROM clientes
UNION
SELECT nombre FROM proveedores;
```

`UNION` junta los resultados de ambas consultas en uno solo, y **elimina los duplicados** automáticamente (esto tiene un coste extra de procesamiento, porque tiene que comparar todas las filas entre sí para saber cuáles son iguales).

```sql
SELECT nombre FROM clientes
UNION ALL
SELECT nombre FROM proveedores;
```

`UNION ALL` hace lo mismo pero **sin eliminar duplicados**, así que es más rápido. Se usa `UNION ALL` en vez de `UNION` siempre que no importe (o directamente interese) que puedan salir filas repetidas.

```sql
SELECT pais FROM clientes
EXCEPT
SELECT pais FROM proveedores;
```

`EXCEPT` devuelve los valores que están en el primer resultado **pero no** en el segundo (una especie de resta de conjuntos).

```sql
SELECT pais FROM clientes
INTERSECT
SELECT pais FROM proveedores;
```

`INTERSECT` devuelve solo los valores que aparecen en **ambos** resultados a la vez.

---

# 14. SQL — SUBCONSULTAS Y CTE

## 14.1 ¿Qué es una subconsulta?

Una subconsulta es una consulta `SELECT` colocada dentro de otra consulta, entre paréntesis. Sirve para calcular algo intermedio que necesitas para resolver la consulta principal.

### Subconsulta escalar (devuelve un único valor)

```sql
SELECT nombre, precio, (SELECT AVG(precio) FROM productos) AS precio_medio
FROM productos
WHERE precio > (SELECT AVG(precio) FROM productos);
```

Una subconsulta "escalar" es aquella que devuelve exactamente **una fila y una columna** (un único valor), por eso se puede usar en cualquier sitio donde iría un valor normal, como dentro de un `WHERE` o de un `SELECT`.

### Subconsulta en `FROM` (tabla derivada)

```sql
SELECT cliente_id, AVG(total_pedido) AS ticket_medio
FROM (
    SELECT cliente_id, pedido_id, SUM(importe) AS total_pedido
    FROM detalle_pedidos
    GROUP BY cliente_id, pedido_id
) AS pedidos_agregados
GROUP BY cliente_id;
```

Aquí la subconsulta interior calcula primero el total de cada pedido individual, y la consulta exterior calcula la media de esos totales por cliente. Esto se llama agregación "en dos niveles". ⚠️ En PostgreSQL, toda subconsulta usada dentro de un `FROM` **necesita obligatoriamente un alias** (aquí, `AS pedidos_agregados`), aunque no lo uses en ningún otro sitio; si lo olvidas, PostgreSQL da el error `subquery in FROM must have an alias`.

### Subconsulta correlacionada

Una subconsulta "correlacionada" es una subconsulta que, dentro de sí misma, hace referencia a una columna de la consulta exterior. Esto hace que, conceptualmente, la subconsulta se vuelva a ejecutar una vez por cada fila de la consulta principal (lo cual la hace potente pero más costosa de ejecutar en tablas muy grandes).

```sql
SELECT p.nombre, p.precio, p.categoria_id
FROM productos p
WHERE p.precio = (
    SELECT MAX(p2.precio)
    FROM productos p2
    WHERE p2.categoria_id = p.categoria_id
);
```

Aquí, para cada producto `p` de la consulta exterior, la subconsulta calcula cuál es el precio máximo **dentro de su misma categoría** (fíjate en `p2.categoria_id = p.categoria_id`, esa es la "correlación": la subconsulta usa un dato de la fila exterior). El resultado son los productos que tienen el precio más alto de su propia categoría.

### Anti-join con `NOT EXISTS`

```sql
SELECT c.nombre
FROM clientes c
WHERE NOT EXISTS (
    SELECT 1 FROM pedidos p WHERE p.cliente_id = c.id
);
```

Esto devuelve los clientes para los que **no existe** ningún pedido asociado. `EXISTS` comprueba solo si la subconsulta devuelve alguna fila o ninguna (no le importa qué valores devuelva exactamente, por eso dentro se suele poner `SELECT 1`, un valor cualquiera, solo como comprobación de existencia).

⚠️ Alternativa con el mismo objetivo: `NOT IN`. Pero tiene una trampa peligrosa: si la subconsulta usada con `NOT IN` puede devolver algún valor `NULL`, el resultado completo de la consulta sale **vacío, sin ningún mensaje de error** que te avise del problema. Por eso, cuando se trata de comprobar "que no exista relación", `NOT EXISTS` es la opción más segura.

## 14.2 CTE (Common Table Expression) — la cláusula `WITH`

Una CTE es una forma de dar nombre a una subconsulta y definirla **antes** de la consulta principal, para que el código se lea de arriba abajo como una receta, en vez de tener que descifrarlo de dentro hacia fuera como pasa con las subconsultas anidadas.

```sql
WITH ventas_por_cliente AS (
    SELECT cliente_id, SUM(importe) AS total
    FROM pedidos
    GROUP BY cliente_id
),
clasificados AS (
    SELECT *, NTILE(4) OVER (ORDER BY total DESC) AS cuartil
    FROM ventas_por_cliente
)
SELECT cuartil, COUNT(*) AS num_clientes, SUM(total) AS facturacion
FROM clasificados
GROUP BY cuartil;
```

`WITH nombre AS (...)` define una CTE llamada `nombre`, cuyo contenido es el resultado de la consulta entre paréntesis. Puedes encadenar varias CTE separadas por comas, y cada una puede usar las que se definieron antes que ella (aquí, `clasificados` usa `ventas_por_cliente`). `NTILE(4)` es una función que reparte las filas en 4 grupos de tamaño lo más parecido posible (aquí, 4 cuartiles según la facturación).

---

# 15. SQL — FUNCIONES DE VENTANA (WINDOW FUNCTIONS)

## 15.1 ¿Qué es una función de ventana?

Una función de ventana calcula un valor para cada fila **teniendo en cuenta un grupo de filas relacionadas** (su "ventana"), pero, a diferencia de `GROUP BY`, **no reduce el número de filas del resultado**: cada fila original sigue apareciendo, solo que ahora con una columna extra calculada sobre su ventana.

La sintaxis general es: `FUNCION() OVER (PARTITION BY columna ORDER BY otra_columna)`.

- `PARTITION BY` divide las filas en grupos (parecido a `GROUP BY`, pero sin fusionar filas).
- `ORDER BY`, dentro del `OVER`, indica el orden en el que se van "recorriendo" las filas dentro de cada partición, algo necesario para funciones que dependen del orden, como un ranking o un acumulado.

## 15.2 Funciones de ranking

```sql
SELECT categoria, producto, facturacion,
       RANK() OVER (PARTITION BY categoria ORDER BY facturacion DESC) AS posicion
FROM productos_facturacion;
```

`RANK()` asigna una posición a cada fila dentro de su partición, según el orden indicado. Las tres funciones de ranking se diferencian en cómo tratan los empates:

- `ROW_NUMBER()`: da un número distinto y consecutivo a cada fila, sin importar si hay empates (dos filas empatadas reciben números distintos igualmente, uno detrás de otro).
- `RANK()`: si dos filas empatan, ambas reciben la misma posición, pero la siguiente posición "salta" el hueco correspondiente (por ejemplo, dos empatados en el puesto 2 hacen que el siguiente sea el puesto 4, no el 3).
- `DENSE_RANK()`: igual que `RANK()`, pero sin dejar huecos en la numeración (después de dos empatados en el puesto 2, el siguiente sería el puesto 3).

## 15.3 Totales acumulados y medias móviles

```sql
SELECT mes, facturacion,
       SUM(facturacion) OVER (ORDER BY mes) AS acumulado,
       AVG(facturacion) OVER (ORDER BY mes ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS media_movil_3m
FROM ventas_mensuales;
```

`SUM(...) OVER (ORDER BY mes)`, sin especificar nada más, calcula por defecto la suma de todas las filas desde el principio hasta la fila actual (según el orden indicado), lo cual da exactamente un "total acumulado" o *running total*.

Para una **media móvil** (la media de, por ejemplo, los últimos 3 meses incluyendo el actual), ese comportamiento por defecto no sirve, así que hay que declarar explícitamente el "marco" (*frame*) de la ventana con `ROWS BETWEEN`. `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` significa "las 2 filas anteriores más la fila actual" (3 filas en total).

## 15.4 `LAG()` y `LEAD()` — comparar con la fila anterior o siguiente

```sql
SELECT mes, facturacion,
       LAG(facturacion) OVER (ORDER BY mes) AS mes_anterior
FROM ventas_mensuales;
```

`LAG(columna)` te trae el valor de esa columna de la fila **anterior** (según el `ORDER BY` de la ventana); `LEAD(columna)` haría lo mismo pero con la fila **siguiente**. Se usan mucho para calcular variaciones entre un periodo y el anterior. La primera fila no tiene "fila anterior", así que `LAG()` devuelve `NULL` en ese caso.

## 15.5 Por qué no se puede filtrar directamente una función de ventana con `WHERE`

Las funciones de ventana se calculan **después** de que el `WHERE` ya se ha aplicado (en el orden interno en que la base de datos procesa una consulta, `WHERE` va antes que las funciones de ventana). Por eso, si quieres quedarte, por ejemplo, solo con "los 3 productos más vendidos de cada categoría" usando `RANK()`, no puedes escribir `WHERE RANK() <= 3` directamente. La solución es calcular el ranking dentro de una CTE o subconsulta, y filtrar en la consulta exterior, donde el ranking ya existe como una columna normal:

```sql
WITH ranking AS (
    SELECT categoria, producto, facturacion,
           RANK() OVER (PARTITION BY categoria ORDER BY facturacion DESC) AS posicion
    FROM productos_facturacion
)
SELECT * FROM ranking WHERE posicion <= 3;
```

---

# 16. SQL — FECHAS, TEXTO Y PIVOTADO

## 16.1 Funciones de fecha

```sql
EXTRACT(YEAR FROM fecha)     -- saca el año de una fecha, como número
DATE_TRUNC('month', fecha)   -- "trunca" la fecha al inicio de su mes (útil para agrupar por mes)
```

## 16.2 Funciones de texto

```sql
CONCAT(nombre, ' ', apellido)     -- une varios textos en uno solo
nombre || ' ' || apellido          -- forma alternativa de concatenar en PostgreSQL, con el operador ||
UPPER(texto)                        -- convierte a mayúsculas
LOWER(texto)                        -- convierte a minúsculas
TRIM(texto)                         -- quita espacios sobrantes al principio y al final
SUBSTRING(texto, 1, 3)               -- extrae 3 caracteres empezando en la posición 1
REPLACE(texto, '-', '.')              -- sustituye un carácter (o trozo de texto) por otro
```

## 16.3 `CASE WHEN` — lógica condicional dentro de una consulta

`CASE WHEN` es el equivalente en SQL al `if/elif/else` de Python: permite crear una columna cuyo valor depende de una condición.

```sql
SELECT nombre, stock,
       CASE WHEN stock = 0 THEN 'CRÍTICO' ELSE 'AVISO' END AS situacion
FROM productos;
```

Se lee: "para cada fila, si `stock` es igual a 0, el valor de `situacion` es 'CRÍTICO'; si no, es 'AVISO'". Se pueden encadenar varios `WHEN` seguidos, igual que varios `elif` en Python.

## 16.4 Pivotado — convertir filas en columnas

"Pivotar" significa transformar datos que están organizados en filas (por ejemplo, una fila por cada combinación de categoría y año) en una tabla donde cada año se convierte en su propia columna. En SQL estándar esto se consigue combinando una función de agregación con una condición:

```sql
SELECT categoria,
       SUM(CASE WHEN anio = 1997 THEN importe ELSE 0 END) AS f_1997,
       SUM(CASE WHEN anio = 1998 THEN importe ELSE 0 END) AS f_1998
FROM ventas
GROUP BY categoria;
```

Esto suma `importe` solo cuando `anio` es 1997 (y pone 0 en caso contrario, así que no afecta a la suma), y lo mismo para 1998. PostgreSQL además ofrece una sintaxis más moderna y legible, específica de esta base de datos, usando `FILTER`:

```sql
SELECT categoria,
       SUM(importe) FILTER (WHERE anio = 1997) AS f_1997,
       SUM(importe) FILTER (WHERE anio = 1998) AS f_1998
FROM ventas
GROUP BY categoria;
```

## 16.5 Un apunte importante sobre precisión numérica

Las columnas de tipo `real` (un tipo de dato numérico "de coma flotante") pueden acumular pequeños errores de redondeo cuando sumas muchas filas, porque internamente no representan los decimales de forma exacta. Para cálculos de dinero, es importante convertir ("castear") esos valores al tipo `numeric` antes de operar, usando `::numeric`:

```sql
ROUND((precio_unitario::numeric) * cantidad * (1 - descuento::numeric), 2)
```

`columna::tipo` es la forma que tiene PostgreSQL de decir "trata este valor como si fuera de este otro tipo". Sin este casteo, sumar miles de filas en `real` puede dar un resultado ligeramente distinto (y "incorrecto" para efectos contables) del que se obtiene sumando en `numeric`.

---

# 17. SCALA — FUNDAMENTOS

## 17.1 `val` frente a `var`: inmutabilidad

En Scala hay dos formas de declarar una variable, y la diferencia es fundamental para el examen:

```scala
val nombre = "Ana"     // val = "value", INMUTABLE: una vez asignado, no se puede cambiar
var puntuacion = 10      // var = "variable", MUTABLE: se puede reasignar más adelante
```

"Inmutable" significa que, una vez que le has dado un valor a esa variable, ya no puedes cambiarlo nunca más durante la ejecución del programa. Si lo intentas:

```scala
val nombre = "Ana"
nombre = "Otro"   // ERROR: reassignment to val
```

Scala directamente da un error de compilación, con el mensaje "reassignment to val" ("reasignación a un val"), porque estás intentando hacer algo que va en contra de la naturaleza de un `val`.

En cambio, con `var` sí puedes cambiar el valor guardado:

```scala
var puntuacion = 10
puntuacion = puntuacion + 5   // esto es válido, puntuacion ahora vale 15
```

En Scala, la recomendación general (y el estilo que se espera que uses salvo que sea estrictamente necesario lo contrario) es usar siempre `val`, y reservar `var` solo para los casos en los que de verdad necesitas que un valor cambie con el tiempo (como un contador dentro de un bucle `while`).

## 17.2 Tipos de datos e inferencia de tipos

Los tipos básicos en Scala son parecidos a los de Python, pero con nombres distintos y empezando con mayúscula:

```scala
val entero: Int = 5
val decimal: Double = 3.14159265358979323846
val flotante: Float = 3.14159265358979323846f
val activo: Boolean = true
val texto: String = "hola"
```

La parte `: Int`, `: Double`, etc., después del nombre de la variable, es la **declaración explícita del tipo**: le estás diciendo a Scala qué tipo de dato vas a guardar ahí. Pero Scala también tiene "inferencia de tipos" (*type inference*), lo que significa que si no escribes el tipo, el propio compilador lo deduce automáticamente a partir del valor que le das:

```scala
val entero = 5          // Scala deduce que es Int
val decimal = 3.14       // Scala deduce que es Double
```

Ambas formas son válidas y hacen exactamente lo mismo; la diferencia es solo si escribes el tipo tú explícitamente o dejas que Scala lo adivine.

⚠️ Diferencia entre `Double` y `Float`: ambos representan números decimales, pero `Double` guarda muchos más decimales de precisión que `Float`. Si usas un número con muchos decimales y lo guardas como `Float`, perderás precisión respecto a guardarlo como `Double`.

## 17.3 Tipado estático

Scala es un lenguaje de "tipado estático", lo que significa que el tipo de cada variable se comprueba **antes** de ejecutar el programa (durante la compilación). Esto es diferente de Python, que es de "tipado dinámico" (el tipo se comprueba mientras el programa se está ejecutando). La ventaja del tipado estático es que muchos errores de tipo (por ejemplo, intentar meter un texto donde se espera un número) se detectan antes de que el programa llegue siquiera a ejecutarse, en vez de fallar a mitad de la ejecución como podría pasar en Python.

---

# 18. SCALA — FUNCIONES

```scala
def bust(puntuacion: Int): Boolean = {
  puntuacion > 21
}
```

Desglosando esto:
- `def` es la palabra clave para definir una función (igual que en Python).
- `bust` es el nombre de la función.
- `(puntuacion: Int)` es el parámetro que recibe, y aquí sí es obligatorio declarar su tipo (`Int`).
- `: Boolean` después del paréntesis indica el **tipo del valor que la función devuelve**.
- Dentro de las llaves `{ }` va el cuerpo de la función. En Scala **no hace falta escribir la palabra `return`**: el valor de la última expresión que se evalúa dentro del bloque es automáticamente lo que la función devuelve.

Si el cuerpo de la función es una sola línea, se puede escribir de forma más corta, sin llaves:

```scala
def maxHand(a: Int, b: Int): Int = if (a > b) a else b
```

Aquí `if (a > b) a else b` no es una instrucción de control de flujo normal como en Python: en Scala, `if/else` es una **expresión**, lo que significa que produce un valor por sí misma, que se puede usar directamente (aquí, para devolverlo como resultado de la función). Esto es distinto de Python, donde `if/else` es una instrucción que ejecuta un bloque u otro, pero no "vale" nada por sí misma (en Python, para conseguir un efecto parecido, se usaría un operador ternario aparte).

---

# 19. SCALA — COLECCIONES (ARRAY Y LIST)

## 19.1 `Array` — mutable en contenido, tamaño fijo

Un `Array` en Scala es una colección de tamaño fijo (no puedes añadirle ni quitarle elementos una vez creado) pero cuyo **contenido sí se puede modificar** (puedes cambiar qué valor hay en cada posición).

```scala
val jugadores = Array("Alex", "Chen", "Marta")
jugadores(0) = "Sindhu"   // esto SÍ funciona, aunque "jugadores" esté declarado con val
```

Esto puede parecer contradictorio con lo que dijimos sobre `val`, pero no lo es: lo que `val` protege es la **variable en sí** (no puedes hacer que `jugadores` pase a apuntar a un array distinto), pero no protege el contenido del array al que apunta. Es decir, `val` impide reasignar la variable completa, pero no impide modificar lo que hay dentro del objeto si ese objeto (como el `Array`) es mutable por su propia naturaleza.

```scala
jugadores(0) = 500   // ERROR de tipos: el array es de tipo Array[String], no admite un número entero ahí
```

Para crear un array vacío indicando su tamaño y tipo:

```scala
val vacio = new Array[Int](4)   // crea Array(0, 0, 0, 0) -> los Int se inicializan automáticamente a 0
```

`jugadores.length` te da el número de elementos del array.

## 19.2 `List` — inmutable de verdad

Una `List` en Scala es una colección **inmutable**: ni el contenido, ni el tamaño, se pueden cambiar una vez creada.

```scala
val jugadores = List("Alex", "Chen", "Marta")
```

Para "añadir" un elemento al principio, se usa el operador `::` (llamado "cons", de *construct*), pero en realidad esto **no modifica la lista original**, sino que crea una lista **completamente nueva**:

```scala
val nuevaLista = "Sindhu" :: jugadores
```

Después de esto, `jugadores` sigue teniendo exactamente los mismos tres elementos de antes, sin ningún cambio; `nuevaLista` es un objeto distinto, nuevo, que contiene "Sindhu" seguido de los elementos de `jugadores`.

Para concatenar (unir) dos listas completas entre sí, se usa `:::`:

```scala
val lista1 = List("Ana", "Luis")
val lista2 = List("Pedro", "Sofia")
val todos = lista1 ::: lista2   // List("Ana", "Luis", "Pedro", "Sofia"), lista1 y lista2 siguen intactas
```

`Nil` representa la **lista vacía**, y se usa como "base" para construir listas manualmente encadenando `::`:

```scala
val construida = "Ana" :: "Luis" :: "Marta" :: Nil
```

Esto se lee de derecha a izquierda: empiezas con la lista vacía (`Nil`), le añades "Marta" delante, luego "Luis" delante de esa, y luego "Ana" delante de todo, resultando en `List("Ana", "Luis", "Marta")`.

`lista.reverse` te da una nueva lista con el orden invertido; `lista.length` te da el número de elementos.

## 19.3 La diferencia clave entre `Array` y `List`

`Array` es de tamaño fijo pero contenido mutable (puedes cambiar los valores de dentro). `List` es completamente inmutable (ni el contenido ni el tamaño cambian nunca; cualquier operación que "parezca" modificarla, en realidad crea una lista nueva y deja la original tal cual).

---

# 20. SCALA — CONTROL DE FLUJO Y ESTILO FUNCIONAL

## 20.1 El bucle `while` (estilo imperativo)

```scala
var i = 0
while (i < jugadores.length) {
  println(jugadores(i))
  i = i + 1
}
```

Esto funciona igual que en Python: mientras la condición `i < jugadores.length` se cumpla, se repite el bloque. Fíjate en que hace falta declarar `i` como `var` (no como `val`), porque dentro del bucle se reasigna su valor en cada vuelta (`i = i + 1`); si `i` fuera un `val`, esa línea daría el mismo error de "reassignment to val" que vimos antes. Este estilo, en el que dependes de una variable mutable (`var i`) que vas cambiando manualmente para controlar el bucle, se llama "estilo imperativo": le vas diciendo al programa, paso a paso, exactamente qué hacer y cuándo parar.

## 20.2 `foreach` (estilo funcional)

```scala
jugadores.foreach(j => println(j))
```

`foreach` es un método de las colecciones (arrays, listas...) que recibe una función y la ejecuta una vez por cada elemento de la colección, sin que tú tengas que gestionar ningún contador ni ninguna variable mutable: Scala se encarga internamente de recorrer todos los elementos. `j => println(j)` es una función anónima (parecida a las lambdas de Python): `j` es el nombre que le damos, dentro de esa función, a "cada elemento de la colección, uno por uno", y `println(j)` es lo que se hace con él.

Si la función que le pasas a `foreach` ya existe con ese nombre, puedes pasársela directamente sin necesidad de escribir la flecha `=>`:

```scala
jugadores.foreach(bust)   // aplica la función bust a cada elemento
```

Este estilo, en el que describes **qué** quieres hacer con cada elemento sin gestionar manualmente el recorrido (sin contador, sin variable mutable), se llama "estilo funcional".

## 20.3 Comparación directa: `while` frente a `foreach`

La diferencia práctica más importante para el examen es esta: la versión con `while` necesita una variable mutable (`var i`) que actúa como contador y que hay que incrementar manualmente en cada vuelta; la versión con `foreach` no necesita ningún contador ni ninguna variable mutable, porque el propio método se encarga de recorrer la colección internamente. Por eso `while` se considera el estilo más "imperativo" (más cercano a dar instrucciones paso a paso) y `foreach` el estilo más "funcional" (más cercano a describir qué transformación u operación quieres aplicar).

## 20.4 Efectos secundarios (side effects)

Un "efecto secundario" ocurre cuando una función modifica algo que existe **fuera** de ella (por ejemplo, una variable `var` global), en vez de limitarse a recibir datos y devolver un resultado nuevo.

```scala
var total = 0

def sumarAlTotal(valor: Int) = {
  total = total + valor   // esto modifica una variable que está FUERA de la función -> efecto secundario
}
```

Frente a esto, una función "pura" (sin efectos secundarios) solo trabaja con lo que recibe como parámetros y devuelve un resultado nuevo, sin tocar nada externo:

```scala
def sumar(a: Int, b: Int): Int = {
  a + b   // no modifica nada fuera de la función, solo devuelve un valor nuevo
}
```

El estilo funcional que se recomienda en el curso prioriza este segundo tipo de funciones, sin efectos secundarios, porque son más fáciles de entender, de probar y de combinar entre sí sin sorpresas.

## 20.5 Operadores relacionales y lógicos

Son los mismos conceptos que en Python, pero con distinta forma de escribirlos:

```scala
>, <, >=, <=, ==, !=   // comparación (igual que en Python)
&&                        // "y" lógico (equivalente a "and" en Python)
||                        // "o" lógico (equivalente a "or" en Python)
!                         // negación (equivalente a "not" en Python)
```

---

# 21. ÍNDICE DE EJERCICIOS DEL PROFESOR

Esta sección te sirve para localizar, dentro de tus propios ejercicios ya resueltos, dónde está trabajado cada concepto de este manual, por si necesitas ver un ejemplo más largo y aplicado.

### Scala — 15 ejercicios del capítulo 3

- **Ejercicios 1–3**: `val`/`var`, inferencia de tipos, `Double` vs `Float`.
- **Ejercicios 4–6**: funciones (`bust`, `maxHand`, `ganador`), combinación de condiciones con `if/elif/else`.
- **Ejercicios 7–9**: `Array`, mutabilidad del contenido, creación con `new Array[Int](n)`, recorrido con `while`.
- **Ejercicios 10–11**: `List`, inmutabilidad, `::`, `:::`, `Nil`.
- **Ejercicio 12**: operadores relacionales y lógicos.
- **Ejercicios 13–14**: `foreach` frente a `while`, efectos secundarios frente a funciones puras.
- **Ejercicio 15**: proyecto integrado que combina todo lo anterior (torneo de Twenty-One).

### Scala — Parte 3 (mini proyectos con sbt)

- **Parte 3.1** (VS Code + Metals): clasificador de resultados de un torneo, con funciones `bust`, `estadoMano`, `mejorMano`, recorrido con `while` y comparación con `foreach`.
- **Parte 3.2** (IntelliJ IDEA): analizador de calificaciones de un grupo, con funciones `aprobado`, `estadoNota`, `maxNota`, `clasificacion`, y comparación entre dos evaluaciones.

### SQL — 20 consultas sobre la base de datos Northwind

- **Preguntas 1–3**: `WHERE`, `BETWEEN`, `GROUP BY`, `HAVING`, `CASE WHEN`, cuidado con `NULL` en comparaciones entre columnas.
- **Preguntas 4–6**: `INNER JOIN` (con varias tablas), `USING`, agregación combinada con `JOIN` y `HAVING`.
- **Preguntas 7–10**: `LEFT JOIN`, `SELF JOIN`, `CROSS JOIN`, `FULL JOIN`, `COALESCE`.
- **Preguntas 11–12**: `UNION ALL`, `EXCEPT`, `INTERSECT`.
- **Preguntas 13–15**: subconsultas con `NOT EXISTS`, subconsulta escalar, subconsulta en `FROM` con agregación en dos niveles.
- **Preguntas 16–17**: subconsultas correlacionadas, CTE encadenadas, `NTILE()`.
- **Preguntas 18–20**: funciones de ventana (`RANK()`, `PARTITION BY`, `LAG()`, medias móviles), pivotado con `FILTER`/`CASE WHEN`.

### Python — 20 ejercicios (de listas a pandas)

- **Ejercicios 1–4**: listas, slicing con paso, listas anidadas, copia frente a referencia (`=` vs `list()`/`[:]`), métodos de lista (`.pop()`, `.sort()`, `.insert()`).
- **Ejercicios 5–7**: funciones con valores por defecto, tuplas y desempaquetado, `import`, módulo propio (`sys.path.append`).
- **Ejercicios 8–11**: NumPy: vectorización, arrays 2D, máscaras booleanas, estadística descriptiva, reproducibilidad con semillas.
- **Ejercicios 12–15**: diccionarios anidados, creación de DataFrames, `pd.read_csv`, `.loc`/`.iloc`, columnas calculadas, `.groupby()`/`.agg()`.
- **Ejercicios 16–18**: operadores de comparación y lógicos, `and`/`or` frente a `&`/`|` en NumPy y pandas, filtrado de DataFrames (`.isin()`, `.between()`, `.query()`).
- **Ejercicios 19–20**: bucles (`while`, `for`, `enumerate`, `.items()`, `.iterrows()`), construcción de diccionarios resumen con bucles frente a `.groupby()`.

---

# 22. TEMARIO DE LOS CURSOS DE DATACAMP

Esta lista te sirve para comprobar que ya has repasado, dentro de este manual, cada punto del temario de los cursos que has hecho.

### SQL Fundamentals

Consultas básicas (`SELECT`, `FROM`, `LIMIT`, alias), filtrado (`WHERE`, comparadores, `AND`/`OR`, `BETWEEN`, `IN`, `LIKE`, `NULL`), ordenación (`ORDER BY`), funciones de agregación, `GROUP BY`/`HAVING`, los seis tipos de `JOIN`, operadores de conjunto, subconsultas (en `SELECT`, `FROM`, `WHERE`), subconsultas correlacionadas, `CASE WHEN`, CTE (`WITH`), funciones de ventana (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `PARTITION BY`, `LAG`/`LEAD`, acumulados y medias móviles), fechas (`EXTRACT`) y texto (`CONCAT`, `UPPER`, `LOWER`, `SUBSTRING`, `TRIM`, `REPLACE`).

### Introduction to Python

Operadores aritméticos, variables, tipos primitivos y casting, listas (creación, listas anidadas, indexado, slicing, modificar/combinar/eliminar elementos), funciones y métodos integrados (`len`, `type`, `max`, `min`, `round`, `.upper()`, `.count()`, `.index()`, `.append()`, `.reverse()`), paquetes (`import`), NumPy 1D y 2D, operaciones vectorizadas, `.shape`, indexado 2D, estadística básica con NumPy.

### Intermediate Python

Matplotlib (`plt.plot()`, `plt.scatter()`, `plt.hist()`, personalización de gráficos), diccionarios, DataFrames de pandas (creación, `pd.read_csv()`, `[]`, `[[]]`, `.loc[]`, `.iloc[]`), operadores de comparación y booleanos (incluyendo la versión vectorial con NumPy), `if`/`elif`/`else`, filtrado de DataFrames con máscaras booleanas, bucles (`while`, `for`, `.items()`, `np.nditer()`, `.iterrows()`), números aleatorios y simulación (`numpy.random`, random walk, Monte Carlo).

### Introduction to Python for Developers

Tipos primitivos, listas, tuplas, diccionarios, conjuntos (sets), `if`/`elif`/`else`, bucles con `break`/`continue`, funciones con parámetros y valores por defecto, ámbito de variables (local/global), clases y objetos, `__init__`, atributos y métodos, herencia, manejo de excepciones (`try`/`except`/`else`/`finally`), lectura y escritura de archivos con `with open(...)`.

### Intermediate Python for Developers

`*args` y `**kwargs`, funciones como valores de primera clase, funciones lambda, `map()`/`filter()`/`reduce()`, métodos mágicos (`__repr__`, `__str__`, `__len__`, `__eq__`), `@property`, `@classmethod`, `@staticmethod`, generadores y `yield`, expresiones generadoras, decoradores personalizados, organización de módulos/paquetes (`__init__.py`), pruebas unitarias con `unittest`, buenas prácticas PEP 8 y *type hinting*.

### Introduction to Scala

Uso del intérprete, `val` frente a `var`, tipos principales (`Int`, `Double`, `Boolean`, `String`) e inferencia de tipos, formas de ejecutar Scala (scripts frente a aplicaciones compiladas), definición de funciones, `Array` (mutable, tamaño fijo) y `List` (inmutable, `::`, `:::`), tipado estático frente a dinámico, `if/else` como expresión, bucle `while`, refactorización de `while` a `foreach` como transición al estilo funcional idiomático de Scala.

---
