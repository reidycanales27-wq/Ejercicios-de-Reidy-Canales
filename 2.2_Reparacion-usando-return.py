saldo = 1000
def retirar(saldo, cantidad):
    saldo = saldo - cantidad
    return saldo
saldo = retirar(saldo, 200)
print(saldo)
