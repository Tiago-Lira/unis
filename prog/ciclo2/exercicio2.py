"""
Atividade 2

Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam
ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
não formam triângulo escrever os valores lidos. (Se a &gt; b + c não formam
triângulo algum, se a é o maior).
"""
import argparse

app = argparse.ArgumentParser(
    usage="python3 exercicio2.py 4 4 4",
    description=(
        "Calcula a area de um triangulo dado os seus lados. "
        "Caso não seja um triangulo, o programa vai escrever os valores lidos."
    )
)
app.add_argument('a', type=int)
app.add_argument('b', type=int)
app.add_argument('c', type=int)

args = app.parse_args()
a = args.a
b = args.b
c = args.c

if a > (b + c):
    print(f"Não é um triangulo.\na: {args.a}\nb: {args.b}\nc: {args.c}")
else:
    # https://pt.wikipedia.org/wiki/Teorema_de_Herão
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print(f"A area do triangulo é: {area:.2f}")
