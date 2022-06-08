package Ejercicio_4;

import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var num1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite otro numero: ");
        var num2 = Integer.parseInt(entrada.nextLine());
        System.out.println(num1>num2?"El mayor es: "+num1:"El mayor es: "+num2);
    }
}
