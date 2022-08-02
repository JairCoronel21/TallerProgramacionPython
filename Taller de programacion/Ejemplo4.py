# Diccionario
usuario1 = {"Nombre": "jperez", "Password": "123456", "Estado": 1}
usuario2 = {"Nombre": "ccastro", "Password": "abc", "Estado": 0}

# Diccionario
usuarios = {
    "jperez": {"Password": "123456", "Estado": 1},
    "ccastro": {"Password": "abc", "Estado": 0},
    "agarcia": {"Password": "123abc", "Estado": 1},
}

# Recorrer diccionario
for user in usuarios:
    print("Clave:", user)

for user in usuarios.items():
    print("Items:", user)

# Obtener valores de uan clave


# Recorriendo la coleccion de la clave con FOR
print("Recorrer valores de uan clave")
for user in usuarios["jperez"].values():
    print("Valores:", user)

# Usando el metodo get
print("Obtener valores de una clave con metodo get")
print("Valores de jperez: ", usuarios.get("jperez"))
print("Password de jperez: ", usuarios.get("jperez").get("Password"))
print("Password de jperez: ", usuarios.get("jperez").get("Estado"))
