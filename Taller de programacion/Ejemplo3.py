# Crear funciones haciendo uso de diccionarios

# Con Listas
from cgi import print_arguments


usuarios = ['jperez', 'ccastro']
password = ['123456', 'abc']
estado = [1, 0]

def ValidarUsuarioL(user, pwd, lusuarios, lpassword):    
    if user in lusuarios:
        mensaje = 'Usuario existe'
        if pwd in lpassword:
            mensaje += ' - Password Correcto'
        else:
            mensaje += ' - Password incorrecto'            
    else:
        mensaje = 'Usuario no existe'
    return mensaje

print(ValidarUsuarioL("jperez", "123456", usuarios, password))

#Modificar la funcion ValidarUsuarioL y crear la funcion ValidarUsuarioLv2
# de tal manera que muestre un mensaje de bienvenida al usuario que ha validado (nombre de usuario y
# password son correctos) siempre y cuando el usuario este activo


print('*******************Validar Usuario v2***************')
def ValidarUsuarioLV2(user, pwd, lusuarios, lpassword, lestado):
    if user in lusuarios and pwd in lpassword:
        i = lusuarios.index(user)
        if lestado[i] ==1:
            return 'Bienvenido al sistema'
    return 'Acceso no Autorizado'       
   

print(ValidarUsuarioLV2('jperez', '123456', usuarios, password, estado))


print('*******************Validar Usuario v3***************')
def ValidarUsuarioLV3(user, pwd, lusuarios, lpassword, lestado):
    if user in lusuarios and pwd in lpassword:
        i = lusuarios.index(user)
        if lestado[i] ==1:
            return True
    return False       
   

if(ValidarUsuarioLV3('jperez', '123456', usuarios, password, estado)):
    print('Bienvenido al sistema')
else:
    print('Error de acceso')
     


#Diccionario
usuario1 = {'Nombre': 'jperez', 'Password': '123456', 'Estado': 1}
usuario2 = {'Nombre': 'ccastro', 'Password': 'abc', 'Estado': 0}

#Definir una funcion que valide el nombre del usuario
#Ejemplo de listados 