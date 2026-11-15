import limpieza as lp
from limpieza import ORDENES

crudos = [
    {"nombre": "  ana lópez", "email": "ANA@Gmail.com ", "ciudad": "madrid", "gasto": 320.5},
    {"nombre": "LUIS PÉREZ ", "email": "luis@empresa.es", "ciudad": " Sevilla", "gasto": 89.9},
    {"nombre": "marta ruiz", "email": "marta@gmail.com", "ciudad": "Madrid ", "gasto": 145.0},
    {"nombre": "ana lópez", "email": "ana@gmail.com", "ciudad": "madrid", "gasto": 60.0},
]

clientes = lp.normalizar(crudos)
print([c["nombre"] for c in clientes])
print("Dominios:", sorted(lp.dominios(clientes)))

indice = lp.indexar_por_email(clientes)
print(len(clientes), "registros ->", len(indice), "emails distintos")
print("Gasto por ciudad:", lp.gasto_por_ciudad(clientes))

mejores = lp.ordenar(clientes, "gasto", descendente=True)
print("Por gasto:", [(c["nombre"], c["gasto"]) for c in mejores[:2]])
print("Criterios disponibles:", list(ORDENES))
