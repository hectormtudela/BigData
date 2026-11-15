# Práctica 18 · Programación modular y paquetes (Clase 22)

## Objetivo

Resolver y ejecutar **todos los ejemplos de la Clase 22** (programación modular y paquetes): crear módulos, importarlos de distintas formas, entender qué pasa al importar, usar `if __name__ == "__main__":`, organizar clases y funciones en varios archivos, crear paquetes y subpaquetes, usar la biblioteca estándar y construir un pipeline ETL modular (incluida la conversión de un notebook a un proyecto de producción).

## Requisitos

- Python 3.10 o superior (probado con Python 3.13).
- VS Code con la terminal integrada (PowerShell en Windows).
- Para el notebook del ejemplo 9.2: extensión *Jupyter* de VS Code (o `pip install jupyter`).
- No se necesita ninguna librería externa: todo usa la biblioteca estándar.

## Estructura del repositorio

```text
practica_18_programacion_modular/
├── README.md
├── ejemplo_1_1_primer_modulo/
├── ejemplo_2_1_modulo_saludos/
├── ejemplo_2_2_modulo_finanzas/
├── ejemplo_2_3_formas_de_importar/
├── ejemplo_2_4_modulo_comprehensions/
├── ejemplo_3_1_que_pasa_al_importar/
├── ejemplo_3_2_objeto_compartido/
├── ejemplo_4_1_name_main/
├── ejemplo_4_2_clase_con_pruebas/
├── ejemplo_5_1_modulos_con_clases/
├── ejemplo_5_2_clases_y_funciones/
├── ejemplo_6_1_donde_busca_python/
├── ejemplo_7_1_primer_paquete/
├── ejemplo_7_2_subpaquetes/
├── ejemplo_7_3_init_e_imports_relativos/
├── ejemplo_8_1_biblioteca_estandar/
├── ejemplo_9_1_pipeline_modular/
└── ejemplo_9_2_del_notebook_a_produccion/
    ├── informe_ventas.ipynb
    └── pedidos_etl/
```

## Cómo ejecutar cada ejemplo

Cada ejemplo es independiente. Hay que ejecutar **desde dentro de su carpeta** (así `sys.path[0]` es esa carpeta y Python encuentra los módulos):

```powershell
cd ejemplo_1_1_primer_modulo
python main.py
```

Las carpetas `__pycache__/` que aparecen al ejecutar son normales y no se suben a Git (ver `.gitignore`).

---

## Ejemplo 1.1 · Del script único al primer módulo

**Qué se practica:** Sacar las reglas de tarifas de un script `monolito.py` a un módulo `tarifas.py` que importa `main.py`.

**Archivos:** `monolito.py · tarifas.py · main.py`

**Código:** en la carpeta [`ejemplo_1_1_primer_modulo`](./ejemplo_1_1_primer_modulo/).

**Ejecución:**

```powershell
cd ejemplo_1_1_primer_modulo
python monolito.py
python main.py
```

Salida de `python monolito.py`:

```text
A-101: 5.1 €
A-102: 11.88 €
A-103: 3.9 €
```

Salida de `python main.py`:

```text
A-101: 5.1 €
A-102: 11.88 €
A-103: 3.9 €
Tarifa base: 3.5
```

**Conceptos clave:**

- `import tarifas` se escribe sin `.py`; Python busca `tarifas.py` en la carpeta de `main.py`.
- Se usa con la forma `modulo.nombre` (`tarifas.coste_envio()`, `tarifas.TARIFA_BASE`).
- Modularizar no cambia lo que hace el programa, solo cómo está organizado: la salida es idéntica.

---

## Ejemplo 2.1 · Un módulo con una función y una clase

**Qué se practica:** Crear `saludos.py` (función `saludar()` y clase `Saludo`) y usarlo con `import modulo` y con `from modulo import Clase`.

**Archivos:** `saludos.py · main.py`

