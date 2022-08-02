users = ['jair','alex']
passwords = ['123','456']
import time

usuarios = {
    "74721487" : {"Ruc": 20552103816, "Empresa": "AGROLIGHT PERU S.A.C", "Nombre": "Jilmer Coronel Ramos", "Razon": "Agricultura", "Telefono": +51900278514},
}



def ValidarUsuario():
    i = 0
    while i <= 3:
        print('██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░')
        print('██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗')
        print('██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║')
        print('██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║')
        print('██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝')
        print('╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░')
        inuser = input ('Nombre de usuario:')
        inpassword = input ('Contraseña:')
        i += 1
        if inuser in users:
           index = users.index (inuser)
           password = passwords[index]
           if inpassword == password:
              print ('Estimado  %  s inicio de sesión exitoso'% (inuser))
              print("Espera un momento por favor.....")
              time.sleep(5)
              break
           else:
               print('% s error de inicio de sesión: error de contraseña'% inuser)
		    			
def listausers():
    print("{:<10}{:<20}{:<25}{:<30}{:<25}{:<10}".format("Dni", "Ruc", "Empresa", "Nombre Comprador", "Razon Social", "Telefono"))
    for u in usuarios:
        print("{:<10}{:<20}{:<25}{:<30}{:<25}{:<10}".format(u, usuarios[u].get("Ruc"), usuarios[u].get("Empresa"), usuarios[u].get("Nombre"), usuarios[u].get("Razon"),usuarios[u].get("Telefono")))
    print('======================================================')