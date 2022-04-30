import javax.crypto.ShortBufferException;
import java.util.Scanner;

public class HolaMundo {



    public static void main(String[] args) {
        /*System.out.println("Hola mundo desde Java");
        int miVariable= 100;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        String miVariableCadena= "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena="Sigamos Creciendo en programacion";
        System.out.println(miVariableCadena);

        //clase 22/04
        //var : inferencia de tipos en java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos Estudiando";
        System.out.println("miVariableEntera2 = "+miVariableEntera2);
        System.out.println("miVariableCadena2 = "+miVariableCadena2);

        var usuario = "Osvaldo";
        var titulo1 = "Ingeniero";
        var union = titulo1 + " " + usuario;
        System.out.println("Union= "+ union);
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));

        //Ejercicio: Caracteres especiales con Java
        var nombre = "Natalia";
        System.out.println("\nNueva Linea: \n"+nombre);
        System.out.println("Tabulador: \t"+nombre);
        System.out.println("\t\t.:MENU:."+nombre);
        System.out.println("Retroceso: \b\b"+nombre);
        System.out.println("Comillas Simples: \'"+nombre+"\'");
        System.out.println("Comillas Dobles: \""+nombre+"\"");

        //Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2= entrada.nextLine();
        System.out.println("Usuario2= "+usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo3 = entrada.nextLine();
        System.out.println("Resultado: "+titulo3+" "+usuario2);

        //Ejercicio
        Scanner scanner = new Scanner(System.in);
        System.out.println("Proporiciona el titulo: ");
        String titulo= scanner.nextLine();
        System.out.println("Proporiciona el Autor: ");
        String autor= scanner.nextLine();
        System.out.println(titulo+" fue escrito por "+ autor);
    */
        //Clase 28/04
        byte numeroByte = 10;
        System.out.println("numero entero byte: "+numeroByte);
        System.out.println("El valor minimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("El valor maximo del Byte: "+ Byte.MAX_VALUE);

        short numeroEnteroShort= 32767;
        System.out.println("numEnteroShort: "+numeroEnteroShort);
        System.out.println("El valor minimo del Short: "+ Short.MIN_VALUE);
        System.out.println("El valor maximo del Short: "+ Short.MAX_VALUE);

        int numeroEnteroInt= 2147483647;
        System.out.println("numEnteroInt: "+ numeroEnteroInt);
        System.out.println("El valor minimo del Short: "+ Integer.MIN_VALUE);
        System.out.println("El valor maximo del Short: "+ Integer.MAX_VALUE);

        long numeroEnteroLong = 9223372036854775806L;
        System.out.println("numEnteroInt: " + numeroEnteroLong);
        System.out.println("El valor minimo del Short: " + Long.MIN_VALUE);
        System.out.println("El valor maximo del Short: " + Long.MAX_VALUE);

        float numFloat= 3.4028235E38F;
        System.out.println("numFloat: " + numFloat);
        System.out.println("El valor minimo del Float: " + Float.MIN_VALUE);
        System.out.println("El valor maximo del FLoat: " + Float.MAX_VALUE);

        double numDouble= 1.7976931348623157E308D;
        System.out.println("numFloat: " + numDouble);
        System.out.println("El valor minimo del Double: " + Double.MIN_VALUE);
        System.out.println("El valor maximo del Double: " + Double.MAX_VALUE);


    }


}

