package domain;

public class Empleado extends Persona{
    private int idEmpleado;
    private double sueldo;

    private static int contadorEmpleados;

    public Empleado() {
        this.idEmpleado = ++Empleado.contadorEmpleados;
    }

    public Empleado(String nombre, double sueldo) {
        //super(nombre);
        this();//Estamos llamando desde aqui al constructor vacio(llamar a un constructor)
        this.nombre=nombre;
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return idEmpleado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append('}');
        return sb.toString();
    }
}
