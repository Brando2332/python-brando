# Registro de ventas

# 1 agregar venta
# 2 lista ventas
# 3 mostrar promedio ventas
# 4 total ventas
# 5 venta mayor 
# 6 salir


ventas = []

def agregarVenta(venta):
    ventas.append(venta)

def listarVentas():
    """ print(f"han habido {len(ventas)} ventas")
    cont = 0
    for venta in ventas:
        cont += 1
        print(f"{cont}. {venta}") """

    for index, venta in enumerate(ventas):
        print(f"{index+1}. {venta}")


def promedioVentas():
    sumatoria = 0
    for venta in ventas:
        sumatoria += venta
    promedio = sumatoria / len(ventas)
    return promedio

def ventaMayor():
    """ venta_mayor = 0
    for venta in ventas:
        if venta > venta_mayor:
            venta_mayor = venta
    return venta_mayor """

    venta_mayor = max(ventas)
    return venta_mayor
    # return max(ventas)

def totalVentas():
    """ sumatoria = 0
    for venta in ventas:
        sumatoria += venta
    return sumatoria """

    sumatoria = sum(ventas) #identificar
    return(sumatoria)


while True:
    opcion = int(input("""
MENU REGISTRO DE VENTAS

[1] Agregar venta
[2] Lista ventas
[3] Mostrar promedio ventas
[4] Total ventas
[5] venta mayor 
[6] Salir
                    
"""))
    
    if opcion == 1:
        venta = float(input("ingrese el monto de la nueva venta: "))
        agregarVenta(venta)
    elif opcion == 2:
        listarVentas()
    elif opcion == 3:
        print(f"el promedio de ventas es: {promedioVentas()}")
    elif opcion == 4:
        print(f"el total de las ventas es: {totalVentas()}")
    elif opcion == 5:
        print(f"la venta mayor es: {ventaMayor()}")
    elif opcion == 6:
        break

