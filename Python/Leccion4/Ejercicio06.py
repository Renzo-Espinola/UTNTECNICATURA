# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. por Ejemplo:
# si digita el 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50

numero = int(input("Ingrese un numero: "))
lista = []
for i in (range(1,11)):
        lista.append(i*numero)

print(f"La tabla de multiplicar del numero {numero} es: \n {lista}")

for indice,r in enumerate(lista):
    print(f'{numero} X {indice+1} = {lista[indice]}')