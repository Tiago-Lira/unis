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
}
