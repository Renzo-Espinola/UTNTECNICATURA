class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property  # decorador
    def nombre(self):  # metodo getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo setter
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):  # Override sobrescribe
        return f'Persona: [Nombre: {self._nombre}, Edad: {self._edad}]'


class Empleado(Persona):  # Esta clase es hija de la clase persona
    def __init__(self, _nombre, _edad, sueldo):
        super().__init__(_nombre, _edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):  # Override sobrescribe
        return f'Empleado: [Sueldo: {self._sueldo}, Edad: {self._edad}]'


empleado1 = Empleado("Renzo", "Espinola", 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

empleado1.nombre = "Tatiana"
empleado1.edad = 34
empleado1.sueldo = 80000

print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
