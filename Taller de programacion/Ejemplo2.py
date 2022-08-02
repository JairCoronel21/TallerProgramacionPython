# funciones y colecciones
# Coleccion => diccionario

factura = {"SubTotal": 1271, "IGV": 228, "Total": 1499}
print("Imprimir valores del diccionario - factura.values()")
for i in factura.values():
    print(i)
    
print("Imprimir llaves y valores del diccionario - factura.items()")
for k, v in factura.items():
    print("Llave: ", k, "Values: ", v)
    
print("Imprimir Diccionario Factura") 
for k, v in factura.items():
    print('{:<10}{:<0}'.format(k,v))   

def Generarfactura(Total):
    SubTotal = round((Total / 1.18), 2)
    IGV = round((Total - SubTotal), 2)
    factura = [SubTotal, IGV, Total]
    return factura

print("Usando funcion GenerarFactura")
print(Generarfactura(1500))


def Generarfacturav2(Total):
    SubTotal = round((Total / 1.18), 2)
    IGV = round((Total - SubTotal), 2)
    factura = {"subTotal": SubTotal, "IGV": IGV, "Total": Total}
    return factura

print("Usando Generarfacturav2")
factura = Generarfacturav2(1500)
for k, v in factura.items():
    print("{:<10}{:<0}".format(k, v))
    
    
importes = [240, 250, 152, 120]
timportes = sum(importes)
print("Usnado funcion Generarfacturav2 para calcular Importe y SubTotal")
factura = Generarfacturav2(timportes)
for k, v in factura.items():
    print("{:<10}{:<0}".format(k, v))
    
    

def Generarfacturav3(importes):
    Total = sum(importes)
    SubTotal = round((Total / 1.18), 2)
    IGV = round((Total - SubTotal), 2)
    factura = {"subTotal": SubTotal, "IGV": IGV, "Total": Total}
    return factura
    


print("Usnado funcion Generarfacturav3 para calcular Importe y SubTotal de la lista")
imp = [240, 250, 152, 120]
factura = Generarfacturav3(imp)
for k, v in factura.items():
    print("{:<10}{:<0}".format(k, v))

    