**Código:** en la carpeta [`ejemplo_2_1_modulo_saludos`](./ejemplo_2_1_modulo_saludos/).

**Ejecución:**

```powershell
cd ejemplo_2_1_modulo_saludos
python main.py
```

Salida de `python main.py`:

```text
Hola, te estoy saludando desde la función saludar() del módulo saludos
Hola, te estoy saludando desde el __init__ de la clase Saludo
Hola Ana, desde la clase Saludo
----------------------------------------
Hola, te estoy saludando desde el __init__ de la clase Saludo
Hola Ana, desde la clase Saludo
```

**Conceptos clave:**

- Forma 1: `import saludos` → `saludos.saludar()`, `saludos.Saludo()`.
- Forma 2: `from saludos import Saludo` → se usa `Saludo()` sin prefijo.
- El `__init__` de la clase se ejecuta al crear el objeto, por eso aparece su mensaje.

---

## Ejemplo 2.2 · Un módulo de funciones financieras

**Qué se practica:** Módulo de funciones puras y constantes (`finanzas.py`) y su inspección como objeto (`type`, `__name__`, `__doc__`, `dir`).

**Archivos:** `finanzas.py · main.py`

**Código:** en la carpeta [`ejemplo_2_2_modulo_finanzas`](./ejemplo_2_2_modulo_finanzas/).

**Ejecución:**

```powershell
cd ejemplo_2_2_modulo_finanzas
python main.py
```

Salida de `python main.py`:

```text
<class 'module'>
finanzas
Funciones financieras del departamento de ventas.
['IVA_GENERAL', 'IVA_REDUCIDO', 'aplicar_descuento', 'con_iva', 'margen']
121.0
110.0
212.5
40.0 %
[145.2, 55.05, 96.8]
```

**Conceptos clave:**

- `type(finanzas)` es `<class 'module'>`: un módulo es un objeto.
- `dir()` filtrando los nombres que empiezan por `_` muestra solo lo escrito por el programador.
- `map(finanzas.con_iva, precios)` pasa la función sin paréntesis: una función sigue siendo un objeto aunque esté en otro archivo.

---

## Ejemplo 2.3 · Las formas de importar y el conflicto de nombres

**Qué se practica:** Las 4 formas de importar (`import`, `import as`, `from import`, `from import as`) y un conflicto de nombres provocado.

**Archivos:** `envios_nacionales.py · envios_internacionales.py · main.py`

**Código:** en la carpeta [`ejemplo_2_3_formas_de_importar`](./ejemplo_2_3_formas_de_importar/).

**Ejecución:**

```powershell
cd ejemplo_2_3_formas_de_importar
python main.py
```

Salida de `python main.py`:

```text
1. nacional 6.4
2. internacional 22.0
3. 6.4
4. 22.0
5. 22.0
   ¿De qué módulo viene ahora? envios_internacionales
```

**Conceptos clave:**

- Con `import modulo` no hay conflicto: el nombre del módulo es el «apellido».
- En el paso 5 el segundo `from ... import calcular_coste` sobrescribe el del paso 3 sin avisar.
- `funcion.__module__` indica en qué módulo se definió: útil para depurar.

---

## Ejemplo 2.4 · Módulo de utilidades con comprehensions y lambdas

**Qué se practica:** `limpieza.py` con comprehension de lista, set y diccionario, expresión generadora y un diccionario de lambdas (`ORDENES`).

**Archivos:** `limpieza.py · main.py`

**Código:** en la carpeta [`ejemplo_2_4_modulo_comprehensions`](./ejemplo_2_4_modulo_comprehensions/).

**Ejecución:**

```powershell
cd ejemplo_2_4_modulo_comprehensions
python main.py
```

Salida de `python main.py`:

```text
['Ana López', 'Luis Pérez', 'Marta Ruiz', 'Ana López']
Dominios: ['empresa.es', 'gmail.com']
4 registros -> 3 emails distintos
Gasto por ciudad: {'Madrid': 525.5, 'Sevilla': 89.9}
Por gasto: [('Ana López', 320.5), ('Marta Ruiz', 145.0)]
Criterios disponibles: ['nombre', 'gasto']
```

