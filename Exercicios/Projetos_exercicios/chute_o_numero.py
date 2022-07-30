# 2. CHUTE O NÚMERO
# Objetivo: Criar um script que gerá um valor aleatoriamente,
# guarda este valor, e pergunta repetidamente para o usuário chutar o valor gerado até que ele acerte.

# importar a funcao de numero aleatorio e opcao para desligar o programa
from random import randint

import sys


# explicação de como funciona
print("Olá, bem vindo ao 'chute o numero',\nNele sera criado um numero inteiro aleatorio de 1 a 50,")
print("E seu objetivo sera tentar acerta-lo,\n\nBoa sorte!\n")
print("AVISO: Digite a letra s para desistir/sair.\n")


# o valor gerado aleatoriamente e a tentativa do usuarios
random_number = randint(1, 50)

tentativa_usuario = int(input("Chute um numero de 1 até 50: "))


# funcao de sair
def exit():
    if tentativa_usuario == 0:
        print("\n\nPrograma encerrado.")
        sys.exit()


while tentativa_usuario != random_number:

    exit()

    # tentaviva do usuarios maior que o numero aleatorio ex: tu = 45 na = 23
    if tentativa_usuario > 50 or tentativa_usuario < 1 and tentativa_usuario != 0:
        print("Lembre-se de apenas digitar de 1 a 50.\n")
        tentativa_usuario = int(input("Chute um numero de 1 até 50: "))

    if tentativa_usuario > random_number and tentativa_usuario > 0 and tentativa_usuario < 51:
        print("Voce chutou alto. Tente denovo!\n")
        tentativa_usuario = int(input("Chute um numero de 1 até 50: "))

    # tentaviva do usuarios menor que o numero aleatorio ex: tu = 23 na = 45
    if tentativa_usuario < random_number and tentativa_usuario > 0 and tentativa_usuario < 51:
        print("Voce chutou baixo. Tente denovo!\n")
        tentativa_usuario = int(input("Chute um numero de 1 até 50: "))

    # tentaviva do usuarios igual que o numero aleatorio
    if tentativa_usuario == random_number:
        print("\nVoce acertou! Parabens!!!")
