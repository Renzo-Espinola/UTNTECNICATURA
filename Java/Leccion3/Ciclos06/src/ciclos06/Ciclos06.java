package ciclos06;

import java.util.Scanner;

public class Ciclos06 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese un numero distinto de 0");
        var numero=Integer.parseInt(scanner.nextLine());
        var acumulador=0;
        while(numero!=0){
            acumulador+=numero;
            System.out.println("Ingrese un numero distinto de 0");
            numero=Integer.parseInt(scanner.nextLine());
        }
        /*
        do{
            System.out.println("Digite un numero");
            numero=Integer.parseInt(scanner.nextLine());
            suma+=numero;
        }while(numero!=0)
         */
        System.out.println("La suma total es: "+acumulador);
    }
}