**Conceptos clave:**

- Las funciones son puras: no modifican la lista original (`crudos`).
- `dominios()` devuelve un set (sin repetidos); `indexar_por_email()` deduplica porque las claves del dict no se repiten (4 registros → 3 emails).
- `import limpieza as lp` y `from limpieza import ORDENES` conviven: son dos accesos al mismo módulo.

---

## Ejemplo 3.1 · Un módulo de configuración compartido

**Qué se practica:** Qué ocurre al importar: el módulo se ejecuta una sola vez, se guarda en `sys.modules` y se comparte el mismo objeto.

**Archivos:** `configuracion.py · informes.py · main.py`

**Código:** en la carpeta [`ejemplo_3_1_que_pasa_al_importar`](./ejemplo_3_1_que_pasa_al_importar/).

**Ejecución:**

```powershell
cd ejemplo_3_1_que_pasa_al_importar
python main.py
```

Salida de `python main.py`:

```text
Inicio del programa
  [cargando el módulo configuracion]
Fin de los import
¿Está en sys.modules? True
¿Es el mismo objeto? True
1234.70 EUR
1235 USD
```

**Conceptos clave:**

- El mensaje `[cargando el módulo configuracion]` sale una sola vez aunque se importe tres veces.
- `informes.configuracion is configuracion` es `True`: no son copias.
- Por eso cambiar `CONFIG` desde `main.py` afecta a `informes.formatear()` (útil, pero peligroso si se abusa).

---

## Ejemplo 3.2 · Un objeto compartido por todos los módulos

**Qué se practica:** Un módulo (`auditoria.py`) que crea una instancia única (`registro`) usada por `pagos.py` y `envios.py`.

**Archivos:** `auditoria.py · pagos.py · envios.py · main.py`

**Código:** en la carpeta [`ejemplo_3_2_objeto_compartido`](./ejemplo_3_2_objeto_compartido/).

**Ejecución:**

```powershell
cd ejemplo_3_2_objeto_compartido
python main.py
```

Salida de `python main.py`:

```text
['aceite', 'Cava', 'vino tinto']
Eventos registrados: 3
  1. [pagos] cobro de 245.0 € a Bodegas Sol
  2. [envios] 3 artículos para Bodegas Sol
  3. [pagos] cobro de 99.9 € a Talleres Norte
Solo pagos: 2
¿Mismo objeto en todos los módulos? True
```

**Conceptos clave:**

- `registro = RegistroAuditoria()` se ejecuta una sola vez, en el primer import.
- Todos los módulos anotan en el mismo registro: los eventos salen numerados del 1 al 3.
- `__iter__` es un generador y `filtrar()` una comprehension; es un patrón típico para logs, configuraciones y conexiones.

---

## Ejemplo 4.1 · Validaciones con pruebas propias (`__name__`)

**Qué se practica:** El patrón `if __name__ == "__main__":` ejecutando el mismo archivo directamente y por importación.

**Archivos:** `validaciones.py · main.py`

**Código:** en la carpeta [`ejemplo_4_1_name_main`](./ejemplo_4_1_name_main/).

**Ejecución:**

```powershell
cd ejemplo_4_1_name_main
python validaciones.py
python main.py
```

Salida de `python validaciones.py`:

```text
  [validaciones.py] __name__ = '__main__'
  Pruebas rápidas del módulo:
   True False
   +34612345678 None
```

Salida de `python main.py`:

```text
  [validaciones.py] __name__ = 'validaciones'
[main.py] __name__ = '__main__'
[('Ferretería Ruiz', '+34915551234'), ('Talleres Norte', None)]
```

**Conceptos clave:**

