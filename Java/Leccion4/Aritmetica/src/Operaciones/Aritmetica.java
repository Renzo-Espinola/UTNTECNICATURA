package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;

    //constructor es un metodo especial
    public Aritmetica(){
        System.out.println("Se esta ejecutando este constructor numero uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a,int b){
        this.a=a;
        this.b=b;
        System.out.println("Se esta ejecutando el constructor numero 2");
    }


    //Metodos
    public void sumaNumeros(){
        int resultado= a + b;
        System.out.println("resultado = " + resultado);
    }
    public int sumarConRetorno(){
        //int resultado= a +b;
        return a+b;
    }
    public int sumarConArgumentos(int a,int b){

        //this.a=arg1;//el argumento a se asigna al atributo this.a
        //this.b=arg2;
        this.a=a;//el argumento a se asigna al atributo this.a
        this.b=b;
        //return a+b;
        return sumarConRetorno();
    }
}
