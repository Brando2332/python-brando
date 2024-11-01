operacion = input("ingrese el tipo de operacion: ")

if(operacion == "suma" or operacion == "+"):
    num1 = int(input("ingresa un numero: "))
    num2 = int(input("ingresa un numero: "))
    print(num1+num2)
elif(operacion == "resta" or operacion ==  "-"):
    num1 = int(input("ingresa un numero: "))
    num2 = int(input("ingresa un numero: "))
    print(num1-num2)
elif(operacion == "multiplicacion" or operacion ==  "*"):
    num1 = int(input("ingresa un numero: "))
    num2 = int(input("ingresa un numero: "))
    print(num1*num2)
elif(operacion == "division" or operacion ==  "/"):
    num1 = int(input("ingresa un numero: "))
    num2 = int(input("ingresa un numero: "))
    print(num1/num2)
else:
    print("operador invalido")
