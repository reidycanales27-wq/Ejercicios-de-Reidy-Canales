saldo = 1000
def retirar(cantidad):
    global saldo
    saldo = saldo - cantidad
retirar(200)
print(saldo)
#==========================================================
# Prefiero global porque modifica directamente el saldo que está fuera de la función y no necesito usar return.