miVariable = 3
print(miVariable)
miVariable = "Hola a todos los Estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# las literales se escriben x528, la variable y = x272, la variable z= x592
print(id(y))
print(id(z))
# Las variables en python son dinamicas pueden adoptar diferentes tipos
a = "Hola Alumnos"
print(type(a))
a = 10.78
print(type(a))
b = True
print(type(b))
b = False
print(type(b))
# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola ALumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))
# Manejo de cadenas
miGrupoFavorito = "Ramones: "
caracteristicas = " The best Punk Rock Band"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))
# Tipos Booleano
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("EL Resultado es Verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# funcion input
# resultado = input("Digite un numero: ") # regresa un dato de tipo string

# Conversion de la entrada de datos
numero3 = int(input("Escribe el primer numero: "))
numero4 = int(input("Escribe el segundo numero: "))
resultado2 = numero3 + numero4

print("El resultado es: ", resultado2)
