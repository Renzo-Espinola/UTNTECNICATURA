package test;

import domain.Cliente;
import domain.Empleado;

import javax.swing.event.CaretListener;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado = new Empleado();
        System.out.println("empleado = " + empleado);
        Empleado empleado1 = new Empleado("Ariel",57000);
        System.out.println("Empleado1: "+empleado1);
//        Date fecha1= new Date();
//        Cliente cliente1 = new Cliente(fecha1, true, "Renzo", 'F', 32, "9 de Julio 1413");
//        System.out.println("cliente1 = " + cliente1);
//
//        Persona persona1 = new Persona();
    }
}
