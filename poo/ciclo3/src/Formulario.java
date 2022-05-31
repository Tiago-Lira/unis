import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Formulario {
    private JPanel painel;
    private JTextField campoAltura;
    private JTextField campoPeso;
    private String titulo = "Calculo do IMC";

    private class FormularioInvalidoException extends RuntimeException {
        public FormularioInvalidoException(String mensagem) {
            super(mensagem);
        }
    }

    public Formulario() {
        this.campoAltura = new JTextField(5);
        this.campoPeso = new JTextField(5);
        this.painel = new JPanel();
        painel.add(new JLabel("Altura (cm):"));
        painel.add(this.campoAltura);
        painel.add(new JLabel("Peso (kg):"));
        painel.add(this.campoPeso);
    }

    public void mostrar() {
        int acao = JOptionPane.showConfirmDialog(
                null,
                painel,
                this.titulo,
                JOptionPane.OK_CANCEL_OPTION);

        if (acao == JOptionPane.OK_OPTION) {
            try {
                Pessoa pessoa = this.criarPessoa();
                String mensagem = "O seu IMC é: " + pessoa.calcularImc() + " (" + pessoa.getSituacao() + ")";
                JOptionPane.showMessageDialog(null, mensagem);
            } catch (FormularioInvalidoException e) {
                String mensagem = e.getMessage();
                JOptionPane.showMessageDialog(null, mensagem);
                this.mostrar();
            }
        }
    }

    private Pessoa criarPessoa() throws FormularioInvalidoException {
        Pessoa pessoa;
        Integer altura;
        Float peso;

        try {
            altura = Integer.parseInt(this.campoAltura.getText());
        } catch (java.lang.NumberFormatException e) {
            throw new FormularioInvalidoException("Altura precisa ser um número.");
        }

        try {
            peso = Float.parseFloat(this.campoPeso.getText());
        } catch (java.lang.NumberFormatException e) {
            throw new FormularioInvalidoException("Peso precisa ser um número.");
        }

        if (altura <= 0) {
            throw new FormularioInvalidoException("Altura precisa ser maior que zero.");
        }

        if (peso <= 0) {
            throw new FormularioInvalidoException("Peso precisa ser maior que zero.");
        }

        pessoa = new Pessoa(altura, peso);

        return pessoa;
    }
}
