# Crear una aplicación que solicite la fecha de nacimiento de una persona y genere la edad
from datetime import datetime
def edad(f):
  fechaHoy = datetime.now()
  fecha = datetime.strptime(f, '%d/%m/%Y')
  e = fechaHoy.year - fecha.year
  if fecha.month <= fechaHoy.month:
     if fecha.day <= fechaHoy.day:
       print('Tienes', e, 'años')
     else: print('Tienes', e-1, 'años')

edad(input('Intoduce tu fecha de nacimiento: '))
  