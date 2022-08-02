from datos.datos import alumnos as alu

aprobados = {}
desaprobados = {}


# Añadir estudiantes--
def añadir():
    n = (input('Ingrese ID para crear:'))
    no = input("Ingrese nombre: ")
    tr1 = (input('Ingrese nota del TR1:'))
    foro = (input('Ingrese nota del foro:'))
    a1 = (input('Ingrese nota del la AutoEvaluación 1:'))
    a2 = (input('Ingrese nota del la AutoEvaluación 2:'))
    alu[n] = {"Nombre": no, "TR1": tr1, "Foro": foro, "AutoEva1": a1, "AutoEva2": a2}

# Eliminar estudiantes--

def eliminar():
    n = (input('Ingrese ID del que desea eliminar:'))
    alu.pop(n)


# Ver lista de estudiantes--
def lista():
    print("***************LISTA DE ALUMNOS*************************************")
    print("{:<10}{:<30}{:<15}{:<20}{:<20}{:<20}".format("ID", "Nombre", "TR1", "Foro", "AutoEva1", "AutoEva2"))
    for a in alu:
        print("{:<10}{:<30}{:<15}{:<20}{:<20}{:<20}".format(a, alu[a].get("Nombre"), alu[a].get("TR1"), alu[a].get("Foro"), alu[a].get("AutoEva1"), alu[a].get("AutoEva2")))
    print('======================================================')


def promedio(alu, id):
    id = input ('ingrese el codigo del estudiante: ')
    for id in alu:
        promedio = (alu[id].get("TR1") + alu[id].get("Foro") + alu[id].get("AutoEva1") + alu[id].get("AutoEva2") / 4)
    print(promedio)
promedio(alu, id)