- `__name__` vale `'__main__'` al ejecutar el archivo y `'validaciones'` al importarlo.
- Al importarlo, las pruebas del bloque `if` no se ejecutan.
- `Bodegas Sol` se descarta (CP 99), `Talleres Norte` pasa pero su teléfono (6 cifras) queda como `None`.

---

## Ejemplo 4.2 · Un módulo con una clase y sus propias pruebas

**Qué se practica:** `ConversorDivisas` con pruebas rápidas bajo `if __name__ == "__main__":` y uso desde `main.py` (comprehensions, `zip`, `filter`, `lambda`).

**Archivos:** `conversor.py · main.py`

**Código:** en la carpeta [`ejemplo_4_2_clase_con_pruebas`](./ejemplo_4_2_clase_con_pruebas/).

**Ejecución:**

```powershell
cd ejemplo_4_2_clase_con_pruebas
python conversor.py
python main.py
```

Salida de `python conversor.py`:

```text
Prueba convertir: True
Prueba lote:      True
Prueba tabla:     True
```

Salida de `python main.py`:

```text
100 € equivalen a: {'USD': 108.0, 'GBP': 86.0, 'JPY': 16250.0}
Facturas en USD: [1296.0, 377.89, 81.0]
Mayores de 100 € en GBP: {'F-01': 1032.0, 'F-02': 300.91}
Superan 300 USD: [('F-01', 1296.0), ('F-02', 377.89)]
```

**Conceptos clave:**

- Las pruebas usan tasas fáciles (1,10 y 0,85) para verificar la lógica de cabeza.
- `convertir_lote()` y `tabla()` reutilizan `convertir()` en lugar de repetir la fórmula.
- `zip(numeros, en_usd)` empareja factura e importe y `filter()` con `lambda` se queda con los que superan 300 USD.

---

## Ejemplo 5.1 · Inventario de un almacén repartido en módulos

**Qué se practica:** `modelos.py` (herencia `Producto` / `ProductoPerecedero`) e `inventario.py` (clase `Inventario`) importándose entre sí.

**Archivos:** `modelos.py · inventario.py · main.py`

**Código:** en la carpeta [`ejemplo_5_1_modulos_con_clases`](./ejemplo_5_1_modulos_con_clases/).

**Ejecución:**

```powershell
cd ejemplo_5_1_modulos_con_clases
python main.py
```

Salida de `python main.py`:

```text
Productos en almacén: 4
  Aceite 1L      precio venta:   6.4
  Yogur pack 4   precio venta:  1.54
  Arroz 1kg      precio venta:  1.35
  Queso curado   precio venta:   9.9
Bajo stock (<20): [ProductoPerecedero('SKU-02', 'Yogur pack 4'), Producto('SKU-03', 'Arroz 1kg')]
Valor total: 1108.8
Por valor: ['SKU-01', 'SKU-04', 'SKU-02', 'SKU-03']
TypeError: Solo se admiten objetos Producto
```

**Conceptos clave:**

- `inventario.py` importa `Producto` para validar con `isinstance()`; un `ProductoPerecedero` también pasa porque *es un* `Producto`.
- Cada llamada a `precio_venta()` usa la versión de su clase: polimorfismo entre módulos.
- `CRITERIOS` guarda lambdas: añadir un criterio de orden es añadir una entrada, sin tocar `ordenar_por()`.

---

## Ejemplo 5.2 · Reglas funcionales usadas por una clase

**Qué se practica:** `politicas_precio.py` (funciones puras, clausura `crear_descuento`, `componer` con `reduce`) usado por la clase `Tarificador`.

**Archivos:** `politicas_precio.py · tarificador.py · main.py`

**Código:** en la carpeta [`ejemplo_5_2_clases_y_funciones`](./ejemplo_5_2_clases_y_funciones/).

**Ejecución:**

```powershell
cd ejemplo_5_2_clases_y_funciones
python main.py
```

Salida de `python main.py`:

