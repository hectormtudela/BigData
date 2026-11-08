# 📋Clase 19 - OOP Parte 2

# Preparación de la carpeta de la clase

El entorno virtual, el `.gitignore`, el `requirements.txt` y el `README.md` común ya se crearon en la Clase 18. En esta clase solo se crea la carpeta nueva.

1. En VS Code y ejecuta `git pull`.
2. Comprueba que la terminal muestra `(.venv)`.
3. Crea la carpeta de la clase con su estructura interna:
```powershell
mkdir clase_19_detalles_clases_objetos\teoria
mkdir clase_19_detalles_clases_objetos\ejercicios_basicos
mkdir clase_19_detalles_clases_objetos\ejercicios_intermedios
mkdir clase_19_detalles_clases_objetos\ejercicios_avanzados
mkdir clase_19_detalles_clases_objetos\caso_estudio
```
4. Copia los documentos de la clase en su sitio:
- `clase_19_01_teoria_detalles_clases_objetos.md` (este documento) → dentro de `teoria/`.
- `clase_19_02_ejercicios_detalles_clases_objetos.md` → en la raíz de `clase_19_detalles_clases_objetos/`.
5. Crea el `README.md` de la clase con las casillas de progreso, igual que en la Clase 18.
6. Añade la fila de la clase al `README.md` común:
```markdown
| 19 | Detalles de clases y objetos | `clase_19_detalles_clases_objetos/` |
```
7. Haz el primer commit de la clase:
```powershell
git add .
git commit -m "clase 19: estructura de la clase"
git push
```
---

# Sesión 01: Detalles de clases y objetos

> En la Clase 18 se vio cómo definir clases, crear objetos, escribir métodos y representar objetos como texto. Esta clase profundiza en los **detalles** que distinguen un código orientado a objetos profesional:

- Cómo se nombran los **identificadores** y qué significa cada guion bajo.
- **Quién puede llamar a quién**: funciones globales, métodos de instancia y funciones definidas en la clase.
- Cómo enseñar a Python a **usar ****`+`****, , ****`<`****, ****`==`****, ****`in`**** o ****`len()`**** con nuestras propias clases**.
- Por qué en Python **todo es un objeto**.
- Cómo añadir y quitar atributos sobre la marcha.
- Cómo convertir objetos de nuestras clases en tipos nativos y viceversa.
---

## Sección 1. Convenciones de nombres de los identificadores

### Definición

> Un **identificador** es el nombre que damos a una variable, función, método, clase o atributo. Python no obliga a seguir un estilo concreto, pero la comunidad sigue unas **convenciones** que comunican la intención del programador. Al leer `self.__token` o `_reintentos`, cualquier desarrollador sabe, sin leer más, si ese atributo es para usarlo desde fuera o no.

---

| Tipo de identificador | Convención | Ejemplos |
| --- | --- | --- |
| Variables, funciones, métodos y atributos | `snake_case`, en minúsculas | `filas_cargadas`, `calcular_iva()` |
| Variable que se usa y se descarta | Un solo guion bajo: `_` | `for _ in range(3):` |
| Clases | `PascalCase`, primera letra en mayúscula | `TareaIngesta`, `ConexionProveedor` |
| Público | Empieza por letra | `endpoint`, `conectar()` |
| Uso interno («protegido») | Empieza por **un** guion bajo | `_reintentos`, `_registrar_reintento()` |
| Privado | Empieza por **dos** guiones bajos | `__token`, `__token_valido()` |
| Nombres especiales del lenguaje | Empiezan **y** terminan por dos guiones bajos | `__init__()`, `__str__()`, `__add__()` |

---

Puntos clave:

- **Público**: se puede usar desde dentro y desde fuera de la clase.
- **Uso interno o **«protegido»** (****`_nombre`****)**: es solo un aviso para otros programadores: «esto es un detalle interno, no lo uses desde fuera». Python **no lo impide**.
- **Privado (****`__nombre`****)**: Python aplica un mecanismo llamado **name mangling** (alteración del nombre). Dentro de la clase `ConexionProveedor`, el atributo `__token` se guarda realmente como `_ConexionProveedor__token`. Desde fuera, `objeto.__token` no existe y da `AttributeError`. No es una protección absoluta, pero evita usos accidentales.
- **Nombres especiales (****`__nombre__`****)**: los define el lenguaje. **No se llaman directamente**: Python los llama por nosotros. `__init__` se ejecuta al crear un objeto y `__str__` al hacer `print(objeto)`.
---

### Analogía de la vida diaria

![Imagen](images/clase-19-oop-parte-2/image-001.png)

---

### Sintaxis

```python
class NombreClase:                       # PascalCase
    def __init__(self, dato, secreto):   # método especial: lo llama Python
        self.dato = dato                 # público
        self._interno = 0                # uso interno (convención)
        self.__secreto = secreto         # privado: se guarda como _NombreClase__secreto

    def metodo_publico(self):
        ...

    def _metodo_interno(self):
        ...

    def __metodo_privado(self):            # se guarda como _NombreClase__metodo_privado
        ...

for _ in range(3):                         # _ : variable que no se va a usar
    ...
```

---

### Ejemplo 1.1 · Conexión a la API de un proveedor logístico

Una empresa de **Ingeniería de Datos** necesita conectarse a las APIs de diferentes proveedores logísticos para consultar información sobre envíos y entregas.

Para gestionar estas conexiones, se desarrolla una clase llamada `ConexionProveedor` que almacena el nombre del proveedor, la dirección de su API (*endpoint*) y un token de autenticación.

El objetivo es aplicar las **convenciones de nombres , **diferenciando entre atributos y métodos públicos, de uso interno y privados.

---

La clase debe permitir:

- Consultar el nombre del proveedor y su endpoint.
- Almacenar el token como atributo privado (`__token`).
- Validar internamente que el token tenga al menos 12 caracteres.
- Registrar los intentos de conexión fallidos.
- Realizar una conexión simulada mediante el método público `conectar()`.
> Se crearán dos proveedores, uno con un token válido y otro con un token incorrecto, para comprobar cómo se gestionan las conexiones y los reintentos.

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_1_1_convenciones_nombres.py`

---

```python
class ConexionProveedor:
    def __init__(self, proveedor, endpoint, token):
        self.proveedor = proveedor              # público
        self.endpoint = endpoint                # público
        self._reintentos = 0                    # uso interno (convención)
        self.__token = token                    # privado (name mangling)

    def __token_valido(self):                   # método privado
        return len(self.__token) >= 12

    def _registrar_reintento(self):             # método de uso interno
        self._reintentos += 1

    def conectar(self):                         # método público
        if not self.__token_valido():
            self._registrar_reintento()
            return f"{self.proveedor}: token no válido (reintentos:{self._reintentos})"
        return f"{self.proveedor}: conectado a{self.endpoint}"

aws = ConexionProveedor("logistica_sur", "https://api.logsur.com/v1", "tk_9f8e7d6c5b4a")
mal = ConexionProveedor("transportes_rio", "https://api.trio.es/v3", "tk_123")

print(aws.conectar())
print(mal.conectar())
print(mal.conectar())

for _ in range(3):
    print("-", end="")
print()
```

**Salida esperada:**

```plain text
logistica_sur: conectado a https://api.logsur.com/v1
transportes_rio: token no válido (reintentos: 1)
transportes_rio: token no válido (reintentos: 2)
---
```

---

**Highlights:**

8. Desde fuera de la clase solo se usa el método público `conectar()`. Es la «puerta de entrada» del objeto.
9. Dentro de la clase, los métodos usan sin problema `self.__token` y `self.__token_valido()`: el doble guion bajo no limita el acceso **desde dentro** de la propia clase.
10. El token de `logistica_sur` tiene 15 caracteres y es válido. El de `transportes_rio` tiene 6, así que cada intento suma un reintento en `_reintentos`.
11. El bucle `for _ in range(3)` repite tres veces sin usar la variable de control. El nombre `_` comunica justo eso.
---

### Ejemplo 1.2 · Name mangling: qué ocurre con `__token`

Una empresa de **Ingeniería de Datos** necesita proteger los tokens utilizados para conectarse a las APIs de sus proveedores logísticos, evitando que otros programadores accedan a ellos accidentalmente.

Para ello, se utiliza una clase llamada `ConexionProveedor`, que almacena el token como atributo privado mediante el prefijo de doble guion bajo (`__token`).

El objetivo es comprender cómo funciona el mecanismo de **name mangling** en Python y qué diferencias existen entre los atributos públicos, de uso interno y privados.

---

El ejemplo debe permitir:

- Inspeccionar los atributos reales del objeto mediante `vars()`.
- Comprobar que los atributos con un guion bajo (`_reintentos`) pueden consultarse directamente.
- Mostrar una versión enmascarada del token mediante un método público, dejando visibles únicamente sus tres primeros caracteres.
- Acceder al token utilizando el nombre generado por *name mangling* (`_ConexionProveedor__token`).
- Comprobar qué ocurre al intentar acceder directamente a `__token` desde fuera de la clase.
---

> Se creará una conexión con el proveedor `logistica_sur` y se realizarán diferentes consultas para observar cómo Python almacena y permite acceder a sus atributos.

**Pregunta clave:** ¿El doble guion bajo (`__`) hace que un atributo sea realmente inaccesible desde fuera de la clase, o simplemente modifica su nombre para evitar accesos accidentales?

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_1_2_name_mangling.py`

---

