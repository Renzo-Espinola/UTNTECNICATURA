# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostrar la lista

# creamos la lista

marcas = ['toyota','fiat','renault','ford','ford',1,1,2,3]
# conjunto = set(marcas) # convertimos la lista a un conjunto de tipo set
# marcas = list(conjunto)
print(list(set(marcas))) # la conversion hecha en una sola linea de codigo (eficiente)