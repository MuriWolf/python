# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

print('''
M - matutino
V - vespertino
N - noturno
''')

def bomdia():
    pergunta = str(input("Em que horario voce estuda? (M, V ou N): "))

    if pergunta == 'M' or pergunta == 'm':
        print("\nBom Dia!")

    elif pergunta == 'V' or pergunta == 'v':
        print("\nBoa Tarde!")

    elif pergunta == 'N' or pergunta == 'n':
        print("\nBoa Noite!")

    else:
        bomdia()

bomdia()