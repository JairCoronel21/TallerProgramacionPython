# Diccionario de datos
datos = {
    "10101010": {
        "Nombre": "Juan Perez",
        "Direccion": "Lima",
        "Telefono": "99589589",
        "Sueldo": 1500,
    },
    "15124578": {
        "Nombre": "Ana Perez",
        "Direccion": "Lima",
        "Telefono": "895896963",
        "Sueldo": 1800,
    },
    "12457845": {
        "Nombre": "Juan Castro",
        "Direccion": "San Luis",
        "Telefono": "874521258",
        "Sueldo": 1600,
    },
    "23562356": {
        "Nombre": "Perla Gomez",
        "Direccion": "San Luis",
        "Telefono": "896654444",
        "Sueldo": 2500,
    },
}

print(datos)

'''
CREAR LAS SIFGUIENTES FUNCIONES:

01 - Funcion que permita mostrar la lista de Personas que viven en un determiando distrito
02 - Funcion que muestre los datos de una persona segun su DNI.
03 - Modifique la funcion indicada en el punto 02, de tal manera que muestre un error si se ingresa un
     un Nro de Dni que no existe en el diccionario
04 - Funcion que permita indicar si una persona existe o no en el diccionario. (Se debe ingresar el DNI)
05 - Crear una funcion que permita saber la cantidad de personas que viven en un determnado distrito
'''

# Funcion 01
def distrito(datos, dis):
    lista = lista()
    for x in datos.values():
        if x["Direccion"] == dis:
            lista.append(x["Nombre"])
            
    print(lista)
distrito(datos, "San Luis")





# Funcion 02

dni = input('Ingrese el numero de dni: ')

  
def VistaDatosPorDni(dni):
    print("Nombre: ", datos.get(dni).get("Nombre"))
    print("Direccion: ", datos.get(dni).get("Direccion"))
    print("Telefono: ", datos.get(dni).get("Telefono"))
    print("Sueldo: ", datos.get(dni).get("Sueldo"))
    
print(VistaDatosPorDni(dni))




# Funcion 03
def segundni(datos, dni):
    if dni in datos:
        print(f'Dni: {dni}')
        print(f'Nombre: {datos[dni]["Nombre"]}')
        print(f'Direccion: {datos[dni]["Direccion"]}')
        print(f'Telefono: {datos[dni]["Telefono"]}')
        print(f'Sueldo: {datos[dni]["Sueldo"]}')
    else:
        print("No existis")
        
segundni(datos, "")
 

# Funcion 05

def cantidaddistrito(datos, dis):
    p = 0
    dis = dis.title()
    for x in datos.values():
        if x["Direccion"] == dis:
            p = p+1 
            
    print(f"La cantidad de usuarios registrados que viven en {dis} es: {p}" )
    
cantidaddistrito(datos, "Lima")
    
   