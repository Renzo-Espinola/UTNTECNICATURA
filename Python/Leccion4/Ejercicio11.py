# Ejercicio 11: Agenda Telefonica
# Hacer un programa uqe simule una agenda de contactos. crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendra el siguiente menu de opciones
contactos={}

while True:
    opcion = int(input("1. Nuevo contacto "
                       "\n2. Borrar contacto "
                       "\n3. Ver contactos existentes"
                       "\n4. Salir"))
    if opcion == 1:
        nombre=(input("\nIngrese el contacto nuevo: "))
        contactos[nombre]=(input("\nIngrese el telefono: "))
    elif opcion == 2:
        contactos.remove(input("\nIngrese el contacto a eliminar:"))
    elif opcion == 3:
        print(f"CONTACTOS \n{contactos}")
    elif opcion == 4:
        print("ADIOS")
        break
    else:
        print("Ingreso erroneo")

    # VERSION PROFESOR
agenda = {}
while True:
    print("Menu")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opcion del menu"))
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        telefono = input("Digite el numoer de telefono")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente")
        else:
            print("Ese nombre de contacto ya existe")
    elif opcion == 2:
        nombre = input("Digite el nombre del contacto: ")
        if nombre in agenda:
            del(agenda[nombre])
            print("Se ha eliminado el contacto requerido")
        else:
            print("Ese contacto no existe en la agenda")
    elif opcion == 3:
        print("AGENDA DE CONTACTOS")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos")
        break
    else:
        print("Se equivoco de opcion de menu")
    print()