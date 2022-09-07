#lista = ariel, liliana, natalia, osvaldo
# Colecciones en python
# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores
"""
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

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append([4,5])
nombres.append(7)
nombres.append(10.45)

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


# Tipo Set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas))
print('Jupiter' in planetas)
# Agregar un Elemento
planetas.add('Tierra')
print(planetas)
# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') # esta funcion puede arrojar error si no existe el elemento
print(planetas)
planetas.discard('Tierra') # Esta funcion no nos presenta ningun error 
print(planetas)
# Limpiar set
planetas.clear();
print(planetas)
# Eliminar set
del planetas
print(planetas)

# 'Maradona' : 10 un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'SIstema de administracion de base de datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)
# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])
# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))
#Modificamos elementos
diccionario['IDE']='Entorno de Desarrollo Integrado'
print(diccionario)
# Como Recorrer los elementos
for termino in diccionario:
    print(termino)
# Necesitamos una funcion para recorrer un diccionario
for termino,valor in diccionario.items():
    print(termino,valor)
# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # muestra solo las llaves
for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)
# Comprobar la existencia de algun elemento
print('IDE' in diccionario)# devuelve un boolean

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)
# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # el diccionario se borro

# Concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2 # concatenacion
print(lista3)
lista3.extend([7,8,9,1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) Esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista
# Para poner al reves una lista
lista3.reverse()
print(lista3)
# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)
# Metodos de ordenamiento,en python son funciones
lista3.sort() # Ordena los elementos  ascendentemente
print(lista3)
lista3.sort(reverse=True) # ORdena descendentemente
print(lista3)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'edad': 35, 'Altura': 1.70,'Precio': '50 millones','Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'edad': 34, 'Altura': 1.80,'Precio': '12 millones','Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'edad': 28, 'Altura': 1.77,'Precio': '35 millones','Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'edad': 34, 'Altura': 1.83,'Precio': '3.5 millones','Posicion': 'Defensa Central'},
    23:  {'Nombre': 'Franco Armani', 'edad': 35, 'Altura': 1.89,'Precio': '3.5 millones','Posicion': 'Portero'},
    27: {'Nombre': 'Julian Álvarez','edad': 22, 'Altura': 1.73, 'Precio': '23.000 de euros','Posicion': 'delantero'},
     5: {'Nombre': 'Leandro Paredes','edad': 28, 'Altura': 1.78, 'Precio': '7.000 millones de euros','Posicion': 'centrocampista'},
     4: {'Nombre': 'Gonzalo Montiel','edad':  25, 'Altura': 1.75, 'Precio': '14.000 millones de euros','Posicion': 'defensor'},
     1: {'Nombre': 'Emiliano Martinez','edad':  29, 'Altura': 1.95, 'Precio': '28.000 millones de euros','Posicion': 'arquero'}
}
print(seleccionArgentina)


for llave,valor in seleccionArgentina.items():
    print(llave,valor)
# Como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccion argentina
print('Tenemos cargados en el diccionario la cantidad de jugadores: ',end=' ')
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1,2,3]
# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)
# sacamos elementos desde el final
elementoBorrado = pila.pop()# quita el ultimo elemento y lo guarda en la variable
print(f'sacamos en elemento {elementoBorrado}')
print(f'la pila ahora quedo asi {pila}')
# Colas con listas Estructura de datos de tipo(FIFO)
cola =['Ariel','Osvaldo','liliana','Pilar']
# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)
# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido {seRetira}')
print(cola)
"""
# Recorremos el diccionario de la seleccion con un ciclo for
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'edad': 35, 'Altura': 1.70,'Precio': '50 millones','Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'edad': 34, 'Altura': 1.80,'Precio': '12 millones','Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'edad': 28, 'Altura': 1.77,'Precio': '35 millones','Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'edad': 34, 'Altura': 1.83,'Precio': '3.5 millones','Posicion': 'Defensa Central'},
    23:  {'Nombre': 'Franco Armani', 'edad': 35, 'Altura': 1.89,'Precio': '3.5 millones','Posicion': 'Portero'},
    27: {'Nombre': 'Julian Álvarez','edad': 22, 'Altura': 1.73, 'Precio': '23.000 de euros','Posicion': 'delantero'},
     5: {'Nombre': 'Leandro Paredes','edad': 28, 'Altura': 1.78, 'Precio': '7.000 millones de euros','Posicion': 'centrocampista'},
     4: {'Nombre': 'Gonzalo Montiel','edad':  25, 'Altura': 1.75, 'Precio': '14.000 millones de euros','Posicion': 'defensor'},
     1: {'Nombre': 'Emiliano Martinez','edad':  29, 'Altura': 1.95, 'Precio': '28.000 millones de euros','Posicion': 'arquero'}
}

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')

