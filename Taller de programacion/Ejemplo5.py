# Definir una funcion que valide el nombre de usuario
# Ejemplo de listados

productos = {
	"P0001" : {"Nombre": "TV Samsung", "Precio": 150, "Stock": 10},
    "P0002" : {"Nombre": "TV Samsung", "Precio": 200, "Stock": 25},
    "P0003" : {"Nombre": "TV Samsung", "Precio": 180, "Stock": 5},
 
}

# Saber si un producto existe
print("P0001" in productos)
print("P0022" in productos)

# Obtener datos de un producto que existe
print("Nombre:", productos.get("P0001").get("Nombre"))
print("Precio:", productos.get("P0001").get("Precio"))
print("Stock:", productos.get("P0001").get("Stock"))

lprod = []
lprecio = []
lcant = []
limporte = []

pre = productos.get("P0001").get("Precio")
can = 1
imp = float(pre) * float(can)
lprod.append(productos.get("P0001").get("Nombre"))
lprecio.append(pre)
lcant.append(imp)
limporte.append(imp)
print(lprod)
print(lprecio)
print(lcant)
print(limporte)