```python
class ConexionProveedor:
    def __init__(self, proveedor, token):
        self.proveedor = proveedor
        self._reintentos = 0
        self.__token = token

    def token_enmascarado(self):
        return self.__token[:3] + "*" * (len(self.__token) - 3)

c = ConexionProveedor("logistica_sur", "tk_9f8e7d6c5b4a")

print(vars(c))
print(c._reintentos)
print(c.token_enmascarado())
print(c._ConexionProveedor__token)
print(c.__token)
```

**Salida esperada:**

```plain text
{'proveedor': 'logistica_sur', '_reintentos': 0, '_ConexionProveedor__token': 'tk_9f8e7d6c5b4a'}
0
tk_************
tk_9f8e7d6c5b4a
Traceback (most recent call last):
  ...
AttributeError: 'ConexionProveedor' object has no attribute '__token'
```

---

**Highlights:**

12. `vars(c)` revela cómo se guardan realmente los atributos: `__token` aparece como `_ConexionProveedor__token`.
13. `c._reintentos` funciona. El guion bajo simple es solo una convención y Python no lo bloquea.
14. `token_enmascarado()` es la forma correcta de ofrecer el dato hacia fuera: el método público decide qué se muestra.
15. `c._ConexionProveedor__token` funciona porque usa el nombre real. Es posible, pero es **mala práctica**: se salta la intención de quien diseñó la clase.
16. `c.__token` falla: fuera de la clase ese nombre no existe. El programa se detiene con un `AttributeError`.
---

> En Data Engineering, las credenciales, cadenas de conexión y contadores internos de una clase se declaran con `_` o `__`. Lo que otros módulos del pipeline deben usar se expone con métodos públicos.

---

---

## Sección 2. Funciones globales, métodos de instancia y funciones de la clase

>
### Definición

En un programa con clases conviven tres tipos de funciones:

| Tipo | Dónde se define | Recibe `self` | Cómo se llama |
| --- | --- | --- | --- |
| **Función global** | Fuera de cualquier clase | No | `funcion()` |
| **Método de instancia** | Dentro de la clase | Sí | `objeto.metodo()` |
| **Función de la clase** 
(método de clase) | Dentro de la clase, **sin** `self` | No | `Clase.funcion()` |

---

> Una función de la clase no necesita los datos de ningún objeto: sirve para operaciones que pertenecen al concepto de la clase en general (su versión, los formatos que admite, una constante calculada…).

---

Reglas de llamada:

- Una **función global** puede llamar a métodos de instancia (a través de un objeto) y a funciones de la clase (a través del nombre de la clase). El siguiente ejemplo muestra cómo una función global puede llamar a métodos de una clase y cómo los métodos pueden llamar a otras funciones o métodos.
- Un **método** puede llamar a funciones globales directamente por su nombre.
- Dentro de una clase, un método **no** puede llamar a otro método solo por su nombre: necesita `self.metodo()` o `Clase.funcion()`. Si se escribe solo `metodo()`, Python lo busca como función global y da `NameError`.
- Una función de la clase **sin** `self` no se puede llamar desde un objeto: `objeto.funcion()` le pasa el objeto como primer argumento y da `TypeError`.
---

El siguiente ejemplo muestra cómo una función global puede llamar a métodos de una clase y cómo los métodos pueden llamar a otras funciones o métodos.

```python
# Función global
def saludar():
    print("Hola desde la función global")


class Ejemplo:

    # Método de instancia
    def metodo1(self):
        print("Ejecutando método 1")
        saludar()                  # Llama a una función global
        self.metodo2()            # Llama a otro método de instancia

    # Método de instancia
    def metodo2(self):
        print("Ejecutando método 2")

    # Función definida en la clase (sin self)
    def funcion():
        print("Función de la clase")


# Función global
def ejecutar():
    obj = Ejemplo()

    obj.metodo1()                 # Correcto: método de instancia
    Ejemplo.funcion()            # Correcto: función de la clase


ejecutar()
```

**Salida esperada:**

```plain text
Ejecutando método 1
Hola desde la función global
Ejecutando método 2
Función de la clase
```

---

### Resumen de las reglas

| Desde | Llamada | Resultado |
| --- | --- | --- |
| Función global | `obj.metodo1()` | Correcto |
| Función global | `Ejemplo.funcion()` | Correcto |
| Método de instancia | `saludar()` | Correcto |
| Método de instancia | `self.metodo2()` | Correcto |
| Método de instancia | `metodo2()` | `NameError` |
| Código externo | `obj.funcion()` | `TypeError` |

---

```python
obj = Ejemplo()

# ERROR 1: llamar a otro método sin self
# Dentro de metodo1(), escribir:
# metodo2()                 → NameError

# ERROR 2: llamar desde un objeto a una función sin self
obj.funcion()                # TypeError
```

> **Nota importante:** En Python moderno, si queremos definir una función asociada a una clase que no necesita `self`, lo recomendable es utilizar el decorador `@staticmethod`. Así podremos llamarla tanto con `Ejemplo.funcion()` como con `obj.funcion()` sin provocar un error.

---

### Sintaxis

```python
def funcion_global():
    ...

class NombreClase:
    def metodo_instancia(self, dato):
        funcion_global()              # un método puede usar funciones globales
        self.otro_metodo()            # otro método del mismo objeto: con self.

    def funcion_de_clase():           # sin self
        ...

objeto = NombreClase()
objeto.metodo_instancia(1)            # correcto
NombreClase.funcion_de_clase()        # correcto
objeto.funcion_de_clase()             # TypeError
```

---

### Ejemplo 2.1 · Sistema de alertas de un pipeline

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_2_1_funciones_y_metodos.py`

Una empresa de **Ingeniería de Datos** necesita desarrollar un sistema de notificaciones para informar sobre incidencias que se producen durante la ejecución de sus pipelines de datos, como retrasos en las cargas o problemas de almacenamiento.

Para ello, se utiliza una clase llamada `Notificador`, encargada de enviar mensajes de alerta a un canal de comunicación, como Slack o Teams.

El objetivo es comprender **cómo interactúan las funciones globales con los métodos de instancia y las funciones definidas dentro de una clase**.

---

El sistema debe permitir:

- Mostrar una cabecera común mediante la función global `cabecera()`.
- Crear notificadores asociados a diferentes canales de comunicación.
- Enviar mensajes mediante el método de instancia `enviar()`, utilizando `self` para acceder al canal.
- Mostrar la versión del sistema mediante la función `version()`, definida dentro de la clase sin `self`.
- Procesar una lista de alertas mediante la función global `procesar_alertas()`, que utiliza las funciones y métodos de la clase.
---

> Se creará un notificador asociado al canal `slack#datos` para comunicar dos incidencias: un retraso en la carga de ventas y un disco que ha alcanzado el 91 % de ocupación.

**Pregunta clave:** ¿Cómo puede una función global llamar a los métodos de un objeto y a las funciones de una clase? ¿Y cómo puede un método de instancia llamar a una función global?

---

```python
def cabecera():                                   # función global
    print("=== Sistema de alertas ===")

class Notificador:
    def __init__(self, canal):
        self.canal = canal

    def enviar(self, mensaje):                    # método de instancia: recibe self
        cabecera()                                # llama a una función global
        print(f"[{self.canal}]{mensaje}")

    def version():                                # función de la clase: sin self
        cabecera()
        print("Notificador v2.4")

def procesar_alertas(notificador, alertas):       # función global
    Notificador.version()                         # llama a la función de la clase
    for alerta in alertas:
        notificador.enviar(alerta)                # llama al método de instancia

slack = Notificador("slack#datos")
procesar_alertas(slack, ["Carga de ventas retrasada", "Disco al 91 %"])
```

**Salida esperada:**

```plain text
=== Sistema de alertas ===
Notificador v2.4
=== Sistema de alertas ===
[slack#datos] Carga de ventas retrasada
=== Sistema de alertas ===
[slack#datos] Disco al 91 %
```

---

**Highlights:**

17. `procesar_alertas` es una función global que recibe un objeto `Notificador` y una lista de textos.
18. Primero llama a `Notificador.version()` usando el nombre de la clase, porque `version` no tiene `self`.
19. Después recorre las alertas y llama a `notificador.enviar(alerta)`: Python pasa `slack` como `self`.
20. Tanto `version()` como `enviar()` llaman a la función global `cabecera()` directamente por su nombre.
---

### Ejemplo 2.2 · Llamar a una función de la clase desde un objeto

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_2_2_error_llamada.py`

Una empresa de **Ingeniería de Datos** utiliza una clase llamada `Notificador` para gestionar las alertas de sus pipelines.

La clase contiene una función `version()` que devuelve la versión actual del sistema de notificaciones.

Un programador necesita consultar esta información y prueba dos formas diferentes de llamar a la función:

- **Desde la clase:** utilizando `Notificador.version()`.
- **Desde un objeto:** creando un notificador para el canal `email` y utilizando `n.version()`.
---

Aunque ambas llamadas utilizan la misma función, **la primera funciona correctamente y la segunda produce un error**.

El objetivo del ejemplo es comprender cómo Python realiza las llamadas a funciones definidas dentro de una clase y por qué, cuando se invocan desde un objeto, Python pasa automáticamente la instancia como primer argumento.

**Pregunta clave:** ¿Por qué se produce un `TypeError` al ejecutar `n.version()`? ¿Qué relación tiene este error con el parámetro `self` de los métodos de instancia?

---

```python
class Notificador:
    def __init__(self, canal):
        self.canal = canal

    def version():
        return "Notificador v2.4"

n = Notificador("email")
print(Notificador.version())
print(n.version())
```

**Salida esperada:**

```plain text
Notificador v2.4
Traceback (most recent call last):
  ...
