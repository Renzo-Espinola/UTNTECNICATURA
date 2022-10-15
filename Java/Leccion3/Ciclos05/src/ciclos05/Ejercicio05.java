package ciclos05;

import javax.swing.*;
import java.util.Random;
import java.util.Scanner;

public class Ejercicio05 {
    public static void main(String[] args) {
        Random generadorAleatorios = new Random();
        var contador=0;
        var numeroAleatorio= generadorAleatorios.nextInt(100);

        JOptionPane.showMessageDialog(null,"Bienvenido a mi juego de adivinanza de numero");
        var numeroSolicitado= Integer.parseInt(JOptionPane.showInputDialog(("Ingrese un numero")));
        while (numeroSolicitado>100 || numeroSolicitado<0){
            numeroSolicitado=Integer.parseInt(JOptionPane.showInputDialog(("ERROR en el ingreso!! Adivine el numero entre 1 y el 100")));
        }
        while (numeroSolicitado!=numeroAleatorio){
            contador+=1;
            numeroSolicitado= Integer.parseInt(JOptionPane.showInputDialog((numeroSolicitado < numeroAleatorio?
                    "Es MAYOR vuelva a ingresar un numero: ":"Es MENOR vuelva a ingresar un numero: ")));
        }
        JOptionPane.showMessageDialog(null,"  __^__                                                      __^__"+
                "\n ( ___ )------------------------------------------( ___ )"+
                "\n   | / |                                                                | | |"+
                "\n   | / |    HA ACERTADO FELICIDADES!!!!   | | |"+
                "\n   |___|   El numero " + numeroSolicitado + " es el ganador     |___|"+
                "\n   |___|    NUMERO DE INTENTOS: " + contador + "        |___|"+
                "\n (_____)----------------------------------------(_____)");

        }

    }
