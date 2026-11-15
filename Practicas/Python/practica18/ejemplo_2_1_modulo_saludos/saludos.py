def saludar():
    print("Hola, te estoy saludando desde la función saludar() "
          "del módulo saludos")


class Saludo:
    def __init__(self):
        print("Hola, te estoy saludando desde el __init__ "
              "de la clase Saludo")

    def saludar_persona(self, nombre):
        print(f"Hola {nombre}, desde la clase Saludo")
