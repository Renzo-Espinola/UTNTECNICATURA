package ciclos05;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Random generadorAleatorios = new Random();
        var contador=0;
        var numeroAleatorio= generadorAleatorios.nextInt(100);
        Scanner scanner= new Scanner(System.in);
        System.out.println("Bienvenido a mi juego de adivinanza de numero");
        System.out.println("Ingrese un numero");
        var numeroSolicitado=Integer.parseInt(scanner.nextLine());
        while (numeroSolicitado>100 || numeroSolicitado<0){
            System.out.println("ERROR en el ingreso!! Adivine el numero entre 1 y el 100");
            numeroSolicitado=Integer.parseInt(scanner.nextLine());
        }
        while (numeroSolicitado!=numeroAleatorio){
            contador+=1;
            System.out.println(numeroSolicitado < numeroAleatorio?"Es MAYOR vuelva a ingresar un numero: ":"Es MENOR vuelva a ingresar un numero: ");
            numeroSolicitado=Integer.parseInt(scanner.nextLine());
        }
        System.out.println("  __^__                                           __^__");
        System.out.println(" ( ___ )--------------------------s---------------( ___ )");
        for (String s : Arrays.asList("  | / |                                           | | |",
                "  | / |    HA ACERTADO FELICIDADES!!!!            | | |",
                "  |___|   El numero " + numeroSolicitado + " es el ganador              |___|",
                "  |___|    NUMERO DE INTENTOS: " + contador + "                  |___|",
                " (_____)-----------------------------------------(_____)")) {
            System.out.println(s);
        }

    }
}
