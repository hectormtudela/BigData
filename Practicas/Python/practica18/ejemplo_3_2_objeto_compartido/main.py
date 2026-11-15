import auditoria
import pagos
from auditoria import registro
from envios import preparar_envio

pagos.cobrar("Bodegas Sol", 245.0)
print(preparar_envio("Bodegas Sol", ["vino tinto", "Cava", "aceite"]))
pagos.cobrar("Talleres Norte", 99.9)

print("Eventos registrados:", len(registro))
for numero, origen, mensaje in registro:
    print(f"  {numero}. [{origen}] {mensaje}")

print("Solo pagos:", len(registro.filtrar("pagos")))
print("¿Mismo objeto en todos los módulos?", registro is auditoria.registro is pagos.registro)