TypeError: Notificador.version() takes 0 positional arguments but 1 was given
```

---

**Highlights:**

21. `Notificador.version()` funciona: se llama a través de la clase y no recibe ningún argumento.
22. `n.version()` se traduce internamente a `Notificador.version(n)`. Python le pasa el objeto `n` como primer argumento, pero `version` no tiene ningún parámetro que lo reciba.
23. El mensaje del error lo explica: la función admite 0 argumentos posicionales y ha recibido 1.
---

**Errores típicos de llamada:**

| Código | Error | Causa | Corrección |
| --- | --- | --- | --- |
| `objeto.funcion_sin_self()` | `TypeError: ... takes 0 positional arguments but 1 was given` | El objeto se pasa como argumento que nadie recibe | `Clase.funcion_sin_self()` |
| Dentro de un método: `otro_metodo()` | `NameError: name 'otro_metodo' is not defined` | Python lo busca como función global | `self.otro_metodo()` |
| `Clase.metodo_con_self()` | `TypeError: ... missing 1 required positional argument: 'self'` | Falta el objeto sobre el que trabajar | `objeto.metodo_con_self()` |

---

## Sección 3. Sobrecarga de operadores

>
### Definición

Python sabe sumar dos `int` o concatenar dos `str`, pero no sabe qué significa sumar dos objetos de una clase nuestra. **Sobrecargar un operador** es definir en la clase el método especial que Python ejecuta cuando encuentra ese operador. Así, `resumen_lunes + resumen_martes` se convierte internamente en `resumen_lunes.__add__(resumen_martes)`.

> La sobrecarga hace que el código de negocio se lea de forma natural (`total = lunes + martes`, `if version_a < version_b`, `if "A-101" in lote`) y permite usar nuestras clases con funciones nativas como `sorted()`, `max()`, `min()` o `len()`.

---

Supongamos que `resumen_lunes` y `resumen_martes` son objetos de una clase `ResumenVentas` que implementa los métodos correspondientes.

| Operador | Método especial | Ejemplo con objetos |
| --- | --- | --- |
| `+` | `__add__(self, other)` | `resumen_lunes.__add__(resumen_martes)` |
| `-` | `__sub__(self, other)` | `resumen_lunes.__sub__(resumen_martes)` |
| `*` | `__mul__(self, other)` | `resumen_lunes.__mul__(resumen_martes)` |
| `/` | `__truediv__(self, other)` | `resumen_lunes.__truediv__(resumen_martes)` |
| `//` | `__floordiv__(self, other)` | `resumen_lunes.__floordiv__(resumen_martes)` |
| `%` | `__mod__(self, other)` | `resumen_lunes.__mod__(resumen_martes)` |
| `**` | `__pow__(self, other)` | `resumen_lunes.__pow__(resumen_martes)` |

---

Supongamos que tenemos dos objetos de la clase `VersionPipeline`, llamados `version_a` y `version_b`.

| Operador | Método especial | Ejemplo con objetos |
| --- | --- | --- |
| `<` | `__lt__(self, other)` | `version_a.__lt__(version_b)` |
| `>` | `__gt__(self, other)` | `version_a.__gt__(version_b)` |
| `<=` | `__le__(self, other)` | `version_a.__le__(version_b)` |
| `>=` | `__ge__(self, other)` | `version_a.__ge__(version_b)` |
| `==` | `__eq__(self, other)` | `version_a.__eq__(version_b)` |
| `!=` | `__ne__(self, other)` | `version_a.__ne__(version_b)` |

---

Supongamos que tenemos dos objetos de la clase `ResumenVentas`, llamados `resumen_total` y `resumen_martes`.

| Operador | Método especial | Ejemplo con objetos |
| --- | --- | --- |
| `+=` | `__iadd__(self, other)` | `resumen_total.__iadd__(resumen_martes)` |
| `-=` | `__isub__(self, other)` | `resumen_total.__isub__(resumen_martes)` |
| `*=` | `__imul__(self, other)` | `resumen_total.__imul__(resumen_martes)` |
| `/=` | `__itruediv__(self, other)` | `resumen_total.__itruediv__(resumen_martes)` |
| `//=` | `__ifloordiv__(self, other)` | `resumen_total.__ifloordiv__(resumen_martes)` |
| `%=` | `__imod__(self, other)` | `resumen_total.__imod__(resumen_martes)` |
| `**=` | `__ipow__(self, other)` | `resumen_total.__ipow__(resumen_martes)` |

> Una operación como `resumen_total += resumen_martes` utiliza `__iadd__()` cuando está disponible y asigna a `resumen_total` el valor devuelto por el método. Si `__iadd__()` no está implementado, Python puede recurrir a `__add__()` y sus mecanismos alternativos.

---

Supongamos que `lote` es un objeto de la clase `LoteDatos` y `registro` es otro objeto que representa un registro.

| Expresión | Método especial | Ejemplo con objetos |
| --- | --- | --- |
| `registro in lote` | `__contains__(self, x)` | `lote.__contains__(registro)` |
| `len(lote)` | `__len__(self)` | `lote.__len__()` |

---

### Enunciado

Una empresa de **Ingeniería de Datos** necesita combinar los resúmenes de ventas generados diariamente por sus pipelines.

Cada resumen se representa mediante un objeto de la clase `ResumenVentas`, que almacena el importe total de ventas de un día.

El objetivo es implementar el método especial `__add__()` para permitir sumar dos objetos `ResumenVentas` utilizando directamente el operador `+`.

---

```python
class ResumenVentas:
    def __init__(self, total):
        self.total = total

    def __add__(self, other):
        return ResumenVentas(self.total + other.total)


# Crear dos objetos
resumen_lunes = ResumenVentas(100)
resumen_martes = ResumenVentas(200)

# Forma habitual: utilizando el operador +
resultado1 = resumen_lunes + resumen_martes

# Forma explícita: llamando al método especial
resultado2 = resumen_lunes.__add__(resumen_martes)

# Mostrar resultados
print(resultado1.total)
print(resultado2.total)
```

### Salida esperada

```plain text
300
300
```

---

**Highlights:**

24. La clase `ResumenVentas` dispone de un atributo `total` que almacena el importe de las ventas.
25. Se crean dos objetos: `resumen_lunes` con 100 y `resumen_martes` con 200.
26. El método especial `__add__()` define cómo se suman dos objetos de la clase.
27. Cuando Python encuentra `resumen_lunes + resumen_martes`, llama al método `__add__()` del primer objeto, pasando el segundo como argumento.
28. Dentro del método se suman `self.total` y `other.total`.
29. El método devuelve un nuevo objeto `ResumenVentas` cuyo atributo `total` contiene 300.
---

Cuando escribimos:

```python
resultado = resumen_lunes + resumen_martes
```

Python ejecuta conceptualmente:

```python
resultado = resumen_lunes.__add__(resumen_martes)
```

Dentro del método:

```python
def __add__(self, other):
    return ResumenVentas(self.total + other.total)
```

- `self` hace referencia al objeto `resumen_lunes`.
- `other` hace referencia al objeto `resumen_martes`.
- `self.total` contiene `100`.
- `other.total` contiene `200`.
- Se crea un nuevo objeto `ResumenVentas(300)`.
---

| Operador | Método especial | Expresión habitual | Llamada equivalente |
| --- | --- | --- | --- |
| `+` | `__add__()` | `lunes + martes` | `lunes.__add__(martes)` |
| `<` | `__lt__()` | `version_a < version_b` | `version_a.__lt__(version_b)` |
| `+=` | `__iadd__()` | `total += martes` | `total = total.__iadd__(martes)` |
| `in` | `__contains__()` | `registro in lote` | `lote.__contains__(registro)` |
| `len()` | `__len__()` | `len(lote)` | `lote.__len__()` |

> **Nota:** estas equivalencias representan el funcionamiento básico de los métodos especiales cuando están implementados. Python puede utilizar otros mecanismos, como métodos reflejados, cuando corresponde.

---

### Idea clave

> **La sobrecarga de operadores permite definir cómo se comportan los operadores de Python cuando trabajan con objetos de nuestras propias clases.**

En lugar de escribir:

```python
resultado = resumen_lunes.sumar(resumen_martes)
```

Podemos escribir:

```python
resultado = resumen_lunes + resumen_martes
```

Esto hace que nuestro código sea más natural, expresivo y fácil de leer.

---

Detalles importantes:

- Los métodos aritméticos **devuelven un objeto nuevo** y no modifican los operandos.
- Los métodos de asignación compuesta (`__iadd__`, `__isub__`…) **modifican el propio objeto** y deben terminar con `return self`. Si no se definen, `a += b` usa `__add__` y crea un objeto nuevo.
- Si se define `__eq__`, Python obtiene `!=` automáticamente negando su resultado.
- `sorted()`, `min()` y `max()` solo necesitan que la clase sepa comparar con `<` (`__lt__`).
**¿Qué operadores conviene sobrecargar?** Solo aquellos cuyo significado sea **evidente** para el negocio. Sumar dos resúmenes de carga o comparar dos versiones de un esquema es natural. Multiplicar dos clientes no lo es.

---

### Sintaxis

```python
class NombreClase:
    def __add__(self, otro):            # objeto + otro
        return NombreClase(...)         # devuelve un objeto NUEVO

    def __lt__(self, otro):             # objeto < otro
        return True o False

    def __iadd__(self, otro):           # objeto += otro
        ...                             # modifica self
        return self

    def __contains__(self, elemento):   # elemento in objeto
        return True o False

    def __len__(self):                  # len(objeto)
        return numero_entero
```

