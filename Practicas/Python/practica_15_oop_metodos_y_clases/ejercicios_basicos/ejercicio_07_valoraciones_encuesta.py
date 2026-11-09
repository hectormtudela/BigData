# Ejercicio B7 - Valoraciones de clientes desde una encuesta
#
# La herramienta de encuestas exporta las valoraciones como texto: `"4,5/5"`, `"3/5"`, `"0/5"` (el `0` significa *sin valorar*). Crea la clase `Valoracion`:
#
# - El constructor recibe el texto, toma la parte anterior a la `/`, cambia la coma por punto y guarda el valor como `float` en el atributo **privado** `__nota`.
# - `float(v)`: devuelve la nota.
# - `int(v)`: devuelve la nota **redondeada** a entero.
# - `bool(v)`: `False` si la nota es 0 (sin valorar).
# - `str(v)`: tantas `★` como `int(v)` y tantas `☆` como falten hasta 5, seguido de la nota entre paréntesis: `"★★★★☆ (4.5)"`.

# Solución:

class Valoracion:
    """Valoración de un cliente exportada como texto, p. ej. "4,5/5"."""

    def __init__(self, texto):
        parte_nota = texto.split("/")[0]
        self.__nota = float(parte_nota.replace(",", "."))

    def __float__(self):
        """float(v): devuelve la nota."""
        return self.__nota

    def __int__(self):
        """int(v): devuelve la nota redondeada a entero."""
        return round(self.__nota)

    def __bool__(self):
        """bool(v): False si la nota es 0 (sin valorar)."""
        return self.__nota != 0

    def __str__(self):
        """str(v): estrellas llenas y vacías hasta 5, y la nota entre paréntesis."""
        llenas = int(self)
        return "★" * llenas + "☆" * (5 - llenas) + f" ({self.__nota})"


# Código de prueba del enunciado
respuestas = ["4,5/5", "3/5", "0/5", "2,4/5", "5/5", "0/5"]
valoraciones = [Valoracion(r) for r in respuestas]
for v in valoraciones:
    print(str(v), float(v), int(v), bool(v))
validas = [v for v in valoraciones if v]
print("Respuestas válidas:", len(validas), "de", len(valoraciones))
print("Media:", round(sum([float(v) for v in validas]) / len(validas), 2))