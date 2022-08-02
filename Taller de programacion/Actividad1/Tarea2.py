#Crear una aplicación que calcule el pago por los dias trabajados. Se debe solicitar el nombre del
# trabajador, la fecha de inicio y la fecha final del trabajo y el pago día. El trabajador tendrá un bono del
# 10% de su pago si trabaja entre 11 y 20 dias, 15% si trabaja entre 21 y 30 dias, 20% si trabaja entre 31
# y 45 dias, y 30% si trabaja más de 45 dias, si trabajó menos de 11 dias no tiene bono.

from datetime import date

trabajador = input('Ingrese su nombre por favor: ')


fecha_inicio = input('Ingrese fecha de inicio de trabajo: ')
fecha_inicio = date.strptime(fecha_inicio, '%d/%m/%Y')

fecha_final = input('Ingrese fecha final de trabajo: ')
fecha_final = date.strptime(fecha_final, '%d/%m/%Y')

dia = int(input('Ingrese el pago por dia: '))


dias_trans = (fecha_inicio - fecha_final).days

pago = dias_trans * dia

print('Han transcurrido:',dias_trans, 'dias trabajados')


if (dias_trans < 11):
  bono = 0
elif (dias_trans > 10) and (dias_trans < 21):
  bono = 0.10 * pago
elif (dias_trans > 20) and (dias_trans < 31):
  bono = 0.15 * pago
elif (dias_trans > 30) and (dias_trans < 46):
  bono = 0.20 * pago
elif (dias_trans > 45):
  bono = 0.30 * pago
  
print('El pago neto es de', pago)
print('El bono que te corresponde es de', bono, 'soles')