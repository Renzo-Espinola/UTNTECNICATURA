package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        //variables locales
        int a =10;
        int b =7;//MEMORIA STACK
        miMetodo();
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a=3;
        aritmetica1.b=7;

        aritmetica1.sumaNumeros();
        //PAra almacenar un objeto  o los atributos se utiliza la memoria HEAP
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado=aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado = " + resultado);

        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b );
        Aritmetica aritmetica2 = new Aritmetica(2,3);
        System.out.println("aritmetica2.a = " + aritmetica2.a);
        System.out.println("aritmetica2.b = " + aritmetica2.b);
        //GARBAGE COLLECTOR:
        System.gc();
    }

    public static void miMetodo(){
        //int a=10;
        System.out.println("Aqui hay otro metodo");
    }
}
