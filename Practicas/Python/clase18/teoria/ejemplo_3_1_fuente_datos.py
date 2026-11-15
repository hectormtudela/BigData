# Ejemplo 3.1 · Fuentes de datos de una plataforma
# clase_18_clases_objetos/teoria/ejemplo_3_1_fuente_datos.py

class FuenteDatos:
    def __init__(self, nombre, tipo, ubicacion):
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion

crm = FuenteDatos("crm_clientes", "api", "https://api.crm.empresa.com/v2")
erp = FuenteDatos("erp_facturas", "fichero", "/landing/erp/facturas/")

print(crm.nombre, "|", crm.tipo, "|", crm.ubicacion)
print(erp.nombre, "|", erp.tipo, "|", erp.ubicacion)
print(vars(erp))
