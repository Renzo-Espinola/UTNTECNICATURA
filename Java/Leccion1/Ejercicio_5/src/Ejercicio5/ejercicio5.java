package Ejercicio5;

import java.util.Scanner;

public class ejercicio5 {
    public static void main(String[] args) {
        double nota1=0;
        double nota2=0;
        double nota3=0;
        double suma=0;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite las nota 1");
        nota1=Double.parseDouble(entrada.nextLine());
        System.out.println("Digite las nota 2");
        nota2=Double.parseDouble(entrada.nextLine());
        System.out.println("Digite las nota 3");
        nota3=Double.parseDouble(entrada.nextLine());
        suma = nota1+nota2+nota3;
        System.out.println("La suma de las notas som: "+suma);
    }
}
