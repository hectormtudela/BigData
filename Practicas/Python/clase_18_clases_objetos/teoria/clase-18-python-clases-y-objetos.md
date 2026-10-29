# 📋Clase 18 - Python: Clases y Objetos

# Preparación del entorno de trabajo

A partir de esta clase, todo el código de Python se escribe y se ejecuta en **VS Code**, dentro de la **copia local de tu repositorio del máster**, y se entrega subiendo los cambios a ese mismo **repositorio remoto de GitHub**. 

**Entorno de trabajo de la clase:** Windows 11, Python 3.12, VS Code y la terminal PowerShell integrada en VS Code. Todos los comandos de esta guía están escritos para PowerShell.

Ya tienes creado el repositorio remoto general del máster. En esta guía vas a:

1. Tener ese repositorio en tu equipo (repositorio local).
2. Crear dentro de él la carpeta `python_big_data_engineering`, que reunirá **todas las clases de Python**. Contiene **un único entorno virtual**, un `requirements.txt` y un `.gitignore` comunes para todas ellas.
3. Crear dentro la carpeta de la Clase 18.
4. Trabajar en local y enviar los cambios al repositorio remoto.
Los pasos 3 a 8 se hacen **una sola vez**, en esta clase. En las clases siguientes (19, 20…) solo se crea la carpeta de la clase nueva, con el mismo entorno virtual.

---

### Estructura de carpetas

Al terminar estos pasos y la clase, tu repositorio del máster debe contener esta estructura:

```plain text
<repo-del-master>/                          ← tu repositorio general (ya existe)
├── ...                                     ← lo que ya tengas de otras asignaturas
│
└── python_big_data_engineering/                ← carpeta común de todas las clases de Python
    ├── .gitignore                          ← común para todas las clases
    ├── README.md                           ← índice de clases
    ├── requirements.txt                    ← dependencias comunes
    ├── .vscode/
    │   └── settings.json
    ├── .venv/                              ← entorno virtual único (NO se sube a GitHub)
    │
    ├── clase_18_clases_objetos/            ← estructura interna en el apartado siguiente
    ├── clase_19_.../                       ← próximas clases, misma estructura interna
    └── clase_20_.../
```

---

### Estructura interna de cada clase

Todas las carpetas de clase tienen las mismas subcarpetas. Cada una guarda el documento .md de esa parte de la clase junto a los `.py` que le corresponden:

```plain text
clase_18_clases_objetos/
├── README.md                               ← lista de progreso de la clase
├── clase_18_02_ejercicios_clases_objetos.md  ← enunciados de los ejercicios (Parte 02)
│
├── teoria/
│   ├── clase_18_01_teoria_clases_objetos.md  ← este documento (Parte 01)
│   ├── ejemplo_2_1_crear_objetos.py        ← un .py por cada ejemplo resuelto
│   ├── ejemplo_2_2_atributos_a_mano.py
│   └── ...
│
├── ejercicios_basicos/
│   ├── ejercicio_01_....py                 ← un .py por ejercicio resuelto
│   └── ...
├── ejercicios_intermedios/
│   └── ...
├── ejercicios_avanzados/
│   └── ...
│
└── caso_estudio/
    ├── caso_estudio_....md                 ← enunciado del caso (cuando se publique)
    └── ....py                              ← solución del caso
```

---

| Carpeta | Qué contiene |
| --- | --- |
| `teoria/` | El .md de la teoría (esta clase) y un `.py` por cada ejemplo resuelto, con el nombre que indica 📄 |
| `ejercicios_basicos/` | Un `.py` por cada ejercicio de nivel básico resuelto |
| `ejercicios_intermedios/` | Un `.py` por cada ejercicio de nivel intermedio resuelto |
| `ejercicios_avanzados/` | Un `.py` por cada ejercicio de nivel avanzado resuelto |
| `caso_estudio/` | El .md del caso de estudio y el `.py` con su solución, cuando el profesor lo publique |

---

Reglas de nombres para carpetas y archivos:

- Todo en minúsculas y en `snake_case`: sin espacios, sin tildes y sin ñ.
- Las carpetas de clase siguen el formato `clase_NN_tema` (`clase_18_clases_objetos`).
- Nunca llames a un archivo como un módulo de Python (`random.py`, `math.py`, `json.py`, `string.py`): rompería cualquier `import` de ese módulo.
- Usa exactamente los nombres de archivo que indica cada ejemplo y cada ejercicio (📄).
---

### Paso 1 · Instalar y comprobar las herramientas

Necesitas tener instalado en Windows 11:

| Herramienta | Versión | Dónde obtenerla |
| --- | --- | --- |
| Python | **3.12** (cualquier 3.12.x) | python.org → *Downloads* → *Windows* → *Windows installer (64-bit)* de la última versión 3.12 |
| Git | La más reciente | git-scm.com → *Download for Windows* |
| VS Code | La más reciente | code.visualstudio.com |
| Extensión **Python** de Microsoft | La más reciente | En VS Code: panel *Extensions* (`Ctrl+Shift+X`) → buscar «Python» |

Al instalar Python 3.12, en la primera pantalla del instalador:

- Marca **Add python.exe to PATH**.
- Deja marcada la opción **Use admin privileges when installing py.exe**, que instala el *Python Launcher* (`py`).
El *Python Launcher* permite elegir la versión exacta de Python aunque haya varias instaladas en el equipo. En esta guía se usa `py -3.12` para crear el entorno virtual, de modo que siempre se cree con Python 3.12.

Abre PowerShell y comprueba las versiones:

```powershell
py -3.12 --version
git --version
```

La primera línea debe mostrar `Python 3.12.x`.

> Si al escribir `python` en la terminal se abre la Microsoft Store, desactiva los alias de Windows: *Configuración > Aplicaciones > Configuración avanzada de aplicaciones > Alias de ejecución de aplicaciones* y apaga **python.exe** y **python3.exe**.

Comprueba también que Git tiene configurada tu identidad, con el mismo correo que tu cuenta de GitHub:

```powershell
git config --global user.name
git config --global user.email
```

Si alguno de los dos no devuelve nada, configúralo:

```powershell
git config --global user.name "Nombre Apellido"
git config --global user.email "tu_correo@ejemplo.com"
```

### Paso 2 · Tener el repositorio del máster en local

**Si todavía no tienes el repositorio en tu equipo**, clónalo. En GitHub, abre tu repositorio del máster, pulsa **Code** y copia la URL HTTPS. Después, desde la carpeta donde quieras guardarlo (por ejemplo, `Documentos`):

```powershell
git clone https://github.com/<tu_usuario>/<repo-del-master>.git
cd <repo-del-master>
```

`git clone` descarga el repositorio con todo su historial y deja configurado el remoto con el nombre `origin`.

**Si ya lo tienes clonado**, entra en su carpeta y trae los últimos cambios del remoto antes de empezar:

```powershell
cd <repo-del-master>
git pull
```

En los dos casos, comprueba que el repositorio local está conectado con tu remoto:

```powershell
git remote -v
git status
```

`git remote -v` debe mostrar la URL de tu repositorio del máster, y `git status` debe indicar la rama actual (normalmente `main`) y que no hay cambios pendientes.

> La primera vez que te conectes, Git puede pedir autenticación. En Windows se abre el navegador para iniciar sesión en GitHub. Si la terminal pide usuario y contraseña, la contraseña **no** es la de GitHub: es un *Personal Access Token* que se genera en `GitHub > Settings > Developer settings > Personal access tokens`.

### Paso 3 · Crear la carpeta común de Python y abrirla en VS Code

Desde la raíz del repositorio del máster:

```powershell
mkdir python_big_data_engineering
```

En VS Code, abre **esa carpeta** (no un archivo suelto ni la carpeta de una clase): `File > Open Folder…` y selecciona `python_big_data_engineering`. Es la carpeta que abrirás en todas las clases de Python.

> Si VS Code pregunta si quieres abrir el repositorio Git de la carpeta superior, responde **Sí**. Así el panel de control de código fuente muestra los cambios del repositorio del máster.

Abre la terminal integrada: `Terminal > New Terminal`. **Todos los comandos siguientes se ejecutan en esa terminal, situada dentro de ****`python_big_data_engineering`****.**

### Paso 4 · Crear y activar el entorno virtual común

El entorno virtual es una instalación de Python aislada. Se crea **una sola vez** en `python_big_data_engineering` y lo usan todas las clases de Python: las librerías que se instalen en una clase estarán disponibles en las siguientes.

```powershell
py -3.12 -m venv .venv
```

`py -3.12` garantiza que el entorno se crea con Python 3.12, aunque el equipo tenga otras versiones instaladas.

Actívalo:

```powershell
.venv\Scripts\Activate.ps1
```

Cuando está activo, el *prompt* de la terminal empieza por `(.venv)`. Comprueba que el Python del entorno es el 3.12:

```powershell
python --version
```

> Si PowerShell muestra un error de *execution policy* («la ejecución de scripts está deshabilitada en este sistema»), ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, confirma con `S` y vuelve a activar el entorno.