---

### Ejemplo 3.1 · Sumar y comparar resúmenes de carga

**Enunciado**

Una empresa de **Ingeniería de Datos** ejecuta cada noche un pipeline que procesa las ventas del día y las almacena en un Data Warehouse.

Al finalizar cada ejecución, el pipeline genera un resumen con tres indicadores:

- **Filas:** número de registros procesados.
- **Rechazadas:** número de registros que no pudieron cargarse por errores de calidad.
- **Megas:** volumen de datos procesados en MB.
El equipo necesita analizar los resultados de diferentes días, calcular diferencias entre ejecuciones y estimar el volumen de datos que podría procesarse durante un mes.

---

Para ello, se desarrolla una clase llamada `ResumenCarga` que utiliza la **sobrecarga de operadores** para realizar operaciones directamente entre objetos.

La clase debe permitir:

30. **Sumar dos resúmenes (****`__add__`****):** combinar los resultados de dos días, acumulando las filas, los rechazos y los megabytes procesados.
31. **Restar dos resúmenes (****`__sub__`****):** calcular las diferencias entre las ejecuciones de dos días.
32. **Multiplicar un resumen (****`__mul__`****):** estimar los resultados de varios días a partir de un resumen diario y un factor numérico.
33. **Mostrar un resumen (****`__str__`****):** presentar los resultados de forma legible cuando se utiliza `print()`.
---

Se dispone de los resultados de dos ejecuciones del pipeline:

| Indicador | Lunes | Martes |
| --- | --- | --- |
| Filas procesadas | 120.000 | 98.500 |
| Filas rechazadas | 35 | 12 |
| Volumen (MB) | 48,60 | 40,15 |

---

Utilizando los objetos `lunes` y `martes`, se realizarán las siguientes operaciones:

- `lunes + martes`: obtener el total acumulado de ambos días.
- `lunes - martes`: conocer las diferencias entre las dos ejecuciones.
- `martes * 30`: proyectar los resultados de 30 días suponiendo que diariamente se procesa la misma cantidad de datos que el martes.
- `lunes.__add__(martes)`: comprobar que llamar directamente al método especial produce el mismo resultado que utilizar el operador `+`.
---

**Pregunta clave:** ¿Cómo consigue Python sumar, restar y multiplicar objetos de una clase creada por nosotros? ¿Qué papel desempeñan los métodos especiales `__add__()`, `__sub__()` y `__mul__()`?

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_3_1_resumen_carga.py`

---

```python
class ResumenCarga:
    def __init__(self, filas=0, rechazadas=0, megas=0.0):
        self.filas = filas
        self.rechazadas = rechazadas
        self.megas = megas

    def __add__(self, otro):
        return ResumenCarga(self.filas + otro.filas,
                            self.rechazadas + otro.rechazadas,
                            round(self.megas + otro.megas, 2))

    def __sub__(self, otro):
        return ResumenCarga(self.filas - otro.filas,
                            self.rechazadas - otro.rechazadas,
                            round(self.megas - otro.megas, 2))

    def __mul__(self, factor):
        return ResumenCarga(self.filas * factor,
                            self.rechazadas * factor,
                            round(self.megas * factor, 2))

    def __str__(self):
        return f"filas={self.filas:,} rechazadas={self.rechazadas} megas={self.megas}"

lunes = ResumenCarga(120_000, 35, 48.6)
martes = ResumenCarga(98_500, 12, 40.15)

semana = lunes + martes
diferencia = lunes - martes
proyeccion_mes = martes * 30

print("Total     :", semana)
print("Diferencia:", diferencia)
print("Proyección:", proyeccion_mes)
print("Equivale a:", lunes.__add__(martes))
```

**Salida esperada:**

```plain text
Total     : filas=218,500 rechazadas=47 megas=88.75
Diferencia: filas=21,500 rechazadas=23 megas=8.45
Proyección: filas=2,955,000 rechazadas=360 megas=1204.5
Equivale a: filas=218,500 rechazadas=47 megas=88.75
```

---

**Highlights:**

34. `lunes + martes` ejecuta `lunes.__add__(martes)`: `self` es `lunes` y `otro` es `martes`. Devuelve un `ResumenCarga` **nuevo**; `lunes` y `martes` no cambian.
35. `lunes - martes` ejecuta `__sub__` de la misma forma.
36. `martes * 30` ejecuta `martes.__mul__(30)`. El segundo operando no tiene por qué ser de la misma clase: aquí es un número.
37. La última línea demuestra que el operador `+` y la llamada explícita a `__add__` son equivalentes. En la práctica siempre se usa el operador.
38. `{self.filas:,}` muestra el número con separador de miles.
---

### Ejemplo 3.2 · Comparar versiones de un esquema de datos

Una empresa de **Ingeniería de Datos** utiliza diferentes aplicaciones para producir y consumir eventos de datos. Para garantizar que estas aplicaciones puedan intercambiar información correctamente, cada esquema de datos tiene asignado un número de versión.

Las versiones siguen el formato **mayor.menor.parche**, por ejemplo, `2.10.0`, donde:

- **Mayor:** indica cambios importantes en la estructura del esquema.
- **Menor:** indica cambios menores, como la incorporación de nuevos campos.
- **Parche:** indica pequeñas correcciones o ajustes.
---

El equipo necesita comparar las versiones utilizadas por los productores y consumidores de datos para identificar cuáles son más recientes, cuáles son anteriores y cuáles son iguales.

Para ello, se desarrolla una clase llamada `VersionEsquema` que utiliza la **sobrecarga de operadores de comparación**.

---

La clase debe permitir:

39. **Comparar igualdad (****`__eq__`****):** determinar si dos objetos representan la misma versión mediante `==`.
40. **Comparar versiones anteriores (****`__lt__`****):** identificar si una versión es menor que otra mediante `<`.
41. **Comparar versiones posteriores (****`__gt__`****):** identificar si una versión es mayor que otra mediante `>`.
42. **Representar versiones (****`__repr__`****):** mostrar los objetos con un formato legible, como `v2.10.0`.
---

Se dispone de las siguientes versiones:

| Objeto | Versión | Descripción |
| --- | --- | --- |
| `productor` | `2.10.0` | Versión utilizada por el productor de datos |
| `consumidor` | `2.9.3` | Versión utilizada por el consumidor |
| `copia` | `2.10.0` | Otro objeto con la misma versión del productor |

---

El programa debe realizar las siguientes comprobaciones:

- Comparar `productor == copia` y `productor is copia` para distinguir entre **igualdad de valores e identidad de objetos**.
- Comprobar si las versiones del productor y del consumidor son diferentes mediante `!=`.
- Determinar qué versión es anterior o posterior utilizando `<` y `>`.
- Ordenar una lista de versiones mediante `sorted()`.
- Identificar la versión más reciente utilizando `max()`.
---

**Pregunta clave:** ¿Cómo podemos conseguir que Python compare y ordene correctamente objetos que representan versiones de esquemas de datos, utilizando operadores como `==`, `<` y `>`?

**Importante:** las versiones deben compararse utilizando sus componentes numéricos y no como cadenas de texto. Además, que una versión sea más reciente no garantiza por sí solo que sea compatible con otra aplicación.

Un productor de datos publica eventos con un esquema versionado (`mayor.menor.parche`). Los consumidores deben saber si su versión es anterior o posterior a la del productor.

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_3_2_version_esquema.py`

---

```python
class VersionEsquema:
    def __init__(self, mayor, menor, parche):
        self.mayor = mayor
        self.menor = menor
        self.parche = parche

    def __eq__(self, otra):
        return (self.mayor, self.menor, self.parche) == (otra.mayor, otra.menor, otra.parche)

    def __lt__(self, otra):
        return (self.mayor, self.menor, self.parche) < (otra.mayor, otra.menor, otra.parche)

    def __gt__(self, otra):
        return (self.mayor, self.menor, self.parche) > (otra.mayor, otra.menor, otra.parche)

    def __repr__(self):
        return f"v{self.mayor}.{self.menor}.{self.parche}"

productor = VersionEsquema(2, 10, 0)
consumidor = VersionEsquema(2, 9, 3)
copia = VersionEsquema(2, 10, 0)

print(productor == copia)
print(productor is copia)
print(productor != consumidor)
print(consumidor < productor)
print(productor > consumidor)

historico = [VersionEsquema(1, 4, 2), VersionEsquema(2, 10, 0), VersionEsquema(2, 9, 3), VersionEsquema(1, 12, 0)]
print(sorted(historico))
print(max(historico))
```

**Salida esperada:**

```plain text
True
False
True
True
True
[v1.4.2, v1.12.0, v2.9.3, v2.10.0]
v2.10.0
```

---

**Highlights:**

43. Cada comparación construye una tupla `(mayor, menor, parche)` y compara tuplas. Python compara las tuplas elemento a elemento, que es exactamente la regla de las versiones.
44. `productor == copia` es `True` gracias a `__eq__`: tienen los mismos números. Sin embargo, `productor is copia` es `False`: son objetos distintos.
45. `!=` funciona aunque no se haya definido `__ne__`: Python niega el resultado de `__eq__`.
46. `sorted()` usa `__lt__` y `max()` usa `__gt__` para ordenar y elegir.
47. Las versiones se comparan como **números**. Si se compararan como texto, `"1.12.0" < "1.4.2"` sería `True`, porque el carácter `"1"` va antes que `"4"`. Con la clase, `v1.4.2` queda correctamente antes que `v1.12.0`.
---

