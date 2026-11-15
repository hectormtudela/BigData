"""Registro de auditoría compartido por todo el programa."""


class RegistroAuditoria:
    def __init__(self):
        self._eventos = []

    def anotar(self, origen, mensaje):
        self._eventos.append((len(self._eventos) + 1, origen, mensaje))

    def filtrar(self, origen):
        return [evento for evento in self._eventos if evento[1] == origen]

    def __len__(self):
        return len(self._eventos)

    def __iter__(self):
        for evento in self._eventos:
            yield evento


registro = RegistroAuditoria()          # instancia única, creada al importar el módulo
