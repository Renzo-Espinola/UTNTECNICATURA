package ciclos04;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio04 {
    public static void main(String[] args) {

        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        int contador = 0;
        while (numero >= 0) {
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        }
        JOptionPane.showMessageDialog(null,"La cantidad de numeros ingresados son: "+contador);
    }
}