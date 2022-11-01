"""
Atividade 3

Faça um programa que leia 3 números inteiros e mostre o menor deles.
"""
import argparse

app = argparse.ArgumentParser(
    usage="python3 exercicio3.py 3 2 1",
    description="Imprime o menor número informado.",
)
app.add_argument('n1', type=int)
app.add_argument('n2', type=int)
app.add_argument('n3', type=int)

args = app.parse_args()
n1 = args.n1
n2 = args.n2
n3 = args.n3

menor = min(n1, n2, n3)
print("O menor número é: {}".format(menor))
