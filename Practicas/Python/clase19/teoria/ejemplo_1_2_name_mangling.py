# Ejemplo 1.2 · Name mangling: qué ocurre con `__token`
# clase_19_detalles_clases_objetos/teoria/ejemplo_1_2_name_mangling.py

class ConexionProveedor:
    def __init__(self, proveedor, token):
        self.proveedor = proveedor
        self._reintentos = 0
        self.__token = token

    def token_enmascarado(self):
        return self.__token[:3] + "*" * (len(self.__token) - 3)

c = ConexionProveedor("logistica_sur", "tk_9f8e7d6c5b4a")

print(vars(c))
print(c._reintentos)
print(c.token_enmascarado())
print(c._ConexionProveedor__token)
print(c.__token)
