"""
Práctica 15 · Ejercicio R1 - Refactorizar el gestor de pedidos de una distribuidora
Nivel: refactorización
Regla: sin herencia ni polimorfismo (usa composición). Solo biblioteca estándar.
Objetivo: misma salida que gestion_pedidos_original.py, carácter a carácter.
"""

# ======================================================================
# ENUNCIADO (copiado tal cual del profesor)
# ======================================================================
# ### Ejercicio R1 - Refactorizar el gestor de pedidos de una distribuidora
#
# Una distribuidora de bebidas para hostelería (canal **horeca**) y supermercados (canal **retail**) factura con un script escrito en 2017 por un becario que ya no está en la empresa. «Funciona», pero nadie se atreve a tocarlo: cada vez que cambia una regla de descuento hay que buscar en varios sitios y siempre se rompe algo. Te encargan **reescribirlo con programación orientada a objetos sin cambiar su comportamiento**.
#
# **Restricción: no está permitido usar herencia ni polimorfismo.** Toda la reutilización se consigue con **composición** (objetos que contienen o usan otros objetos).
#
# **Código heredado:**
#
# ```python
# # gestion_pedidos.py · versión heredada (2017). "Funciona, no tocar".
# p_cod = ["AG-01", "RF-02", "ZM-03", "CV-04", "VN-05"]
# p_nom = ["Agua 1,5L pack 6", "Refresco cola pack 12", "Zumo naranja 1L", "Cerveza pack 24", "Vino tinto crianza"]
# p_pre = [3.20, 9.60, 1.85, 18.90, 7.45]
# p_stk = [120, 40, 60, 15, 30]
# c_cod = ["CL-1", "CL-2", "CL-3"]
# c_nom = ["Bar El Puerto", "Hotel Mirador", "Supermercado Sol"]
# c_tip = ["horeca", "horeca", "retail"]
# c_vip = [False, True, False]
# peds = [
#     ["CL-1", [["AG-01", 10], ["CV-04", 4], ["VN-05", 6]]],
#     ["CL-2", [["RF-02", 20], ["VN-05", 12], ["XX-99", 1]]],
#     ["CL-3", [["AG-01", 100], ["ZM-03", 30], ["CV-04", 10]]],
#     ["CL-9", [["AG-01", 1]]],
#     ["CL-1", [["CV-04", 5], ["ZM-03", 12]]],
#     ["CL-2", [["CV-04", 3]]],
# ]
# tot_emp = 0
# n_ok = 0
# n_ko = 0
# for i in range(len(peds)):
#     ped = peds[i]
#     ci = -1
#     for j in range(len(c_cod)):
#         if c_cod[j] == ped[0]:
#             ci = j
#     if ci == -1:
#         print("Pedido " + str(i + 1) + ": cliente " + ped[0] + " desconocido")
#         n_ko = n_ko + 1
#     else:
#         print("Pedido " + str(i + 1) + " - " + c_nom[ci])
#         sub = 0
#         for l in ped[1]:
#             pi = -1
#             for k in range(len(p_cod)):
#                 if p_cod[k] == l[0]:
#                     pi = k
#             if pi == -1:
#                 print("   ! producto " + l[0] + " no existe")
#             else:
#                 if p_stk[pi] >= l[1]:
#                     p_stk[pi] = p_stk[pi] - l[1]
#                     imp = p_pre[pi] * l[1]
#                     sub = sub + imp
#                     print("   " + p_nom[pi] + " x" + str(l[1]) + " = " + str(round(imp, 2)))
#                 else:
#                     print("   ! sin stock de " + p_nom[pi] + " (quedan " + str(p_stk[pi]) + ")")
#         d = 0
#         if c_tip[ci] == "horeca":
#             if sub > 100:
#                 d = 0.05
#             if c_vip[ci] == True:
#                 d = d + 0.05
#         else:
#             if sub > 300:
#                 d = 0.08
#             if c_vip[ci] == True:
#                 d = d + 0.05
#         desc = sub * d
#         base = sub - desc
#         iva = base * 0.21
#         tot = base + iva
#         if sub > 0:
#             print("   Subtotal: " + str(round(sub, 2)) + " | Dto: " + str(round(desc, 2)) + " | IVA: " + str(round(iva, 2)) + " | Total: " + str(round(tot, 2)))
#             tot_emp = tot_emp + tot
#             n_ok = n_ok + 1
#         else:
#             print("   Pedido vacío")
#             n_ko = n_ko + 1
# print("==============================")
# print("Pedidos facturados: " + str(n_ok) + " | Rechazados: " + str(n_ko))
# print("Facturación total: " + str(round(tot_emp, 2)))
# print("Stock bajo (<20):")
# for k in range(len(p_cod)):
#     if p_stk[k] < 20:
#         print("   " + p_cod[k] + " " + p_nom[k] + ": " + str(p_stk[k]))
# ```
#
# **Salida del código heredado:**
#
# ```plain text
# Pedido 1 - Bar El Puerto
#    Agua 1,5L pack 6 x10 = 32.0
#    Cerveza pack 24 x4 = 75.6
#    Vino tinto crianza x6 = 44.7
#    Subtotal: 152.3 | Dto: 7.62 | IVA: 30.38 | Total: 175.07
# Pedido 2 - Hotel Mirador
#    Refresco cola pack 12 x20 = 192.0
#    Vino tinto crianza x12 = 89.4
#    ! producto XX-99 no existe
#    Subtotal: 281.4 | Dto: 28.14 | IVA: 53.18 | Total: 306.44
# Pedido 3 - Supermercado Sol
#    Agua 1,5L pack 6 x100 = 320.0
#    Zumo naranja 1L x30 = 55.5
#    Cerveza pack 24 x10 = 189.0
#    Subtotal: 564.5 | Dto: 45.16 | IVA: 109.06 | Total: 628.4
# Pedido 4: cliente CL-9 desconocido
# Pedido 5 - Bar El Puerto
#    ! sin stock de Cerveza pack 24 (quedan 1)
#    Zumo naranja 1L x12 = 22.2
#    Subtotal: 22.2 | Dto: 0.0 | IVA: 4.66 | Total: 26.86
# Pedido 6 - Hotel Mirador
#    ! sin stock de Cerveza pack 24 (quedan 1)
#    Pedido vacío
# ==============================
# Pedidos facturados: 4 | Rechazados: 2
# Facturación total: 1136.78
# Stock bajo (<20):
#    AG-01 Agua 1,5L pack 6: 10
#    ZM-03 Zumo naranja 1L: 18
#    CV-04 Cerveza pack 24: 1
#    VN-05 Vino tinto crianza: 12
# ```
#
# **Reglas de negocio que esconde el código** (descúbrelas tú también leyéndolo):
#
# - Canal `horeca`: 5 % de descuento si el subtotal supera 100 €. Canal `retail`: 8 % si supera 300 €.
# - Los clientes VIP suman un 5 % extra de descuento, en cualquier canal.
# - El IVA es del 21 % sobre la base (subtotal − descuento).
# - Si no hay stock suficiente de un producto, esa línea no se sirve. Si ninguna línea se sirve, el pedido es vacío y cuenta como rechazado.
# **Se pide:**
#
# 4. **Diagnóstico.** Al principio de `gestion_pedidos_oop.py`, en un comentario, enumera **al menos 6 problemas** de diseño del código heredado (por ejemplo: listas paralelas, búsquedas repetidas, números mágicos…).
# 5. **Diseño.** Implementa como mínimo estas clases (los nombres de los métodos los decides tú):
# | Clase | Responsabilidad |
# | --- | --- |
# | `Producto` | Código, nombre, precio y **stock privado**. Sabe si tiene stock suficiente y descuenta unidades. |
# | `Cliente` | Código, nombre, canal y si es VIP. Sabe **qué porcentaje de descuento le corresponde** para un subtotal. Las reglas por canal son un **atributo de clase**. |
# | `Pedido` | Cliente, líneas servidas o con incidencia, subtotal, descuento, IVA y total. El IVA es un **atributo de clase**. `bool(pedido)` indica si tiene algo facturable y `str(pedido)` produce su bloque de texto. |
# | `Distribuidora` | Catálogo de productos y clientes (diccionarios **privados** por código), procesa pedidos, acumula la facturación y genera el informe final. |
# 6. **Prohibido** en tu versión: listas paralelas, variables globales que se modifiquen dentro de bucles, búsquedas con `for j in range(len(...))` para encontrar un elemento y números sueltos (`0.21`, `100`, `0.05`, `20`…) fuera de atributos de clase.
# 7. **Test de caracterización.** La salida de tu programa debe ser **idéntica carácter a carácter** a la del código heredado. Compruébalo en PowerShell:
# ```powershell
# python gestion_pedidos_original.py > salida_original.txt
# python gestion_pedidos_oop.py > salida_oop.txt
# Compare-Object (Get-Content salida_original.txt) (Get-Content salida_oop.txt)
# ```
#
# Si `Compare-Object` no muestra nada, las dos salidas son iguales.
# 8. **Prueba de extensibilidad.** Cuando termines, responde en un comentario: si mañana se crea el canal `online` (3 % de descuento a partir de 50 €), ¿cuántas líneas tienes que cambiar en tu versión? ¿Y en la original?

# ===== DIAGNÓSTICO: al menos 6 problemas de diseño del código heredado =====
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.


# ===== ESCRIBE AQUÍ TU SOLUCIÓN (Producto, Cliente, Pedido, Distribuidora) =====



# ===== PRUEBA DE EXTENSIBILIDAD =====
# Si mañana se crea el canal "online" (3 % de descuento a partir de 50 €):
# - Líneas a cambiar en mi versión:
# - Líneas a cambiar en la original:
