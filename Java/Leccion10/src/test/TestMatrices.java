package test;

import domain.Persona;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int [3][2];
        System.out.println("Edades="+edades);
        edades[0][0]=5;
        edades[0][1]=7;
        edades[1][0]=8;
        edades[1][1]=4;
        edades[2][0]=10;
        edades[2][1]=11;
        System.out.println("edades[0][0] = " + edades[0][0]);
        System.out.println("edades[0][1] = " + edades[0][1]);
        System.out.println("edades[1][0] = " + edades[1][0]);
        System.out.println("edades[1][1] = " + edades[1][1]);
        System.out.println("edades[2][0] = " + edades[2][0]);
        System.out.println("edades[2][1] = " + edades[2][1]);

        for (int fila=0;fila< edades.length;fila++){
            for (int col=0;col< edades[fila].length;col++){
                System.out.println("EDADES "+fila+"-"+col+": "+edades[fila][col]);
            }
        }
        //Sintaxis Clasica
        //String frutas[][]= new String[3][2];
        //Sintaxis simplificada
        String frutas[][]={{"Limon","Naranja"},{"Ciruela","Kiwi"},{"Manzana","Banana"}};
        for (int i=0;i< frutas.length;i++){
            for (int j=0;j< frutas[i].length;j++){
                System.out.println("FRUTAS "+i+"-"+j+": "+frutas[i][j]);
            }
        }
        //Creamos una matriz de Objetos
        Persona personas[][]= new Persona[2][3];
        //Signamos valores a la matriz
        personas[0][0]=new Persona("Renzo");
        personas[0][1]=new Persona("Osvaldo");
        personas[0][2]=new Persona("Tatiana");
        personas[1][0]=new Persona("Athena");
        personas[1][1]=new Persona("Raul");
        personas[1][2]=new Persona("Tigresin");
        imprimir(personas);
    }
    public static void imprimir(Object matriz[][]){
        for (int i=0;i< matriz.length;i++){
            for (int j=0;j< matriz[i].length;j++){
                System.out.println("Personas "+i+"-"+j+": "+matriz[i][j]);
            }
        }
    }
}
