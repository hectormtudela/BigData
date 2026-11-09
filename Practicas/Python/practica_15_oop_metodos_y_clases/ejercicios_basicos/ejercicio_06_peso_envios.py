# Ejercicio B6 - Peso de los envíos de un almacén
#
# El almacén de una empresa de e-commerce agrupa paquetes en palés y necesita sumar, comparar y ordenar pesos. Crea la clase `PesoEnvio`:
#
# - Constructor con `gramos` (entero). Si llega un valor negativo, se guarda `0`.
# - Sobrecarga `+` para que la suma de dos pesos devuelva un **objeto nuevo** `PesoEnvio`.
# - Sobrecarga `==` y `<` comparando los gramos.
# - `__str__`: si el peso es de 1000 g o más, se muestra en kilos con 2 decimales (`"1.25 kg"`); si no, en gramos (`"850 g"`).
# - `__repr__`: `PesoEnvio(850)`.

# Solución:

class PesoEnvio:
    """Peso de un envío en gramos, con operadores para sumar, comparar y ordenar."""

    def __init__(self, gramos):
        self.gramos = gramos if gramos >= 0 else 0

    def __add__(self, otro):
        """pesoA + pesoB devuelve un objeto NUEVO, sin modificar los originales."""
        return PesoEnvio(self.gramos + otro.gramos)

    def __eq__(self, otro):
        """pesoA == pesoB compara los gramos (no si son el mismo objeto)."""
        return self.gramos == otro.gramos

    def __lt__(self, otro):
        """pesoA < pesoB; con esto también funcionan sorted() y max()."""
        return self.gramos < otro.gramos

    def __str__(self):
        if self.gramos >= 1000:
            return f"{self.gramos / 1000:.2f} kg"
        return f"{self.gramos} g"

    def __repr__(self):
        return f"PesoEnvio({self.gramos})"


# Código de prueba del enunciado
paquetes = [PesoEnvio(850), PesoEnvio(1250), PesoEnvio(400), PesoEnvio(-30), PesoEnvio(2300)]
print(paquetes[0] + paquetes[2])
print(paquetes[0] + paquetes[1])
pale = PesoEnvio(0)
for p in paquetes:
    pale = pale + p
print("Palé:", pale)
print(sorted(paquetes))
print("Más pesado:", max(paquetes))
print(PesoEnvio(1250) == paquetes[1], PesoEnvio(1250) is paquetes[1])