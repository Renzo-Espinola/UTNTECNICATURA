# Ejercicio 4: sumar numeros pares dentro de un rango
# Hacer un programa para sumar numeros pares denntro
# de un rango, por ejemplo
numRangoInf = int(input(" Digite un numero de rango inferior "))
numRangoMax = int(input(" Digite un numero de rango maximo "))
lista = list(range(numRangoInf,numRangoMax+1))
acumulador = 0
for i in lista:
    if i % 2 == 0:
        acumulador = acumulador + i

print(f"La suma de numeros pares en el rango {numRangoInf}-{numRangoMax}= {acumulador}")
