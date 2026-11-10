# Ejercicio I1 - Historial de conversación de un asistente · IA Generativa
#
# Una aseguradora está construyendo un asistente para tramitar partes de siniestros. Las API de los LLM reciben el historial como una lista de diccionarios `{"role": ..., "content": ...}` y tienen una **ventana de contexto** limitada. Modela el historial con **dos clases relacionadas por composición**.
#
# **Clase ****`Mensaje`**
#
# - Atributo de clase `ROLES_VALIDOS = ("system", "user", "assistant")`.
# - Constructor con `rol` y `contenido`.
# - Método `tokens()`: estimación sencilla, **1 token por palabra** (`len(contenido.split())`).
# - Método `a_dict()`: devuelve `{"role": rol, "content": contenido}`.
# - `__str__`: `"[user] Quiero dar un parte de mi coche"`.
# **Clase ****`Conversacion`**
#
# - Constructor con `max_tokens`. Guarda los mensajes en una lista **privada** `__mensajes`.
# - Método `agregar(rol, contenido)`: si el rol no está en `Mensaje.ROLES_VALIDOS`, no añade nada y devuelve `False`. Si es válido, crea el `Mensaje`, lo añade, llama a `_recortar()` y devuelve `True`.
# - `+=` recibe una **tupla** `(rol, contenido)` y usa `agregar`.
# - Método `tokens_totales()`.
# - Método de uso interno `_recortar()`: mientras los tokens totales superen `max_tokens`, elimina el **mensaje más antiguo que no sea ****`system`** (el mensaje de sistema nunca se borra).
# - `len(conv)`: número de mensajes. `palabra in conv`: `True` si la palabra aparece en algún mensaje, sin distinguir mayúsculas.
# - Método `para_api()`: lista de diccionarios de todos los mensajes.
# - `__str__`: un mensaje por línea.

# Solución:

class Mensaje:
    """Un mensaje del historial: quién lo dice (rol) y qué dice (contenido)."""

    ROLES_VALIDOS = ("system", "user", "assistant")

    def __init__(self, rol, contenido):
        self.rol = rol
        self.contenido = contenido

    def tokens(self):
        """Estimación sencilla: 1 token por palabra."""
        return len(self.contenido.split())

    def a_dict(self):
        """Formato que esperan las API de los LLM."""
        return {"role": self.rol, "content": self.contenido}

    def __str__(self):
        return f"[{self.rol}] {self.contenido}"


class Conversacion:
    """Historial de mensajes con una ventana de contexto limitada (composición)."""

    def __init__(self, max_tokens):
        self.max_tokens = max_tokens
        self.__mensajes = []

    def agregar(self, rol, contenido):
        """Añade un mensaje si el rol es válido; devuelve True/False."""
        if rol not in Mensaje.ROLES_VALIDOS:
            return False
        self.__mensajes.append(Mensaje(rol, contenido))
        self._recortar()
        return True

    def __iadd__(self, mensaje):
        """conv += (rol, contenido). Debe devolver self, si no conv pasaría a ser None."""
        rol, contenido = mensaje
        self.agregar(rol, contenido)
        return self

    def tokens_totales(self):
        return sum(m.tokens() for m in self.__mensajes)

    def _recortar(self):
        """Uso interno: borra el mensaje más antiguo que no sea 'system' hasta caber."""
        while self.tokens_totales() > self.max_tokens:
            indices = [i for i, m in enumerate(self.__mensajes) if m.rol != "system"]
            if not indices:
                break
            del self.__mensajes[indices[0]]

    def __len__(self):
        return len(self.__mensajes)

    def __contains__(self, palabra):
        """palabra in conv: True si aparece en algún mensaje, sin distinguir mayúsculas."""
        return any(palabra.lower() in m.contenido.lower() for m in self.__mensajes)

    def para_api(self):
        return [m.a_dict() for m in self.__mensajes]

    def __str__(self):
        return "\n".join(str(m) for m in self.__mensajes)


# Código de prueba del enunciado
conv = Conversacion(max_tokens=30)
conv += ("system", "Eres el asistente de siniestros de Seguros Brisamar")
conv += ("user", "Quiero dar un parte de mi coche")
conv += ("assistant", "Claro, ¿cuál es la matrícula del vehículo?")
print(conv.agregar("cliente", "Hola"))
print(len(conv), conv.tokens_totales())
conv += ("user", "Es la 4821 KLM y el golpe fue en un parking")
print(len(conv), conv.tokens_totales())
print(conv)
print("matrícula" in conv, "COCHE" in conv)
print(conv.para_api()[0])