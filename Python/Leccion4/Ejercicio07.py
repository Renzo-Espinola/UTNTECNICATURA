import random
# Ejercicio 7: Juego adivina el numero
# Realizar un juego para adivinar un numero. para ello se debe
# generar un numero aleatorio entre 1 - 100 y luego ir pidiendo
# numeros indicando "es mayor" o "es menor" segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostrar el numero de intentos


numeroAleatorio = random.randint(1,100)
cont = 0
print("              \|||/ ")
print("              (o o) ")
print("     ------ooO-(_)-Ooo------")
print("BIENVENIDO A MI JUEGO DE ADIVINANZA")
numeroSolicitado= int(input("\nAdivine el numero entre 1 y el 100: "))

while numeroSolicitado > 100 or numeroSolicitado < 1:
    numeroSolicitado = int(input("\nError en el ingreso!! Adivine el numero entre 1 y el 100: "))

while numeroSolicitado != numeroAleatorio:
    cont += 1
    condicion = numeroSolicitado < numeroAleatorio
    numeroSolicitado = int(input("Es MAYOR vuelva a ingresar un numero: " if (numeroSolicitado < numeroAleatorio) else "Es MENOR vuelva a ingresar un numero: "))


print("  __^__                                           __^__")
print(" ( ___ )-----------------------------------------( ___ )")
print("  | / |                                           | \ |")
print("  | / |    HA ACERTADO FELICIDADES!!!!            | \ |")
print(f"  |___|   El numero {numeroSolicitado} es el ganador              |___|")
print(f"  |___|    NUMERO DE INTENTOS: {cont}                  |___|")
print(f" (_____)-----------------------------------------(_____)")

