# Funciones en Python
def promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3
    return prom

prom = round(promedio(12, 15, 16), 2)
print('Tu promedio es: ', prom) 

def operaciones(num1, num2):
    suma = num1 + num2
    prod = num1 + num2
    divi = num1 / num2
    resta = num1 - num2
    resultado = [suma, resta, divi, prod]
    return resultado
print(operaciones(12, 5))


opera = operaciones(5, 2)
for r in opera:
    print('Resulatdo: ', r)

