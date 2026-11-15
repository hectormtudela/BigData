"""Utilidades para limpiar y organizar los datos de clientes del CRM."""

ORDENES = {
    "nombre": lambda c: c["nombre"],
    "gasto": lambda c: c["gasto"],
}


def normalizar(clientes):
    return [
        {
            "nombre": c["nombre"].strip().title(),
            "email": c["email"].strip().lower(),
            "ciudad": c["ciudad"].strip().title(),
            "gasto": c["gasto"],
        }
        for c in clientes
    ]


def dominios(clientes):
    return {c["email"].split("@")[1] for c in clientes}


def indexar_por_email(clientes):
    return {c["email"]: c for c in clientes}


def gasto_por_ciudad(clientes):
    ciudades = sorted({c["ciudad"] for c in clientes})
    return {
        ciudad: round(sum(c["gasto"] for c in clientes if c["ciudad"] == ciudad), 2)
        for ciudad in ciudades
    }


def ordenar(clientes, criterio, descendente=False):
    return sorted(clientes, key=ORDENES[criterio], reverse=descendente)
