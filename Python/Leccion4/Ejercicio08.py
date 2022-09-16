import random
# Ejercicio 8: Menu interactivo - Cajero automatico
# Hacer un programa que simule un caejero automatico con un saldo
# inicial de 1000 $ y tendra el sigueinte menu de opciones:
#           1. Ingresar dinero en la cuenta
#           2. Retirar dinero de la cuenta
#           3. Mostrar dinero disponible
#           4. Salir
cajaAhorro = random.randint(100000,999999)
saldo = 1000
monto = 0
opcion = int(
    input("1.Ingrese Dinero en la cuenta \n2.Retirar dinero de la cuenta \n3.Mostrar dinero disponible \n4.Salir "))
while 0 > opcion > 5:
    print("\nATENCION: Ingreso Erroneo!!!")
    opcion = int(
        input("\n1.Ingrese Dinero en la cuenta \n2.Retirar dinero de la cuenta \n3.Mostrar dinero disponible \n4.Salir"))

while opcion != 4:
    if opcion == 1:
        saldo += float(input(f"\nIngrese el monto de dinero a depositar de la caja de ahorro N° {cajaAhorro} $"))
    elif opcion == 2:
        monto = float(input(f"\nIngrese el monto de dinero a extraer de la caja de ahorro N° {cajaAhorro} $"))
        condicion = saldo-monto < 0
        if condicion:
            print(f"El saldo de la caja de ahorro N° {cajaAhorro} es insuficiente")
        else:
            saldo -= monto
            print(f"Se realizo con exito la extraccion de la caja N° {cajaAhorro}")
            print(f"\nSALDO CAJA DE AHORRO N° {cajaAhorro} $ {saldo}")
    elif opcion == 3:
        print(f"El saldo de la caja de ahorro N° {cajaAhorro} es: ${saldo}")
    opcion = int(
        input("\n1.Ingrese Dinero en la cuenta \n2.Retirar dinero de la cuenta \n3.Mostrar dinero disponible \n4.Salir "))

print("\nGracias por usar nuestros servicios")