### Ejemplo 3.3 · Asignación compuesta, `in` y `len()` en un lote de tickets

Una empresa de **Ingeniería de Datos** recibe diariamente miles de tickets de compra procedentes de diferentes tiendas. Antes de enviarlos al sistema central, cada tienda agrupa sus tickets en lotes para facilitar su procesamiento.

Cada ticket contiene un **identificador único (****`id`****)** y el **importe de la compra (****`importe`****)**.

Para gestionar estos datos, se desarrolla una clase llamada `LoteTickets` que almacena los tickets de cada tienda en una lista privada y utiliza la **sobrecarga de operadores** para añadir, contar y buscar tickets de forma sencilla.

---

La clase debe permitir:

48. **Añadir tickets (****`__iadd__`****):** incorporar nuevos tickets al lote utilizando el operador `+=`, sin crear un nuevo objeto.
49. **Contar tickets (****`__len__`****):** obtener el número de tickets almacenados utilizando `len()`.
50. **Buscar tickets (****`__contains__`****):** comprobar si existe un ticket con un identificador determinado mediante `in` o `not in`.
51. **Mostrar información (****`__str__`****):** presentar el nombre de la tienda y la cantidad de tickets del lote al utilizar `print()`.
---

Se creará un lote de tickets para la tienda `T-07`, inicialmente vacío, al que se añadirán las siguientes compras:

| ID del ticket | Importe (€) |
| --- | --- |
| A-100 | 23,50 |
| A-101 | 8,75 |
| A-102 | 112,00 |

---

Una vez añadidos los tickets, el programa debe:

- Mostrar el estado del lote antes y después de incorporar las compras.
- Consultar cuántos tickets contiene mediante `len(lote)`.
- Comprobar si el ticket `A-101` existe utilizando `in`.
- Comprobar si el ticket `Z-999` existe utilizando `in` y `not in`.
---

**Pregunta clave:** ¿Cómo podemos utilizar operadores como `+=`, `in` y funciones como `len()` con objetos de nuestras propias clases, de manera similar a como trabajamos con las listas de Python?

Cada tienda envía sus tickets al sistema central agrupados en lotes.

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_3_3_lote_operadores.py`

---

```python
class LoteTickets:
    def __init__(self, tienda):
        self.tienda = tienda
        self.__tickets = []

    def __iadd__(self, ticket):
        self.__tickets.append(ticket)
        return self

    def __len__(self):
        return len(self.__tickets)

    def __contains__(self, id_ticket):
        return id_ticket in [t["id"] for t in self.__tickets]

    def __str__(self):
        return f"Lote{self.tienda}:{len(self)} tickets"

lote = LoteTickets("T-07")
print(lote)

lote += {"id": "A-100", "importe": 23.5}
lote += {"id": "A-101", "importe": 8.75}
lote += {"id": "A-102", "importe": 112.0}

print(lote)
print(len(lote))
print("A-101" in lote)
print("Z-999" in lote)
print("Z-999" not in lote)
```

**Salida esperada:**

```plain text
Lote T-07: 0 tickets
Lote T-07: 3 tickets
3
True
False
True
```

**Highlights:**

52. `lote += {...}` ejecuta `lote = lote.__iadd__({...})`. El método añade el ticket a la lista privada y devuelve `self`, de modo que `lote` sigue apuntando al mismo objeto.
53. Si `__iadd__` olvidara el `return self`, devolvería `None` y la variable `lote` pasaría a valer `None`.
54. `len(lote)` ejecuta `lote.__len__()`. El propio `__str__` lo reutiliza con `len(self)`.
55. `"A-101" in lote` ejecuta `lote.__contains__("A-101")`. `not in` funciona automáticamente negando el resultado.
56. La lista `__tickets` es privada: desde fuera solo se puede añadir con `+=`, preguntar con `in` y contar con `len()`.
---

### Ejemplo 3.4 · Operadores ya sobrecargados en los tipos nativos

En Python, los tipos de datos nativos como `int`, `str`, `list` y `tuple` también son clases que tienen implementados sus propios métodos especiales.

Esto explica por qué **un mismo operador puede comportarse de manera diferente dependiendo del tipo de objeto con el que trabaje**.

Por ejemplo, el operador `+` permite sumar números, concatenar cadenas de texto o unir listas. Sin embargo, no todos los operadores están disponibles para todos los tipos de datos.

El objetivo de este ejemplo es comprender cómo Python utiliza la **sobrecarga de operadores en sus clases nativas**, sin necesidad de que nosotros implementemos los métodos especiales.

---

El programa debe permitir:

57. **Operador de suma (****`__add__`****):** comprobar cómo `+` realiza diferentes operaciones con números, cadenas, listas y tuplas.
58. **Operador de multiplicación (****`__mul__`****):** observar cómo  permite repetir cadenas de texto y listas.
59. **Llamadas explícitas:** utilizar directamente métodos como `int.__add__()`, `str.__add__()` y `list.__mul__()` para comprobar su relación con los operadores.
60. **Operaciones no permitidas:** intentar restar dos cadenas de texto y analizar el `TypeError` que produce Python.
---

Se realizarán operaciones con diferentes tipos de datos, utilizando ejemplos relacionados con números, nombres de recursos de datos, listas y fechas.

Posteriormente, se repetirán algunas operaciones llamando directamente a sus métodos especiales para comprobar que producen los mismos resultados.

Finalmente, se intentará ejecutar `"ventas" - "s"` para observar qué sucede cuando utilizamos un operador que no está implementado para un determinado tipo de dato.

**Pregunta clave:** ¿Por qué el operador `+` suma números, concatena cadenas y une listas, mientras que el operador `-` funciona con números, pero produce un error cuando intentamos restar dos cadenas de texto?

Los tipos nativos de Python también son clases con métodos especiales. Por eso el mismo `+` suma números, concatena textos y une listas.

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_3_4_operadores_nativos.py`

---

```python
print(10 + 20)
print("data" + "_" + "lake")
print([1, 2] + [3, 4])
print((2026, 10) + (29,))

print("-" * 20)
print([0] * 5)

print(int.__add__(10, 20))
print(str.__add__("data", "_lake"))
print(list.__mul__([0], 5))

print("ventas" - "s")
```

**Salida esperada:**

```plain text
30
data_lake
[1, 2, 3, 4]
(2026, 10, 29)
--------------------
[0, 0, 0, 0, 0]
30
data_lake
[0, 0, 0, 0, 0]
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

**Highlights:**

61. `+` está sobrecargado en `int`, `str`, `list` y `tuple`, con un significado distinto en cada clase: sumar, concatenar o unir.
62.  está sobrecargado en `str` y `list` para repetir su contenido.
63. Las tres llamadas explícitas (`int.__add__`, `str.__add__`, `list.__mul__`) demuestran qué método se ejecuta detrás de cada operador.
64. La clase `str` **no** define `__sub__`. Restar dos textos no tiene un significado evidente, así que Python da `TypeError`.
---

## Sección 4. Todo es un objeto

>
### Definición

En Python, **todo lo que se puede asignar a una variable es un objeto**: números, textos, listas, diccionarios, `None`, funciones, clases e incluso módulos importados. Cada objeto tiene:

- Un **tipo** (la clase a la que pertenece), que se obtiene con `type(objeto)`.
- Una **identidad**, un número único mientras el objeto existe, que se obtiene con `id(objeto)`. En CPython corresponde a su dirección de memoria.
- Un conjunto de **atributos y métodos**, que se listan con `dir(objeto)`.
---

Una variable no guarda el objeto, sino una **referencia** a él. Esto tiene consecuencias distintas según el tipo:

|  | Inmutables | Mutables |
| --- | --- | --- |
| Tipos | `int`, `float`, `complex`, `bool`, `str`, `tuple` | `list`, `dict`, `set`, objetos de nuestras clases |
| ¿Se pueden cambiar? | No. «Cambiar» el valor crea un objeto nuevo | Sí, el mismo objeto se modifica |
| Si dos variables apuntan al mismo objeto | Reasignar una no afecta a la otra | Modificar desde una se ve desde la otra |

---

### Analogía de la vida diaria

![Imagen](images/clase-19-oop-parte-2/image-002.png)

---

### Sintaxis

```python
type(objeto)              # clase del objeto
type(objeto).__name__     # nombre de la clase como texto
id(objeto)                # identidad única del objeto
dir(objeto)               # lista de atributos y métodos
a is b                    # True si id(a) == id(b)
globals()                 # diccionario con los nombres globales del programa
```

---

### Ejemplo 4.1 · El tipo de cada cosa

Una empresa de **Ingeniería de Datos** desarrolla una aplicación para gestionar información de sus proveedores logísticos. Durante el procesamiento de los datos, el programa necesita trabajar con diferentes elementos: números, textos, listas, diccionarios, funciones, clases y módulos.

Aunque estos elementos parecen muy diferentes, en Python **todos son objetos y cada uno pertenece a una clase determinada**.

El objetivo de este ejemplo es comprender el principio **«Todo es un objeto en Python»** y aprender a utilizar la función `type()` para identificar a qué clase pertenece cada elemento.

---

El programa debe permitir:

65. **Definir una clase ****`Proveedor`** y crear un objeto a partir de ella.
66. **Crear una función ****`validar_fichero()`** que compruebe si una ruta corresponde a un archivo CSV.
67. **Importar el módulo ****`math`** para comprobar que los módulos también son objetos.
68. **Almacenar diferentes elementos en una misma lista**, incluyendo tipos de datos nativos, una función, una clase, una instancia y un módulo.
69. **Recorrer la lista con un bucle ****`for`** y utilizar `type()` para mostrar la clase a la que pertenece cada elemento.
---

El programa analizará una lista que contiene diferentes tipos de datos utilizados habitualmente en aplicaciones de Ingeniería de Datos:

- **Datos simples:** números enteros, decimales, complejos, cadenas de texto y valores booleanos.
- **Colecciones:** listas, tuplas, conjuntos y diccionarios.
- **Otros objetos:** `None`, una función, una clase, una instancia de esa clase y un módulo importado.
Se utilizará `type()` para identificar el tipo de cada elemento y comprobar que incluso las funciones, las clases y los módulos son objetos en Python.

**Pregunta clave:** Si en Python todo es un objeto, ¿qué diferencia existe entre el tipo de una función, el de una clase y el de un objeto creado a partir de esa clase? ¿Por qué `type(Proveedor)` y `type(Proveedor())` devuelven resultados diferentes?

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_4_1_todo_es_objeto.py`

