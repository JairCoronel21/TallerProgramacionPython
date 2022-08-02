# Crear una aplicación que permita calcular el IMC de una persona. La aplicación debe indicar el estado
# de la persona (Falta peso, peso ideal, sobre peso, obesidad, etc.)


def imc(estatura, peso):
    # Calcula el indice de masa corporal
    return peso / estatura**2

peso = float(input('Escriba su peso(KG): '))	
estatura = float(input('Escriba su estatura (m)'))

indice = imc(estatura, peso)

print('Su IMC es: {}'.format(indice))

if (indice < 18.5):
    print('Su estado es Peso Bajo')
elif (indice > 18.5) and (indice < 24.9):
    print('Su estado es Normal')
elif (indice > 25) and (indice < 29.9):
    print('Su estado es de SobrePeso')
elif (indice > 30) and (indice < 34.9):
    print('Su estado es de Obesidad I')
elif (indice > 35) and (indice < 39.9):
    print('Su estado es de Obesidad II')
elif (indice > 40) and (indice < 49.9):
    print('Su estado es de Obesidad III')
else:
    print('Su estado es de Obesidad IV')
        
        