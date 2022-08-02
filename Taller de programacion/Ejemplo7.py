productos = {
	"P0001" : {"Nombre": "TV Samsung", "Precio": 1500, "Stock": 10},
    "P0002" : {"Nombre": "TV LG", "Precio": 2000, "Stock": 25},
    "P0003" : {"Nombre": "TV Sony", "Precio": 1800, "Stock": 5},
    "P0004" : {"Nombre": "TV Phillips", "Precio": 1900, "Stock": 15},
 
}


#Imprime por defecto las claves
for p in productos:
    print(p)

# Mostrar el Nombre del producto, Stock por Producto y Stock Total
for p in productos:
    print("{:<20}{:<0}".format(productos[p].get("Nombre"), productos[p].get("Stock")))
    
#Obtener los valores de una columna Stock 
Stock  = (col["Stock"] for col in productos.values())
for c in Stock:
    print(c)
    
#Sumar todos los valores de la columna Stock
Stock = sum(col["Stock"] for col in productos.values())
print("Total Stock: ", Stock)    
