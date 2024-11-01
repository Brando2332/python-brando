import math

print("\n - CALCULADORA DE INTERES COMPUESTO - \n")

monto = float(input("ingrese el monto de el prestamo inicial: "))
interes_mensual = float(input("ingrese el porcentaje de interes mensual: "))
tiempo_pago = int(input("ingrese el plazo de pago en meses: "))

monto_total = monto
contador = 0
while(tiempo_pago > contador):
    monto_total = monto_total + monto_total * interes_mensual / 100
    contador += 1
    monto_total = round(monto_total,2)

print(f"El monto total a pagar luego de los {tiempo_pago} meses es: {monto_total}")