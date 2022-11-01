"""
Atividade 1

Faça um programa que leia a idade de uma pessoa expressa em dias e
mostre-a expressa em anos, meses e dias.
"""
import argparse

app = argparse.ArgumentParser(
    usage="python exercicio1.py 396",
    description=(
        "Informa a idade de uma pessoa em anos, "
        "meses e dias ao receber a idade em dias."
    )
)
app.add_argument(
    'numero_de_dias',
    type=int,
    help='Idade de uma pessoa expressa em dias',
)

args = app.parse_args()
anos = args.numero_de_dias // 365
meses = (args.numero_de_dias % 365) // 30
dias = (args.numero_de_dias % 365) % 30
print("{} anos, {} meses, {} dias.".format(anos, meses, dias))
