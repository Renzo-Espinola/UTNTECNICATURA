# Ejercicio 5: Factorial de un numero positivo
# HAcer un programa para calcular el factorial de un numero positivo
numero = int(input(" Digite un numero "))

while numero < 0:
    print(f"Error el numero ingresado es negativo")
    numero = int(input(" Digite un numero "))
factorial = 1
for i in range(1,numero+1):
    factorial*=i


print(f"Factorial de {numero} es: {factorial}")