# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas,
#  com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.
#  Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

# 8  3  4 
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
#  Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
#  Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

import random

cont=0
while True:
    cont+=1
    lista=[]
    um_nove=[1,2,3,4,5,6,7,8,9]
    ja_foram=[]
    while True:
        num=random.choice(um_nove)
        if num not in ja_foram:
            ja_foram.append(num)
            lista.append(num)
        else:
            pass
        if len(lista) == 9:
            break
    if lista[0] + lista[1] + lista[2] == lista[2] + lista[5] + lista[8] == lista[0] + lista[3] + lista[6] == lista[6] + lista[7] + lista[8] == lista[0] + lista[4] + lista[8] == lista[2] + lista[4] + lista[6]:
        print(f"\nQuadrado magico encontrado na tentativa {cont}!")
        print(f"\nQuadrado mágico\n(Todas as somas de diagonais, colunas e linhas desse quadrado dão {lista[0] + lista[1] + lista[2]})\n")
        for x in range(9):
            print(lista[x], end="  ")
            if (x+1) % 3 == 0:
                print("")
        break
    else:
        print(f"\nTentativa {cont}")
        continue