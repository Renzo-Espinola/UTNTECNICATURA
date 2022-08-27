#lista = ariel, liliana, natalia, osvaldo

nombres = ['Naty','Osvaldo','Lily','Ariel']

print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2])#Solo muestra el indice 0,1 pero no el indice 2
print(nombres[ :3])#Solo muestra el indice 0 en adelatnte
print(nombres[1: ])#Solo muestra desde el indice hasta el final

#Modificar un valor dentro de la lista

nombres[2] = 'Liliana'
print(nombres)
#Iterar una lista
for nombre in nombres: #nombre es singular la lista plural
    print(nombre)
else:
    print("Se acabaron los elemnteos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) #le pasamos como parametro la lista

# Agregamos un elemnto
nombres.append('Marcelo')
print(nombres)

# Insertar un nuevo elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)
# Eleminamos un elemento
nombres.remove('Alberto')
print(nombres)
# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminamos un indice especifico
del nombres[2] #del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos

nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
#print(nombres)

#tuplas
cocina = ('cuchara','cuchillo','tenedor')
print(cocina)
print(len(cocina))
# Acceder a un elemento para esto utilizamons corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])
# Acceder a un rango
print(cocina[0:2])
# Ejemplo
verduras = ('papa',) # una tupla necesita aunque sea un elemnte la coma
# de lo contrario solo seria un tipo  str cadena

# recorremos los elementos de la tupla
for cocinar in cocina: # Print esta usando  /n par saltos de lineas
    print(cocinar,end=' ') # Usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n',cocina)


del cocina
"""print(cocina)"""

