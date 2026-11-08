# Ejemplo 7.3 · Composición: un pipeline formado por etapas
# clase_18_clases_objetos/teoria/ejemplo_7_3_pipeline_etapas.py

class Etapa:
    def __init__(self, nombre, duracion_seg):
        self.nombre = nombre
        self.duracion_seg = duracion_seg
        self.ejecutada = False

    def ejecutar(self):
        self.ejecutada = True
        return f"  OK  {self.nombre} ({self.duracion_seg}s)"

class Pipeline:
    def __init__(self, nombre):
        self.nombre = nombre
        self.etapas = []

    def agregar_etapa(self, etapa):
        self.etapas.append(etapa)

    def duracion_total(self):
        return sum([etapa.duracion_seg for etapa in self.etapas])

    def ejecutar(self):
        print(f"Pipeline '{self.nombre}' ({len(self.etapas)} etapas)")
        for etapa in self.etapas:
            print(etapa.ejecutar())
        print(f"Duración total: {self.duracion_total()}s")

pipeline = Pipeline("ventas_nocturno")
pipeline.agregar_etapa(Etapa("extraer_ficheros_tiendas", 120))
pipeline.agregar_etapa(Etapa("validar_esquema", 35))
pipeline.agregar_etapa(Etapa("deduplicar_tickets", 48))
pipeline.agregar_etapa(Etapa("publicar_zona_curated", 60))

print([etapa.ejecutada for etapa in pipeline.etapas])
pipeline.ejecutar()
print([etapa.ejecutada for etapa in pipeline.etapas])
