MONEDA = "C$"
IVA = 0.15
def agregar_producto(inventario, nombre, precio):
    inventario.append([nombre, precio])

def calcular_valor_total(inventario):
    total = 0
    for producto in inventario:
        total = total + producto[1]
    total = total + (total * IVA)
    return total

def mostrar_inventario(inventario):
    for producto in inventario:
        print(producto[0], MONEDA, producto[1])

inventario = []
agregar_producto(inventario, "Arroz", 45)
agregar_producto(inventario, "Frijoles", 35)
agregar_producto(inventario, "Aceite", 75)
mostrar_inventario(inventario)
total = calcular_valor_total(inventario)
print("Total:", MONEDA, total)