```text
Normal:       {'Zapatillas': 89.9, 'Mochila': 45.0, 'Gorra': 19.5}
Black Friday: {'Zapatillas': 58.44, 'Mochila': 29.25, 'Gorra': 12.68}
Outlet:       {'Zapatillas': 53.99, 'Mochila': 27.99, 'Gorra': 11.99}
Socios -10%:  {'Zapatillas': 80.91, 'Mochila': 40.5, 'Gorra': 17.55}
Políticas disponibles: ['normal', 'rebajas', 'black_friday', 'outlet']
```

**Conceptos clave:**

- El atributo `politica` guarda una función: cambiar de campaña es asignar otra función.
- `componer(crear_descuento(40), redondeo_comercial)` encadena dos políticas con `reduce()`.
- Lo que cambia a menudo (reglas) va en su módulo, separado de lo que cambia poco (la clase).

---

## Ejemplo 6.1 · Un archivo que tapa a un módulo estándar

**Qué se practica:** Cómo busca Python los módulos (`sys.path`) y el error de llamar `random.py` a un archivo propio.

**Archivos:** `random.py · main.py`

**Código:** en la carpeta [`ejemplo_6_1_donde_busca_python`](./ejemplo_6_1_donde_busca_python/).

**Ejecución:**

```powershell
cd ejemplo_6_1_donde_busca_python
python main.py
```

Salida de `python main.py`:

```text
Primera ruta de búsqueda: ejemplo_6_1_donde_busca_python
Número de rutas > 1: True
random se ha cargado desde: random.py
AttributeError: module 'random' has no attribute 'randint' (consider renaming '…/ejemplo_6_1_donde_busca_python/random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
ModuleNotFoundError: No module named 'tarifas_2027'
```

**Conceptos clave:**

- `sys.path[0]` es la carpeta del script y se mira **antes** que la biblioteca estándar.
- `random.__file__` delata que se cargó nuestro `random.py`, que no tiene `randint()`.
- Solución: renombrar el archivo (p. ej. `prueba_sorteo.py`) y borrar su `__pycache__/`.
- En Python 3.13+ el `AttributeError` añade una sugerencia de renombrar el archivo (por eso el mensaje es más largo que en el enunciado).

---

## Ejemplo 7.1 · Un primer paquete de logística

**Qué se practica:** Paquete `logistica` con `__init__.py` vacío y dos módulos (`vehiculos.py`, `rutas.py`).

**Archivos:** `logistica/{__init__.py, vehiculos.py, rutas.py} · main.py`

**Código:** en la carpeta [`ejemplo_7_1_primer_paquete`](./ejemplo_7_1_primer_paquete/).

**Ejecución:**

```powershell
cd ejemplo_7_1_primer_paquete
python main.py
```

Salida de `python main.py`:

```text
Distancia: 245.5 km
  Furgoneta 1234-KLM -> 85.92 €
  Camion 5678-PQR -> 220.95 €
Aptos para 3500 kg: ['5678-PQR']
<class 'module'>
logistica | logistica.rutas | logistica.vehiculos
```

**Conceptos clave:**

- `logistica.vehiculos` se lee como una ruta: módulo `vehiculos` del paquete `logistica`.
- El `__module__` de las clases muestra su nombre completo (`logistica.vehiculos`).
- `rutas.py` no importa `vehiculos.py`: solo llama a `coste_por_km()` (polimorfismo).

---

## Ejemplo 7.2 · Subpaquetes

**Qué se practica:** Paquete `paquete` con subpaquetes `hola` y `adios`, cada uno con su `__init__.py`.

**Archivos:** `paquete/{__init__.py, hola/, adios/} · main.py`

**Código:** en la carpeta [`ejemplo_7_2_subpaquetes`](./ejemplo_7_2_subpaquetes/).

**Ejecución:**

```powershell
cd ejemplo_7_2_subpaquetes
python main.py
```

Salida de `python main.py`:

```text
Hola, te estoy saludando desde la función saludar() del módulo saludos
Adiós, me estoy despidiendo desde el __init__ de la clase Despedida
```

**Conceptos clave:**

