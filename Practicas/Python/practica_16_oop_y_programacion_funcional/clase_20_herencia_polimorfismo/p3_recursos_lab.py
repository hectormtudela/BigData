r"""
Práctica 16 · Clase 20 · Ejercicio P3 (Recursos del laboratorio)

ENUNCIADO DEL PROFESOR (copiado íntegro)
========================================

# Ejercicio P3. Gestión de recursos de un laboratorio de Big Data

### Enunciado

> Un centro de formación tecnológica necesita desarrollar una aplicación para gestionar los recursos informáticos utilizados en sus laboratorios de Big Data e Inteligencia Artificial.
El laboratorio dispone de ordenadores, servidores y dispositivos de procesamiento Edge AI.

Debes implementar un sistema basado en herencia para organizar estos recursos, consultar su información y calcular su consumo eléctrico.

### Requisitos

Desarrollar una clase `RecursoComputacional` con los siguientes atributos:

- `id_recurso`: identificador único.
- `nombre`: nombre del equipo.
- `fabricante`: fabricante del dispositivo.
- `potencia_w`: potencia eléctrica en vatios.
- `horas_uso`: horas acumuladas de funcionamiento.
La superclase debe incluir estos métodos:

- `mostrar_informacion()`: muestra los atributos comunes.
- `calcular_consumo()`: devuelve el consumo eléctrico acumulado en kWh, calculado como `(potencia_w * horas_uso) / 1000`.
| Subclase | Atributos específicos |
| --- | --- |
| `Ordenador` | `procesador`, `ram_gb`, `sistema_operativo` |
| `Servidor` | `num_cpu`, `ram_gb`, `almacenamiento_tb` |
| `DispositivoEdge` | `modelo_gpu`, `memoria_gpu_gb`, `tipo_inferencia` |

Cada subclase debe sobrescribir el método `mostrar_informacion()` para mostrar sus atributos específicos.

13. Crear al menos dos objetos de cada subclase.
14. Guardar todos los objetos en una lista `recursos`.
15. Recorrer la lista para mostrar la información de cada recurso.
16. Calcular el consumo eléctrico individual de cada dispositivo.
17. Calcular el consumo total acumulado de todos los recursos.
18. Utilizar `isinstance()` para contar cuántos objetos hay de cada subclase.
19. Identificar qué dispositivo tiene el mayor consumo eléctrico.
### Salida esperada (orientativa)

```plain text
========== LABORATORIO BIG DATA ==========

Recurso: PC-01
Tipo: Ordenador
Fabricante: Dell
Procesador: Intel Core i7
RAM: 32 GB
Sistema operativo: Windows 11
Consumo acumulado: 12.5 kWh

Recurso: SRV-01
Tipo: Servidor
Fabricante: HPE
Número de CPU: 2
RAM: 128 GB
Almacenamiento: 4 TB
Consumo acumulado: 42.0 kWh

========== RESUMEN DEL LABORATORIO ==========

Ordenadores: 2
Servidores: 2
Dispositivos Edge: 2

Consumo total: 78.5 kWh
Dispositivo de mayor consumo: SRV-01
```

> Los valores anteriores son orientativos y deben corresponder a los datos de los objetos que crees.
"""

class RecursoComputacional:
    """Superclase: datos comunes y cálculo del consumo eléctrico."""

    def __init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso):
        self.id_recurso = id_recurso
        self.nombre = nombre
        self.fabricante = fabricante
        self.potencia_w = potencia_w
        self.horas_uso = horas_uso

    def mostrar_informacion(self):
        print(f"Recurso: {self.id_recurso}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {type(self).__name__}")
        print(f"Fabricante: {self.fabricante}")

    def calcular_consumo(self):
        """Consumo acumulado en kWh = (potencia en W * horas) / 1000."""
        return (self.potencia_w * self.horas_uso) / 1000


class Ordenador(RecursoComputacional):
    def __init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso,
                 procesador, ram_gb, sistema_operativo):
        super().__init__(id_recurso, nombre, fabricante, potencia_w, horas_uso)
        self.procesador = procesador
        self.ram_gb = ram_gb
        self.sistema_operativo = sistema_operativo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram_gb} GB")
        print(f"Sistema operativo: {self.sistema_operativo}")


class Servidor(RecursoComputacional):
    def __init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso,
                 num_cpu, ram_gb, almacenamiento_tb):
        super().__init__(id_recurso, nombre, fabricante, potencia_w, horas_uso)
        self.num_cpu = num_cpu
        self.ram_gb = ram_gb
        self.almacenamiento_tb = almacenamiento_tb

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de CPU: {self.num_cpu}")
        print(f"RAM: {self.ram_gb} GB")
        print(f"Almacenamiento: {self.almacenamiento_tb} TB")


class DispositivoEdge(RecursoComputacional):
    def __init__(self, id_recurso, nombre, fabricante, potencia_w, horas_uso,
                 modelo_gpu, memoria_gpu_gb, tipo_inferencia):
        super().__init__(id_recurso, nombre, fabricante, potencia_w, horas_uso)
        self.modelo_gpu = modelo_gpu
        self.memoria_gpu_gb = memoria_gpu_gb
        self.tipo_inferencia = tipo_inferencia

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Modelo GPU: {self.modelo_gpu}")
        print(f"Memoria GPU: {self.memoria_gpu_gb} GB")
        print(f"Tipo de inferencia: {self.tipo_inferencia}")


def main():
    recursos = [
        Ordenador("PC-01", "Estación de análisis", "Dell", 125, 100,
                  "Intel Core i7", 32, "Windows 11"),
        Ordenador("PC-02", "Puesto de prácticas", "Lenovo", 100, 80,
                  "AMD Ryzen 5", 16, "Ubuntu 24.04"),
        Servidor("SRV-01", "Servidor Spark", "HPE", 350, 120,
                 2, 128, 4),
        Servidor("SRV-02", "Servidor de backups", "Dell", 80, 75,
                 1, 64, 8),
        DispositivoEdge("EDGE-01", "Nodo de visión", "NVIDIA", 30, 200,
                        "Jetson Orin", 8, "Visión artificial"),
        DispositivoEdge("EDGE-02", "Nodo de audio", "NVIDIA", 20, 200,
                        "Jetson Nano", 4, "Reconocimiento de voz"),
    ]

    print("========== LABORATORIO BIG DATA ==========\n")

    consumo_total = 0
    recurso_mayor_consumo = recursos[0]

    for recurso in recursos:
        recurso.mostrar_informacion()
        consumo = recurso.calcular_consumo()
        print(f"Consumo acumulado: {consumo:.1f} kWh\n")

        consumo_total += consumo
        if consumo > recurso_mayor_consumo.calcular_consumo():
            recurso_mayor_consumo = recurso

    # Conteo por subclase con isinstance()
    num_ordenadores = sum(1 for r in recursos if isinstance(r, Ordenador))
    num_servidores = sum(1 for r in recursos if isinstance(r, Servidor))
    num_edge = sum(1 for r in recursos if isinstance(r, DispositivoEdge))

    print("========== RESUMEN DEL LABORATORIO ==========\n")
    print(f"Ordenadores: {num_ordenadores}")
    print(f"Servidores: {num_servidores}")
    print(f"Dispositivos Edge: {num_edge}\n")
    print(f"Consumo total: {consumo_total:.1f} kWh")
    print(f"Dispositivo de mayor consumo: {recurso_mayor_consumo.id_recurso}")


if __name__ == "__main__":
    main()