---

```python
import math

class Proveedor:
    pass

def validar_fichero(ruta):
    return ruta.endswith(".csv")

valores = [
    250,
    19.99,
    3 + 2j,
    "Logística Sur",
    True,
    [10, 20, 30],
    (40.41, -3.70),
    {"csv", "json"},
    {"tienda": "T-07"},
    None,
    validar_fichero,
    Proveedor,
    Proveedor(),
    math,
]

for v in valores:
    print(type(v))
```

**Salida esperada:**

```plain text
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'bool'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
<class 'NoneType'>
<class 'function'>
<class 'type'>
<class '__main__.Proveedor'>
<class 'module'>
```

---

**Highlights:**

70. Una sola lista guarda números, textos, colecciones, `None`, una función, una clase, un objeto y un módulo. Esto solo es posible porque todos son objetos.
71. La función `validar_fichero` es un objeto de la clase `function`: se puede guardar en una lista, pasar como argumento o asignar a otra variable.
72. La clase `Proveedor` es un objeto de la clase `type`. En cambio, `Proveedor()` es un objeto de la clase `Proveedor`.
73. El módulo `math` es un objeto de la clase `module`.
---

### Ejemplo 4.2 · Referencias con objetos inmutables y mutables

Una empresa de **Ingeniería de Datos** desarrolla una aplicación para configurar y supervisar sus pipelines. Durante su funcionamiento, el programa utiliza diferentes variables para almacenar límites de procesamiento, listas de columnas y umbrales de calidad de los datos.

El equipo necesita comprender qué sucede cuando **dos variables hacen referencia al mismo objeto** y cómo cambia su comportamiento dependiendo de si el objeto es mutable o inmutable.

El objetivo de este ejemplo es comprender cómo funcionan las **referencias a objetos en Python**, diferenciando entre la reasignación de variables y la modificación de objetos compartidos.

---

El programa debe permitir:

74. **Objetos inmutables (****`int`****):** asignar el mismo número a dos variables y comprobar qué ocurre cuando una de ellas recibe un nuevo valor.
75. **Objetos mutables (****`list`****):** crear dos variables que apuntan a la misma lista de columnas y observar cómo una modificación afecta a ambas.
76. **Objetos de nuestras propias clases:** crear dos instancias de la clase `Umbral` con el mismo valor y comprobar si son realmente el mismo objeto.
77. **Referencias compartidas:** asignar un objeto `Umbral` a otra variable y modificar uno de sus atributos para observar cómo afecta al objeto original.
78. **Identidad de objetos:** utilizar `is` e `id()` para comprobar cuándo dos variables hacen referencia al mismo objeto.
---

Se realizarán tres pruebas relacionadas con la configuración de un pipeline:

**Prueba 1. Límite de registros**

Un pipeline tiene un límite inicial de 500 registros. Se crea una segunda variable que hace referencia al mismo número y posteriormente se le asigna el valor 800.

Se comprobará si el límite original también cambia.

---

**Prueba 2. Columnas de una tabla**

Un proceso utiliza una lista con las columnas `id` y `fecha`. Se crea otra variable que apunta a esa misma lista y se añade la columna `importe`.

Se comprobará si ambas variables reflejan la modificación.

---

**Prueba 3. Umbrales de calidad**

Se crean dos objetos independientes de la clase `Umbral`, ambos con un valor inicial de `0.05`.

Posteriormente, se crea una tercera variable que apunta al primer objeto y se modifica su valor a `0.10`.

Se comprobará qué objetos se ven afectados y cuáles mantienen su valor original.

---

**Pregunta clave:** ¿Por qué reasignar una variable que contiene un número no modifica otra variable que apuntaba al mismo objeto, mientras que modificar una lista o los atributos de un objeto compartido sí afecta a todas las variables que lo referencian?

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_4_2_referencias.py`

---

```python
class Umbral:
    def __init__(self, valor):
        self.valor = valor

# Objetos inmutables: int
limite = 500
alias = limite
print(alias is limite)
alias = 800
print(limite, alias)
print(alias is limite)

# Objetos mutables: list
columnas = ["id", "fecha"]
mismas = columnas
mismas.append("importe")
print(columnas)
print(mismas is columnas)

# Dos objetos con los mismos datos
u1 = Umbral(0.05)
u2 = Umbral(0.05)
print(u1 is u2, id(u1) == id(u2))
u3 = u1
u3.valor = 0.10
print(u1.valor, u2.valor)
print(id(u3) == id(u1))
```

**Salida esperada:**

```plain text
True
500 800
False
['id', 'fecha', 'importe']
True
False False
0.1 0.05
True
```

**Higjhlights:**

79. `alias = limite` hace que las dos variables apunten al mismo objeto `500`. Al hacer `alias = 800`, `alias` pasa a apuntar a un objeto nuevo; `limite` sigue en `500`.
80. Con la lista ocurre lo contrario: `mismas.append(...)` **modifica** el objeto compartido, así que el cambio se ve desde `columnas`.
81. `u1` y `u2` tienen el mismo dato, pero son dos objetos con identidades distintas.
82. `u3 = u1` comparte el objeto: cambiar `u3.valor` cambia `u1.valor`. `u2` no se ve afectado.
83. No se imprimen los valores de `id()` porque cambian en cada ejecución; se comparan entre sí, que es lo que interesa.
---

### Ejemplo 4.3 · Los atributos de los objetos nativos

Como todo es un objeto, los números, los textos y las funciones tienen sus propios métodos especiales. Los operadores y funciones nativas los llaman por nosotros, pero se pueden ver con `dir()` y llamar explícitamente.

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_4_3_atributos_de_objetos.py`

---

```python
def validar_fichero(ruta):
    return ruta.endswith(".csv")

print("__add__" in dir(55))
print("__abs__" in dir(-5.67))
print("__call__" in dir(validar_fichero))
print("upper" in dir("texto"))

print((55).__add__(45))
print((-5.67).__abs__())
print("ventas".__len__())
print(validar_fichero.__call__("ventas_07.csv"))
print(validar_fichero.__name__)

funcion = globals()["validar_fichero"]
print(funcion("clientes.json"))
```

**Salida esperada:**

```plain text
True
True
True
True
100
5.67
6
True
validar_fichero
False
```

---

**Highlights:**

84. `dir()` devuelve una lista de nombres. Con `in` se comprueba si un objeto tiene un atributo concreto.
85. `(55).__add__(45)` es lo que Python ejecuta al escribir `55 + 45`. El número va entre paréntesis para que el punto no se confunda con un decimal.
86. `(-5.67).__abs__()` es lo que ejecuta `abs(-5.67)` y `"ventas".__len__()` lo que ejecuta `len("ventas")`.
87. Las funciones tienen el método `__call__`: es lo que se ejecuta al poner paréntesis detrás de su nombre. También tienen atributos como `__name__`.
88. `globals()` devuelve un diccionario con todos los nombres globales del programa. Al buscar `"validar_fichero"` se obtiene el objeto función, que se guarda en otra variable y se llama con ella.
---

## Sección 5. Imitar una estructura: atributos dinámicos

>
### Definición

En Python se pueden **crear, modificar y eliminar atributos de un objeto en tiempo de ejecución**, después de crearlo. Con una clase vacía (`pass`) se obtiene un contenedor de datos con acceso por punto (`registro.cliente`), parecido a las *structs* de otros lenguajes.

---

> Además de la notación con punto, Python ofrece funciones para trabajar con atributos cuyo **nombre está en una variable**, algo muy habitual cuando los nombres vienen de la cabecera de un CSV o de las claves de un JSON:

| Operación | Con nombre fijo | Con nombre en una variable |
| --- | --- | --- |
| Crear o modificar | `obj.cliente = "C-1"` | `setattr(obj, nombre, valor)` |
| Leer | `obj.cliente` | `getattr(obj, nombre)` |
| Leer con valor por defecto | — | `getattr(obj, nombre, defecto)` |
| Eliminar | `del obj.cliente` | `delattr(obj, nombre)` |
| Comprobar si existe | — | `hasattr(obj, nombre)` |

---

> Los atributos dinámicos son útiles para prototipos y para cargar datos de estructura variable. Para entidades estables (pedidos, clientes, tareas), es mejor definir todos los atributos en `__init__`: así todos los objetos tienen la misma forma.

### Analogía de la vida diaria

---

![Imagen](images/clase-19-oop-parte-2/image-003.png)

---

### Sintaxis

