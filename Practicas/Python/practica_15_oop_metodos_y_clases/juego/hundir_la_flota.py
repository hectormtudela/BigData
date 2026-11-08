"""
Práctica 15 · Ejercicio J1 - Juego interactivo: Hundir la flota
Nivel: juego interactivo
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio J1  - Juego interactivo: Hundir la flota
#
# Vas a programar una versión de un jugador de **Hundir la flota** que se juega en la terminal. El ordenador esconde una flota en un tablero de 6 × 6 y el jugador dispara escribiendo coordenadas como `B4` hasta hundir todos los barcos o quedarse sin munición.
#
# **Restricción: no está permitido usar herencia ni polimorfismo.** El diseño se basa en clases independientes que colaboran por **composición**.
#
# **Reglas del juego**
#
# - Tablero de 6 × 6. Columnas `AF` y filas `16`.
# - Flota (atributo de clase de `Partida`): `Destructor` (3 casillas), `Fragata` (2) y `Lancha` (2). Se colocan al azar, en horizontal o vertical, sin salirse del tablero y sin solaparse.
# - El jugador tiene **20 disparos**.
# - Resultados de un disparo: `Agua.`, `¡Tocado!` o `¡Hundido! Barco hundido: <nombre>.`
# - Disparar a una casilla ya disparada **no gasta munición**. Una coordenada mal escrita tampoco.
# - Comandos especiales: `mapa` (dibuja el tablero sin mostrar los barcos), `flota` (estado de cada barco) y `salir`.
# - La partida termina al hundir toda la flota (victoria), al agotar la munición o al escribir `salir`. Al terminar se muestra un resumen con las estadísticas y el tablero con los barcos al descubierto.
# - Símbolos del tablero: `·` desconocido, `~` agua, `X` tocado, `#` barco hundido, `B` barco (solo en el resumen final).
# **Diseño obligatorio**
#
# | Clase | Responsabilidad | Detalles mínimos |
# | --- | --- | --- |
# | `Barco` | Un barco de la flota | Nombre, tamaño, lista de posiciones `(fila, columna)` y un `set` **privado** de impactos. `ocupa(pos)`, `recibir_impacto(pos)`, `hundido()`, `len(barco)` y `__str__` (`"Fragata (2) · 1/2 impactos"` o `"Fragata (2) · hundido"`). |
# | `Tablero` | La cuadrícula y los barcos | Tamaño, lista de barcos y diccionario **privado** de disparos. Los símbolos son **atributos de clase**. Coloca barcos al azar, procesa un disparo, sabe si toda la flota está hundida y se dibuja como texto. |
# | `Jugador` | Estadísticas del jugador | Nombre, munición, disparos y aciertos. `precision()`, `bool(jugador)` (`True` si le queda munición) y `__str__`. |
# | `Partida` | Coordina el juego | **Tiene** un `Tablero` y un `Jugador`. Convierte el texto `B4` en `(fila, columna)` con un método de uso interno, procesa un turno, sabe si la partida ha terminado y contiene el bucle con `input()`. |
#
# **Requisitos técnicos**
#
# 9. El constructor de `Partida` recibe un parámetro opcional `semilla`. Crea con él un **objeto** generador de números aleatorios: `random.Random(semilla)`. Con la misma semilla los barcos quedan siempre en el mismo sitio, lo que permite probar el juego.
# 10. Separa la lógica de la interacción: el método `turno(texto)` recibe una coordenada y **devuelve** el mensaje (no hace `print` ni `input`). Solo `jugar()` usa `input()` y `print()`.
# 11. Al final del archivo, protege el arranque con `if __name__ == "__main__":`, pidiendo el nombre del jugador y creando la partida con `semilla=7`.
# 12. Añade un bloque de **pruebas sin teclado** (por ejemplo, en una función `probar()`) que cree una partida con `semilla=7` y `municion=3`, llame tres veces a `turno()` y compruebe que la partida termina.
# **Ejemplo de partida** (con `semilla=7`; tu tablero puede ser diferente si colocas los barcos con otro algoritmo, pero el formato debe ser este):
#
# ```plain text
# Nombre del jugador: Ana
# HUNDIR LA FLOTA · tablero 6x6 · 3 barcos · 20 disparos
# Comandos: coordenada (B4), 'mapa', 'flota', 'salir'
# [20] Disparo: A1
# Agua.
# [19] Disparo: D2
# ¡Tocado!
# [18] Disparo: D3
# ¡Tocado!
# [17] Disparo: d4
# ¡Hundido! Barco hundido: Destructor.
# [16] Disparo: D4
# Ya habías disparado ahí. No gastas munición.
# [16] Disparo: Z9
# Coordenada no válida: 'Z9'. Usa letra + número, por ejemplo B4.
# [16] Disparo: mapa
#     A B C D E F
#  1  ~ · · · · ·
#  2  · · · # · ·
#  3  · · · # · ·
#  4  · · · # · ·
#  5  · · · · · ·
#  6  · · · · · ·
# [16] Disparo: E3
# ¡Tocado!
# [15] Disparo: F3
# ¡Hundido! Barco hundido: Lancha.
# [14] Disparo: flota
#   - Destructor hundido
#   - Fragata a flote
#   - Lancha hundido
# [14] Disparo: E1
# ¡Tocado!
# [13] Disparo: F1
# ¡Hundido! Barco hundido: Fragata.
#
# === FIN DE LA PARTIDA ===
# ¡Victoria, Ana! Flota enemiga hundida.
# Ana · disparos: 8 · aciertos: 7 · precisión: 87.5 % · munición: 12
#   - Destructor (3) · hundido
#   - Fragata (2) · hundido
#   - Lancha (2) · hundido
#     A B C D E F
#  1  ~ · · · # #
#  2  · · · # · ·
#  3  · · · # # #
#  4  · · · # · ·
#  5  · · · · · ·
#  6  · · · · · ·
# ```
#
# **Ampliaciones interesantes**:
#
# - Impedir que dos barcos queden en casillas contiguas.
# - Elegir el tamaño del tablero y la dificultad (munición) al empezar.
# - Guardar un ranking de partidas en una lista de objetos `Jugador` ordenada por precisión (sobrecarga `<`).
# - Modo «radar»: una vez por partida, el comando `radar B4` indica cuántas casillas con barco hay en el cuadrado 3 × 3 alrededor de la coordenada.
#
# > 💡 Puedes hacer tu propio juego si quieres. No tiene que ser obligatoriamente el ejercicio J1

import random


# ===== ESCRIBE AQUÍ TU SOLUCIÓN (Barco, Tablero, Jugador, Partida) =====



if __name__ == "__main__":
    pass
