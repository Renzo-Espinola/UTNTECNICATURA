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
        //Tarea: crear otro objeto de tipo Persona, asignar valores de manera inicial
        // e imprimir luego modificar sus valroes y volver a imprimir
        Persona persona2 = new Persona("Tatiana",45000,false);
        System.out.println("persona 1 con su nombre modificado es: " + persona2.getNombre());
        System.out.println("persona1 su sueldo es: "+persona2.getSueldo());
        System.out.println("persona1 esta Eliminado? = " + persona2.isEliminado());
        persona2.setNombre("Athena");
        persona2.setSueldo(89000);
        persona2.setEliminado(true);
        System.out.println("persona 2 con su nombre modificado es: " + persona1.getNombre());
        System.out.println("persona 2 su sueldo es: "+persona1.getSueldo());
        System.out.println("persona 2  esta Eliminado? = " + persona1.isEliminado());
    }
}