```python
class Estructura:
    pass

obj = Estructura()
obj.campo = valor                  # crear
obj.campo = nuevo_valor            # modificar
del obj.campo                      # eliminar

setattr(obj, "campo", valor)       # crear o modificar con el nombre en un str
getattr(obj, "campo", defecto)     # leer; si no existe, devuelve defecto
delattr(obj, "campo")              # eliminar
hasattr(obj, "campo")              # True / False
vars(obj)                          # diccionario con todos los atributos
```

---

### Ejemplo 5.1 · Evento de clic en una tienda online

Una empresa de **Ingeniería de Datos** desarrolla un sistema para recopilar y analizar los clics que realizan los usuarios mientras navegan por una tienda online.

Cada vez que un usuario visita una página, se genera un evento que contiene información como su identificador, la página visitada, el dispositivo utilizado y la campaña publicitaria de procedencia.

Sin embargo, **no todos los eventos tienen necesariamente los mismos atributos**, y algunos datos pueden cambiar o dejar de ser necesarios durante el procesamiento.

---

Para gestionar esta información, se utiliza una clase vacía llamada `EventoClic`, a la que se pueden añadir, modificar y eliminar atributos dinámicamente.

El objetivo es comprender cómo funcionan los **atributos dinámicos en Python**, sin necesidad de definirlos previamente en el constructor `__init__()`.

---

El programa debe permitir:

89. **Crear atributos:** añadir al objeto los datos del usuario, la página visitada, el dispositivo y la campaña publicitaria.
90. **Consultar atributos:** utilizar `vars()` para mostrar los atributos almacenados en el objeto.
91. **Modificar atributos:** actualizar la página visitada y el dispositivo utilizado.
92. **Eliminar atributos:** eliminar la campaña publicitaria mediante `del`.
93. **Comprobar atributos:** utilizar `hasattr()` para verificar si un atributo sigue existiendo.
---

Se registra un evento de navegación con los siguientes datos iniciales:

| Atributo | Valor |
| --- | --- |
| `usuario` | `u_4471` |
| `pagina` | `/checkout` |
| `dispositivo` | `movil` |
| `campania` | `black_friday` |

---

Durante el procesamiento del evento, se realizan las siguientes operaciones:

- Se actualiza la página a `/checkout/pago`.
- Se cambia el dispositivo de `movil` a `tablet`.
- Se elimina el atributo `campania` porque ya no es necesario para este procesamiento.
- Se consulta el estado final del objeto para comprobar los cambios realizados.
**Pregunta clave:** ¿Cómo puede un objeto de una clase vacía almacenar información, modificar sus atributos y eliminar aquellos que ya no necesita, sin que estos hayan sido definidos previamente en `__init__()`?

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_5_1_atributos_dinamicos.py`

---

```python
class EventoClic:
    pass

e = EventoClic()

# crear atributos sobre la marcha
e.usuario = "u_4471"
e.pagina = "/checkout"
e.dispositivo = "movil"
e.campania = "black_friday"
print(vars(e))

# modificar atributos
e.pagina = "/checkout/pago"
e.dispositivo = "tablet"

# eliminar un atributo
del e.campania

print(vars(e))
print(hasattr(e, "campania"))
print(e.pagina)
```

**Salida esperada:**

```plain text
{'usuario': 'u_4471', 'pagina': '/checkout', 'dispositivo': 'movil', 'campania': 'black_friday'}
{'usuario': 'u_4471', 'pagina': '/checkout/pago', 'dispositivo': 'tablet'}
False
/checkout/pago
```

**Highlights:**

94. La clase `EventoClic` está vacía. Los cuatro atributos se crean después de construir el objeto.
95. Asignar a un atributo que ya existe lo modifica.
96. `del e.campania` lo elimina del objeto. A partir de ahí, `hasattr` devuelve `False`, y leer `e.campania` daría `AttributeError`.
---

### Ejemplo 5.2 · Convertir una línea de CSV en un objeto

Una empresa de **Ingeniería de Datos** recibe diariamente archivos CSV con información sobre los pedidos realizados en una tienda online.

Cada archivo contiene una **cabecera con los nombres de las columnas** y varias líneas con los datos de los pedidos. Sin embargo, los nombres de las columnas pueden variar entre archivos, por lo que no siempre es posible definir previamente los atributos de una clase.

Para solucionar este problema, se utiliza una clase vacía llamada `Registro`, cuyos atributos se crean dinámicamente a partir de los nombres de las columnas del CSV.

---

El objetivo es aprender a utilizar **`setattr()`****, ****`getattr()`****, ****`delattr()`**** y ****`hasattr()`** para crear, consultar, modificar y eliminar atributos de un objeto.

El programa debe permitir:

97. **Separar los datos:** utilizar `split(",")` para convertir la cabecera y la línea del CSV en dos listas.
98. **Crear atributos dinámicamente:** recorrer las columnas y utilizar `setattr()` para asignar a cada atributo su valor correspondiente.
99. **Consultar atributos:** utilizar `getattr()` para obtener el cliente y consultar un atributo inexistente mediante un valor por defecto.
100. **Modificar atributos:** convertir el importe del pedido de texto (`str`) a número decimal (`float`).
101. **Eliminar atributos:** utilizar `delattr()` para eliminar el atributo `canal`.
102. **Comprobar atributos:** utilizar `hasattr()` para verificar si el atributo eliminado sigue existiendo.
---

Se recibe el siguiente registro de un archivo CSV:

| id_pedido | cliente | importe | canal |
| --- | --- | --- | --- |
| PED-9001 | C-188 | 149.90 | web |

El programa debe convertir este registro en un objeto `Registro`, utilizando los nombres de las columnas como atributos.

---

Posteriormente, se realizarán las siguientes operaciones:

- Consultar el identificador del cliente.
- Consultar el atributo `descuento`, devolviendo `"sin descuento"` si no existe.
- Convertir el atributo `importe` a `float` para permitir operaciones numéricas.
- Eliminar el atributo `canal`.
- Mostrar los atributos finales mediante `vars()` y comprobar que `canal` ya no existe.
---

**Pregunta clave:** ¿Cómo podemos convertir automáticamente las columnas de un archivo CSV en atributos de un objeto Python cuando sus nombres no se conocen de antemano, sin tener que definir cada atributo manualmente en una clase?

> Este ejemplo utiliza `split(",")` para simplificar el aprendizaje. En un proyecto real de Ingeniería de Datos conviene utilizar el módulo `csv` de Python, especialmente `csv.DictReader`, porque gestiona correctamente campos entrecomillados, separadores dentro de los valores y otras particularidades del formato CSV.

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_5_2_setattr_getattr.py`

---

```python
class Registro:
    pass

cabecera = "id_pedido,cliente,importe,canal"
linea = "PED-9001,C-188,149.90,web"

columnas = cabecera.split(",")
valores = linea.split(",")

r = Registro()
for i in range(len(columnas)):
    setattr(r, columnas[i], valores[i])

print(vars(r))
print(getattr(r, "cliente"))
print(getattr(r, "descuento", "sin descuento"))

setattr(r, "importe", float(r.importe))
delattr(r, "canal")
print(vars(r))
print(hasattr(r, "canal"))
```

**Salida esperada:**

```plain text
{'id_pedido': 'PED-9001', 'cliente': 'C-188', 'importe': '149.90', 'canal': 'web'}
C-188
sin descuento
{'id_pedido': 'PED-9001', 'cliente': 'C-188', 'importe': 149.9}
False
```

---

**Highlights:**

103. `split(",")` separa la cabecera y la línea en dos listas del mismo tamaño.
104. En cada vuelta, `setattr(r, columnas[i], valores[i])` crea un atributo cuyo nombre es el texto de la columna. Es equivalente a escribir `r.id_pedido = "PED-9001"`, `r.cliente = "C-188"`…
105. Todo lo leído de un CSV es texto: `importe` vale `'149.90'`.
106. `getattr(r, "descuento", "sin descuento")` no falla aunque el atributo no exista: devuelve el valor por defecto.
107. `setattr` también sirve para modificar: `importe` pasa a ser un `float`. `delattr` elimina la columna `canal`.
---

## Sección 6. Conversión de tipos

> 💡
### Definición

Convertir un dato de un tipo a otro es una tarea diaria en Data Engineering: todo lo que llega de un fichero de texto o de una API es `str`, y hay que pasarlo a `int`, `float` o a objetos de nuestras clases. Hay tres tipos de conversión:

---

| Conversión | Cómo se hace | Ejemplo |
| --- | --- | --- |
| Entre tipos nativos simples | Funciones `int()`, `float()`, `str()`, `bool()`, `complex()` | `int("250")` |
| Entre tipos nativos y contenedores | Funciones `list()`, `tuple()`, `set()`, `dict()` | `set(["a", "a", "b"])` |
| Entre tipos nativos y clases propias | **Nativo → clase**: el constructor `__init__`. **Clase → nativo**: métodos especiales | `DuracionTarea("00:12:40")`, `int(duracion)` |

---

Métodos especiales de conversión de una clase a un tipo nativo:

| Función nativa | Método especial | Debe devolver |
| --- | --- | --- |
| `int(obj)` | `__int__(self)` | `int` |
| `float(obj)` | `__float__(self)` | `float` |
| `str(obj)` | `__str__(self)` | `str` |
| `bool(obj)` y `if obj:` | `__bool__(self)` | `bool` |

---

Detalles de las conversiones nativas:

- `int(9.99)` **trunca** (quita los decimales) y da `9`. Para redondear se usa `round()`.
- `int(" 1520 ")` admite espacios alrededor, pero `int("3.75")` da error: primero hay que pasar por `float()`.
- `bool()` de un valor «vacío» (`0`, `0.0`, `""`, `[]`, `{}`, `None`) es `False`. Cualquier texto no vacío es `True`, incluso `"0"`.
- `int(texto, base)` interpreta el texto en otra base, por ejemplo hexadecimal.
---

