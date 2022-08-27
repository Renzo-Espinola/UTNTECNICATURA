package ejercicio7;


import java.util.Scanner;

public class Ejercicio7 {
    private static final int SALARIO=1000;
    public static void main(String[] args) {
        //Definimos las variables y la inicializamos en 0
        int cantCarros=0;
        double porcenVenta=0;
        double precioCarro=0;
        double salarioPagar=0;
        double comision =0;
        //Se solicita que el usuario ingrese los datos
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite cantidad de carros vendidos: ");
        cantCarros= Integer.parseInt(entrada.nextLine());
        System.out.print("Digite el precio del carro: $");
        precioCarro=Double.parseDouble(entrada.nextLine());
        //realizo los los calculos para poder determinar el sueldo a pagar
        comision=cantCarros>0?cantCarros*150:0;
        porcenVenta=(precioCarro>0?((precioCarro*5)/100):0);
        porcenVenta=porcenVenta*(cantCarros>0?cantCarros:0);
        salarioPagar=SALARIO+porcenVenta+comision;
        //Muestro por pantalla el sueldo basico,la bonificacion, la comision y el salario a pagar
        System.out.println("Sueldo Basico           : $"+SALARIO);
        System.out.println("Bonificacion por ventas : $"+porcenVenta);
        System.out.println("Comision cant. Ventas   : $"+comision);
        System.out.println("El salario a pagar es de: $"+salarioPagar);
    }
}
