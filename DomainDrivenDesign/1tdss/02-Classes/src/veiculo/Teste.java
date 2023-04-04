package veiculo;

public class Teste {

    public static void main(String[] args) {
        Carro gol = new Carro();
        Aviao jumbo = new Aviao();
        Lancha cimitarra = new Lancha();

        Cor preto = new Cor();
        preto.alterarCor(0, 0, 0, "Preto");
        Cor branco = new Cor();
        branco.alterarCor(255, 255, 255, "Branco");
        Cor vermelho = new Cor();
        vermelho.alterarCor(255, 0, 0, "Vermelho");

        gol.setCor(branco);
        jumbo.setCor(preto);
        cimitarra.setCor(vermelho);

        System.out.println(gol.getCor().getNome());
        System.out.println(jumbo.getCor().getNome());
        System.out.println(cimitarra.getCor().getNome());
    
    }

}
