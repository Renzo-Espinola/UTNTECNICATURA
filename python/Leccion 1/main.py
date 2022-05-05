"""
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

# Ejercicio python 1

print("Califica tu Dia")
respuesta = (input("¿Cómo estuvo tu día (1 al 10)?"))
print("Mi día estuvo de:", respuesta)

# Ejercicio python 2

titulo = (input("Proporciona el título: "))
autor = (input("Proporciona el título: "))

print(titulo, " fue escrito por ", autor)

operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("El resultado de la suma es: ", suma)
print(f"El resultado de la suma {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")

division = operandoA // operandoB
print(f"El resultado de la division es: {division}")

modulo = operandoA % operandoB
print(f"El residuo de la division es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
"""
"""
alto = int(input("Proporciona el ancho del rectangulo: "))
ancho = int(input("Proporciona el alto del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f"Area: {area}")
print(f"perimetro: {perimetro}")
"""
"""
miVariable3 = 10
print(miVariable3)
# Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)
miVariable3 += 1
print(miVariable3)
miVariable3 -= 2
print(miVariable3)
miVariable3 *= 3
print(miVariable3)
miVariable3 /= 2
print(miVariable3)

# operadores de comparacion
d = 4
b = 2
resultado = d == b
print(resultado)
resultado = d != b
print(resultado)
resultado = d > b
print(resultado)
resultado = d <= b
print(resultado)
resultado = d >= b
print(resultado)
"""
"""
numero = int(input("Ingrese el numero: "))

if (numero % 2) == 0:
    print(True)
else:
    print(False)
"""
"""
numero = int(input("Ingrese la edad: "))

if numero >= 18:
    print(f"Eres mayor de edad {numero}")
else:
    print(f"Eres menor de edad {numero}")

# Operador AND Clase 04/05/2022
print("OPERADOR AND")
a = True
b = True
resultado = a and b
print(resultado)

a = False
b = True
resultado = a and b
print(resultado)

a = False
b = False
resultado = a and b
print(resultado)

# Operador OR
print("OPERADOR OR")
a = True
b = True
resultado = a or b
print(resultado)

a = False
b = True
resultado = a or b
print(resultado)

a = False
b = False
resultado = a and b
print(resultado)

# OPERADOR NOT
print("OPERADOR NOT es unario solo una variable")
a = False
resultado = not a
print(resultado)

a = True
resultado = not a
print(resultado)

# Ejercicio 1

num = int(input("Ingrese el valor: "))
if 0 <= num <= 5:
    print(f"El valor {num} esta dentro del rango")
else:
    print(f"El valor {num} se encuentra fuera del rango")

#Ejercicio 2

vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("Tiene Trabajo que hacer")

# Ejercicio 3 rango
edad = int(input("Cual es la edad de la persona? "))

if (edad >= 20 and edad <=29) or (edad >= 30 and edad <= 39):
    print(f"La edad {edad} esta dentro del rango")
else:
    print(f"El edad {edad} se encuentra fuera del rango")

veinte = edad > 19 and edad < 30
treinta = edad > 29 and edad < 40
if veinte or treinta:
    if veinte:
        print(f"La edad {edad} esta dentro del rango (20\'0)")
    elif treinta:
        print(f"El edad {edad} se encuentra fuera del rango (30\'0)")
    else:
        print(f"El edad {edad} se encuentra fuera del rango")

else:
    print(f"El edad {edad} se encuentra fuera del rango")

# Ejercicio 4
numero1 = int(input("Digite el valor para el numero1: "))
numero2 = int(input("Digite el valor para el numero2: "))
if numero1 > numero2:
    print(f"El numero mayor es: {numero1}")
else:
    print(f"El numero mayor es: {numero2}")
"""
# Ejercicio 5
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el preico del libro: "))
envio = bool(input("Indique si el envio es gratuito (True/False): "))
print(f"Nombre: {nombre}")
print(f"id: {id}")
print(f"precio: {precio}")
if envio:
    print("Envio: Gratuito")
else:
    print("Envio: No posee Envio Gratuito")