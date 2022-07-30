# Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n

# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

denovo = 'abc'

while denovo != 'n':
    numero = int(input("\nDigite um numero: "))
    def escadaNumerica(numero):
        for i in range(numero):
            if i == 0:
                print("")
            escada = [i+1] * (i+1)
            print(escada)

    escadaNumerica(numero)
    denovo = input("\nDeseja usar o program denovo? [s/n]: ")