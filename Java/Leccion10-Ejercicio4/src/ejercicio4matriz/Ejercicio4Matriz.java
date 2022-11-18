package ejercicio4matriz;

public class Ejercicio4Matriz {
    public static void main(String[] args) {
        int matriz[][] = new int[7][7];
        System.out.println("Rellenar Matriz");
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                if(i==j){
                    matriz[i][j]=1;
                }else
                    matriz[i][j]=0;
            }
        }
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.print(matriz[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }
}
