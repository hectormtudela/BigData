# Ejemplo 1.1 · Conexión a la API de un proveedor logístico
# clase_19_detalles_clases_objetos/teoria/ejemplo_1_1_convenciones_nombres.py

class ConexionProveedor:
    def __init__(self, proveedor, endpoint, token):
        self.proveedor = proveedor              # público
        self.endpoint = endpoint                # público
        self._reintentos = 0                    # uso interno (convención)
        self.__token = token                    # privado (name mangling)

    def __token_valido(self):                   # método privado
        return len(self.__token) >= 12

    def _registrar_reintento(self):             # método de uso interno
        self._reintentos += 1

    def conectar(self):                         # método público
        if not self.__token_valido():
            self._registrar_reintento()
            return f"{self.proveedor}: token no válido (reintentos: {self._reintentos})"
        return f" {self.proveedor}: conectado a {self.endpoint}"

aws = ConexionProveedor("logistica_sur", "https://api.logsur.com/v1", "tk_9f8e7d6c5b4a")
mal = ConexionProveedor("transportes_rio", "https://api.trio.es/v3", "tk_123")

print(aws.conectar())
print(mal.conectar())
print(mal.conectar())

for _ in range(3):
    print("-", end="")
print()
