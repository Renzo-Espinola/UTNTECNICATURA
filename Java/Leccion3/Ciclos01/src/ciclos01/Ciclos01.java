package ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero,cuadrado;
        System.out.println("Ingrese un numero o para salir un numero negativo: ");
        numero= Integer.parseInt(scanner.nextLine());
        while (numero>=0){
            cuadrado = (int)Math.pow(numero,2);
            System.out.println("Su numero: "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Vuelva a ingresar numero o para salir un numero negativo: ");
            numero = Integer.parseInt(scanner.nextLine());
        }
        System.out.println("FIN");
    }
}
