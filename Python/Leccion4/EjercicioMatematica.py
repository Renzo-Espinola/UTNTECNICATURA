import math
# Sacar la Raiz cuadrada de un numero positivo

# Ejercicio matematicas
# para sacar la raiz cuadrada de un numero

numero = int(input(" Digite un numero positivo "))
while numero < 0:
    print(f' Error -> Deberia ser un numero positivo {numero}')
    numero = int(input(" Digite un numero positivo "))
print(f'\nSu Raiz cuadrada es: {math.sqrt(numero):.2f}')