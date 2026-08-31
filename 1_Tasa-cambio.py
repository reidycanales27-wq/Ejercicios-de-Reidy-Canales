Tasa_de_cambio = 36.6
def a_dolares(cordobas):
    dolares = cordobas / TASA_CAMBIO
    return dolares
print(a_dolares(366))
print(dolares)
# NameError: name 'dolares' is not defined. Did you mean: 'a_dolares'?\
#Este mensaje de error que aparece al ejecutar el codigo.