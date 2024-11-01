import datetime
print("calculadora de edad")

# sin datetime
""" dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
año_nacimiento = int(input("Ingresa el año de nacimiento: "))

dia_actual = int(input("Ingresa el dia de actual: "))
mes_actual = int(input("Ingresa el mes de actual: "))
año_actual = int(input("Ingresa el año de actual: "))
 
año_diferencia = año_actual - año_nacimiento

if mes_actual < mes_nacimiento:
    año_diferencia -= 1
elif mes_actual == mes_nacimiento:
    if dia_actual < dia_nacimiento:
        año_diferencia -= 1

edad = año_diferencia

print(f"tu edad es de: {edad} años") """

# con datetime 
dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
año_nacimiento = int(input("Ingresa el año de nacimiento: "))

dia_actual = datetime.datetime.now().day
mes_actual = datetime.datetime.now().month
año_actual = datetime.datetime.now().year
 
año_diferencia = año_actual - año_nacimiento

if mes_actual < mes_nacimiento:
    año_diferencia -= 1
elif mes_actual == mes_nacimiento:
    if dia_actual < dia_nacimiento:
        año_diferencia -= 1

edad = año_diferencia

print(f"tu edad es de: {edad} años")

# full datetime 
""" fecha_nacimiento = datetime.datetime.strptime(input("ingresa tu fecha de nacimiento (dd-mm-yyyy): "), "%d-%m-%Y").date()
fecha_actual = datetime.datetime.now().date()

edad = fecha_actual.year - fecha_nacimiento.year
diferencia_dias = (fecha_actual-fecha_nacimiento).days % 365

print(f"tu edad es de: {edad} años")
print(diferencia_dias) """