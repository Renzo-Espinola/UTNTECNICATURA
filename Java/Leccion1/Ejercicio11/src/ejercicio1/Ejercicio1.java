package ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double n1=0;
        double n2=0;
        double n3=0;
        System.out.print("Ingrese la notas del alumno en escala de 1-100: ");
        n1 = Double.parseDouble(leer.nextLine());
        n2 = Double.parseDouble(leer.nextLine());
        n3 = Double.parseDouble(leer.nextLine());
        double promedio = (n1+n2+n3)/3;
        if (promedio >= 70){
            System.out.println("El alumno esta aprobado con "+promedio);
        }else{
            System.out.println("El alumno esta desaprobado con "+promedio);}
    }

}
