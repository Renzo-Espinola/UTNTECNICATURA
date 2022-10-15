package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        //variables locales
        int a =10;// variables locales
        int b =7;//MEMORIA STACK
        miMetodo();//llamamos al metodo nuevo
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
        //System.gc();
        Persona persona = new Persona("Ariel","Bentancoud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre:"+persona.nombre);
        System.out.println("Persona apellido:"+persona.apellido);
    }
    //
    public static void miMetodo(){
        //int a=10;
        System.out.println("Aqui hay otro metodo");
    }
}
class Persona{
    String nombre;
    String apellido;
    Persona (String nombre, String apellido) {//Constructor
        super();//llamada al constructor de la clase padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto Persona usando this: " + this);
    }

}
class Imprimir{
    public Imprimir(){
        super();
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+ this);
    }
}
