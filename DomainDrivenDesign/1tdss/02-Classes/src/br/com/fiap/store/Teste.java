package br.com.fiap.store;

import java.util.List;

public class Teste {

	//Criar o m�todo que come�a a execucao do programa Java
	//main -> CTRL + espa�o
	public static void main(String[] args) {
		
		//Criar um objeto do tipo Editora (instanciar a classe)
		Editora churros = new Editora();
		//Colocar informa��es dentro do objeto
		churros.nome = "Editora Abril";
		churros.endereco = "Marginal Tiete";
		churros.cnpj = "132.131.323/0001-12";
		
		//Criar um outro objeto do tipo Editora
		Editora atlas =new Editora();
		//Colocar informa��es dentro do objeto
		atlas.cnpj = "456.545.123/0001-54";
		atlas.nome = "Editora Atlas";
		atlas.endereco = "Av Aclimação";
		
		//Criar um objeto do tipo Ebook
		Ebook supremacyGames = new Ebook();
		//Colocar informa��es dentro do objeto
		supremacyGames.nome = "Supremacy Games";
		supremacyGames.isbn = "12345";
		supremacyGames.genero = List.of("REINCARNATION", "EVOLUTION", "CULTIVATION", "COMEDY", "ACTION", "RAREBLOODLINE", "ROMANCE");
		supremacyGames.idioma = "Inglês";
		supremacyGames.quantidadePagina = 27_408;
		supremacyGames.valor = 0.0;
		supremacyGames.resumo = "Felix Maxwell was destined to be a loser, born on one of the weakest races and on the least favorable of situations, he was forced to face adversity head-on as he traveled across the vast universe where dangers laid in every corner, one day traveling in hopes of riches he stumbled upon a ruin where a supreme being laid imprisoned, in a stroke of bad luck the being laid its eyes on him and tried to take over his body, forcing itself upon him.";
		supremacyGames.editora = atlas;
		
		
		System.out.println(churros.nome);

		System.out.println(supremacyGames.nome);
		
		System.out.println(supremacyGames.valor);
		System.out.println(supremacyGames.editora);
		
	}
}