- La ruta del import sigue la ruta de carpetas: `paquete.hola.saludos` = `paquete/hola/saludos.py`.
- Cada nivel lleva su `__init__.py`, aunque esté vacío.
- `main.py` está junto a la carpeta `paquete`, por eso Python la encuentra (Sección 6).

---

## Ejemplo 7.3 · El `__init__.py` como recepción e imports relativos

**Qué se practica:** Paquete `facturacion` con `__init__.py` que expone `Cliente`, `Factura`, `__version__` y `__all__`, e imports relativos (`from .modelos import ...`).

**Archivos:** `facturacion/{__init__.py, modelos.py, calculos.py, factura.py} · main.py`

**Código:** en la carpeta [`ejemplo_7_3_init_e_imports_relativos`](./ejemplo_7_3_init_e_imports_relativos/).

**Ejecución:**

```powershell
cd ejemplo_7_3_init_e_imports_relativos
python main.py
python facturacion/factura.py
```

Salida de `python main.py`:

```text
Versión del paquete: 1.0.0
F-0001 | Hostelería Levante SL | líneas: 3 | total: 2758.8 €
F-0002 | Panadería Ortiz | líneas: 1 | total: 704.0 €
['Cliente', 'LineaFactura', 'Factura']
facturacion.factura
```

Salida de `python facturacion/factura.py`:

```text
Traceback (most recent call last):
  File "…/ejemplo_7_3_init_e_imports_relativos/facturacion/factura.py", line 3, in <module>
    from .modelos import Cliente, LineaFactura
ImportError: attempted relative import with no known parent package
```

**Conceptos clave:**

- Gracias al `__init__.py`, `main.py` hace `from facturacion import Factura` sin saber en qué módulo está.
- Cálculo de `F-0001`: base 2 400 € → descuento 5 % (120 €) → 2 280 € → IVA 21 % (478,80 €) → **2 758,80 €**.
- Ejecutar `factura.py` directamente da `ImportError: attempted relative import with no known parent package`: los módulos internos se importan, no se ejecutan; el punto de entrada es `main.py`.
- `agregar_linea()` devuelve `self` para poder encadenar llamadas.

---

## Ejemplo 8.1 · El cierre semanal de una cafetería (biblioteca estándar)

**Qué se practica:** `collections.Counter`, `statistics`, `math.ceil`, `datetime` y `functools.partial`.

**Archivos:** `main.py`

**Código:** en la carpeta [`ejemplo_8_1_biblioteca_estandar`](./ejemplo_8_1_biblioteca_estandar/).

**Ejecución:**

```powershell
cd ejemplo_8_1_biblioteca_estandar
python main.py
```

Salida de `python main.py`:

```text
Más vendidos: [('café', 3), ('tostada', 2)]
Ticket medio: 1.86 | mediana: 1.8
Sacos de café a pedir: 4
Próximo pedido: 2026-11-17
Con IVA del 10 %: [1.54, 2.31, 3.08]
```

**Conceptos clave:**

- `Counter` + `most_common(2)` cuenta sin escribir el bucle.
- `math.ceil(3.65)` = 4: no se puede pedir medio saco.
- `partial(con_iva, tipo=0.10)` fija un argumento y encaja directamente en `map()`.

---

## Ejemplo 9.1 · Pipeline de ventas de una cadena de tiendas

**Qué se practica:** Paquete ETL `pipeline_ventas` con un módulo por responsabilidad (modelos, extracción, transformación, carga, orquestador).

**Archivos:** `pipeline_ventas/{__init__, modelos, extraccion, transformacion, carga, orquestador}.py · main.py`

**Código:** en la carpeta [`ejemplo_9_1_pipeline_modular`](./ejemplo_9_1_pipeline_modular/).

**Ejecución:**

```powershell
cd ejemplo_9_1_pipeline_modular
python main.py
```

Salida de `python main.py`:

