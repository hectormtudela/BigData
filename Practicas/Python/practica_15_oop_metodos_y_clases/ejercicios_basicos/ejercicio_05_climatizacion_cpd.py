# Ejercicio B5 - Climatización de un centro de datos
#
# La consigna de temperatura de cada sala del CPD solo puede estar entre **18 y 27 °C**. Nadie debe poder cambiarla «a mano» desde fuera del objeto. Crea la clase `Climatizador` aplicando las convenciones de nombres:
#
# - Atributos de clase `TEMP_MIN = 18` y `TEMP_MAX = 27`.
# - Constructor con `sala` (público) y `consigna` inicial. La consigna se guarda en el atributo **privado** `__consigna`, ya limitada al rango permitido. Crea también el atributo de **uso interno** `_historial`, una lista con la consigna inicial.
# - Método **de uso interno** `_limitar(valor)`: devuelve el valor ajustado al rango (si es menor que el mínimo, el mínimo; si es mayor que el máximo, el máximo).
# - Método `ajustar(grados)`: suma (o resta, si es negativo) los grados a la consigna, la limita con `_limitar`, la añade al historial y devuelve la nueva consigna.
# - Método `consigna()`: devuelve el valor actual.
# - `__str__`: `"Sala A · 22 °C · 3 cambios"` (los cambios son las entradas del historial menos la inicial).
# Responde en un comentario al final del archivo: ¿por qué `hasattr(sala_a, "__consigna")` devuelve `False` si el atributo existe?

# Solución:

class Climatizador:
    """Control de la consigna de temperatura de una sala del CPD."""

    TEMP_MIN = 18
    TEMP_MAX = 27

    def __init__(self, sala, consigna):
        self.sala = sala
        self.__consigna = self._limitar(consigna)
        self._historial = [self.__consigna]

    def _limitar(self, valor):
        """Uso interno: ajusta el valor al rango permitido."""
        if valor < Climatizador.TEMP_MIN:
            return Climatizador.TEMP_MIN
        if valor > Climatizador.TEMP_MAX:
            return Climatizador.TEMP_MAX
        return valor

    def ajustar(self, grados):
        """Suma (o resta) grados a la consigna, respetando el rango, y la devuelve."""
        self.__consigna = self._limitar(self.__consigna + grados)
        self._historial.append(self.__consigna)
        return self.__consigna

    def consigna(self):
        """Devuelve la consigna actual."""
        return self.__consigna

    def __str__(self):
        cambios = len(self._historial) - 1
        return f"Sala {self.sala} · {self.__consigna} °C · {cambios} cambios"


# Código de prueba del enunciado
sala_a = Climatizador("A", 22)
sala_b = Climatizador("B", 31)
print(sala_a.ajustar(-3), sala_a.ajustar(-4), sala_a.ajustar(6))
print(sala_a)
print(sala_b)
print(sala_a._historial)
print(vars(sala_b))
print(hasattr(sala_a, "__consigna"), hasattr(sala_a, "_Climatizador__consigna"))


# RESPUESTA:
# ¿Por qué hasattr(sala_a, "__consigna") devuelve False si el atributo existe?
# Porque Python aplica "name mangling" a los atributos que empiezan por dos guiones
# bajos: dentro de la clase, __consigna se renombra a _Climatizador__consigna
# (_NombreClase__atributo). El atributo existe, pero con ese nombre; desde fuera
# no hay ninguno llamado literalmente "__consigna", y por eso hasattr da False.
# Con el nombre real, hasattr(sala_a, "_Climatizador__consigna") da True. Esto no es
# una protección absoluta, solo evita accesos accidentales y choques de nombres.