Con el entorno activo, actualiza `pip`:

```powershell
python -m pip install --upgrade pip
```

Por último, indica a VS Code que use este entorno: `Ctrl+Shift+P` → **Python: Select Interpreter** → elige el que aparece como `Python 3.12.x ('.venv')`. A partir de ahora, el botón ▶ de VS Code ejecuta los archivos de cualquier clase con este Python.

### Paso 5 · Crear `requirements.txt`

`requirements.txt` es la lista de librerías externas que necesitan las clases de Python. Permite reproducir el mismo entorno en cualquier equipo con un solo comando. Como el entorno es común, el archivo también lo es y se mantiene en `python_big_data_engineering`.

En esta clase **solo se usa Python estándar**, así que no hay librerías externas. Aun así, el archivo se crea desde el principio. Crea `requirements.txt` dentro de `python_big_data_engineering` con este contenido:

```plain text
# Dependencias comunes de las clases de Python
# Clase 18: solo biblioteca estándar de Python, sin librerías externas
```

Cuando en clases posteriores se instalen librerías, el flujo será siempre el mismo, con la terminal en `python_big_data_engineering` y el entorno activo:

```powershell
pip install nombre_libreria                                  # instalar dentro del entorno activo
pip freeze | Out-File -Encoding utf8 requirements.txt        # actualizar la lista de dependencias
pip install -r requirements.txt                              # reproducir el entorno en otro equipo
```

> En PowerShell se usa `Out-File -Encoding utf8` en lugar de `pip freeze > requirements.txt`, porque la redirección `>` de Windows PowerShell guarda el archivo en UTF-16 y puede dar problemas al leerlo en otros equipos.

### Paso 6 · Crear `.gitignore`

`.gitignore` indica a Git qué archivos **no** debe subir nunca al repositorio. Un `.gitignore` colocado en `python_big_data_engineering` se aplica a esa carpeta y a **todas las carpetas de clase** que contenga, sin afectar al resto del repositorio del máster.

Se crea **antes del primer commit**: si un archivo ya se ha subido, añadirlo después a `.gitignore` no lo borra del historial.

Crea el archivo `.gitignore` dentro de `python_big_data_engineering` con este contenido exacto:

```plain text
# Entorno virtual de Python
.venv/
venv/
env/

# Caché y compilados de Python
__pycache__/
*.pyc
*.pyo

# Variables de entorno y secretos
.env

# Archivos de sistema de Windows
Thumbs.db
ehthumbs.db
desktop.ini

# Configuración personal de VS Code (solo se comparte settings.json)
.vscode/*
!.vscode/settings.json
```

| Entrada | Qué excluye | Por qué no se sube |
| --- | --- | --- |
| `.venv/`, `venv/`, `env/` | El entorno virtual | Ocupa cientos de MB, depende del sistema operativo y se reconstruye con `requirements.txt` |
| `__pycache__/`, `*.pyc`, `*.pyo` | Archivos compilados que Python genera al ejecutar, en cualquier carpeta de clase | Se regeneran solos en cada equipo |
| `.env` | Variables de entorno (contraseñas, claves de API) | Nunca se suben secretos a un repositorio |
| `Thumbs.db`, `ehthumbs.db`, `desktop.ini` | Archivos ocultos que crea el Explorador de Windows (miniaturas y configuración de carpetas) | No forman parte del proyecto |
| `.vscode/*` y `!.vscode/settings.json` | Toda la carpeta `.vscode` **excepto** `settings.json` | Se comparten los ajustes comunes, no los personales |

### Paso 7 · Crear `.vscode/settings.json`

Dentro de `python_big_data_engineering`, crea la carpeta `.vscode` y, dentro, el archivo `settings.json`:

```json
{
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "python.terminal.activateEnvironment": true,
    "python.terminal.executeInFileDir": true,
    "files.encoding": "utf8"
}
```

| Ajuste | Para qué sirve |
| --- | --- |
| `terminal.integrated.defaultProfile.windows` | Abre siempre PowerShell como terminal integrada, que es la que usan los comandos de esta guía |
| `python.terminal.activateEnvironment` | Activa `.venv` automáticamente en cada terminal nueva |
| `python.terminal.executeInFileDir` | El botón ▶ ejecuta cada archivo desde su propia carpeta, sea de la clase que sea |
| `files.encoding` | Guarda los archivos en UTF-8 (tildes y ñ en los textos) |

La ruta del intérprete no se incluye en este archivo porque depende de dónde esté el repositorio en cada equipo: se selecciona en el Paso 4.

### Paso 8 · Crear el `README.md` común

Dentro de `python_big_data_engineering`, crea `README.md`. Es el índice de todas las clases de Python; en cada clase nueva se añade una fila a la tabla.

```markdown
# Python para Big Data Engineering

**Alumno:** Nombre Apellido

## Preparar el entorno

Windows 11 · Python 3.12 · PowerShell

    py -3.12 -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

## Clases

| Clase | Tema | Carpeta |
|---|---|---|
| 18 | Clases y objetos | `clase_18_clases_objetos/` |
```

### Paso 9 · Crear la carpeta de la Clase 18

Este es el paso que se repetirá en cada clase nueva, con su número y su tema. Desde la terminal, dentro de `python_big_data_engineering`:

```powershell
mkdir clase_18_clases_objetos\teoria
mkdir clase_18_clases_objetos\ejercicios_basicos
mkdir clase_18_clases_objetos\ejercicios_intermedios
mkdir clase_18_clases_objetos\ejercicios_avanzados
mkdir clase_18_clases_objetos\caso_estudio
```

En PowerShell, `mkdir` crea también la carpeta `clase_18_clases_objetos` si todavía no existe.

Copia los documentos de la clase en su sitio:

- `clase_18_01_teoria_clases_objetos.md` (este documento) → dentro de `teoria/`.
- `clase_18_02_ejercicios_clases_objetos.md` → en la raíz de `clase_18_clases_objetos/`.
Dentro de `clase_18_clases_objetos`, crea su `README.md`:

```markdown
# Clase 18 · Clases y objetos

## Progreso
-[ ] Ejemplos de teoría (`teoria/`)
-[ ] Ejercicios básicos (`ejercicios_basicos/`)
-[ ] Ejercicios intermedios (`ejercicios_intermedios/`)
-[ ] Ejercicios avanzados (`ejercicios_avanzados/`)
-[ ] Caso de estudio (`caso_estudio/`)
```

Marca cada casilla (`- [x]`) cuando completes ese bloque. En GitHub se verán como casillas marcadas.

> Git no guarda carpetas vacías. `teoria/` aparecerá en GitHub con el primer commit porque ya contiene el .md; las carpetas de ejercicios y `caso_estudio/` aparecerán en cuanto contengan su primer archivo.

### Paso 10 · Primer commit y envío al repositorio remoto

Antes de hacer el commit, comprueba qué va a subir Git:

```powershell
git status
```

Deben aparecer como nuevos `.gitignore`, `README.md`, `requirements.txt`, `.vscode/` y `clase_18_clases_objetos/` (con su `README.md` y los dos .md de la clase). **No** debe aparecer `.venv/`. Si aparece, revisa que `.gitignore` está dentro de `python_big_data_engineering` y que su nombre empieza por punto y no tiene extensión (`.gitignore`, no `gitignore.txt`).

Añade el contenido, haz el commit y envíalo al remoto:

```powershell
git add .
git commit -m "python: entorno común y estructura de la clase 18"
git push
```

- Como la terminal está dentro de `python_big_data_engineering`, `git add .` solo añade el contenido de esta carpeta, no el resto del repositorio del máster.
- `git push` envía el commit al repositorio remoto (`origin`) que ya tenías configurado.
Recarga la página de tu repositorio en GitHub: debe aparecer la carpeta `python_big_data_engineering` con `.gitignore`, `README.md`, `requirements.txt`, `.vscode/settings.json` y `clase_18_clases_objetos/` (con su `README.md`, el .md de ejercicios y `teoria/` con el .md de teoría), y **no** debe aparecer `.venv`.

### Paso 11 · Flujo de trabajo durante la clase

Cada ejemplo de la teoría y cada ejercicio indica el archivo donde va su código, con la ruta desde la carpeta `python_big_data_engineering`:

> 📄 `clase_18_clases_objetos/teoria/ejemplo_2_1_crear_objetos.py`

Para cada uno:

5. Crea el archivo en la carpeta indicada, con el nombre exacto.
6. Escribe el código y ejecútalo con ▶ (o con `python nombre_archivo.py` desde su carpeta).
7. Compara lo que sale en la terminal con la **Salida esperada** del documento.
8. Al terminar cada sección o cada nivel de ejercicios, guarda y envía el trabajo al remoto, desde la terminal situada en `python_big_data_engineering`:
```powershell
git add .
git commit -m "clase 18: ejemplos de la sección 3"
git push
```

