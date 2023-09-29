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
		supremacyGames.admin = true;
		//Colocar informa��es dentro do objeto
		supremacyGames.setNome("Supremacy Games");;
		supremacyGames.setIsbn("12345");
		supremacyGames.setGenero(List.of("REINCARNATION", "EVOLUTION", "CULTIVATION", "COMEDY", "ACTION", "RAREBLOODLINE", "ROMANCE"));
		supremacyGames.setIdioma("Inglês");
		supremacyGames.setQuantidadePagina(27_408);
		supremacyGames.setValor(0.0);
		supremacyGames.setResumo("Felix Maxwell was destined to be a loser, born on one of the weakest races and on the least favorable of situations, he was forced to face adversity head-on as he traveled across the vast universe where dangers laid in every corner, one day traveling in hopes of riches he stumbled upon a ruin where a supreme being laid imprisoned, in a stroke of bad luck the being laid its eyes on him and tried to take over his body, forcing itself upon him.");
		supremacyGames.setEditora(atlas);
		
		System.out.println(supremacyGames.getNome());
		System.out.println(supremacyGames.getIsbn());
		System.out.println(supremacyGames.getGenero());
		System.out.println(supremacyGames.getIdioma());
		System.out.println(supremacyGames.getQuantidadePagina());
		System.out.println(supremacyGames.getValor());
		System.out.println(supremacyGames.getResumo());
		System.out.println(supremacyGames.getEditora());
	}
}