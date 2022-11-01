"""
Atividade 4

Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.
"""
import argparse


def is_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if (numero % i) == 0:
            return False
    return True


app = argparse.ArgumentParser(
    usage="python3 exercicio4.py 2",
    description="Imprime o menor número informado.",
)
app.add_argument('numero', type=int)
args = app.parse_args()

if is_primo(args.numero):
    print("Verdadeiro")
else:
    print("Falso")
