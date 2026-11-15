"""Validaciones de los datos de clientes."""

print(f"  [validaciones.py] __name__ = {__name__!r}")


def es_codigo_postal_valido(cp):
    return len(cp) == 5 and cp.isdigit() and 1 <= int(cp[:2]) <= 52


def normalizar_telefono(telefono):
    digitos = "".join(c for c in telefono if c.isdigit())
    if len(digitos) < 9:
        return None
    return "+34" + digitos[-9:]


if __name__ == "__main__":
    print("  Pruebas rápidas del módulo:")
    print("  ", es_codigo_postal_valido("28013"), es_codigo_postal_valido("99001"))
    print("  ", normalizar_telefono("612 34 56 78"), normalizar_telefono("123"))
