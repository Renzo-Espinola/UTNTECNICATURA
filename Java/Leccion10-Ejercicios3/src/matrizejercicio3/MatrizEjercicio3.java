package matrizejercicio3;

import java.util.Scanner;

public class MatrizEjercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int[3][3];
        System.out.println("Rellenar Matriz");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("Matriz[" + i + "][" + j + "]" + "");
                matriz[i][j] = entrada.nextInt();
            }
        }
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    System.out.print(matriz[j][i]+" ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }

