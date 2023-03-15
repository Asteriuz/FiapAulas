package br.com.fiap.store;

public class Editora {
	
	String nome;
	
	String cnpj;
	
	String endereco;

	// @Override
	public String toString(){
		return "Nome: " + this.nome + "\n" + "Cnpj: " + this.cnpj + "\n" + "Endereço: " + this.endereco;
	}
}