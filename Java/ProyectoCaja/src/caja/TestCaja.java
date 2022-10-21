package caja;

public class TestCaja {
    public static void main(String[] args) {
        int medidaAncho=10;
        int medidaAlto = 5;
        int medidaProf = 8;

        Caja caja = new Caja();
        caja.alto=medidaAlto;
        caja.ancho = medidaAncho;
        caja.profundo=medidaProf;

        int resultado = caja.calcularVolumen();

        System.out.println("resultado del calculo de volumen de caja = " + resultado);

        Caja caja1 = new Caja(5, 2, 3);

        System.out.println("calcular el volumen para caja1 = " + caja1.calcularVolumen());
    }
}
