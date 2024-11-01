print("CALCULADORA DE PROPINA")

costo_total = float(input("Ingrese el costo total de la factura: "))
nivel_servicio = input("Ingrese el nivel del servicio (excelente, bueno, regular, malo, pesimo): ")

if nivel_servicio == "excelente":
    propina = 20
elif nivel_servicio == "bueno":
    propina = 15
elif nivel_servicio == "regular":
    propina = 10
elif nivel_servicio == "malo":
    propina = 5
elif nivel_servicio == "pesimo":
    propina = 0 

monto_propina = costo_total * (propina / 100)
monto_final = costo_total + monto_propina

print(f"la propina sera del {propina}%")
print(f"el monto de la propina sera de {monto_propina}")
print(f"el costo final con la propina sera de {monto_final}")