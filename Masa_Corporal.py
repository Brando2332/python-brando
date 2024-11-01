
peso = float(input("Ingresa el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

IMC = peso / (altura ** 2)

print(f"Tu indice de masa corporal es de: {round(IMC, 3)}")

if IMC < 18.5:
    print("tienes peso insuficiente")
elif IMC >= 18.5 and IMC < 24.9:
    print("tienes un peso saludable")    
elif IMC >= 24.9 and IMC < 29.9:
    print("tienes sobrepeso")        
elif IMC >= 30:
    print("tienes obesidad")        