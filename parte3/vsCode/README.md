# Mini proyecto 3.1 — Torneo de Twenty-One

## Entorno

- Visual Studio Code
- Metals (extensión Scala)
- Scala 2.12.21
- JDK 17
- sbt

## Descripción

Programa en Scala que analiza los resultados de dos rondas de un torneo de **Twenty-One**. Cada jugador tiene un nombre y una puntuación, y el programa determina:

- Si cada jugador se ha pasado de 21 (*bust*) o tiene una mano válida.
- Cuántos jugadores tienen una mano válida y cuántos se han pasado.
- La mejor puntuación válida de cada ronda.
- Qué ronda tuvo la mejor puntuación, o si ambas empataron.

## Colecciones utilizadas

| Colección | Contenido | Tipo |
| --- | --- | --- |
| `jugadores` | Nombres de los 5 jugadores | `List[String]` (inmutable) |
| `puntuaciones` | Puntuaciones de la ronda 1 | `Array[Int]` |
| `puntuacionesRonda2` | Puntuaciones de la ronda 2 | `Array[Int]` |

Cada posición de `jugadores` se corresponde con la misma posición de las puntuaciones. La lista de jugadores no se modifica en ningún momento y se reutiliza en las dos rondas.

## Funciones utilizadas

| Función | Qué hace |
| --- | --- |
| `bust(puntuacion: Int): Boolean` | Devuelve `true` si la puntuación es mayor que 21 |
| `estadoMano(puntuacion: Int): String` | Devuelve `"BUST"` si la mano se ha pasado y `"VALIDA"` en caso contrario |
| `mejorMano(handA: Int, handB: Int): Int` | Compara dos manos con `if / else if / else`: devuelve `0` si ambas se pasan, la otra mano si solo una se pasa, o la mayor si ninguna se pasa |
| `contarValidas(puntos: Array[Int]): Int` | Recorre el array con `while` y cuenta las manos que no se han pasado |
| `mejorPuntuacion(puntos: Array[Int]): Int` | Recorre el array con `while` y usa `mejorMano` para quedarse con la mejor puntuación válida |
| `mostrarRonda(...)` | Muestra cada jugador con su puntuación y estado usando `while` |
| `mostrarRondaForeach(...)` | Muestra el estado de cada puntuación usando `foreach` |
| `mostrarResumen(...)` | Muestra el número de jugadores, manos válidas, bust y la mejor puntuación |

## Ejecución

Desde la terminal integrada de Visual Studio Code, dentro de la carpeta del proyecto:

```bash
sbt compile
sbt run
```

## Resultados

### Ronda 1

```
Alex -> 18 -> VALIDA
Chen -> 24 -> BUST
Marta -> 21 -> VALIDA
Sindhu -> 20 -> VALIDA
Luis -> 26 -> BUST

Jugadores: 5
Manos válidas: 3
Bust: 2
Mejor puntuación válida: 21
```

### Ronda 2

```
Alex -> 22 -> BUST
Chen -> 19 -> VALIDA
Marta -> 20 -> VALIDA
Sindhu -> 21 -> VALIDA
Luis -> 17 -> VALIDA

Jugadores: 5
Manos válidas: 4
Bust: 1
Mejor puntuación válida: 21
```

### Comparación de rondas

```
Mejor puntuación ronda 1: 21
Mejor puntuación ronda 2: 21
Ambas rondas tuvieron la misma mejor puntuación.
```

En la ronda 1 se pasaron 2 jugadores (Chen y Luis) y en la ronda 2 solo 1 (Alex). Aun así, la mejor puntuación válida fue 21 en ambas

## Comparación: `while` frente a `foreach`

Ambas versiones muestran el estado de cada mano, pero de forma distinta

**Versión A (`while`):**

```scala
var i = 0
while (i < puntos.length) {
  println(s"${nombres(i)} -> ${puntos(i)} : ${estadoMano(puntos(i))}")
  i += 1
}
```

**Versión B (`foreach`):**

```scala
puntos.foreach(p => println(s"Puntuación $p : ${estadoMano(p)}"))
```

| Aspecto | `while` | `foreach` |
| --- | --- | --- |
| ¿Necesita un contador? | **Sí**: `i` indica la posición actual y hay que incrementarlo con `i += 1` | **No**: `foreach` recorre los elementos internamente. |
| ¿Necesita una `var` para recorrer? | **Sí**: `var i = 0`, que cambia en cada iteración | **No**: no hay estado mutable; cada elemento llega como parámetro `p` de la función |
| ¿Qué riesgos tiene? | Olvidar `i += 1` (bucle infinito) o equivocarse en el límite | Ninguno de esos errores puede ocurrir. |
| ¿Es más cercano al estilo funcional? | No. Es un estilo imperativo. | **Sí**. |

## Mutabilidad e inmutabilidad

- **Inmutable:** `jugadores` , todos los `val` y las funciones `bust`, `estadoMano` y `mejorMano`, que solo dependen de sus parámetros.
- **Mutable:** las `var` dentro de los bucles `while`. Solo existen dentro de cada función y no afectan a datos externos.
- Los `Array` son mutables por naturaleza, pero en este proyecto solo se leen, nunca se modifican.

## Problemas encontrados y soluciones

| Problema | Solución |
| --- | --- |
| *(ej.) sbt no encontraba Scala 2.12.21* | *(ej.) Comprobar la conexión a internet y volver a ejecutar `sbt compile`.* |
| *(ej.) Las tildes salían mal en la consola* | *(ej.) Es un tema de codificación de la terminal; se quitaron las tildes de los `println`.* |

## Capturas

![VSCode abierto con Scala, JDK y SBT funcionando][images/Captura1.PNG]

![SBT Compile en uso][images/sbtCompile.PNG]

![SBT Run en uso y ejecución del programa][images/sbtRun.PNG]
