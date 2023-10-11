package br.com.fiap.banco.view;

import java.sql.Connection;

import br.com.fiap.banco.dao.ProdutoDao;
import br.com.fiap.banco.factory.ConnectionFactory;
import br.com.fiap.banco.model.Produto;

public class TesteAtualizar {
    public static void main(String[] args) {
        Produto produto = new Produto(5, "Caminhao", 1, 1, 300);
        Connection conn = null;
        try {
            conn = ConnectionFactory.getConnection();
            ProdutoDao dao = new ProdutoDao(conn);
            dao.atualizar(produto);
            System.out.println("Atualizado!");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

    }
}
