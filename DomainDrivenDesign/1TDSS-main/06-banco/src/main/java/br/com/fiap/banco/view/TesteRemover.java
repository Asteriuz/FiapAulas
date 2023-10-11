package br.com.fiap.banco.view;

import java.sql.Connection;

import br.com.fiap.banco.dao.ProdutoDao;
import br.com.fiap.banco.factory.ConnectionFactory;

public class TesteRemover {
    public static void main(String[] args) {

        Connection conn = null;
        try {
            conn = ConnectionFactory.getConnection();
            ProdutoDao dao = new ProdutoDao(conn);
            dao.remover(5);
            System.out.println("Removido!");
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
