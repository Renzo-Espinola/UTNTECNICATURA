package ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        double n1=0;
        double n2=0;
        double resultado=0;
        Scanner leer = new Scanner(System.in);
        System.out.print("Digite 2 numeros: ");
        n1 = Double.parseDouble(leer.nextLine());
        n2 = Double.parseDouble(leer.nextLine());
        if (n1 == n2) {
            resultado = (n1*n2);
        }else if (n1 > n2){
            resultado = (n1 - n2);
        }else{
            resultado = (n1 + n2);}
        System.out.println("El resultado es: "+resultado);
    }
}
