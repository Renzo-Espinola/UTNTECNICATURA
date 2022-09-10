package ciclos03;

import java.util.Scanner;

public class Ciclo03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese un numero");
        var num = scanner.nextInt();
        while (num!=0){
            if(num % 2 == 0){
                System.out.println("ES PAR");
            }else {
                System.out.println("ES IMPAR");
            }
            System.out.println("Ingrese un numero");
            num = scanner.nextInt();
        }
        System.out.println("FIN");
    }
}
