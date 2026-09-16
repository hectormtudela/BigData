# 1.1 Entorno 1 — JupyterLab + Almond Kernel + Scala 2.12.21

## Objetivo

El objetivo de este entorno es preparar un entorno interactivo basado en **JupyterLab** que permita crear notebooks y ejecutar código utilizando **Scala 2.12.21** mediante el **Almond Kernel**.

El uso de notebooks permite ejecutar instrucciones de forma interactiva y observar inmediatamente sus resultados, de forma similar al intérprete de Scala utilizado durante el curso.

---

## 1. Instalar los requisitos necesarios

Para poder utilizar JupyterLab junto con Almond y Scala fue necesario preparar previamente el entorno de desarrollo en Windows 11.

Los principales componentes utilizados son:

* **Java / JDK**
* **JupyterLab**
* **Almond Kernel**
* **Scala 2.12.21**

Una vez instalados los requisitos necesarios, se comprobó que las herramientas podían utilizarse correctamente desde la terminal de Windows.

![Requisitos del entorno](parte1/images/entorno1-requisitos.png)

---

## 2. Instalar JupyterLab

La instalación de JupyterLab se realizó utilizando **Python y pip**, el gestor de paquetes de Python.

El comando utilizado para realizar la instalación fue:

```bash
pip install jupyterlab
```

Una vez finalizada la instalación, se comprobó que JupyterLab estaba disponible correctamente.

Para iniciar JupyterLab se utilizó:

```bash
jupyter lab
```

Este comando inicia el servidor local de JupyterLab y permite acceder a la interfaz desde un navegador web.

![Instalación de JupyterLab](images/jupyterlab-install.png)

Al ejecutar el comando, JupyterLab se abrió en el navegador web mediante una dirección local proporcionada por el propio servidor.

![JupyterLab ejecutándose](images/jupyterlab-running.png)

De esta forma se comprobó que JupyterLab estaba correctamente instalado y funcionando en Windows 11.

---

## 3. Instalar Almond Kernel

Una vez JupyterLab estuvo funcionando, se procedió a instalar **Almond**, que permite utilizar Scala dentro de los notebooks de Jupyter.

Almond actúa como un **kernel de Scala para Jupyter**, permitiendo ejecutar código Scala directamente desde las celdas de un notebook.

La instalación se realizó siguiendo el procedimiento correspondiente para Almond y la versión de Scala requerida.

![Instalación de Almond](images/almond-install.png)

Una vez finalizada la instalación, se comprobó que Almond estaba disponible mirando su versión y también desde Jupyter mirando que estaba en la lista de los Kernels.

![Almond version](images/almond-version.png)
![Almond disponible como Kernel](images/almond-kernel.png)

En la lista aparece la opción correspondiente a **Scala**, proporcionada por Almond.

---

## 4. Crear un Notebook con Scala

Una vez instalado Almond, se creó un nuevo Notebook utilizando el kernel de Scala.

Cada celda puede ejecutarse individualmente y el resultado aparece directamente debajo del código.

---

## 5. Verificar la versión de Scala

Una vez creado el Notebook, se comprobó que la versión de Scala utilizada era la requerida para el ejercicio: **Scala 2.12.21**.

Para comprobar la versión se ejecutó una instrucción desde una celda del Notebook.

![Versión de Scala 2.12.21](images/scala-version.png)

El resultado obtenido confirma que el entorno está utilizando:

```text
Scala 2.12.21
```

De esta forma se verifica que Almond está utilizando correctamente la versión de Scala especificada.

---

## 6. Ejecutar código Scala

Una vez comprobada la versión de Scala, se realizaron varias pruebas para verificar que el código Scala podía ejecutarse correctamente dentro del Notebook.

### 6.1. Prueba con variables y `println`

En primer lugar se crearon dos variables utilizando `val` y se mostró un mensaje mediante `println`.

```scala
val nombre = "Scala"
val version = "2.12.21"

println(s"Hola desde$nombre$version")
```

El resultado obtenido fue:

```text
Hola desdeScala2.12.21
```

![Primera prueba de Scala](images/scala-version.png)

Esta prueba permite comprobar el funcionamiento de variables, interpolación de cadenas y salida mediante `println`.

---

### 6.2. Prueba con operaciones numéricas

A continuación se realizó una operación matemática sencilla utilizando dos variables.

```scala
val a = 10
val b = 20
val resultado = a + b

println(resultado)
```

El resultado obtenido fue:

```text
30
```

![Pruebas abajo]

Esta prueba permite comprobar que el Notebook ejecuta correctamente operaciones aritméticas mediante Scala.

---

### 6.3. Prueba con colecciones

Finalmente se creó una colección sencilla utilizando `List`.

```scala
val lenguajes = List("Scala", "Java", "Python")

println(lenguajes)
```

El resultado obtenido fue:

```text
List(Scala, Java, Python)
```

![Pruebas abajo]

Esta prueba permite comprobar la creación y visualización de una colección básica en Scala.

---

## 7. Comprobación final del entorno

Una vez completados todos los pasos, se comprobó que el entorno funcionaba correctamente.

El entorno final está compuesto por:

```text
JupyterLab
    │
    ▼
Almond Kernel
    │
    ▼
Scala 2.12.21
```

El Notebook permite ejecutar código Scala de manera interactiva y mostrar sus resultados directamente en cada celda.

![Comprobación final del entorno](images/entorno1-final.png)

Por tanto, el **Entorno 1 — JupyterLab + Almond Kernel + Scala 2.12.21** queda correctamente configurado y preparado para trabajar con Scala mediante notebooks.

---

## Evidencias

Las evidencias incluidas en esta documentación permiten comprobar:

* JupyterLab correctamente instalado y ejecutándose.
* Almond instalado como kernel.
* Scala disponible como opción para crear un Notebook.
* Uso de **Scala 2.12.21**.
* Ejecución correcta de código Scala.
* Ejecución de una operación numérica.
* Creación y visualización de una colección `List`.
