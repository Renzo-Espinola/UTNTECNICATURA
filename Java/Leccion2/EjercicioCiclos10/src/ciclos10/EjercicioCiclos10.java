package ciclos10;

import javax.swing.*;

public class EjercicioCiclos10 {
    public static void main(String[] args) {
        int numero, suma = 0;
        for(int i = 1; i<=10;i++){
            numero= Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            suma+=numero;
        }
        JOptionPane.showMessageDialog(null,"La suma total es: "+suma);
    }
}
