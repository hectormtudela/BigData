# Ejercicio B4 - Coste de las llamadas a un LLM · IA Generativa
#
# Finanzas quiere saber cuánto cuesta cada llamada al proveedor de modelos de lenguaje. El proveedor cobra en dólares **por cada millón de tokens**, con un precio distinto para los tokens de entrada y los de salida. Crea la clase `LlamadaLLM`:
#
# - Atributo de clase `PRECIOS`, un diccionario `{modelo: (precio_entrada, precio_salida)}`:
# | Modelo | Entrada (/M tokens) | Salida (/M tokens) |  |
# | --- | --- | --- |
# | `modelo-lite` | 0.20 | 0.80 |
# | `modelo-pro` | 3.00 | 12.00 |
#
# - Atributo de clase `total_llamadas = 0`, que se incrementa cada vez que se crea una llamada.
# - Constructor con `modelo`, `tokens_entrada` y `tokens_salida`.
# - Método `coste()`: devuelve el coste en dólares redondeado a **6 decimales**.
# - Método `tokens_totales()`.
# - `__repr__` con el formato `LlamadaLLM(modelo-lite, 1500 tokens, $0.00048)`.

# Solución:

class LlamadaLLM:
    """Una llamada al proveedor de modelos de lenguaje y su coste en dólares."""

    PRECIOS = {
        "modelo-lite": (0.20, 0.80),
        "modelo-pro": (3.00, 12.00),
    }
    total_llamadas = 0

    def __init__(self, modelo, tokens_entrada, tokens_salida):
        self.modelo = modelo
        self.tokens_entrada = tokens_entrada
        self.tokens_salida = tokens_salida
        LlamadaLLM.total_llamadas += 1

    def coste(self):
        """Coste en dólares, redondeado a 6 decimales."""
        precio_entrada, precio_salida = LlamadaLLM.PRECIOS[self.modelo]
        coste = (
            self.tokens_entrada * precio_entrada + self.tokens_salida * precio_salida
        ) / 1_000_000
        return round(coste, 6)

    def tokens_totales(self):
        """Tokens de entrada + tokens de salida."""
        return self.tokens_entrada + self.tokens_salida

    def __repr__(self):
        return f"LlamadaLLM({self.modelo}, {self.tokens_totales()} tokens, ${self.coste()})"


# Código de prueba del enunciado
llamadas = [
    LlamadaLLM("modelo-lite", 1200, 300),
    LlamadaLLM("modelo-pro", 1200, 300),
    LlamadaLLM("modelo-lite", 8000, 1500),
    LlamadaLLM("modelo-pro", 25000, 4000),
]
for llamada in llamadas:
    print(llamada)
print("Llamadas registradas:", LlamadaLLM.total_llamadas)
print(f"Coste total: ${round(sum([l.coste() for l in llamadas]), 6)}")
coste_pro = sum([l.coste() for l in llamadas if l.modelo == "modelo-pro"])
print("Peso de modelo-pro:", round(100 * coste_pro / sum([l.coste() for l in llamadas]), 1), "%")