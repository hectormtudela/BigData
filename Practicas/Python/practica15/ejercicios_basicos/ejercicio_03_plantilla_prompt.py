# Ejercicio B3 - Plantilla de prompt reutilizable · IA Generativa
#
# El equipo de atención al cliente de una cadena de electrónica usa un LLM para clasificar reseñas. Cada analista escribe el prompt a mano y los resultados son inconsistentes. Crea la clase `PlantillaPrompt` para que todos usen la misma estructura:
#
# - Constructor con `rol`, `tarea` y `formato_salida` (por defecto `"texto libre"`). Crea también la lista `restricciones`, vacía.
# - Método `agregar_restriccion(texto)`: añade una restricción a la lista.
# - Método `construir(entrada)`: devuelve **un único texto** con varias líneas, en este orden:
# 1. `Actúa como <rol>.`
# 2. `Tarea: <tarea>`
# 3. Si hay restricciones, la línea `Restricciones:` y una línea `<restricción>` por cada una.
# 4. `Formato de salida: <formato_salida>`
# 5. `Entrada: """<entrada>"""`
# - `__repr__` con el formato `PlantillaPrompt(rol='analista de experiencia de cliente', restricciones=2)`.
# Pista: construye una lista de líneas y únelas con `"\n".join(lineas)`.

# Solución:

class PlantillaPrompt:
    """Plantilla reutilizable para que todos los analistas construyan el prompt igual."""

    def __init__(self, rol, tarea, formato_salida="texto libre"):
        self.rol = rol
        self.tarea = tarea
        self.formato_salida = formato_salida
        self.restricciones = []

    def agregar_restriccion(self, texto):
        """Añade una restricción a la lista."""
        self.restricciones.append(texto)

    def construir(self, entrada):
        """Devuelve el prompt completo como un único texto de varias líneas."""
        lineas = [
            f"Actúa como {self.rol}.",
            f"Tarea: {self.tarea}",
        ]
        if self.restricciones:
            lineas.append("Restricciones:")
            for restriccion in self.restricciones:
                lineas.append(f"- {restriccion}")
        lineas.append(f"Formato de salida: {self.formato_salida}")
        lineas.append(f'Entrada: """{entrada}"""')
        return "\n".join(lineas)

    def __repr__(self):
        return f"PlantillaPrompt(rol={self.rol!r}, restricciones={len(self.restricciones)})"


# Código de prueba del enunciado
clasificador = PlantillaPrompt(
    "analista de experiencia de cliente",
    "clasifica el sentimiento de la reseña como POSITIVO, NEUTRO o NEGATIVO",
    "JSON con las claves sentimiento y motivo",
)
clasificador.agregar_restriccion("No inventes información que no aparezca en la reseña")
clasificador.agregar_restriccion("El motivo debe tener como máximo 15 palabras")
print(repr(clasificador))
print(clasificador.construir("El portátil llegó en 24 h pero la batería dura la mitad de lo anunciado."))
print("---")
resumen = PlantillaPrompt("redactor técnico", "resume la incidencia en una frase")
print(resumen.construir("El TPV de la tienda 14 no imprime tickets desde las 10:00."))