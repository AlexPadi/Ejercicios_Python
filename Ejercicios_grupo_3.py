import math
#Ejercicio 3
print("----------------------------------------------------------")
print("Calculadora del área de un triángulo")
base = float(input("Ingrese la base del Triangulo: "))
altura = float(input("Ingrese la altura del Triangulo: "))
area = (base*altura)/2

print("El area del triangulo es", area)

#Ejercicio 7
#Hacer un programa para resolver una ecuación de segundo grado mediante la fórmula.
#Considerar todos los posibles casos.
print("----------------------------------------------------------")
print("Calculadora de ecuaciones de segundo grado")
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

x1 = (b*(-1)+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
x2 = (b*(-1)-math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
print("El resultado es:")
print("x1 = ",x1)
print("x2 = ",x2)

#Ejercicio 8
#Calcular la suma de dos vectores
vector1 = []
vector2 = []
print("----------------------------------------------------------")
print("Suma de 2 vectores")
n = int(input("Ingrese el número de elementos en los vectores: "))

for i in range(n):
    elemento = float(input("Ingrese el elemento "+ str(i+1) + " del vector 1: "))
    vector1.append(elemento)

for i in range(n):
    elemento = float(input("Ingrese el elemento "+ str(i+1) + " del vector 2: "))
    vector2.append(elemento)

suma = []
for i in range(n):
    suma.append(vector1[i] + vector2[i])

print("La suma de los vectores es:", suma)