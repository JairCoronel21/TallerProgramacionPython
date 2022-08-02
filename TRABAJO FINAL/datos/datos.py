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

def Buscar(Codigo):
    valores = productos[Codigo].values()
    return valores

def Nombre(Codigo):
    nombre = productos[Codigo].get("Nombre")
    return nombre

def Precio(Codigo):
    nombre = productos[Codigo].get("Precio")
    return nombre

def Stock(Codigo):
    nombre = productos[Codigo].get("Stock")
    return nombre


def lista():
    print("******************************************************")
    print("░█▀▀█ █▀▀ █▀▀█ █──█ 　 ░█▀▀▄ █▀▀ █── ─▀─ ▀█─█▀ █▀▀ █▀▀█ █──█")
    print("░█▄▄█ █▀▀ █▄▄▀ █──█ 　 ░█─░█ █▀▀ █── ▀█▀ ─█▄█─ █▀▀ █▄▄▀ █▄▄█ ")
    print("░█─── ▀▀▀ ▀─▀▀ ─▀▀▀ 　 ░█▄▄▀ ▀▀▀ ▀▀▀ ▀▀▀ ──▀── ▀▀▀ ▀─▀▀ ▄▄▄█")
    print("========lista de productos en el catalogo==========")

    print("{:<10}{:<30}{:<15}{:<20}".format("Codigo", "Nombre", "Precio", "Stock"))
    for p in productos:
        print("{:<10}{:<30}{:0}{:<15}{:<20}".format(p, productos[p].get("Nombre"),"S/", productos[p].get("Precio"), productos[p].get("Stock")))
    print('======================================================')