Formato de los mensajes de commit: `clase NN: qué se ha hecho`. Haz commits pequeños y frecuentes; el historial de GitHub es también la evidencia de tu trabajo.

> Si trabajas desde más de un equipo, ejecuta siempre `git pull` antes de empezar a trabajar, para traer los cambios que subiste desde el otro. En un equipo nuevo, después de clonar, el entorno se recrea con `py -3.12 -m venv .venv`, se activa con `.venv\Scripts\Activate.ps1` y se ejecuta `pip install -r requirements.txt`.

### En las próximas clases de Python

No se vuelve a crear el entorno ni los archivos comunes. Al empezar cada clase:

9. Abre `python_big_data_engineering` en VS Code y ejecuta `git pull`.
10. Comprueba que la terminal muestra `(.venv)`.
11. Crea la carpeta de la clase nueva con la misma estructura interna del Paso 9 (por ejemplo, `clase_19_metodos_encapsulamiento/` con `teoria/`, `ejercicios_basicos/`, `ejercicios_intermedios/`, `ejercicios_avanzados/` y `caso_estudio/`) y copia en ella los .md de la clase.
12. Añade la fila de la clase al `README.md` común.
### Entrega

Se entrega el **repositorio remoto del máster en GitHub**, que debe contener `python_big_data_engineering/clase_18_clases_objetos` con:

- La estructura interna indicada al principio de esta guía.
- Todos los ejemplos de la teoría en `teoria/`, junto al .md de la teoría.
- Todos los ejercicios resueltos en `ejercicios_basicos/`, `ejercicios_intermedios/` y `ejercicios_avanzados/`, según su nivel.
- El caso de estudio en `caso_estudio/`, cuando se publique.
- Cada `.py` ejecutable sin errores y con una salida igual a la esperada.
- El `README.md` de la clase con las casillas de progreso actualizadas.
---

# Parte 01 - Clases y objetos

## ¿Qué son las clases y los objetos?

> El mundo está orientado a objetos. Está lleno de objetos como Gorrión, Rosa, Guitarra, Teclado, etc.-

- Cada objeto es una instancia específica de una clase. Por ejemplo, el Gorrión es una instancia específica de la clase Pájaro o Rosa es una instancia específica de la clase Flor.
- Pájaro es una clase. Gorrión, Cuervo, Águila son objetos de la clase Pájaro.
- Futbolista es una clase. Messi, Ronaldo, Iniesta son objetos de la clase Futbolista.
- Flor es una clase. Rosas, Tulipanes, Girasoles son objetos de la clase Flor.
- Instrumento musical es una clase: Guitarra, Piano y Flauta son objetos de la clase Instrumento musical.
---

> Una clase describe dos cosas: la forma que tendrá un objeto creado a partir de ella y la funcionalidad que tendrá. Por ejemplo, la clase Pájaro puede especificar la forma en términos de peso, color, número de plumas, mientras que la funcionalidad nos habla de volar, saltar, comer, entre otros.

- A la 'forma' suele denominarse como **propiedades** y a la funcionalidad: **métodos**. Una clase nos permite agrupar propiedades y funcionalidad juntos.
- Cuando se crean objetos como Gorrión o Águila a partir de la clase Pájaro, las propiedades tendrán valores. Los métodos nos permiten acceder o manipular estos valores. Por ejemplo, la propiedad peso tendrá un valor de 250 gramos para un objeto Gorrión, mientras que para un objeto Águila su peso es de 10 Kg.
> Así pues, una clase es de naturaleza genérica, mientras que un objeto es de naturaleza específica. Se pueden crear múltiples objetos a partir de una clase. El proceso de creación de un objeto a partir de una clase se denomina **instanciación.**

---

![Imagen](images/clase-18-python-clases-y-objetos/image-001.png)
![Imagen](images/clase-18-python-clases-y-objetos/image-002.png)
---

![Imagen](images/clase-18-python-clases-y-objetos/image-003.png)
![Imagen](images/clase-18-python-clases-y-objetos/image-004.png)
---

## Clases y Objetos en Python

- En Python cada tipo de dato es una clase. Así, `int`, `float`, `complex`, `bool`, `str`, `list`, `tuple`, `set`, `dict` son todos clases.
- Una clase tiene un nombre, mientras que los objetos no tienen nombre. Como los objetos no tienen nombre, se hace referencia a ellos utilizando sus direcciones en memoria.
---

## Ejemplos programáticos de clases y objetos:

```python
a = 3.14  # a es un objeto de la clase float
s = "Marge"  # s es un objeto de la clase str
lst = [19, 20, 30]  # lst es un objeto de la clase list
tpl = ('a', 'b', 'c')  # tpl es un objeto de la clase tuple

```

---

- Diferentes objetos de un tipo particular pueden contener diferentes datos, pero los mismos métodos:
```python
s1 = 'Sonia'  # s1 es un objeto de tipo str
s2 = 'Greta'  # s2 es un objeto de tipo str

```

> Aquí s1 y s2 son objetos de la clase **str** que contienen datos diferentes, pero los mismos métodos como upper(), lower(), capitalize(), etc.

---

> Los datos específicos de un objeto a menudo se denominan **datos de instancia o propiedades** del objeto o estado del objeto o **atributos **del objeto. Los *métodos de un objeto* se denominan **métodos de instancia**.

---

## Clases definidas por el usuario

- Además de proporcionar clases prefabricadas como `int`, `str`, `list`, `tuple`, etc., Python nos permite definir nuestras propias clases y crear objetos a partir de ellas.
- Las clases que definimos o creamos se llaman *user-defined data types*. Las reglas para definir y utilizar una clase definida por el usuario y una clase estándar de Python son las mismas.
---

## Definamos una clase que llamaremos Empleado:

```python
class Empleado:
    def set_data(self, n, e, s):
        self.nombre = n
        self.edad = e
        self.salario = s

    def display_data(self):
        print(self.nombre, self.edad, self.salario)

e1 = Empleado()
e1.set_data('Julian', 23, 25000)
e1.display_data()

e2 = Empleado()
e2.set_data('Thomas', 25, 30000)
e2.display_data()

```

Salida:

```plain text
Julian 23 25000
Thomas 25 30000
```

---

> La clase Empleado contiene dos métodos `set_data()` y `display_data()` que se utilizan para establecer y mostrar los datos presentes en los objetos creados a partir de la clase Empleado.

> Se crean dos objetos mediante las sentencias:

```python
e1 = Empleado()
e2 = Empleado()
```

- Las direcciones de los objetos  se almacenan en `e1` y `e2`.
- En principio, ambos objetos deberían contener los datos de instancia `nombre`, `edad`, `salario` y los métodos de instancia `set_data()` y `display_data()`.
---

> En la práctica, cada objeto tiene sus propios datos de instancia: nombre, edad y salario, mientras que los métodos set_data() y display_data() se comparten entre los objetos.

>
> Los datos de instancia no se comparten, ya que los valores de los datos de instancia serían diferentes de un objeto a otro.

- La sintaxis para llamar al método de un objeto es `object.method()`, tal como en `e1.set_data()`.
- Dentro de `set_data()`, `self` contiene la dirección del primer objeto. Del mismo modo, cuando `set_data()` es llamado usando `e2`, `self` contiene la dirección del segundo objeto.
---

## Convenio de acceso.

Hemos accedido a los métodos de instancia `set_data()` y `display_data()` desde fuera de la clase. Incluso los datos de instancia `nombre`, `edad` y `salario` son accesibles desde fuera de la clase. Por lo tanto, las siguientes sentencias funcionarán:

```python
e3 = Empleado()
e3.nombre = 'Ana'
e3.edad = 25
e3.salario = 30000
e3.display_data()
```

Salida:

```plain text
Ana 25 30000
```

---

> Sin embargo, es una buena idea mantener los datos de una clase inaccesibles desde fuera de la clase y acceder a ellos sólo a través de funciones miembro de la clase.

- No hay ningún mecanismo o palabra clave disponible en Python para hacer cumplir esto. Por lo tanto, se utiliza una convención para iniciar los identificadores de datos de instancia con dos guiones bajos (a menudo llamado `underscore`, abreviatura de double underscore). Ejemplo:  `__nombre`, `__edad` y `__salario`.
---

## Inicialización de objetos:

Hay dos maneras de inicializar un objeto:

> **inicializar un objeto** significa **crear una instancia con datos iniciales**.

---

- **Método 1**: Usando métodos como `get_data()`/`set_data()`. 
> Primero se crea el objeto vacío (por ejemplo: `e = Empleado()`).
Luego se usa un **método** para **cargarle datos**:

`get_data()` → suele pedir los datos por teclado (con `input()`).

`set_data()` → recibe valores como parámetros y los asigna a los atributos.

```python
# Ejemplo ilustrativo
e = Empleado()
e.set_data('Ana', 25, 30000)
```
---

