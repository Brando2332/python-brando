numero = int(input("ingresa un numero: "))
numero2 = numero
factorial = 1
while(numero >= 1):
    factorial *= numero
    numero = numero - 1
print(f"el factorial de {numero2} es {factorial}")    
