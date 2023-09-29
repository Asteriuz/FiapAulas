package br.com.fiap.banco.view;

import br.com.fiap.banco.dao.ProdutoDao;

public class TesteRemover {
    public static void main(String[] args) {
        ProdutoDao dao = new ProdutoDao();

        try {
            dao.remover(5);
            System.out.println("Removido!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
