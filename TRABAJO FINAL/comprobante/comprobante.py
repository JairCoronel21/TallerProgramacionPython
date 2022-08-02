from datos.datos import productos as prod, Nombre, Precio


detalle = {}

def comprobantef():
      total = sum(col["Importe"] for col in detalle.values())
      print("-" * 72)
      print("{:<20}{:<15}{:<10}{:<0}".format("", "Total a Pagar", "", total))
      print()
      print("**Muchas Gracias!!! Vuelva Pronto")
       
                   

def comprobante():
    total = sum(col["Importe"] for col in detalle.values())
    totaligv = sum(col["IGV"] for col in detalle.values())
    totalsub = sum(col["SubTotal"] for col in detalle.values())
    print("-" * 72)
    print("{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}".format("","","", "IGV", "S/", totaligv))
    print("{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}".format("","","", "SUB TOTAL", "S/", totalsub))
    print("{:<25}{:<20}{:<20}{:<20}{:<10}{:<15}".format("","","", "TOTAL A PAGAR", "S/", total))
    print()
    print("**Muchas Gracias!!! Vuelva Pronto")
   
   

    
    

  
    