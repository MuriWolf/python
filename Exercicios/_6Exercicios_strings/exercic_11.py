# Jogo de Forca. Desenvolva um jogo da forca. 
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

from random import choice

def print_forca(forca):
    print(' '.join(forca).upper())
    print('')

print("Jogo da forca. Você terá seis chances de acertar a palavra. Boa sorte!")

palavras = ["borracha", "danone", "guitarra", "camisa", "viagem", "notebook"] 
palavra = choice(palavras)

forca = ['_' for i in range(len(palavra))]
erros = 0
ganhou = False

while erros < 6 and not ganhou:
    print_forca(forca)
    chute = str(input("Digite uma letra: "))

    if chute not in palavra:
        erros += 1
        print(f"Voce errou pela {erros} vez! voce tem mais {6 - erros} chance(s). tente novamente.")
        continue

    for index, letra in enumerate(palavra):
        if letra == chute:
            forca[index] = chute

    if '_' not in forca:
        ganhou = True

if ganhou:
    print('You win!')
else:
    print('Game over!')
