from bdb import Breakpoint
from usuario.usuario import ValidarUsuario, listausers
from datetime import  datetime
from datos.datos import productos as prod

from datos.datos import lista
from comprobante.comprobante import comprobantef, comprobante, detalle
from datetime import  datetime

   
ValidarUsuario()



lista()

i = 1
rp = "si"
while rp.lower() == "si":
    if i <= 10:
      print("-" * 72)
      print('Pedido Número: ', i)
      print('Recuerda que solo puedes adquirir 10 productos como máximo.....')
      print("Aun puede comprar ", 10-i, "productos mas")
      print("-" * 72)
      codp = input("Ingrese codigo de Producto: ")
      codp = codp.upper()
      if codp in prod:
        canp = input("Ingrese cantidad de " + prod[codp].get("Nombre") + " a comprar:")
        imp = prod[codp].get("Precio") * int(canp)
        sub = round((imp / 1.18),2)
        igv = round((imp - sub),2)
        nombrep = prod[codp].get("Nombre")
        preciop = prod[codp].get("Precio")
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
                  print("\nB̲o̲l̲e̲t̲a̲ d̲e̲ P̲a̲g̲o̲\n")
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
              comprobantef()  

              break
            elif ele == 2:
              
              
              def factura():
                  fechaHoy = datetime.now()
                  print("Fecha: ", fechaHoy.date())
                  
                  print("\nF̲a̲c̲t̲u̲r̲a̲ d̲e̲ P̲a̲g̲o̲\n")
                  listausers() 
                  print('{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}'.format("Nombre del producto", "Cantidad", "Precio Unidad", "SubTotal", "IGV", "Total"))
                  
                  for d in detalle:
                      
                      print('{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}'.format
                            (d, detalle[d]["Cantidad"], detalle[d]["Precio"], detalle[d]["SubTotal"], detalle[d]["IGV"], detalle[d]["Importe"]
                            ))
                    
                    
              factura() 
              comprobante()      
              break   
            else:
                print('Ingrese una opción valida Por favor')
                exit(0)
      else:
        print("Codigo Ingresado no existe!!! Intentelo de nuevo y revise la lista: ")  
        continue  
    else:
            print("Lastimosamente usted llego al limite de compras")
            print("====Escoja el tipo de Comprobante=====")
            print("1. Boleta")
            print("2. Factura")
            ele = int(input("¿Que desea generar? Boleta o Factura: "))
            
            if ele == 1:
              def boleta():  
                  print("\nB̲o̲l̲e̲t̲a̲ d̲e̲ P̲a̲g̲o̲\n")
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
              comprobantef()  

              break
            elif ele == 2:
              
              
              def factura():
                  fechaHoy = datetime.now()
                  print("Fecha: ", fechaHoy.date())
                  
                  print("\nF̲a̲c̲t̲u̲r̲a̲ d̲e̲ P̲a̲g̲o̲\n")
                  listausers() 
                  print('{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}'.format("Nombre del producto", "Cantidad", "Precio Unidad", "SubTotal", "IGV", "Total"))
                  
                  for d in detalle:
                      
                      print('{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}'.format
                            (d, detalle[d]["Cantidad"], detalle[d]["Precio"], detalle[d]["SubTotal"], detalle[d]["IGV"], detalle[d]["Importe"]
                            ))
                    
                    
              factura() 
              comprobante()      
              break   
            else:
                print('Ingrese una opción valida Por favor')
                exit(0)
      