```text
Ventas cargadas: 5
Total por tienda: {'Madrid': 18.0, 'Barcelona': 24.4, 'Valencia': 14.0}
Top 2 productos: [('café molido', 36.0), ('cacao', 14.0)]
```

**Conceptos clave:**

- De 7 filas se cargan 5: las de unidades `dos` y vacía no pasan `es_valido()`.
- Toda la cadena es perezosa: `leer_registros()` es un generador y `transformar()` devuelve un `map`; nunca se guarda una lista intermedia.
- `main.py` solo importa `ejecutar_pipeline` (definido en `__all__`) y `_es_decimal()` lleva guion bajo por ser interno.

---

## Ejemplo 9.2 · Del notebook a producción

**Qué se practica:** Convertir `informe_ventas.ipynb` en el proyecto modular `pedidos_etl` (config, modelos, E-T-L, orquestador, `main.py`) obteniendo la misma salida.

**Archivos:** `informe_ventas.ipynb (notebook de partida) · pedidos_etl/{main.py, probar_validacion.py, etl/…}`

**Código:** en la carpeta [`ejemplo_9_2_del_notebook_a_produccion/pedidos_etl`](./ejemplo_9_2_del_notebook_a_produccion/pedidos_etl/).

**Ejecución:**

```powershell
cd ejemplo_9_2_del_notebook_a_produccion\pedidos_etl
python main.py
python probar_validacion.py
```

Salida de `python main.py`:

```text
Pedidos leídos: 7
Rechazados por datos erróneos: ['P004', 'P007']
Pedidos cancelados: ['P002']
Pedidos procesados: 4
Ventas con IVA por ciudad:
  Sevilla     96.80 €
  Madrid      91.65 €
  Valencia    27.10 €
```

Salida de `python probar_validacion.py`:

```text
True
False
False
```

**Conceptos clave:**

- El IVA y el texto `"cancelado"` salen a `config.py`: si cambian, se cambia una línea.
- `Pedido.total_con_iva` es una `@property` calculada, no una columna que se añade a mano y puede faltar o duplicarse.
- El orden de las etapas lo fija `ejecutar_pipeline()`, no quien pulsa las celdas.
- `probar_validacion.py` prueba `es_valido()` aislado: la línea con coma decimal (`9,95`) se rechaza por tener 6 campos.

---

## Notebook de partida del ejemplo 9.2

El notebook `informe_ventas.ipynb` reproduce las 5 celdas del análisis original y está **ejecutado**, por lo que guarda sus salidas. Su resultado coincide con el de `pedidos_etl/main.py`, que es la comprobación del paso 9 de la conversión.

---

## Conclusiones

- Un **módulo** es un archivo `.py`; un **paquete** es una carpeta con `__init__.py`; una **librería** agrupa paquetes.
- `import modulo` evita conflictos de nombres; `from modulo import nombre` es más corto pero puede sobrescribir nombres sin avisar; `import *` se desaconseja.
- Un módulo se **ejecuta una sola vez** por programa y queda en `sys.modules`: todos los archivos comparten el mismo objeto (útil para configuración, logs y conexiones).
- `if __name__ == "__main__":` separa lo que el módulo **define** de lo que se **ejecuta** al lanzarlo directamente.
- Python busca los módulos en `sys.path` (primero la carpeta del script): nunca hay que llamar a un archivo propio como un módulo estándar (`random.py`, `math.py`…).
- Dentro de un paquete se usan **imports relativos** (`from .modelos import ...`) y el `__init__.py` actúa de «recepción» exponiendo lo importante con `__all__`.
- Un pipeline ETL encaja en un módulo por etapa (extracción, transformación, carga) más un orquestador y un `main.py` como punto de entrada; un notebook sirve para explorar, el proyecto modular para producción.

## Notas

- Todas las salidas coinciden con las del enunciado, salvo el mensaje del `AttributeError` del ejemplo 6.1: en Python 3.13 o posterior incluye una sugerencia de renombrar el archivo (el propio enunciado lo avisa).
