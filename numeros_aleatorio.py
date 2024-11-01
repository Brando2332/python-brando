import random
aleatorio = random.randint(0,100)
adivinanza = -1
intentos = 0
while(adivinanza != aleatorio and intentos < 10):
    intentos += 1
    adivinanza = int(input("adivina el numero: "))
    if(adivinanza > aleatorio):
        print("fallaste, el numero es Menor")
    elif(adivinanza < aleatorio):
        print("fallaste, el numero es Mayor")
    else:
        print(f"lo adivinaste en {intentos} intentos")
    if(intentos==10):
        print("Perdiste, no adivinaste el numero")