- **Método 2**: Usando el método especial `__init__()`.
> `__init__()` es el **constructor** de Python: se ejecuta **automáticamente** cuando se crea el objeto. Recibe parámetros **directamente al crear el objeto**, así que no necesitas llamar a un método aparte.
```python
class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

e = Empleado('Ana', 25, 30000)  # Se inicializa de inmediato
```

- El beneficio de inicializar un objeto usando el método especial `__init__()` es que garantiza la inicialización, ya que `__init__()` siempre se llama cuando se crea un objeto.
- `__init__()` es llamado una sola vez durante toda la vida de un objeto.
- El método `__del__()` es llamado automáticamente cuando un objeto sale del ámbito. La actividad de limpieza, si la hay, debe hacerse en `__del__()`.
---

## Variables y métodos de clase

### Definición de variable de clase

> 💡 Una variable de clase es aquella que se **comparte entre todas las instancias de una clase**. Se define a nivel de clase y no está asociada a un objeto específico, lo que significa que su valor es común para todos los objetos creados a partir de esa clase.

---

**Ejemplo:**

```python
class Coche:
    total_coches = 0  # Variable de clase

    def __init__(self, marca):
        self.marca = marca  # Variable de instancia
        Coche.total_coches += 1  # Incrementa la variable de clase

# Creando instancias
coche1 = Coche("Toyota")
coche2 = Coche("Honda")

# Accediendo a la variable de clase
print(Coche.total_coches)  # Salida: 2

```

Salida:

```plain text
2
```

---

### Definición de método de clase

> 💡 Un método de clase es una función que pertenece a la clase en su conjunto y no a una instancia específica. Se define utilizando el decorador `@classmethod` y recibe el parámetro `cls` como referencia a la clase, en lugar de `self`.

---

**Ejemplo:**

```python
class Estudiante:
    total_estudiantes = 0  # Variable de clase

    @classmethod
    def incrementar_contador(cls):
        cls.total_estudiantes += 1
        return cls.total_estudiantes

    @classmethod
    def obtener_total(cls):
        return cls.total_estudiantes

# Usando los métodos de clase
Estudiante.incrementar_contador()  # Añade 1 estudiante
Estudiante.incrementar_contador()  # Añade otro estudiante

print(Estudiante.obtener_total())  # Salida: 2

```

Salida:

```plain text
2
```

---

### Diferencia con variables/métodos de instancia

> 💡 **Variables de instancia**: Están asociadas a objetos individuales y se declaran con `self`. Cada objeto tiene su propia copia de estas variables.

> **Métodos de instancia**: Operan sobre un objeto específico y requieren `self` como primer argumento.

---

Ejemplo:

```python
class Perro:
    # Variable de clase
    total_perros = 0

    def __init__(self, nombre):
        # Variable de instancia
        self.nombre = nombre
        Perro.total_perros += 1

    # Método de instancia
    def ladrar(self):
        return f"{self.nombre} está ladrando!"

    # Método de clase
    @classmethod
    def contar_perros(cls):
        return f"Total de perros: {cls.total_perros}"

# Creando instancias
perro1 = Perro("Rex")
perro2 = Perro("Luna")

# Accediendo a variables y métodos
print(perro1.nombre)  # Salida: Rex (variable de instancia única por objeto)
print(perro2.nombre)  # Salida: Luna (variable de instancia única por objeto)
print(Perro.total_perros)  # Salida: 2 (variable de clase compartida)
print(perro1.ladrar())  # Salida: Rex está ladrando! (método de instancia)
print(Perro.contar_perros())  # Salida: Total de perros: 2 (método de clase)
```

Salida:

```plain text
Rex
Luna
2
Rex está ladrando!
Total de perros: 2
```

---

## Se puede destacar que:

- Para compartir una variable entre todos los objetos de una clase, se debe declarar como variable de clase o atributo de clase.
- Las variables de clase se declaran sin `self` y no forman parte de los objetos de la clase.
- El acceso a variables de clase se realiza con la sintaxis `classname.varname`.
- Los métodos de clase no reciben el argumento `self`, a diferencia de los métodos de instancia.
- El acceso a métodos de clase se hace con `classname.methodname()`.
- Las variables de clase pueden usarse para contar cuántos objetos se han creado a partir de una clase.
---

## Funciones `vars()` y `dir()`

> 💡 Existen dos útiles funciones integradas (built-in) `vars()` y `dir()`. De ellas, `vars()` devuelve un **diccionario de atributos y sus valores,** mientras que `dir()` devuelve una **lista de atributos.**

---

### Ejemplo aplicado a una clase propia de la librería estandar de Python. 

```python
import math # módulo estándar

print("--- Atributos del módulo 'math' (vars) ---")
print("Estos son los atributos y sus valores definidos en el diccionario interno de 'math':")
print(vars(math)) 
print("\n" + "="*50 + "\n") # Separador para mayor claridad

print("--- Lista de atributos y métodos del módulo 'math' (dir) ---")
print("Estos son todos los nombres (atributos y métodos) accesibles en el módulo 'math':")
print(dir(math))
print("\n" + "="*50 + "\n") # Separador final
```

Salida:

```plain text
--- Atributos del módulo 'math' (vars) ---
Estos son los atributos y sus valores definidos en el diccionario interno de 'math':
{'__name__': 'math', '__doc__': 'This module provides access to the mathematical functions\ndefined by the C standard.', '__package__': '', '__loader__': <_frozen_importlib_external.ExtensionFileLoader object at 0x7fd4f30697e0>, '__spec__': ModuleSpec(name='math', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd4f30697e0>, origin='/usr/local/lib/python3.10/lib-dynload/math.cpython-310-x86_64-linux-gnu.so'), 'acos': <built-in function acos>, 'acosh': <built-in function acosh>, 'asin': <built-in function asin>, 'asinh': <built-in function asinh>, 'atan': <built-in function atan>, 'atan2': <built-in function atan2>, 'atanh': <built-in function atanh>, 'ceil': <built-in function ceil>, 'copysign': <built-in function copysign>, 'cos': <built-in function cos>, 'cosh': <built-in function cosh>, 'degrees': <built-in function degrees>, 'dist': <built-in function dist>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'exp': <built-in function exp>, 'expm1': <built-in function expm1>, 'fabs': <built-in function fabs>, 'factorial': <built-in function factorial>, 'floor': <built-in function floor>, 'fmod': <built-in function fmod>, 'frexp': <built-in function frexp>, 'fsum': <built-in function fsum>, 'gamma': <built-in function gamma>, 'gcd': <built-in function gcd>, 'hypot': <built-in function hypot>, 'isclose': <built-in function isclose>, 'isfinite': <built-in function isfinite>, 'isinf': <built-in function isinf>, 'isnan': <built-in function isnan>, 'isqrt': <built-in function isqrt>, 'lcm': <built-in function lcm>, 'ldexp': <built-in function ldexp>, 'lgamma': <built-in function lgamma>, 'log': <built-in function log>, 'log1p': <built-in function log1p>, 'log10': <built-in function log10>, 'log2': <built-in function log2>, 'modf': <built-in function modf>, 'pow': <built-in function pow>, 'radians': <built-in function radians>, 'remainder': <built-in function remainder>, 'sin': <built-in function sin>, 'sinh': <built-in function sinh>, 'sqrt': <built-in function sqrt>, 'tan': <built-in function tan>, 'tanh': <built-in function tanh>, 'trunc': <built-in function trunc>, 'prod': <built-in function prod>, 'perm': <built-in function perm>, 'comb': <built-in function comb>, 'nextafter': <built-in function nextafter>, 'ulp': <built-in function ulp>, '__file__': '/usr/local/lib/python3.10/lib-dynload/math.cpython-310-x86_64-linux-gnu.so', 'pi': 3.141592653589793, 'e': 2.718281828459045, 'tau': 6.283185307179586, 'inf': inf, 'nan': nan}

==================================================

--- Lista de atributos y métodos del módulo 'math' (dir) ---
Estos son todos los nombres (atributos y métodos) accesibles en el módulo 'math':
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

==================================================


```

---

Ejemplo aplicado a una clase creada por un usuario:

```python
class Fruta:
    count = 0

    def __init__(self, nombre='', tamaño=0, color=''):
        self._nombre = nombre
        self._tamaño = tamaño
        self._color = color
        Fruta.count += 1

    def display():
        print(Fruta.count)

f1 = Fruta('Banana', 5, 'Amarillo')
print(vars(Fruta))
print(dir(Fruta))

```

Salida:

```plain text
{'__module__': '__main__', 'count': 1, '__init__': <function Fruta.__init__ at 0x7fd4a1eabd90>, 'display': <function Fruta.display at 0x7fd4a1eabf40>, '__dict__': <attribute '__dict__' of 'Fruta' objects>, '__weakref__': <attribute '__weakref__' of 'Fruta' objects>, '__doc__': None}
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'count', 'display']


```

---

```python
print(vars(f1))
print(dir(f1))
```

Salida:

```plain text
{'_nombre': 'Banana', '_tamaño': 5, '_color': 'Amarillo'}
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_color', '_nombre', '_tamaño', 'count', 'display']
```

