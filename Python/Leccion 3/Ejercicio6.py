# EJERCICIO 6
num2 = int(input("Ingrese c/Numeros: "))

pares = 0
impares = 0
contPares = 0
contImpares = 0

for i in range(num2):
    num3 = int(input("Ingrese un numero: "))
    if num3 % 2 == 0:
        pares += num3
        contPares += 1
    else:
        impares += num3
        contImpares += 1

print("Numeros pares: ", contPares, " suma: ", pares)
print("Promedio de impares: ", impares / contImpares)
