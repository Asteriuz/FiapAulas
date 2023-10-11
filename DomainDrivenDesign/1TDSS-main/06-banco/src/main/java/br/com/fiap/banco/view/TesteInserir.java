package br.com.fiap.banco.view;

import java.sql.Connection;
import java.sql.SQLException;

import br.com.fiap.banco.dao.ProdutoDao;
import br.com.fiap.banco.factory.ConnectionFactory;
import br.com.fiap.banco.model.Produto;

//View
public class TesteInserir {

	public static void main(String[] args) {

		// Instanciar um produto (a ideia é que o usuário informe os dados)
		Produto produto = new Produto(5, "Caminhao", 1, 200000, 300000);

		// Instanciar o objeto que é capaz de realizar as ações no banco de dados

		// Gravar no banco
		Connection conn = null;
		try {
			conn = ConnectionFactory.getConnection();
			ProdutoDao dao = new ProdutoDao(conn);
			dao.cadastrar(produto);
			System.out.println("Gravado!");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
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