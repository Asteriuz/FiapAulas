package br.com.fiap.store;

import java.util.Scanner;

public class TesteOperadoresAritmeticos {
    public static void main(String[] args) {
        // 3 checkpoints 20%, Challenge 20%, Global Solution 60%
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite a primeira nota do checkpoint: ");
        double checkpoint1 = sc.nextDouble();
        System.out.print("Digite a segunda nota do checkpoint: ");
        double checkpoint2 = sc.nextDouble();
        System.out.print("Digite a terceira nota do checkpoint: ");
        double checkpoint3 = sc.nextDouble();
        System.out.print("Digite a nota do desafio: ");
        double challenge = sc.nextDouble();
        System.out.print("Digite a nota da solução global: ");
        double globalSolution = sc.nextDouble();
        double checkpointMedia = (checkpoint1 + checkpoint2 + checkpoint3) / 3;
        double total = (checkpointMedia * 20) + (challenge * 20) + (globalSolution * 60);
        double totalMedia = total/100;
        System.out.print("A média final é: " + totalMedia);
        sc.close();
    }
}
