# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolvera la misma frase pero sin espacios en blanco
# ademas un contador de cuantos caracteres tiene la frase
# (sin contar lso espacios en blanco)
# Ejemplo: frase = vivir por siempre en paz
#          frase final = vivirporsiempreenpaz
#          N° de caracteres = 20

frase = input("Ingrese la frase: ")
fraseLimpia = frase.replace(" ","")
print(f"\nFrase Final: {fraseLimpia}")
print(f"N° de caracteres= {len(fraseLimpia)}")