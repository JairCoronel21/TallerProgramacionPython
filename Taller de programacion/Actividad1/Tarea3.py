# Crear un aplicación que valide el nombre de usuario y contraseña. Se deberá mostrar un mensaje de
# bienvenida solo si se ingreso el usuario y contraseña correcta. La aplicación debe mostrar un mensaje
# especifico que indique si el error fue el nombre de usuario, la contraseña o ambos.

user = 'Jair'
password = '@234'

print('****BIENVENIDO AL SISTEMA****')
userpw = input('Ingrese su usuario por favor: ')
passwordpw = input('Ingrese su contraseña por favor: ')

if (user == userpw) and (password == passwordpw):
    print('Ingreso correcto al sistema !Bienvenido!')
elif (user != userpw) and (password == passwordpw):
    print('La contraseña esta bien pero el usuario es incorrecto')
elif (user == userpw) and (password != passwordpw):
    print('El usuario esta bien pero la contraseña es incorrecta')
else:
    print('¡Ambos datos son erroneos! Vuelva a intentarlo por favor')