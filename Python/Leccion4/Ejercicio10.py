# Ejercicio 10: No repetir caracteres
# Haer un programa que pida una cadena por teclado luego meter los caracteres en una lista
# sin repetir caracteres

frase = input("Ingrese la frase: ")
caracter=0
lista=[]
for i in frase:
    if i not in lista: #si el caracter no esta en la lista
        lista.append(i)

print(f"Lista sin repetir caracteres: {lista}")