package clases;

public class Persona {
    public String nombre;
    public String apellido;
    public Persona(){}
    public void obtenerInformacion() {
        System.out.println("Nombre: "+ nombre);
        System.out.println("Apellido: "+apellido);
    }
}
