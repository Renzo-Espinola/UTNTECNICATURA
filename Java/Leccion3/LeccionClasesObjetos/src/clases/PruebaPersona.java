package clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1= new Persona();//llamamos al constructor
        persona1.nombre = "Renzo";
        persona1.apellido= "Espinola";// el valor hexadecimal normalmente comienza con 0x
        persona1.obtenerInformacion();
        Persona persona2 = new Persona();
        System.out.println("persona2: "+persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre="Osvaldo";
        persona2.apellido="Giordanini";
        persona2.obtenerInformacion();
    }
}
