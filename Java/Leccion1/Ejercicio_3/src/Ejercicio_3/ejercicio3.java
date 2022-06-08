package Ejercicio_3;

import java.util.Scanner;

public class ejercicio3 {
    public static void main(String[] args) {
        var entrada =  new Scanner(System.in);
        System.out.println("Digite el alto del rectangulo: ");
        var alto= Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el ancho del rectangulo: ");
        var ancho= Integer.parseInt(entrada.nextLine());
        var area = alto * ancho;
        var perimetro = (alto + ancho) *2;
        System.out.println("El area del rectangulo es: "+ area);
        System.out.println("El perimetro del rectangulo es: "+ perimetro);
    }

}
