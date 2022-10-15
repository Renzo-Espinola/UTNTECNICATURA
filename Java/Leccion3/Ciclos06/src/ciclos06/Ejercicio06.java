package ciclos06;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio06 {
    public static void main(String[] args) {

        var numero=Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero distinto de 0"));
        var acumulador=0;
        while(numero!=0){
            acumulador+=numero;
            numero=Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero distinto de 0"));
        }
         /*
        do{
            System.out.println("Digite un numero");
            numero=Integer.parseInt(scanner.nextLine());
            suma+=numero;
        }while(numero!=0)
         */
        JOptionPane.showMessageDialog(null,"La suma total es: "+acumulador);
    }
}
