package veiculo;

public class Cor {
    private String nome;
    private int r;
    private int g;
    private int b;

    public void alterarCor(int r, int g, int b, String nome) {
        this.r = r;
        this.g = g;
        this.b = b;
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public int getR() {
        return r;
    }

    public int getG() {
        return g;
    }

    public int getB() {
        return b;
    }

}
