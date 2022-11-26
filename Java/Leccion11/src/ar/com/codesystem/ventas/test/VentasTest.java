package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.Orden;
import ar.com.codesystem.ventas.Producto;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon",9500.00);
        Producto producto2 = new Producto("Campera",29000.00);
        Producto producto3 = new Producto("Camisas",9800.00);
        Producto producto4 = new Producto("Remeras",9000.00);
        Producto producto5 = new Producto("Ropa interior",6500.00);
        Producto producto6 = new Producto("Medias",200.00);
        Producto producto7 = new Producto("Musculosa",3800.00);
        Producto producto8 = new Producto("Gorra",5000.00);
        Producto producto9 = new Producto("Anteojos de sol",10800.00);
        Producto producto10 = new Producto("Bermuda",6000.00);

        Orden orden1 =new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);
        orden1.mostrarOrden();
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto10);
        orden2.mostrarOrden();
        //Tarea:
        //Crear mas objetos de tipo producto = 10
        //Crear mas objetos de tipo Orden =2
    }
}
