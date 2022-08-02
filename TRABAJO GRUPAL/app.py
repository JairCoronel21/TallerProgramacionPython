from funciones.funciones import añadir, eliminar, lista


print("******Bienvenido a la base de datos*********")

print("Estimado Usuario..........")
print("=================================")
print("\t 1. Añadir alumnos")
print("\t 2. Eliminar alumnos")
print("\t 3. Ver lista de alumnos")
rp = "si"
while rp.lower() == "si":
    op = int(input("Elija la opcion que desee: "))
    if op == 1:
        añadir()
    elif op == 2:
        eliminar()
    elif op == 3:
        lista()
    else:
        print("Elija una opción correcta por favor")    
    rp = input("¿Desea continuar? (SI/NO): ")
    if rp.lower() == "no":
        print("Muchas Gracias Vuelva Pronto!!!")
        exit(0)
    

