# Ejemplo 6.2 · Eventos de log con formato homogéneo
# clase_18_clases_objetos/teoria/ejemplo_6_2_evento_log.py

class EventoLog:
    def __init__(self, timestamp, nivel, servicio, mensaje):
        self.timestamp = timestamp
        self.nivel = nivel
        self.servicio = servicio
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.timestamp} [{self.nivel:<5}] {self.servicio:<12} | {self.mensaje}"

    def __repr__(self):
        return f"EventoLog('{self.timestamp}', '{self.nivel}', '{self.servicio}')"

eventos = [
    EventoLog("2026-10-26 02:00:01", "INFO", "ingesta", "Inicio de carga de ventas"),
    EventoLog("2026-10-26 02:03:47", "WARN", "ingesta", "Fichero tienda_12 llega vacío"),
    EventoLog("2026-10-26 02:05:10", "ERROR", "transform", "Columna 'importe' con texto no numérico"),
    EventoLog("2026-10-26 02:09:33", "INFO", "carga", "Lote publicado en zona curated"),
]

for evento in eventos:
    print(evento)

errores = [e for e in eventos if e.nivel == "ERROR"]
print(errores)
