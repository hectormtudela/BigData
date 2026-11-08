"""
Práctica 15 · Ejercicio B2 - Pool de conexiones a una base de datos
Nivel: básico
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio B2 - Pool de conexiones a una base de datos
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
# **Código de prueba:**
#
# ```python
# etl_ventas = ConexionBD("pg-prod-01")
# etl_stock = ConexionBD("pg-prod-01")
# etl_crm = ConexionBD("pg-prod-01")
# etl_logs = ConexionBD("pg-prod-01")
# print(etl_ventas.abrir(), "|", etl_stock.abrir(), "|", etl_crm.abrir())
# print(etl_logs.abrir())
# print(etl_ventas.abrir())
# print(ConexionBD.estado_pool())
# print(etl_stock.cerrar())
# print(etl_logs.abrir())
# print(etl_stock.cerrar())
# print(ConexionBD.estado_pool())
# ```
#
# **Salida esperada:**
#
# ```plain text
# abierta | abierta | abierta
# rechazada: límite alcanzado
# ya estaba abierta
# 3/3 conexiones en uso
# cerrada
# abierta
# no estaba abierta
# 3/3 conexiones en uso
# ```

# ===== ESCRIBE AQUÍ TU SOLUCIÓN =====



# ===== Código de prueba del enunciado =====
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
