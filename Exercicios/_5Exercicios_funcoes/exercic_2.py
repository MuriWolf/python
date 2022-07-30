# aça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

denovo = 'abc'

def escadaNumerica(numero):
    escada = [1]
    for i in range(numero):
        if i == 0:
            print("")
        print(escada)
        escada.append((escada[-1]) + 1)

while denovo != 'n':
    numero = int(input("\nDigite um numero: "))
    escadaNumerica(numero)
    denovo = input("\nDeseja usar o program denovo? [s/n]: ")