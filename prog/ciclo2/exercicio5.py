"""
Atividade 5

Escreva uma função que:
a) Receba uma frase como parâmetro.
b) Retorne uma nova frase com cada palavra com as letras invertidas.
"""
import argparse


def reverter_letras(palavra):
    return "".join(reversed(palavra))


def reverter_frase(frase):
    return " ".join(reverter_letras(palavra) for palavra in frase.split())


app = argparse.ArgumentParser(
    usage=(
        "python3 exercicio5.py \"atse edadivita anoicnuf\""
    ),
    description=(
        "Dada uma frase, imprime uma nova frase com cada "
        "palavra com as letras invertidas."
    )
)
app.add_argument('frase', type=str)
args = app.parse_args()
print(reverter_frase(args.frase))
