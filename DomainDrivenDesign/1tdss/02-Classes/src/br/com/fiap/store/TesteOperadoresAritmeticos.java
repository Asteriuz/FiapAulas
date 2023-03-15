package br.com.fiap.store;

import java.util.Scanner;

public class TesteOperadoresAritmeticos {
    public static void main(String[] args) {
        // 3 checkpoints 20%, Challenge 20%, Global Solution 60%
        Scanner sc = new Scanner(System.in);
        double checkpoint1 = sc.nextDouble();
        double checkpoint2 = sc.nextDouble();
        double checkpoint3 = sc.nextDouble();
        double challenge = sc.nextDouble();
        double globalSolution = sc.nextDouble();

        double checkpointMedia = (checkpoint1 + checkpoint2 + checkpoint3) / 3;
        double total = (checkpointMedia * 20) + (challenge * 20) + (globalSolution * 60);
        double totalMedia = total/100;
        System.out.println(totalMedia);
        sc.close();
    }
}