---

### Ejemplo 2.1 · Crear objetos de una clase vacía

> 💡  Un sistema de gestión de pedidos necesita empezar definiendo el tipo `Pedido`, aunque todavía no tenga atributos ni comportamiento. Crea una clase `Pedido` **vacía**, usando `pass` como cuerpo.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_2_1_crear_objetos.py`

---

```python
class Pedido:
    pass

pedido_a = Pedido()
pedido_b = Pedido()

print(type(pedido_a))
print(type(pedido_a).__name__)
print(isinstance(pedido_a, Pedido))
print(isinstance("PED-1001", Pedido))
print(pedido_a is pedido_b)
```

```plain text
<class '__main__.Pedido'>
Pedido
True
False
False
```

---

### Ejemplo 2.2 · Atributos añadidos a mano y el problema que generan

> 💡 En Python, a un objeto se le pueden añadir atributos en cualquier momento con la notación `objeto.atributo = valor`. En este ejercicio vas a comprobar qué problema genera hacerlo así.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_2_2_atributos_a_mano.py`

---

```python
class Pedido:
    pass

pedido_a = Pedido()
pedido_a.codigo = "PED-1001"
pedido_a.importe = 149.90

pedido_b = Pedido()
pedido_b.codigo = "PED-1002"

print(pedido_a.codigo, pedido_a.importe)
print(pedido_b.codigo)
print(hasattr(pedido_a, "importe"))
print(hasattr(pedido_b, "importe"))
print(vars(pedido_a))
print(vars(pedido_b))
```

**Salida esperada:**

```plain text
PED-1001 149.9
PED-1002
True
False
{'codigo': 'PED-1001', 'importe': 149.9}
{'codigo': 'PED-1002'}
```

---

## Sección 3. El constructor `__init__` y `self`

### Definición

El **constructor** es un método especial llamado `__init__` (dos guiones bajos a cada lado) que Python ejecuta **automáticamente** cada vez que se crea un objeto. Su función es dar a cada objeto sus atributos iniciales, de modo que **todos los objetos de la clase nazcan con la misma estructura**.

El primer parámetro de `__init__`, y de cualquier método de instancia, es **`self`**: una referencia al objeto que se está creando o usando. `self.nombre = nombre` significa «guarda en **este** objeto un atributo `nombre` con el valor recibido».

---

### Sintaxis

```python
class NombreDeLaClase:
    def __init__(self, parametro1, parametro2, parametro_opcional=valor_por_defecto):
        self.atributo1 = parametro1
        self.atributo2 = parametro2
        self.atributo3 = parametro_opcional
        self.atributo_calculado = ...       # no tiene por qué venir de un parámetro

objeto = NombreDeLaClase(valor1, valor2)    # self NO se pasa: lo pone Python
```

---

Qué ocurre al ejecutar `objeto = NombreDeLaClase(valor1, valor2)`:

13. Python crea un objeto vacío de la clase.
14. Llama a `__init__` pasando ese objeto como `self`, seguido de `valor1` y `valor2`.
15. `__init__` rellena los atributos del objeto.
16. El objeto ya inicializado se asigna a la variable `objeto`.
> `__init__` no lleva `return`: su trabajo es inicializar el objeto, no devolver un valor.

---

### Ejemplo 3.1 · Fuentes de datos de una plataforma

> 💡 💡 El equipo de datos quiere registrar las fuentes de las que se alimenta su *data lake*. Crea una clase `FuenteDatos` cuyo constructor reciba tres **parámetros obligatorios** y los guarde como atributos del objeto:
- `nombre`: identificador de la fuente.
- `tipo`: forma de acceso a los datos (por ejemplo, `"api"` o `"fichero"`).
- `ubicacion`: URL o ruta donde se encuentran los datos.
Después, crea dos fuentes:

- `crm`: `"crm_clientes"`, de tipo `"api"`, ubicada en `"https://api.crm.empresa.com/v2"`.
- `erp`: `"erp_facturas"`, de tipo `"fichero"`, ubicada en `"/landing/erp/facturas/"`.
Por último:

1. Muestra el nombre, tipo y ubicación de cada fuente en una línea, separados por `|`.
2. Usa la función `vars()` sobre `erp` para mostrar todos sus atributos en forma de diccionario.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_3_1_fuente_datos.py`

---

```python
class FuenteDatos:
    def __init__(self, nombre, tipo, ubicacion):
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion

crm = FuenteDatos("crm_clientes", "api", "https://api.crm.empresa.com/v2")
erp = FuenteDatos("erp_facturas", "fichero", "/landing/erp/facturas/")

print(crm.nombre, "|", crm.tipo, "|", crm.ubicacion)
print(erp.nombre, "|", erp.tipo, "|", erp.ubicacion)
print(vars(erp))
```

**Salida esperada:**

```plain text
crm_clientes | api | https://api.crm.empresa.com/v2
erp_facturas | fichero | /landing/erp/facturas/
{'nombre': 'erp_facturas', 'tipo': 'fichero', 'ubicacion': '/landing/erp/facturas/'}
```

---

### Ejemplo 3.2 · Valores por defecto y atributos de estado

> 💡  Crea una clase `TareaIngesta` que represente una tarea de carga de datos. El constructor debe recibir:
- `nombre` y `origen` como **parámetros obligatorios**.
- `formato` y `reintentos_max` como **parámetros opcionales**, con valores por defecto `"csv"` y `3`.
Además, el constructor debe crear dos **atributos de estado** que **no se reciben como parámetro** y que toda tarea nueva tiene con el mismo valor inicial:

- `estado`, con el valor `"pendiente"`.
- `filas_cargadas`, con el valor `0`.
Después, crea dos tareas:

- `t1`: `"ventas_diarias"` desde `"sftp_tiendas"`, usando los valores por defecto.
- `t2`: `"clics_web"` desde `"blob_logs"`, con formato `"json"` y `5` reintentos.
Por último, recorre ambas tareas con un bucle `for` y muestra en una línea por tarea su nombre, formato, reintentos, estado y filas cargadas, alineando las columnas como en la salida esperada.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_3_2_tarea_ingesta.py`

---

```python
class TareaIngesta:
    def __init__(self, nombre, origen, formato="csv", reintentos_max=3):
        self.nombre = nombre
        self.origen = origen
        self.formato = formato
        self.reintentos_max = reintentos_max
        self.estado = "pendiente"
        self.filas_cargadas = 0

t1 = TareaIngesta("ventas_diarias", "sftp_tiendas")
t2 = TareaIngesta("clics_web", "blob_logs", formato="json", reintentos_max=5)

for tarea in [t1, t2]:
    print(f"{tarea.nombre:<15} formato={tarea.formato:<5} reintentos={tarea.reintentos_max} "
          f"estado={tarea.estado} filas={tarea.filas_cargadas}")
```

**Salida esperada:**

```plain text
ventas_diarias  formato=csv   reintentos=3 estado=pendiente filas=0
clics_web       formato=json  reintentos=5 estado=pendiente filas=0
```

---

### Ejemplo 3.3 · Atributos calculados en el constructor

> 💡 Cuando llega un fichero a la zona *landing*, el equipo de datos necesita extraer automáticamente información derivada de su ruta y su tamaño.
> La **zona *****landing*** (zona de aterrizaje o de llegada) es el primer área de almacenamiento de un *data lake* o de una plataforma de datos: el lugar donde se depositan los ficheros **tal como llegan de los sistemas de origen**, sin transformar ni validar.

Crea una clase `ArchivoLanding` cuyo constructor reciba dos **parámetros obligatorios**:
- `ruta`: ruta completa del fichero.
- `tamano_bytes`: tamaño del fichero en bytes.
Además de guardar ambos valores, el constructor debe crear cuatro **atributos calculados** a partir de ellos, sin recibirlos como parámetro:

- `nombre`: el nombre del fichero, es decir, la última parte de la ruta tras la última `/`.
- `extension`: la extensión del fichero, obtenida a partir de `nombre` y convertida a minúsculas.
- `tamano_mb`: el tamaño en megabytes, redondeado a 2 decimales (1 MB = 1024 × 1024 bytes).
- `es_grande`: `True` si el fichero supera los 100 MB y `False` en caso contrario.
Ten en cuenta que algunos atributos dependen de otros, así que piensa en qué orden debes crearlos.

Después, crea un objeto `archivo` con la ruta `"/landing/ventas/2026/10/ventas_tienda_07.CSV"` y un tamaño de `157_286_400` bytes, y muestra por pantalla su nombre, extensión, tamaño en MB y si es grande.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_3_3_archivo_landing.py`

---

```python
class ArchivoLanding:
    def __init__(self, ruta, tamano_bytes):
        self.ruta = ruta
        self.tamano_bytes = tamano_bytes
        self.nombre = ruta.split("/")[-1]
        self.extension = self.nombre.split(".")[-1].lower()
        self.tamano_mb = round(tamano_bytes / (1024 * 1024), 2)
        self.es_grande = self.tamano_mb > 100

archivo = ArchivoLanding("/landing/ventas/2026/10/ventas_tienda_07.CSV", 157_286_400)

print(archivo.nombre)
print(archivo.extension)
print(archivo.tamano_mb)
print(archivo.es_grande)
```

**Paso a paso:**

17. `self.nombre` se obtiene partiendo la ruta por `/` y tomando el último elemento.
18. `self.extension` reutiliza un atributo ya creado (`self.nombre`) y lo normaliza a minúsculas.
19. `self.tamano_mb` convierte bytes a megabytes (1 MB = 1024 × 1024 bytes).
20. `self.es_grande` depende de otro atributo calculado. El orden de las líneas importa: no se puede usar `self.tamano_mb` antes de haberlo creado.
**Salida esperada:**

```plain text
ventas_tienda_07.CSV
csv
150.0
True
```

---

## Sección 4. Métodos de instancia

### Definición

> 💡 Un **método de instancia** es una función definida dentro de la clase que trabaja con los datos de un objeto concreto. Igual que `__init__`, recibe `self` como primer parámetro, y a través de él puede **leer** y **modificar** los atributos del objeto o **llamar a otros métodos** del mismo objeto.

---

### Sintaxis

```python
class NombreDeLaClase:
    def __init__(self, ...):
        ...

    def nombre_metodo(self, parametro):
        # usa self.atributo y parametro
        return resultado

objeto = NombreDeLaClase(...)
objeto.nombre_metodo(argumento)          # forma habitual
NombreDeLaClase.nombre_metodo(objeto, argumento)   # forma equivalente
```

---

> La forma habitual `objeto.metodo(argumento)` es una abreviatura: Python la traduce a `Clase.metodo(objeto, argumento)`. Por eso `self` aparece en la definición pero no en la llamada.

| Tipo de método | Qué hace | Ejemplo |
| --- | --- | --- |
| Consulta | Lee atributos y devuelve un resultado | `importe_total()` |
| Modificador | Cambia el estado del objeto | `cargar(filas)` |
| Compuesto | Llama a otros métodos con `self.metodo()` | `total()` usa `subtotal()` |

---

### Ejemplo 4.1 · Lote de registros con métodos de consulta

> 💡 💡 Un proceso de ingesta agrupa los tickets de venta de cada día en **lotes**. Crea una clase `LoteDatos` que permita ir añadiendo registros a un lote y consultar información sobre ellos.  El constructor debe recibir el parámetro obligatorio `id_lote` y crear el atributo `registros` como una **lista vacía** propia de cada lote.

---

> 📄 `clase_18_clases_objetos/teoria/ejemplo_4_1_lote_datos.py`

```python
class LoteDatos:
    def __init__(self, id_lote):
        self.id_lote = id_lote
        self.registros = []

    def agregar(self, registro):
        self.registros.append(registro)

    def total_registros(self):
        return len(self.registros)

    def importe_total(self):
        total = 0
        for registro in self.registros:
            total += registro["importe"]
        return round(total, 2)

lote = LoteDatos("L-2026-10-26-01")
lote.agregar({"ticket": "T1", "importe": 23.50})
lote.agregar({"ticket": "T2", "importe": 8.75})
lote.agregar({"ticket": "T3", "importe": 112.00})

print(lote.id_lote)
print(lote.total_registros())
print(lote.importe_total())
print(LoteDatos.total_registros(lote))
```

**Salida esperada:**

```plain text
L-2026-10-26-01
3
144.25
3
```

---

### Ejemplo 4.2 · Métodos que controlan el ciclo de vida de una tarea

> 💡 Una tarea de ingesta pasa por distintos estados a lo largo de su vida: `"pendiente"` → `"en_ejecucion"` → `"completada"`. Crea una clase `TareaIngesta` cuyos **métodos protejan sus propias reglas**, de forma que la tarea no permita acciones que no correspondan a su estado actual.
El constructor debe recibir el parámetro obligatorio `nombre` y crear dos atributos de estado con valor inicial fijo:
- `estado`, con el valor `"pendiente"`.
- `filas_cargadas`, con el valor `0`.
La clase debe tener tres **métodos**:

- `iniciar()`: solo puede ejecutarse si la tarea está `"pendiente"`. En ese caso, cambia el estado a `"en_ejecucion"` y muestra `[nombre] Iniciada`. Si no, muestra `[nombre] No se puede iniciar: estado actual '<estado>'` y no cambia nada.
- `cargar(filas)`: solo puede ejecutarse si la tarea está `"en_ejecucion"`. En ese caso, suma `filas` a `filas_cargadas` y muestra `[nombre] +<filas> filas (acumulado:<filas_cargadas>)`. Si no, muestra `[nombre] Carga rechazada: la tarea no está en ejecución` y no suma nada.
- `finalizar()`: si la tarea está `"en_ejecucion"`, cambia el estado a `"completada"`. En cualquier caso, muestra `[nombre] Estado final:<estado> con<filas_cargadas> filas`.
Después, crea una tarea llamada `"ventas_diarias"` y ejecuta, **en este orden**, las siguientes llamadas:

1. `cargar(500)`
2. `iniciar()`
3. `cargar(12000)`
4. `cargar(8500)`
5. `iniciar()`
6. `finalizar()`
Antes de ejecutar el código, intenta predecir qué mensaje mostrará cada llamada. ¿Cuántas filas se habrán cargado al final? ¿Por qué no cuentan las 500 de la primera llamada?

---

> 📄 `clase_18_clases_objetos/teoria/ejemplo_4_2_ciclo_vida_tarea.py`

```python
class TareaIngesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "pendiente"
        self.filas_cargadas = 0

    def iniciar(self):
        if self.estado != "pendiente":
            print(f"[{self.nombre}] No se puede iniciar: estado actual '{self.estado}'")
            return
        self.estado = "en_ejecucion"
        print(f"[{self.nombre}] Iniciada")

    def cargar(self, filas):
        if self.estado != "en_ejecucion":
            print(f"[{self.nombre}] Carga rechazada: la tarea no está en ejecución")
            return
        self.filas_cargadas += filas
        print(f"[{self.nombre}] +{filas} filas (acumulado:{self.filas_cargadas})")

    def finalizar(self):
        if self.estado == "en_ejecucion":
            self.estado = "completada"
        print(f"[{self.nombre}] Estado final:{self.estado} con{self.filas_cargadas} filas")

tarea = TareaIngesta("ventas_diarias")
tarea.cargar(500)
tarea.iniciar()
tarea.cargar(12000)
tarea.cargar(8500)
tarea.iniciar()
tarea.finalizar()
```

**Salida esperada:**

```plain text
[ventas_diarias] Carga rechazada: la tarea no está en ejecución
[ventas_diarias] Iniciada
[ventas_diarias] +12000 filas (acumulado: 12000)
[ventas_diarias] +8500 filas (acumulado: 20500)
[ventas_diarias] No se puede iniciar: estado actual 'en_ejecucion'
[ventas_diarias] Estado final: completada con 20500 filas
```

### Ejemplo 4.3 · Métodos que llaman a otros métodos

Una factura calcula el total reutilizando el subtotal y los impuestos.

> 💡  El departamento de facturación necesita generar facturas que calculen automáticamente su subtotal, sus impuestos y su total. Crea una clase `Factura` en la que **unos métodos reutilicen a otros** en lugar de repetir los mismos cálculos.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_4_3_factura.py`

---

```python
class Factura:
    def __init__(self, numero, cliente, tipo_iva=0.21):
        self.numero = numero
        self.cliente = cliente
        self.tipo_iva = tipo_iva
        self.lineas = []

    def agregar_linea(self, concepto, cantidad, precio_unitario):
        self.lineas.append({"concepto": concepto, "cantidad": cantidad, "precio": precio_unitario})

    def subtotal(self):
        return round(sum([linea["cantidad"] * linea["precio"] for linea in self.lineas]), 2)

    def impuestos(self):
        return round(self.subtotal() * self.tipo_iva, 2)

    def total(self):
        return round(self.subtotal() + self.impuestos(), 2)

    def imprimir(self):
        print(f"Factura{self.numero} · Cliente:{self.cliente}")
        for linea in self.lineas:
            importe = linea["cantidad"] * linea["precio"]
            print(f"{linea['concepto']:<22}{linea['cantidad']:>3} x{linea['precio']:>8.2f} ={importe:>9.2f}")
        print(f"{'Subtotal':<38}{self.subtotal():>9.2f}")
        print(f"{'IVA ' + str(int(self.tipo_iva * 100)) + '%':<38}{self.impuestos():>9.2f}")
        print(f"{'TOTAL':<38}{self.total():>9.2f}")

factura = Factura("F-2026-0412", "Logística Iberia S.L.")
factura.agregar_linea("Licencia ETL (usuario)", 3, 49.90)
factura.agregar_linea("Soporte anual", 1, 1200.00)
factura.agregar_linea("Formación (jornada)", 2, 350.00)
factura.imprimir()
```

