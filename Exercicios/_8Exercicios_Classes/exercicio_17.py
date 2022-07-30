# Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista.
#  Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, 
# exija que ele tome conta da fazenda inteira.
#  Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos
#  (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). 
# Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

from exercicio_15_16 import tamagushi
from time import sleep
from random import randint

def main():
    tamagushi_01 = tamagushi("unknown", randint(0, 100), randint(0, 100), randint(0, 20), "", "", randint(0, 100))
    tamagushi_02 = tamagushi("unknown", randint(0, 100), randint(0, 100), randint(0, 20), "", "", randint(0, 100))
    tamagushi_03 = tamagushi("unknown", randint(0, 100), randint(0, 100), randint(0, 20), "aas", "assa", randint(0, 100))
    tamagushi_04 = tamagushi("unknown", randint(0, 100), randint(0, 100), randint(0, 20), "", "", randint(0, 100))
    tamagushi_05 = tamagushi("unknown", randint(0, 100), randint(0, 100), randint(0, 20), "", "", randint(0, 100))
    tamagushi_06 = tamagushi("unknown", randint(0, 100), randint(0, 100), randint(0, 20), "", "", randint(0, 100))
    tamagushi_07 = tamagushi("unknown", randint(0, 100), randint(0, 100), randint(0, 20), "", "", randint(0, 100))

    while True:
        choice_tamagushi = str(input("""
1- Alimentar todos os bichinhos
2- Brincar com todos os bichinhos
3- Ver status de todos os bichinhos

R """))
        if choice_tamagushi == 1:
            pass
        if choice_tamagushi == 2:
            pass
        if choice_tamagushi == 3:
            pass
        

main()