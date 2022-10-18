class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')


    @property #decorador
    def nombre(self):# metodo getter
        print("Estamos utilizando el get nombre")
        return self._nombre

    @property  # decorador
    def apellido(self):  # metodo getter
        print("Estamos utilizando el get apellido")
        return self._apellido

    @property  # decorador
    def edad(self):  # metodo getter
        print("Estamos utilizando el get edad")
        return self._edad

    @nombre.setter
    def nombre(self, nombre): #Metodo setter
        print("Estamos utilizando el metodo set")
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):  # Metodo setter
        print("Estamos utilizando el metodo set de edad")
        self._edad = edad

    @apellido.setter
    def apellido(self, apellido):  # Metodo setter
        print("Estamos utilizando el metodo set apellido")
        self._apellido = apellido


persona1 = Persona2("Renzo", "Espinola", 35)

#persona1._nombre#NO SE DEBE HACER
print(persona1.nombre)# Llamamos al metodo getter
print(persona1.apellido)
print(persona1.edad)
persona1.nombre = "Tatiana Tamara"
print(persona1.nombre)
print(persona1.mostrar_detalles())
# Atributo read-only seria la dedad poque no tiene el metodo set
print(persona1.edad)

# Tarea crear tres objetos mas utilizando los metodos getter and setter
# para modificar y mostrar los cambios
print("Objeto N°1")
persona3 = Persona2("Ariel", "Betancud", 40)
persona3.mostrar_detalles()
persona3.nombre = "Agustin"
persona3.apellido = "Romero"
persona3.edad = 50
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)

print("Objeto N° 2")
persona4 = Persona2("Gustavo", "TOmassi", 50)
persona4.mostrar_detalles()
persona4.nombre = "Gus"
persona4.apellido = "Gomez"
persona4.edad = 22
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)

print("Objeto N° 3")
persona5 = Persona2("Espinola", "Athena", 34)
persona5.mostrar_detalles()
persona5.nombre = "Gimenez"
persona5.apellido = "Rios"
persona5.edad = 45
print(persona5.nombre)
print(persona5.apellido)
print(persona5.edad)

