package ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        int numero = Integer.parseInt(scanner.nextLine());
        int contador = 0;
        while (numero >= 0) {
            contador++;
            System.out.println("Ingrese un numero: ");
            numero = Integer.parseInt(scanner.nextLine());
        }
        System.out.println("La cantidad de numeros ingresados son: "+contador);
    }
}