# Ejemplo 3.1 · Sumar y comparar resúmenes de carga
# clase_19_detalles_clases_objetos/teoria/ejemplo_3_1_resumen_carga.py

class ResumenCarga:
    def __init__(self, filas=0, rechazadas=0, megas=0.0):
        self.filas = filas
        self.rechazadas = rechazadas
        self.megas = megas

    def __add__(self, otro):
        return ResumenCarga(self.filas + otro.filas,
                            self.rechazadas + otro.rechazadas,
                            round(self.megas + otro.megas, 2))

    def __sub__(self, otro):
        return ResumenCarga(self.filas - otro.filas,
                            self.rechazadas - otro.rechazadas,
                            round(self.megas - otro.megas, 2))

    def __mul__(self, factor):
        return ResumenCarga(self.filas * factor,
                            self.rechazadas * factor,
                            round(self.megas * factor, 2))

    def __str__(self):
        return f"filas={self.filas:,} rechazadas={self.rechazadas} megas={self.megas}"

lunes = ResumenCarga(120_000, 35, 48.6)
martes = ResumenCarga(98_500, 12, 40.15)

semana = lunes + martes
diferencia = lunes - martes
proyeccion_mes = martes * 30

print("Total     :", semana)
print("Diferencia:", diferencia)
print("Proyección:", proyeccion_mes)
print("Equivale a:", lunes.__add__(martes))
