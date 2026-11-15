import validaciones

print(f"[main.py] __name__ = {__name__!r}")

clientes = [
    ("Ferretería Ruiz", "28013", "91-555-12-34"),
    ("Bodegas Sol", "99001", "600 11 22 33"),
    ("Talleres Norte", "48001", "944 000"),
]

validos = [
    (nombre, validaciones.normalizar_telefono(telefono))
    for nombre, cp, telefono in clientes
    if validaciones.es_codigo_postal_valido(cp)
]
print(validos)
