# Crear una aplicación que solicite el ingreso del nombre del alumno y sus 3 notas (Actividad1, Trabajo
# grupal y Examen Final). Calcular el promedio según el peso (Actividad 1 (20%), Trabajo grupal (40%) y
# Examen Final (40%). Indicar si el alumno esta aprobado o desaprobado.

alumno = input('Estimado alumno Ingrese su nombre por favor: ')

act1 = float(input('Ingrese la nota de su Actividad 01: '))

tgrupal = float(input('Ingrese la nota de su Trabajo Grupal: '))

exafinal = float(input('Ingrese la nota de su Examen Final: '))

promedio = (act1 * 0.2) + (tgrupal * 0.4) + (exafinal * 0.4) 


if promedio < 13:
    print('Alumno: ', alumno,'su promedio es de', promedio, 'y por lo tanto se encuentra desaprobado')
if (promedio >= 13) and (promedio < 21):
    print('Alumno: ', alumno,'su promedio es de', promedio, 'y por lo tanto se encuentra Aprobado')