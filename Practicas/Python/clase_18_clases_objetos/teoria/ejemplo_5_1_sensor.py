# Ejemplo 5.1 · Constante compartida y contador de objetos
# clase_18_clases_objetos/teoria/ejemplo_5_1_sensor.py

class Sensor:
    unidad = "°C"
    total_sensores = 0

    def __init__(self, codigo, ubicacion):
        self.codigo = codigo
        self.ubicacion = ubicacion
        Sensor.total_sensores += 1

    def describir(self, valor):
        return f"{self.codigo} ({self.ubicacion}): {valor} {self.unidad}"

s1 = Sensor("TMP-01", "Cámara frigorífica A")
s2 = Sensor("TMP-02", "Cámara frigorífica B")
s3 = Sensor("TMP-03", "Muelle de carga")

print(s1.describir(-18.4))
print(s3.describir(12.1))
print("Sensores registrados:", Sensor.total_sensores)
print(s2.total_sensores)
