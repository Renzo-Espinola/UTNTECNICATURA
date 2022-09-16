package clases;

public class Persona {
    String nombre;
    String apellido;
    Persona(){}
    public void obtenerInformacion() {
        System.out.println("Nombre: "+ nombre);
        System.out.println("Apellido: "+apellido);
    }
}
