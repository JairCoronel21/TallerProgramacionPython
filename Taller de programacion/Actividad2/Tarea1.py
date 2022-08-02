# Crear una aplicación que permita validar una contraseña que tenga las siguientes características. 
# • Debe contener al menos 10 caracteres 
# • Debe contener al menos 1 mayúscula 
# • Debe contener algunos de estos símbolos especiales: #, $ o @ 
# • No debe contener espacios en blanco 
# • La aplicación debe mostrar un mensaje indicando al usuario cual es la validación que se esta infringiendo.

import re

def validar(password):
  if 10 <= len(password):
    if (re.search('[a-z]', password) and re.search('[A-Z]', password)):
      if (re.search('[0-9]', password)):
         if  (re.search('[$@#]', password)):
           print('Contraseña escrita correctamente')
      
   
         else:
           print("La contraseña debe tener al menos un carácter especial")
      else:
         print("La contraseña debe tener al menos un número")
    else:
      print("La contraseña no debe tener espacios en blanco y debe tener al menos una Mayuscula")
  else:
    print("La contraseña debe tener al menos 10 carcacteres")

clave = input('Escriba la contraseña: ')

print(validar(clave))