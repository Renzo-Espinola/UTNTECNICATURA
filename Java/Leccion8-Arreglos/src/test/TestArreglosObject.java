package test;

import domain.Persona;

public class TestArreglosObject {
    public static void main(String[] args) {
        Persona persona[] = new Persona[3];
        persona[0]= new Persona("Renzo");
        persona[1]=new Persona("Athena");
        persona[2]= new Persona("Tatiana");
        System.out.println("persona[0] = " + persona[0]);
        System.out.println("persona[1] = " + persona[1]);
        System.out.println("persona[2] = " + persona[2]);
    }
}
