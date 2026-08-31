TOTAL_ALUMNOS = 3

def promedio(a, b):
    suma = a + b
    return suma / 2

def reporte(nota1, nota2):
    p = promedio(nota1, nota2)
    print("De", TOTAL_ALUMNOS, "alumnos, promedio parcial:", p)
    return p

final = reporte(80, 95)
print(final)