### Analogía de la vida diaria

![Imagen](images/clase-19-oop-parte-2/image-004.png)

---

### Sintaxis

```python
# Entre tipos nativos
int("250"), float("19.99"), str(2026), bool(0)
list("CSV"), tuple(lista), set(lista), dict(lista_de_pares)

# Clases propias
class MiClase:
    def __init__(self, texto):        # nativo -> MiClase
        ...
    def __int__(self):                # MiClase -> int
        return entero
    def __float__(self):              # MiClase -> float
        return decimal
    def __bool__(self):               # MiClase -> bool (y en if)
        return True o False
    def __str__(self):                # MiClase -> str
        return texto

obj = MiClase("valor")
int(obj), float(obj), bool(obj), str(obj)
```

---

### Ejemplo 6.1 · Conversiones entre tipos nativos

Una empresa de **Ingeniería de Datos** recibe información procedente de archivos CSV, APIs y bases de datos. Durante el procesamiento, algunos valores llegan como cadenas de texto, mientras que otros necesitan transformarse en números, listas, tuplas, conjuntos o diccionarios.

Para poder utilizar estos datos correctamente, es necesario realizar **conversiones entre los tipos nativos de Python**.

El objetivo de este ejemplo es comprender cómo funcionan las principales funciones de conversión de Python y qué ocurre cuando transformamos un valor de un tipo a otro.

---

El programa debe permitir:

108. **Convertir números y cadenas:** utilizar `int()`, `float()` y `str()` para transformar valores entre distintos tipos.
109. **Diferenciar truncamiento y redondeo:** comprobar la diferencia entre `int()` y `round()` al trabajar con números decimales.
110. **Convertir valores a booleanos:** utilizar `bool()` para identificar qué valores se consideran `True` o `False`.
111. **Convertir colecciones:** utilizar `list()`, `tuple()`, `set()` y `dict()` para transformar diferentes estructuras de datos.
112. **Eliminar duplicados:** comprobar cómo `set()` permite obtener valores únicos a partir de una lista.
113. **Convertir números de otras bases:** utilizar `int()` para interpretar una cadena hexadecimal y obtener su equivalente decimal.
---

Se realizarán diferentes conversiones sobre datos habituales en un pipeline:

- Un número de registros recibido como texto (`"250"`) se convierte a entero.
- Un importe recibido como texto (`"19.99"`) se convierte a decimal.
- Un valor decimal (`9.99`) se trunca y se redondea para comparar los resultados.
- Se comprueba cómo Python interpreta valores vacíos y cadenas como `"0"` al convertirlos a booleanos.
- Se transforman cadenas y colecciones para obtener listas, tuplas, conjuntos y diccionarios.
- Se eliminan ciudades duplicadas de una lista.
- Se convierte un número hexadecimal (`"0x1F"`) a su valor decimal.
---

**Pregunta clave:** ¿Cómo podemos transformar datos entre los diferentes tipos nativos de Python y qué diferencias debemos tener en cuenta para evitar errores durante el procesamiento de información en un pipeline de datos?

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_6_1_conversiones_nativas.py`

---

```python
print(int("250"))
print(float("19.99"))
print(int(9.99))
print(round(9.99))
print(str(2026))
print(bool(0), bool(""), bool("0"), bool([]))

print(list("CSV"))
print(tuple(["id", "fecha"]))
print(set(["madrid", "sevilla", "madrid"]) == {"madrid", "sevilla"})
print(dict([("csv", 12), ("json", 3)]))
print(list({"csv": 12, "json": 3}))
print(int("0x1F", 16))
```

**Salida esperada:**

```plain text
250
19.99
9
10
2026
False False True False
['C', 'S', 'V']
('id', 'fecha')
True
{'csv': 12, 'json': 3}
['csv', 'json']
31
```

---

**Highlights:**

114. `int(9.99)` trunca a `9`, mientras que `round(9.99)` redondea a `10`.
115. `bool("0")` es `True`: es un texto con un carácter. Esto causa errores frecuentes al leer flags de ficheros de texto.
116. `list("CSV")` recorre el texto y crea una lista de caracteres.
117. `set(...)` elimina duplicados. Se compara con `==` en lugar de imprimirlo, porque un `set` no tiene orden fijo.
118. `dict(...)` crea un diccionario a partir de una lista de pares. `list(diccionario)` devuelve sus claves.
119. `int("0x1F", 16)` interpreta el texto como hexadecimal: `1F` = 31.
---

### Ejemplo 6.2 · Duración de una tarea: de texto a objeto y de objeto a número

Una empresa de **Ingeniería de Datos** utiliza un orquestador para ejecutar diferentes tareas dentro de sus pipelines, como la extracción, transformación y carga de datos.

El sistema registra la duración de cada tarea como una cadena de texto con el formato `hh:mm:ss` (horas, minutos y segundos).

Sin embargo, el equipo necesita **convertir estas duraciones a diferentes tipos de datos** para realizar cálculos, generar informes y comprobar si alguna tarea tiene una duración de cero segundos.

---

Para ello, se desarrolla una clase llamada `DuracionTarea` que permite transformar una duración expresada como texto en un objeto Python y convertir posteriormente ese objeto a diferentes tipos nativos mediante **métodos especiales de conversión**.

El programa debe permitir:

120. **Texto a objeto (****`__init__`****):** recibir una duración en formato `hh:mm:ss`, convertirla a segundos y almacenarla en un atributo privado.
121. **Objeto a entero (****`__int__`****):** obtener la duración total expresada en segundos mediante `int()`.
122. **Objeto a decimal (****`__float__`****):** obtener la duración expresada en horas decimales mediante `float()`.
123. **Objeto a booleano (****`__bool__`****):** devolver `True` cuando la duración sea mayor que cero y `False` cuando sea igual a cero.
124. **Objeto a texto (****`__str__`****):** mostrar la duración en un formato legible utilizando minutos y segundos.
125. **Calcular duraciones acumuladas:** convertir varios objetos a segundos y utilizar `sum()` para obtener el tiempo total de ejecución.
---

Se dispone de tres tareas de un pipeline con las siguientes duraciones:

| Tarea | Duración (`hh:mm:ss`) | Estado considerado en el ejemplo |
| --- | --- | --- |
| Extracción | `00:12:40` | Con duración registrada |
| Transformación | `01:05:00` | Con duración registrada |
| Tarea sin ejecutar | `00:00:00` | Sin duración registrada |

---

El programa debe realizar las siguientes operaciones:

- Convertir la duración de extracción a segundos.
- Convertir la duración de transformación a horas decimales.
- Mostrar la duración de extracción como texto legible.
- Comprobar qué tareas tienen una duración mayor que cero utilizando `bool()`.
- Calcular la duración total acumulada de las tres tareas.
- Mostrar un mensaje de advertencia cuando una tarea tenga una duración igual a cero.
---

**Pregunta clave:** ¿Cómo podemos transformar una duración recibida como texto en un objeto de nuestra propia clase y conseguir que Python pueda convertir ese objeto a `int`, `float`, `str` o `bool` utilizando los métodos especiales correspondientes?

El orquestador de pipelines registra la duración de cada tarea como texto `hh:mm:ss`. El equipo necesita sumar duraciones, expresarlas en horas y detectar tareas que no se ejecutaron.

> 📄 `clase_19_detalles_clases_objetos/teoria/ejemplo_6_2_duracion_tarea.py`

---

```python
class DuracionTarea:
    def __init__(self, texto="00:00:00"):            # conversión str -> DuracionTarea
        horas, minutos, segundos = texto.split(":")
        self.__segundos = int(horas) * 3600 + int(minutos) * 60 + int(segundos)

    def __int__(self):                                # DuracionTarea -> int
        return self.__segundos

    def __float__(self):                              # DuracionTarea -> float (horas)
        return round(self.__segundos / 3600, 2)

    def __bool__(self):                               # DuracionTarea -> bool
        return self.__segundos > 0

    def __str__(self):                                # DuracionTarea -> str
        return f"{self.__segundos // 60} min{self.__segundos % 60} s"

extraccion = DuracionTarea("00:12:40")
transformacion = DuracionTarea("01:05:00")
sin_ejecutar = DuracionTarea()

print(int(extraccion))
print(float(transformacion))
print(str(extraccion))
print(bool(transformacion), bool(sin_ejecutar))

total_segundos = sum([int(d) for d in [extraccion, transformacion, sin_ejecutar]])
print(total_segundos)

if not sin_ejecutar:
    print("Hay tareas que no han llegado a ejecutarse")
```

**Salida esperada:**

```plain text
760
1.08
12 min 40 s
True False
4660
Hay tareas que no han llegado a ejecutarse
```

---

**Highlights:**

126. El **constructor** hace la conversión de `str` a `DuracionTarea`: separa horas, minutos y segundos y guarda el total en segundos en un atributo privado.
127. `int(extraccion)` ejecuta `__int__` y devuelve los segundos: 12 × 60 + 40 = 760.
128. `float(transformacion)` ejecuta `__float__` y devuelve las horas: 3900 / 3600 ≈ 1.08.
129. `bool()` ejecuta `__bool__`. Una duración de cero segundos es `False`.
130. `if not sin_ejecutar:` también usa `__bool__`: el objeto se comporta como cualquier valor nativo en una condición.
131. La comprehension convierte cada duración a `int` y `sum()` suma los segundos: 760 + 3900 + 0 = 4660.
---

