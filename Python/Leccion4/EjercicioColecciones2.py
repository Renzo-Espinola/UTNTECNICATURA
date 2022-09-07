# Ejercicio 2 Operaciones con conjuntos de listas
# Escriba un programa que tenga 2 listas y que a continuacion
# cree las siguientes listas (en las que no deben haber repeticion)
# 1 lista de palabras que apararecen en las listas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas
lista1 = ['toyota','fiat','renault','ford','ford','quilmes','1870','sneider']
lista2 = ['quilmes','brahama','sneider','1870','heineken','ford','renault','quilmes']
#punto 1
print(f'lista 1 {list(set(lista1))}')
print(f'lista 2 {list(set(lista2))}')
#punto 2
print(f'lista 1 sin elementos de lista 2 {list(set(lista1+lista2)-(set(lista2)))}')
#punto 3
print(f'lista 2 sin elementos de lista 1 {list(set(lista1+lista2)-(set(lista1)))}')
#punto 4
print (f'lista 1 y 2 concatenadas {list((set(lista1)&set(lista2)))}')

# resuelto profe
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union=list(conjunto1|conjunto2)
solo1=list(conjunto1-conjunto2)
solo2=list(conjunto2-conjunto1)
interseccion= list(conjunto1&conjunto2)
print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"lista de palabras que aparecen en la primer lista, pero no en la segunda: {solo1}")
print(f"lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}")
print(f"lista de palabras que aparecen en ambas listas: {interseccion}")
