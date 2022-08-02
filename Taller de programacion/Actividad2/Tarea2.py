# Crear Listas: Nombre, Password, Estado (0/1), Tipo (Cliente/Admin), PalabraClave
# • Crear una aplicación que permita validar los accesos de los usuarios al sistema mediante bloqueos.
# • Registrar 10 usuarios, solo uno debe ser Admin, 5 usuarios tipo Cliente deben estar activos los demás inactivos.
# • La aplicación debe solicitar el nombre del usuario. La contraseña se solicita solo si el usuario existe y tiene su cuenta activa.
# • Si el usuario tiene la cuenta inactiva debe mostrar el mensaje respectivo.
# • Bloqueo por contraseña equivocada: Admin solo se puede equivocar 1 sola vez, Cliente 3 veces. Se le avisa por un mensaje.
# • Crear una aplicación para recuperar contraseña: La contraseña se recupera solo si se ingresa el nombre de usuario y palabra clave correcta.


nombres = ['fer21', 'anacastro22', 'Luc','mar08','chirax','any08','jquintana','sergiog','xime19','joe09']
tipo = ['a','c','c','c','c','c','c','c','c','c','c']
pwd = ['f21','ac15','louen25','mar_v12','123456','any8','j_24@','ser_gy12','xime_q19','coronel123']
estado = [1,0,1,0,0,1,1,0,1,1]
pclave = ['fer','perro','gato','carro','uwu','xd','miau','chale','tutu','maldito']


usuario = input('Ingrese el nombre del usuario: ')

if nombres.count(usuario) == 1:
  c = nombres.index(usuario)
  if estado[c] == 1:
    if tipo[c] == 'a':     
      print('Cuenta de tipo administrador') 
      contador = 1
      contraseña = input('Ingrese su contraseña: ')
      while contador <2:
        if pwd[c] == contraseña:
          print('contraseña correcta ')
          print('*****************')
          print('Bienvenido ',usuario)
          break
          contador = 2
        else:
          print('contraseña incorrecta') 
          if contador == 1:
            print('Cuenta bloqueada,has fallado 1 intento')       
            contador = contador +1
            break          
    else:
      print('Cuenta de tipo cliente')
      contador = 1
      while contador <= 3:
        contraseña = input('Escribe la contraseña: ')
        if contraseña == pwd[c]:
          print('contraseña correcta ')
          print('*****************')
          print('Bienvenido ',usuario)
          break
        else:
          print('Contraseña incorrecta')
          if contador == 3:
            print('Cuenta bloqueda has fallado los 3 intentos')
          contador = contador +1  
  else:
    print('La cuenta',usuario,'esta inactiva, no tiene acceso') 
else:
  print('El usuario',usuario,'no esta registrado')
  
  
  contador = 1
while contador <= 3:
  contraseña = input('Escribe la contraseña: ')
  if contraseña == pwd[c]:
    print('CONTRASEÑA CORRECTA')
    break
  else:
    print('Contraseña incorrecta')
    if contador == 3:
      print('Cuenta bloqueda has fallado los 3 intentos')
    contador = contador +1


contador = 1
contraseña = input('Ingrese su contraseña1: ')
while contador <2:
  if pwd[c] == contraseña:
    print('contraseña correcta 1')
    break
    contador = 2
  else:
    print('contraseña incorrecta') 
    if contador == 1:
      print('Cuenta bloqueada')       
      contador = contador +1
      break


while contador <= +3:
  user = input('Ingrese su usuario: ')
  clave = input('Ingrese palabra clave: ')
  if nombres.count(user) == 1:
    c = nombres.index(user)
    if pclave[c] == clave:  
      print('************************')
      print('clave correcta','su contra es ',pwd[c])                    
      break
    else:
      print('*****************')
      print('clave incorrecta')  
      print('*****************')
  else:
    print('*****************')
    print('usuario incorrecto') 
    print('*****************')


resp2 = 'si'
while resp2.lower()=='si':
  user = input('Ingrese su usuario: ')
  clave = input('Ingrese palabra clave: ')
  if nombres.count(user) == 1:
    c = nombres.index(usuario)
    if pclave[c] == clave:  
      print('clave correcta','su contra es ',pwd[c])
      break
    else:
      print('clave incorrecta')  
  else:
    print('usuario incorrecto')    