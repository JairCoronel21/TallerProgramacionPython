alumnos = {
    "1015125" : {"Nombre": "Juan Pérez Castro", "TR1": 15, "Foro": 14, "AutoEva1": 10, "AutoEva2": 12},
    "1015126" : {"Nombre": "Ana Chávez Pérez", "TR1": 15, "Foro": 14, "AutoEva1": 10,"AutoEva2": 15},
    "1015127" : {"Nombre": "Gabriel Santos Oliva", "TR1": 15, "Foro": 17, "AutoEva1": 18, "AutoEva2": 12},
    "1015128" : {"Nombre": "José Ramos Corone", "TR1": 15, "Foro": 14, "AutoEva1": 16, "AutoEva2": 15},
    "1015129" : {"Nombre": "Angel Vásquez Ramos ", "TR1": 15, "Foro": 16, "AutoEva1": 10, "AutoEva2": 0},

}
print(alumnos)

def promedio(alumnos, id):
    for id in alumnos:
        promedio = (alumnos[id].get("TR1") + alumnos[id].get("Foro") + alumnos[id].get("AutoEva1") + alumnos[id].get("AutoEva2") / 4)
    print(promedio)
promedio(alumnos, '1015129')