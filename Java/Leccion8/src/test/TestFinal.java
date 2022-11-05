/*
Uso de la palabra FInal
Esta palabra tiene diferentes significados dependiendo donde se aplique:
    Variables: Evita cambiar el valor que almacena la variable
    metodos: evita que se modifique la definicion o el comportamiento de un meotdo desde una subclase(hija)
    clases: evita que se creen clases hijas
   otra caracteristica es qque normalmente cuando trabajamos con variables se combina con el modifgicador de acceso
   estatico para convertir su valor, el ejemplo de esto es la clase math en la cual todos sus atributos son de tipo static
   y final es por esto que la varibale pi* se conoce como una constante.
 */
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni=33074277;
        System.out.println("miDni = " + miDni);
        //miDni=20312321;
        // Persona.CONSTANTE_AQUI = 9; No se modifica
        System.out.println("Atributo constante"+Persona.CONSTANTE_AQUI);
        final Persona persona1=new Persona();
        //persona1 = new persona(); No se puee asignar una referencia
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1.getNombre() = " + persona1.getNombre());
        persona1.setNombre("Renzo Espinola");
        System.out.println("persona1.getNombre() = " + persona1.getNombre());
        //para un objeto final no se puede hacer una nueva referencia, pero
        //si podemos modificar sus atributos
    }
}
