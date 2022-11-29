from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalle(objeto):
    # print(objeto)  # De manera indirecta estamos llamando al metood str de la clase empleado o gerente
    print(type(objeto))  # esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Renzo", 50000.00)
imprimir_detalle(empleado)

gerente = Gerente("Athena", 60000, "Sistemas")
imprimir_detalle(gerente)
