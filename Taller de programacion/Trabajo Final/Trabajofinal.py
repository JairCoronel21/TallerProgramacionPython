import time
from datetime import  datetime
users = ['jair','alex']
passwords = ['123','456']

#Intentos de acceso
trycount = 0


while trycount < 3:
   print('BIENVENIDO')
   inuser = input ('Nombre de usuario:')
   inpassword = input ('Contraseña:')
   trycount += 1
   if inuser in users:
      index = users.index (inuser) 
      password = passwords[index]
      if inpassword == password:
            print ('Estimado  %  s inicio de sesión exitoso'% (inuser))
            print("Espera un momento por favor.....")
            time.sleep(5)
            break
      else:
            print ('% s error de inicio de sesión: error de contraseña'% inuser)
   else:
       print ('El usuario% s no existe'% inuser)
else:
      print ('Intentaste más de tres veces, vuelve a intentarlo más tarde')
      exit(0)         
      
      

productos = {
    "P0001" : {"Nombre": "Casco", "Precio": 150, "Stock": 10},
    "P0002" : {"Nombre": "Guantes", "Precio": 200, "Stock": 25},
    "P0003" : {"Nombre": "Lentes", "Precio": 180, "Stock": 5},
    "P0004" : {"Nombre": "Mascarillas", "Precio": 80, "Stock": 5},
    "P0005" : {"Nombre": "Protectores Faciales", "Precio": 30, "Stock": 5},
    "P0006" : {"Nombre": "Mascara", "Precio": 50, "Stock": 20},
    "P0007" : {"Nombre": "Arnes", "Precio": 120, "Stock": 35},
    "P0008" : {"Nombre": "Tapones", "Precio": 80, "Stock": 15},
    "P0009" : {"Nombre": "Botas", "Precio": 100, "Stock": 45},
    "P0010" : {"Nombre": "Chalecos", "Precio": 30, "Stock": 10}  
}
   
     
      

print("******************************************************")
print("*************Peru Delivery*******************")
print("========lista de productos en el catalogo==========")

print("{:<10}{:<30}{:<15}{:<20}".format("Codigo", "Nombre", "Precio", "Stock"))
for p in productos:
      print("{:<10}{:<30}{:0}{:<15}{:<20}".format(p, productos[p].get("Nombre"),"S/", productos[p].get("Precio"), productos[p].get("Stock")))
print('======================================================')

detalle = {}
i = 1
rp = "si"
while rp.lower() == "si":
    if i <= 10:
      print("-" * 72)
      print('Pedido Número: ', i)
      print('Recuerda que solo puedes adquirir 10 productos como máximo.....')
      print("-" * 72)
      codp = input("Ingrese codigo de Producto: ")
      canp = input("Ingrese cantidad de unidades a comprar:")
      imp = productos[codp].get("Precio") * int(canp)
      sub = round((imp / 1.18),2)
      igv = round((imp - sub),2)
      nombrep = productos[codp].get("Nombre")
      preciop = productos[codp].get("Precio")
      detalle.setdefault(nombrep, {"Precio": preciop, "Cantidad": canp, "Importe": imp, "SubTotal": sub, "IGV": igv})
      i += 1
      
      rp = input("¿Desea continuar comprando? (SI/NO): ")
      if rp.lower() == "no":
          print("====Escoja el tipo de Comprobante=====")
          print("1. Boleta")
          print("2. Factura")
          ele = int(input("¿Que desea generar? Boleta o Factura: "))
          
          if ele == 1:
            def boleta():  
                print("\n **************BOLETA DE PAGO******************************* \n")
                fechaHoy = datetime.now()
                print("Fecha: ", fechaHoy.date())
                print("{:<20}{:<15}{:<10}{:<0}".format("Producto", "Precio", "Canitdad", "Importe"))
                print("-" * 52)
                for d in detalle:
                    print(
                        "{:<20}{:<15}{:<10}{:<0}".format(
                            d, detalle[d]["Precio"], detalle[d]["Cantidad"], detalle[d]["Importe"]
                        )
                    )
                    
            boleta()
            total = sum(col["Importe"] for col in detalle.values())
            print("-" * 72)
            print("{:<20}{:<15}{:<10}{:<0}".format("", "Total a Pagar", "", total))
            print()
            print("**Muchas Gracias!!! Vuelva Pronto")  

            break
          elif ele == 2:
            ruc = int(input('Ingrese su numero de ruc: '))
            nom = input ('Ingrese su Nombre Completo: ')
            dn = int(input('Ingrese su Documento de Identidad: '))
            n = input('Ingrese Nombre de la Empresa:')
            rs = input('Ingrese razon social: ')
            
            def factura():
                print("\n******************FACTURA DE PAGO**********************************\n")
                fechaHoy = datetime.now()
                print("Fecha: ", fechaHoy.date())
                print('Empresa: ', n)
                print('Razon Social: ', rs)
                print('Sr: ', nom)
                print('Ruc: ', ruc)
                print('Dni:', dn)
                print("=" * 72)
                print('{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}'.format("Nombre del producto", "Cantidad", "Precio Unidad", "SubTotal", "IGV", "Total"))
                
                for d in detalle:
                    
                    print('{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}'.format
                          (d, detalle[d]["Cantidad"], detalle[d]["Precio"], detalle[d]["SubTotal"], detalle[d]["IGV"], detalle[d]["Importe"]
                           ))
                   
                    
            factura() 
            total = sum(col["Importe"] for col in detalle.values())
            print("-" * 72)
            print("{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}".format("","","", "TOTAL A PAGAR", "", total))
            print()
            print("**Muchas Gracias!!! Vuelva Pronto")      
            break   
          else:
               print('Ingrese una opción valida Por favor')
               exit(0)
              
    else:
      print("Lastimosamente usted llego al limite de compras")
      exit(0)
      
      
          
 
