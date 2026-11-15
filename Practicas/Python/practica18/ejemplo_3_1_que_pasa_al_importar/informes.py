import configuracion


def formatear(importe):
    decimales = configuracion.CONFIG["decimales"]
    moneda = configuracion.CONFIG["moneda"]
    return f"{importe:.{decimales}f} {moneda}"
