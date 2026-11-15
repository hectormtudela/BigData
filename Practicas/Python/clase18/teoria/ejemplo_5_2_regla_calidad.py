# Ejemplo 5.2 · Un objeto puede «tapar» el atributo de clase
# clase_18_clases_objetos/teoria/ejemplo_5_2_regla_calidad.py

class ReglaCalidad:
    umbral_nulos = 0.05

    def __init__(self, columna):
        self.columna = columna

    def evaluar(self, nulos, total):
        ratio = nulos / total
        resultado = "OK" if ratio <= self.umbral_nulos else "FALLO"
        return f"{self.columna}: {ratio:.1%} nulos (umbral {self.umbral_nulos:.0%}) -> {resultado}"

r_email = ReglaCalidad("email")
r_telefono = ReglaCalidad("telefono")
r_telefono.umbral_nulos = 0.20

print(r_email.evaluar(80, 1000))
print(r_telefono.evaluar(150, 1000))
print(vars(r_email))
print(vars(r_telefono))

ReglaCalidad.umbral_nulos = 0.10
print(r_email.evaluar(80, 1000))
print(r_telefono.evaluar(150, 1000))
