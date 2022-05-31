public class Pessoa {
    private int alturaCm;
    private float pesoKg;

    public Pessoa(int alturaCm, float pesoKg) {
        this.alturaCm = alturaCm;
        this.pesoKg = pesoKg;
    }

    public float calcularImc() {
        float alturaM = this.alturaCm / 100.0f;
        return this.pesoKg / (alturaM * alturaM);
    }

    public String getSituacao() {
        float imc = this.calcularImc();

        if (imc < 17) {
            return "Muito abaixo do peso";
        }

        if (imc < 18.5) {
            return "Abaixo do peso";
        }

        if (imc < 25) {
            return "Peso normal";
        }

        if (imc < 30) {
            return "Acima do peso";
        }

        if (imc < 35) {
            return "Obesidade";
        }

        if (imc < 40) {
            return "Obesidade severa";
        }

        return "Obesidade mórbida";
    }
}
