# Ejercicio B2 - Pool de conexiones a una base de datos
#
# El servidor PostgreSQL de producción solo admite **3 conexiones simultáneas** desde los procesos ETL. Crea la clase `ConexionBD`:
#
# - Atributo de clase `MAX_CONEXIONES = 3` y atributo de clase `abiertas = 0`.
# - Constructor con `servidor`. Cada conexión empieza con el atributo `activa = False`.
# - Método `abrir()`:
# - Si la conexión ya estaba activa, devuelve `"ya estaba abierta"`.
# - Si se ha alcanzado el máximo de conexiones, devuelve `"rechazada: límite alcanzado"`.
# - En otro caso la activa, suma 1 a `abiertas` **de la clase** y devuelve `"abierta"`.
# - Método `cerrar()`: si estaba activa, la desactiva, resta 1 a `abiertas` y devuelve `"cerrada"`; si no, devuelve `"no estaba abierta"`.
# - Método de clase `estado_pool()` (con `@classmethod`) que devuelve `"2/3 conexiones en uso"`.

# Solución:

class ConexionBD:
    """Conexión a PostgreSQL con un límite de conexiones simultáneas compartido."""

    MAX_CONEXIONES = 3
    abiertas = 0

    def __init__(self, servidor):
        self.servidor = servidor
        self.activa = False

    def abrir(self):
        """Activa la conexión si no estaba abierta y queda hueco en el pool."""
        if self.activa:
            return "ya estaba abierta"
        if ConexionBD.abiertas >= ConexionBD.MAX_CONEXIONES:
            return "rechazada: límite alcanzado"
        self.activa = True
        ConexionBD.abiertas += 1
        return "abierta"

    def cerrar(self):
        """Desactiva la conexión si estaba activa y libera un hueco del pool."""
        if self.activa:
            self.activa = False
            ConexionBD.abiertas -= 1
            return "cerrada"
        return "no estaba abierta"

    @classmethod
    def estado_pool(cls):
        """Resumen del pool: conexiones en uso sobre el máximo."""
        return f"{cls.abiertas}/{cls.MAX_CONEXIONES} conexiones en uso"


# Código de prueba del enunciado
etl_ventas = ConexionBD("pg-prod-01")
etl_stock = ConexionBD("pg-prod-01")
etl_crm = ConexionBD("pg-prod-01")
etl_logs = ConexionBD("pg-prod-01")
print(etl_ventas.abrir(), "|", etl_stock.abrir(), "|", etl_crm.abrir())
print(etl_logs.abrir())
print(etl_ventas.abrir())
print(ConexionBD.estado_pool())
print(etl_stock.cerrar())
print(etl_logs.abrir())
print(etl_stock.cerrar())
print(ConexionBD.estado_pool())