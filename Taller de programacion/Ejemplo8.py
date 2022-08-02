# Data de Productos que se venden
productos = {
    "P0001": {"Nombre": "Tv Sansung", "Precio": 1500, "Stock": 10},
    "P0002": {"Nombre": "Tv LG", "Precio": 2000, "Stock": 25},
    "P0003": {"Nombre": "Tv Sony", "Precio": 1800, "Stock": 5},
    "P0004": {"Nombre": "Tv Phillips", "Precio": 1900, "Stock": 15},
}

# Proceso de Venta

# Crear la Coleccion detalle de compra => Listado de lo productos comprados por el cliente
# Nombre del Producto, Precio, Cantidad, Importe
detalle = {}

rp = "si"
while rp.lower() == "si":
    # Solicitar al usuario codigo de producto y cantidad a comprar
    codp = input("Ingrese codigo de Producto: ")
    canp = input("Ingrese cantidad de unidades a comprar:")
    # Calcular Importe => Precio * Cantidad
    imp = productos[codp].get("Precio") * int(canp)

    # Añadir la compra la detalle
    nombrep = productos[codp].get("Nombre")
    preciop = productos[codp].get("Precio")
    detalle.setdefault(nombrep, {"Precio": preciop, "Cantidad": canp, "Importe": imp})
    rp = input("¿Desea continuar comprando? (SI/NO): ")
    
    
# Formatear la salida del comprobante de Pago
print("\n ************** Comprobante de Pago ******************************* \n")
print("{:<20}{:<15}{:<10}{:<0}".format("Producto", "Precio", "Canitdad", "Importe"))
print("-" * 52)
for d in detalle:
    print(
        "{:<20}{:<15}{:<10}{:<0}".format(
            d, detalle[d]["Precio"], detalle[d]["Cantidad"], detalle[d]["Importe"]
        )
    )
    
# Total a Pagar
total = sum(col["Importe"] for col in detalle.values())
print("-" * 52)
print("{:<20}{:<15}{:<10}{:<0}".format("", "Total a Pagar", "", total))