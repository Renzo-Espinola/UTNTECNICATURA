package ciclos03;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio03 {
    public static void main(String[] args) {
        var num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (num != 0) {
            JOptionPane.showMessageDialog(null, num % 2 == 0 ? "ES PAR" : "ES IMPAR");
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        JOptionPane.showMessageDialog(null, "FIN");
    }
}