**Salida esperada:**

```plain text
Factura F-2026-0412 · Cliente: Logística Iberia S.L.
  Licencia ETL (usuario)   3 x    49.90 =    149.70
  Soporte anual            1 x  1200.00 =   1200.00
  Formación (jornada)      2 x   350.00 =    700.00
  Subtotal                                 2049.70
  IVA 21%                                   430.44
  TOTAL                                    2480.14
```

---

## Sección 5. Atributos de clase y atributos de instancia

> 💡
### Definición

- Un **atributo de instancia** se crea con `self.atributo` y pertenece a **un objeto concreto**. Cada objeto tiene su propio valor.
- Un **atributo de clase** se define directamente dentro de la clase, fuera de cualquier método, y es **compartido por todos los objetos**. Se usa para constantes comunes (unidades, umbrales por defecto, versión de un esquema) o para contadores globales.
Cuando se lee `objeto.atributo`, Python busca **primero en el objeto** y, si no lo encuentra, **en la clase**.

---

### Sintaxis

```python
class NombreDeLaClase:
    atributo_de_clase = valor          # compartido

    def __init__(self, dato):
        self.atributo_de_instancia = dato   # propio de cada objeto
        NombreDeLaClase.atributo_de_clase += 1  # para modificar el compartido, se usa el nombre de la clase
```

---

|  | Atributo de instancia | Atributo de clase |
| --- | --- | --- |
| Dónde se define | Dentro de los métodos, con `self.` | En el cuerpo de la clase |
| A quién pertenece | A cada objeto | A la clase (todos lo comparten) |
| Cómo se modifica | `self.atributo = valor` | `Clase.atributo = valor` |
| Uso típico | Datos de cada registro | Constantes, contadores, configuración común |

---

### Ejemplo 5.1 · Constante compartida y contador de objetos

> 💡 💡 Una cadena logística monitoriza la temperatura de sus almacenes mediante sensores. Crea una clase `Sensor` que combine **atributos de clase**, compartidos por todos los sensores, con **atributos de instancia**, propios de cada uno.

---

> 📄 `clase_18_clases_objetos/teoria/ejemplo_5_1_sensor.py`

```python
class Sensor:
    unidad = "°C"
    total_sensores = 0

    def __init__(self, codigo, ubicacion):
        self.codigo = codigo
        self.ubicacion = ubicacion
        Sensor.total_sensores += 1

    def describir(self, valor):
        return f"{self.codigo} ({self.ubicacion}):{valor}{self.unidad}"

s1 = Sensor("TMP-01", "Cámara frigorífica A")
s2 = Sensor("TMP-02", "Cámara frigorífica B")
s3 = Sensor("TMP-03", "Muelle de carga")

print(s1.describir(-18.4))
print(s3.describir(12.1))
print("Sensores registrados:", Sensor.total_sensores)
print(s2.total_sensores)
```

**Salida esperada:**

```plain text
TMP-01 (Cámara frigorífica A): -18.4 °C
TMP-03 (Muelle de carga): 12.1 °C
Sensores registrados: 3
3
```

---

### Ejemplo 5.2 · Un objeto puede «tapar» el atributo de clase

> 💡 💡 Un equipo de calidad de datos define un **umbral máximo de nulos** que se aplica por defecto a todas las columnas, aunque algunas columnas concretas pueden tolerar más. En este ejercicio vas a comprobar qué ocurre cuando un objeto **"tapa"** un atributo de clase con uno propio.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_5_2_regla_calidad.py`

---

```python
class ReglaCalidad:
    umbral_nulos = 0.05

    def __init__(self, columna):
        self.columna = columna

    def evaluar(self, nulos, total):
        ratio = nulos / total
        resultado = "OK" if ratio <= self.umbral_nulos else "FALLO"
        return f"{self.columna}:{ratio:.1%} nulos (umbral{self.umbral_nulos:.0%}) ->{resultado}"

r_email = ReglaCalidad("email")
r_telefono = ReglaCalidad("telefono")
r_telefono.umbral_nulos = 0.20

print(r_email.evaluar(80, 1000))
print(r_telefono.evaluar(150, 1000))
print(vars(r_email))
print(vars(r_telefono))

ReglaCalidad.umbral_nulos = 0.10
print(r_email.evaluar(80, 1000))
print(r_telefono.evaluar(150, 1000))
```

**Salida esperada:**

```plain text
email: 8.0% nulos (umbral 5%) -> FALLO
telefono: 15.0% nulos (umbral 20%) -> OK
{'columna': 'email'}
{'columna': 'telefono', 'umbral_nulos': 0.2}
email: 8.0% nulos (umbral 10%) -> OK
telefono: 15.0% nulos (umbral 20%) -> OK
```

---

### Ejemplo 5.3 · La trampa de las listas como atributo de clase

> 💡 Un equipo de integración necesita una cola de mensajes independiente para cada *topic* (por ejemplo, `"pedidos"` y `"pagos"`). Un desarrollador ha definido la lista de mensajes **como atributo de clase** por error. En este ejercicio vas a reproducir el fallo y descubrir por qué ocurre.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_5_3_cola_mensajes_error.py`

---

```python
class ColaMensajes:
    mensajes = []          # atributo de clase mutable: compartido por todas las colas

    def __init__(self, topic):
        self.topic = topic

    def publicar(self, mensaje):
        self.mensajes.append(mensaje)

pedidos = ColaMensajes("pedidos")
pagos = ColaMensajes("pagos")
pedidos.publicar("pedido 501 creado")
pagos.publicar("pago 77 confirmado")

print(pedidos.topic, pedidos.mensajes)
print(pagos.topic, pagos.mensajes)
print(pedidos.mensajes is pagos.mensajes)
```

**Salida obtenida (incorrecta):**

```plain text
pedidos ['pedido 501 creado', 'pago 77 confirmado']
pagos ['pedido 501 creado', 'pago 77 confirmado']
True
```

---

> 💡 `self.mensajes.append(...)` no crea un atributo nuevo: **modifica la lista de la clase**, que es la misma para todas las colas. Los mensajes de pagos aparecen en pedidos y viceversa. La corrección es crear la lista en el constructor, de modo que cada objeto tenga la suya:

> 📄 `clase_18_clases_objetos/teoria/ejemplo_5_3_cola_mensajes_corregida.py`

---

```python
class ColaMensajes:
    def __init__(self, topic):
        self.topic = topic
        self.mensajes = []     # atributo de instancia: una lista por cola

    def publicar(self, mensaje):
        self.mensajes.append(mensaje)

pedidos = ColaMensajes("pedidos")
pagos = ColaMensajes("pagos")
pedidos.publicar("pedido 501 creado")
pagos.publicar("pago 77 confirmado")

print(pedidos.topic, pedidos.mensajes)
print(pagos.topic, pagos.mensajes)
print(pedidos.mensajes is pagos.mensajes)
```

**Salida esperada:**

```plain text
pedidos ['pedido 501 creado']
pagos ['pago 77 confirmado']
False
```

> **Regla práctica:** las listas, diccionarios y `set` que deban ser propios de cada objeto se crean siempre dentro de `__init__` con `self.`.

---

## Sección 6. Representar objetos como texto: `__str__` y `__repr__`

> 💡
### Definición

Si se imprime un objeto de una clase propia sin más, Python muestra algo como `<__main__.Producto object at 0x7f3a2c1b9d50>`: el nombre de la clase y una dirección de memoria que cambia en cada ejecución. Para controlar cómo se muestra un objeto, la clase puede definir dos métodos especiales:

| Método | Lo usa | Pensado para | Estilo recomendado |
| --- | --- | --- | --- |
| `__str__` | `print(obj)`, `str(obj)`, f-strings | Personas: informes, logs, pantallas | Legible y amigable |
| `__repr__` | `repr(obj)`, consola interactiva, objetos dentro de listas o diccionarios | Desarrolladores: depuración | Preciso; idealmente, parecido al código que crea el objeto |

Ambos deben **devolver** (`return`) un `str`, no imprimirlo. Si una clase solo define `__repr__`, Python también lo usa para `print`.

---

### Sintaxis

```python
class NombreDeLaClase:
    def __init__(self, ...):
        ...

    def __str__(self):
        return "texto legible"

    def __repr__(self):
        return "NombreDeLaClase(atributo=valor, ...)"
```

---

### Ejemplo 6.1 · Producto de un catálogo

> 💡 Una tienda online necesita representar los productos de su catálogo de forma legible, tanto para mostrarlos a los usuarios como para depurarlos en el código. Crea una clase `Producto` que defina **dos representaciones en texto** distintas mediante los métodos especiales `__str__` y `__repr__`.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_6_1_producto.py`

---

```python
class Producto:
    def __init__(self, sku, nombre, precio):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} ({self.sku}) -{self.precio:.2f} €"

    def __repr__(self):
        return f"Producto(sku='{self.sku}', nombre='{self.nombre}', precio={self.precio})"

p = Producto("SKU-4471", "Auriculares BT", 59.9)

