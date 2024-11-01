# lista de ejercicios

# calcular area triangulo

def calcularAreaTriangulo(b, a):
    area = (b * a) / 2 
    return f"el area del triangulo es de: {area}"

base = float(input("ingrese la base del triangulo: "))
altura = float(input("ingrese la altura del triangulo: "))

area = calcularAreaTriangulo(base, altura)
print(area)

area1 = calcularAreaTriangulo(30, 15)
print(area1)

area2 = calcularAreaTriangulo(6, 20)
print(area2)

