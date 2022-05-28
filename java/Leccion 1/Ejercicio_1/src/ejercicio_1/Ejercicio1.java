package ejercicio_1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        var entrada =  new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombre = entrada.nextLine();
        System.out.println("Digite el ID del libro: ");
        int id =Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro: ");
        double precio =Double.parseDouble(entrada.nextLine());
        System.out.println("Indique si el envio es gratuito (true/false): ");
        boolean envio =Boolean.parseBoolean(entrada.nextLine());
        System.out.println("**********************************************");
        System.out.println("Nombre: "+nombre);
        System.out.println("ID: "+ id);
        System.out.println("Precio: "+precio);
        if (envio) {
            System.out.println("Envio: Gratuito");
        }else {
            System.out.println("Envio: El envio no es Gratutito");
        }
    }
}
