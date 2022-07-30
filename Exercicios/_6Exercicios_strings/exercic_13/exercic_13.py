# Jogo da palavra embaralhada.

# Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas.
#! O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador terá seis tentativas para adivinhar a palavra.
# Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import random

# pegar todas as palavras
arq = open("C:/Users/Usuario/OneDrive/VScode_projetos/Pycharm_Projetos/DevMuriWolf/Exercicios/6Exercicios_strings/exercic_13/palavras.txt")
palavras = arq.readlines()
arq.close()

# escolher a palavra
palavra = (palavras[random.randint(0, 19)])

palavra = palavra[:-1]

#  embaralhar a palavra
embaralhado = list(palavra)
random.shuffle(embaralhado)
embaralhado = "".join(embaralhado)

# comeca o jogo
print("\nJogo de adivinar a palavra.")
print(f"\nPalavra: {embaralhado}")

# tentativas usuario
acertos = 0
for i in range(6):
    tentativa = str(input(f"\nTentaviva {i+1}: "))
    tentativa = tentativa.casefold()
    if tentativa == palavra:
        acertos+=1

# vitoria ou derrota
if acertos >= 1:
    print("\nVoce acertou!")
    print(f"A palavra era: {palavra}")
else:
    print("\nVoce perdeu! :(")
    print(f"A palavra correta era: {palavra}")
