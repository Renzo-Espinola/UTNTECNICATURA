package test;
import dominio.*;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo",57000,false);
        persona1.setNombre("Juan Ignacion");
        //persona1.nombre="Juan ignacio; ya no se puede utilizar"
        //System.out.println("persona1.nombre = " + persona1.nombre); errror
        System.out.println("persona 1 con su nombre modificado es: " + persona1.getNombre());
        System.out.println("persona1 su sueldo es: "+persona1.getSueldo());
        System.out.println("persona1.isEliminado() = " + persona1.isEliminado());
        //Tarea: crear otro objeto de tipo Persona, asignar valores de manear inicial
        // e imprimir luego modificar sus valroes y volver a imprimir
    }
}
