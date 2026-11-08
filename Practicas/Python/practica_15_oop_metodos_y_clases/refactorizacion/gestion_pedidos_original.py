# Código heredado del ejercicio R1 (NO lo modifiques). Tu versión OOP va en gestion_pedidos_oop.py
# El enunciado completo está al principio de gestion_pedidos_oop.py
# gestion_pedidos.py · versión heredada (2017). "Funciona, no tocar".
p_cod = ["AG-01", "RF-02", "ZM-03", "CV-04", "VN-05"]
p_nom = ["Agua 1,5L pack 6", "Refresco cola pack 12", "Zumo naranja 1L", "Cerveza pack 24", "Vino tinto crianza"]
p_pre = [3.20, 9.60, 1.85, 18.90, 7.45]
p_stk = [120, 40, 60, 15, 30]
c_cod = ["CL-1", "CL-2", "CL-3"]
c_nom = ["Bar El Puerto", "Hotel Mirador", "Supermercado Sol"]
c_tip = ["horeca", "horeca", "retail"]
c_vip = [False, True, False]
peds = [
    ["CL-1", [["AG-01", 10], ["CV-04", 4], ["VN-05", 6]]],
    ["CL-2", [["RF-02", 20], ["VN-05", 12], ["XX-99", 1]]],
    ["CL-3", [["AG-01", 100], ["ZM-03", 30], ["CV-04", 10]]],
    ["CL-9", [["AG-01", 1]]],
    ["CL-1", [["CV-04", 5], ["ZM-03", 12]]],
    ["CL-2", [["CV-04", 3]]],
]
tot_emp = 0
n_ok = 0
n_ko = 0
for i in range(len(peds)):
    ped = peds[i]
    ci = -1
    for j in range(len(c_cod)):
        if c_cod[j] == ped[0]:
            ci = j
    if ci == -1:
        print("Pedido " + str(i + 1) + ": cliente " + ped[0] + " desconocido")
        n_ko = n_ko + 1
    else:
        print("Pedido " + str(i + 1) + " - " + c_nom[ci])
        sub = 0
        for l in ped[1]:
            pi = -1
            for k in range(len(p_cod)):
                if p_cod[k] == l[0]:
                    pi = k
            if pi == -1:
                print("   ! producto " + l[0] + " no existe")
            else:
                if p_stk[pi] >= l[1]:
                    p_stk[pi] = p_stk[pi] - l[1]
                    imp = p_pre[pi] * l[1]
                    sub = sub + imp
                    print("   " + p_nom[pi] + " x" + str(l[1]) + " = " + str(round(imp, 2)))
                else:
                    print("   ! sin stock de " + p_nom[pi] + " (quedan " + str(p_stk[pi]) + ")")
        d = 0
        if c_tip[ci] == "horeca":
            if sub > 100:
                d = 0.05
            if c_vip[ci] == True:
                d = d + 0.05
        else:
            if sub > 300:
                d = 0.08
            if c_vip[ci] == True:
                d = d + 0.05
        desc = sub * d
        base = sub - desc
        iva = base * 0.21
        tot = base + iva
        if sub > 0:
            print("   Subtotal: " + str(round(sub, 2)) + " | Dto: " + str(round(desc, 2)) + " | IVA: " + str(round(iva, 2)) + " | Total: " + str(round(tot, 2)))
            tot_emp = tot_emp + tot
            n_ok = n_ok + 1
        else:
            print("   Pedido vacío")
            n_ko = n_ko + 1
print("==============================")
print("Pedidos facturados: " + str(n_ok) + " | Rechazados: " + str(n_ko))
print("Facturación total: " + str(round(tot_emp, 2)))
print("Stock bajo (<20):")
for k in range(len(p_cod)):
    if p_stk[k] < 20:
        print("   " + p_cod[k] + " " + p_nom[k] + ": " + str(p_stk[k]))
