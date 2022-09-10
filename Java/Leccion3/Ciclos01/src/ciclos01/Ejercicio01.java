package ciclos01;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio01 {
    public static void main(String[] args) {

        int numero,cuadrado;
        numero= Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero o para salir un numero negativo: "));
        while (numero>=0){
            cuadrado = (int)Math.pow(numero,2);
            JOptionPane.showMessageDialog(null,"Su numero: "+numero+" elevado al cuadrado es: "+cuadrado);
            numero =Integer.parseInt(JOptionPane.showInputDialog("Vuelva a ingresar numero o para salir un numero negativo: "));

        }
        JOptionPane.showMessageDialog(null,"FIN");
    }
}
