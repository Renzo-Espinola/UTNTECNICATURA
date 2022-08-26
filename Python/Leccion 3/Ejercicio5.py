# EJERCICIO 5
num = int(input("Digite un numero: "))

if num >= 0:
    contador = 1
    factorial = 1
    while contador <= num:
        factorial = factorial * contador
        contador += 1
    print(f"El Factorial de {num} es: {factorial}")
else:
    print("No se puede calcular el factorial")
