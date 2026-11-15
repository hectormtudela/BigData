import logistica
import logistica.rutas as rutas
from logistica.vehiculos import Furgoneta, Camion

flota = [Furgoneta("1234-KLM", 1200), Camion("5678-PQR", 18000)]
tramos = [120, 85.5, 40]
carga_kg = 3500

print("Distancia:", rutas.distancia_total(tramos), "km")
for vehiculo in flota:
    print(f"  {vehiculo} -> {rutas.coste_ruta(vehiculo, tramos)} €")

aptos = [v.matricula for v in flota if v.puede_cargar(carga_kg)]
print(f"Aptos para {carga_kg} kg:", aptos)

print(type(logistica))
print(logistica.__name__, "|", rutas.__name__, "|", Furgoneta.__module__)
