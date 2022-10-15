class Persona: # Creamos una clase
    def __init__(self,nombre,apellido,edad): # se lo llama metodo Init dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1=Persona('Renzo','Espinola',34) # necesitamos enviar argumentos
print(type(Persona))
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es:  {persona1.edad}')
persona2 = Persona('Tatiana','Gimenez Rios',34)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es:  {persona2.edad}')

persona1.nombre = 'Athena'
persona1.apellido = 'Espinola'
persona1.edad = 6

print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es:  {persona1.edad}')

# Los atributos son las caracteristicas
# Los metodos son el comportamiento que van a tener los objetos (acciones)

