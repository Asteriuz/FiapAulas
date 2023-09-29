package br.com.fiap.banco.view;

import br.com.fiap.banco.dao.ProdutoDao;
import br.com.fiap.banco.model.Produto;

public class TesteAtualizar {
    public static void main(String[] args) {
        Produto produto = new Produto(5, "Caminhao", 1, 1, 300);
        ProdutoDao dao = new ProdutoDao();

        try {
            dao.atualizar(produto);
            System.out.println("Atualizado!");
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
