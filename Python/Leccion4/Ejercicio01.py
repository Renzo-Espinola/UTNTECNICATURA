# Ejercicio 1: llenar una lista
# LLenar una lista con los numeros del 1 al 50, luego mostrar
# la lista con el bucle for, los elementos deben mostrarse
# de la siguiente forma
lista = []

# i = 1
# while i <= 50:
#     lista.append(i)
#     i += 1

lista =  list(range(1,51))
for i in lista:
    print(i, end='-')

