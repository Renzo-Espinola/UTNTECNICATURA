# Ejercicio 2 Modificar los elementos de una lista
# Llenar una lista con los numeros 1 al 10,
#elementos de la lista multiplicacindolos por un valor ingresado por el usuario

lista =  list(range(1,11))
for i in lista:
    print(i,end='-')

numero = int(input(" Digite un numero "))
for indice, i  in enumerate(lista):
    lista[indice] *= numero

print(f' Lista final con los elementos multiplicados por {numero}')

for i in lista:
    print(i, end='-')

