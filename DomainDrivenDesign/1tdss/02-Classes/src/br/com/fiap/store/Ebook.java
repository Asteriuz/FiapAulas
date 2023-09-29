package br.com.fiap.store;

import java.util.List;

public class Ebook {

	private String nome;
	Boolean admin = false;
	private String isbn;
	private List<String> genero;
	private String idioma;
	private int quantidadePagina;
	private double valor;
	private String resumo;
	private double rating;
	private Editora editora;

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		if (admin) {
		nome = nome.toUpperCase();}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
		this.nome = nome;
	}

	public String getIsbn() {
		return isbn;
	}

	public void setIsbn(String isbn) {
		if (admin) {
		this.isbn = isbn;}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
	}

	public List<String> getGenero() {
		return genero;
	}

	public void setGenero(List<String> genero) {
		if (admin) {
		this.genero = genero;}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
	}

	public String getIdioma() {
		return idioma;
	}

	public void setIdioma(String idioma) {
		if (admin) {
		this.idioma = idioma;}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
	}

	public int getQuantidadePagina() {
		return quantidadePagina;
	}

	public void setQuantidadePagina(int quantidadePagina) {
		if (admin) {
		this.quantidadePagina = quantidadePagina;}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
	}

	public double getValor() {
		return valor;
	}

	public void setValor(double valor) {
		if (admin) {
		this.valor = valor;}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
	}

	public String getResumo() {
		return resumo;
	}

	public void setResumo(String resumo) {
		if (admin) {
		this.resumo = resumo;}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
	}

	public double getRating() {
		return rating;
	}

	public void setRating(double rating) {
		if (admin) {
		this.rating = rating;}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
	}

	public Editora getEditora() {
		return editora;
	}

	public void setEditora(Editora editora) {
		if (admin) {
		this.editora = editora;}
		else {
			System.out.println("Você não tem permissão pra realizar isso");
		}
	}

}