# Comenzamos con Funciones

# Definimos una funcion
def mi_funcion():
    print('Saludos a todos los alumnos de la tecnicatura')

mi_funcion()# Estamos llamando a la funcion
mi_funcion()# Se puede llamar a una funcion N cantidad de veces

# Desempaquetado de listas o list unpacking
def show(name,lastName):
    print(name+" "+lastName)

person = ["Renzo","Espinola"]
show(person[0],person[1]) # pasamos uno a uno los datods de la lista a la funcion
show(*person) # esto es lo mismo que lo anterior pero le pasamos todo junto

person2 = ["Tatiana","Gimenez"]
show(*person2)
person3 = {"lastName":"Lucero","name":"Natalia"}
show(**person3)

# Repaso ciclo FOR ELSE
numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    if n == 3:
        break # Unica manera que no entre al else
else:
    print("Esto se termina")

numbers2 = []
for n in numbers2:
    print(n)
else:
    print("Esto se termina number2")

# List comprehension, lista de comprension

names = ["Paolo","Rodrigo","lupe","Pepe"]
alongP = [p for p in names if p[0] == "P"] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name":"Quilmes", "Country":"Arg"},
           {"name":"Corona", "Country":"Mx"},
           {"name":"Stella", "Country":"Belgium"}]
Arg = [b for b in bottleC if b["Country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funcioens)
def mi_funcion2(name,lastName):
    print("Saludos a todos los que ven a traves del canal de youtube")
    print(f"Nombre:{name}, Apellido: {lastName}")
mi_funcion2("Jorge","lucero")
mi_funcion2("Ariel","Betancud")
mi_funcion2("Analia","Pedrosa")

# LA palabra return
# Creamos una funcion para sumar
def sumar(a,b):
    return  a + b
resultado= sumar(78,232)
print(f"el resultado de la suma es: {resultado}")
print(f"el resultado de la suma es: {sumar(55,45)}")

# Damos un valor por default
def sumar2(a = 0,b = 0):
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22,66)}")
#def sumar2(a:int = 0,b:int = 0) -> int: redundancia

#Argumentos, variables en funciones
def listarNombres(*nombres): # de esta manera desconocemos la cantidad de argumentos normalmet se utilizar. *args
    for nombre in nombres:
        print(nombre)

listarNombres("renzo","jose","Tatiana","Athena","tigresin")
listarNombres("Marcos","daniel","juan","carlos")