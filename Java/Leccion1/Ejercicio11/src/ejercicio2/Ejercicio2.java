package ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        double compra=0;
        double descuento=0;
        double pFinal=0;
        Scanner leer = new Scanner(System.in);
        System.out.print("Digite la cantidad a Pagar: $");
        compra =Double.parseDouble(leer.nextLine());
        if (compra > 100){
            descuento = (compra*0.2);
        }else{
            descuento = 0;}
        pFinal = (compra - descuento);
        System.out.println("El precio a final a pagar es: $ "+pFinal);

    }
}