print(p)
print(str(p))
print(repr(p))
print(f"Producto destacado:{p}")

catalogo = [p, Producto("SKU-1020", "Cargador USB-C", 19.95)]
print(catalogo)
```

**Salida esperada:**

```plain text
Auriculares BT (SKU-4471) - 59.90 €
Auriculares BT (SKU-4471) - 59.90 €
Producto(sku='SKU-4471', nombre='Auriculares BT', precio=59.9)
Producto destacado: Auriculares BT (SKU-4471) - 59.90 €
[Producto(sku='SKU-4471', nombre='Auriculares BT', precio=59.9), Producto(sku='SKU-1020', nombre='Cargador USB-C', precio=19.95)]
```

---

### Ejemplo 6.2 · Eventos de log con formato homogéneo

> 💡 El equipo de plataforma necesita que todos los eventos de log de sus *pipelines* se muestren con un **formato homogéneo**, sin tener que repetir el formato en cada `print`. Crea una clase `EventoLog` que defina cómo se representa cada evento mediante los métodos especiales `__str__` y `__repr__`.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_6_2_evento_log.py`

---

```python
class EventoLog:
    def __init__(self, timestamp, nivel, servicio, mensaje):
        self.timestamp = timestamp
        self.nivel = nivel
        self.servicio = servicio
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.timestamp} [{self.nivel:<5}]{self.servicio:<12} |{self.mensaje}"

    def __repr__(self):
        return f"EventoLog('{self.timestamp}', '{self.nivel}', '{self.servicio}')"

eventos = [
    EventoLog("2026-10-26 02:00:01", "INFO", "ingesta", "Inicio de carga de ventas"),
    EventoLog("2026-10-26 02:03:47", "WARN", "ingesta", "Fichero tienda_12 llega vacío"),
    EventoLog("2026-10-26 02:05:10", "ERROR", "transform", "Columna 'importe' con texto no numérico"),
    EventoLog("2026-10-26 02:09:33", "INFO", "carga", "Lote publicado en zona curated"),
]

for evento in eventos:
    print(evento)

errores = [e for e in eventos if e.nivel == "ERROR"]
print(errores)
```

**Salida esperada:**

```plain text
2026-10-26 02:00:01 [INFO ] ingesta      | Inicio de carga de ventas
2026-10-26 02:03:47 [WARN ] ingesta      | Fichero tienda_12 llega vacío
2026-10-26 02:05:10 [ERROR] transform    | Columna 'importe' con texto no numérico
2026-10-26 02:09:33 [INFO ] carga        | Lote publicado en zona curated
[EventoLog('2026-10-26 02:05:10', 'ERROR', 'transform')]
```

---

## Sección 7. Objetos como referencias, colecciones de objetos y composición

> 💡
### Definición

- Una variable **no contiene** el objeto: contiene una **referencia** a él. Si se hace `b = a`, las dos variables apuntan al **mismo** objeto, y un cambio hecho a través de `b` se ve desde `a`. Lo mismo ocurre al pasar un objeto a una función.
- `is` comprueba si dos variables apuntan al mismo objeto. `==` compara valores.
- Los objetos se pueden guardar en **listas** y **diccionarios** como cualquier otro valor, y procesarse con bucles y comprehensions.
- Hay **composición** cuando un objeto contiene otros objetos como atributos: un `Pipeline` tiene `Etapa`s, un `Pedido` tiene `LineaPedido`s. Es la forma natural de modelar sistemas formados por piezas.

---

### Sintaxis

```python
alias = objeto              # misma referencia, no una copia
alias is objeto             # True

coleccion = [Clase(...), Clase(...)]           # lista de objetos
indice = {obj.clave: obj for obj in coleccion} # diccionario de objetos

class Contenedor:
    def __init__(self):
        self.partes = []                       # composición: guarda objetos de otra clase

    def agregar(self, parte):
        self.partes.append(parte)
```

---

### Ejemplo 7.1 · Referencias compartidas

> 💡 💡 Un programa de fidelización gestiona los puntos que acumula cada cliente. En este ejercicio vas a comprobar que una variable **no contiene** el objeto, sino una **referencia** a él, y qué consecuencias tiene esto al asignar variables y al pasar objetos a funciones.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_7_1_referencias.py`

---

```python
class ClienteFidelidad:
    def __init__(self, id_cliente, puntos=0):
        self.id_cliente = id_cliente
        self.puntos = puntos

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad

def aplicar_bono_bienvenida(cliente):
    cliente.sumar_puntos(200)

original = ClienteFidelidad("C-88", 100)
alias = original
alias.sumar_puntos(50)
print(original.puntos)
print(alias is original)

otro = ClienteFidelidad("C-88", 150)
print(otro is original)
print(otro.puntos == original.puntos)

aplicar_bono_bienvenida(otro)
print(otro.puntos)
print(original.puntos)
```

**Salida esperada:**

```plain text
150
True
False
True
350
150
```

### Ejemplo 7.2 · Procesar una lista de objetos

> 💡 💡 Una empresa de paquetería necesita analizar los envíos del día. Crea una clase `Envio` y procesa una **lista de objetos** de esa clase para obtener distintos indicadores.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_7_2_envios.py`

---

```python
class Envio:
    def __init__(self, id_envio, destino, peso_kg, entregado):
        self.id_envio = id_envio
        self.destino = destino
        self.peso_kg = peso_kg
        self.entregado = entregado

    def __repr__(self):
        return f"Envio({self.id_envio},{self.destino},{self.peso_kg} kg)"

def obtener_peso(envio):
    return envio.peso_kg

envios = [
    Envio("E-01", "Madrid", 2.5, True),
    Envio("E-02", "Sevilla", 14.0, False),
    Envio("E-03", "Madrid", 0.8, True),
    Envio("E-04", "Bilbao", 7.2, False),
    Envio("E-05", "Sevilla", 3.1, True),
]

peso_total = sum([e.peso_kg for e in envios])
pendientes = [e.id_envio for e in envios if not e.entregado]

envios_por_destino = {}
for e in envios:
    envios_por_destino[e.destino] = envios_por_destino.get(e.destino, 0) + 1

mas_pesados = sorted(envios, key=obtener_peso, reverse=True)[:2]

print("Peso total:", round(peso_total, 2), "kg")
print("Pendientes:", pendientes)
print("Envíos por destino:", envios_por_destino)
print("Los 2 más pesados:", mas_pesados)
```

**Salida esperada:**

```plain text
Peso total: 27.6 kg
Pendientes: ['E-02', 'E-04']
Envíos por destino: {'Madrid': 2, 'Sevilla': 2, 'Bilbao': 1}
Los 2 más pesados: [Envio(E-02, Sevilla, 14.0 kg), Envio(E-04, Bilbao, 7.2 kg)]
```

---

### Ejemplo 7.3 · Composición: un pipeline formado por etapas

> 💡 El equipo de datos ejecuta cada noche un *pipeline* que procesa las ventas de las tiendas. Un *pipeline* está formado por varias **etapas** que se ejecutan en orden. Modela este sistema mediante **composición**: un objeto `Pipeline` que contiene objetos `Etapa` como parte de sus atributos.

> 📄 `clase_18_clases_objetos/teoria/ejemplo_7_3_pipeline_etapas.py`

---

```python
class Etapa:
    def __init__(self, nombre, duracion_seg):
        self.nombre = nombre
        self.duracion_seg = duracion_seg
        self.ejecutada = False

    def ejecutar(self):
        self.ejecutada = True
        return f"  OK{self.nombre} ({self.duracion_seg}s)"

class Pipeline:
    def __init__(self, nombre):
        self.nombre = nombre
        self.etapas = []

    def agregar_etapa(self, etapa):
        self.etapas.append(etapa)

    def duracion_total(self):
        return sum([etapa.duracion_seg for etapa in self.etapas])

    def ejecutar(self):
        print(f"Pipeline '{self.nombre}' ({len(self.etapas)} etapas)")
        for etapa in self.etapas:
            print(etapa.ejecutar())
        print(f"Duración total:{self.duracion_total()}s")

pipeline = Pipeline("ventas_nocturno")
pipeline.agregar_etapa(Etapa("extraer_ficheros_tiendas", 120))
pipeline.agregar_etapa(Etapa("validar_esquema", 35))
pipeline.agregar_etapa(Etapa("deduplicar_tickets", 48))
pipeline.agregar_etapa(Etapa("publicar_zona_curated", 60))

print([etapa.ejecutada for etapa in pipeline.etapas])
pipeline.ejecutar()
print([etapa.ejecutada for etapa in pipeline.etapas])
```

**Salida esperada:**

```plain text
[False, False, False, False]
Pipeline 'ventas_nocturno' (4 etapas)
  OK  extraer_ficheros_tiendas (120s)
  OK  validar_esquema (35s)
  OK  deduplicar_tickets (48s)
  OK  publicar_zona_curated (60s)
Duración total: 263s
[True, True, True, True]
```

