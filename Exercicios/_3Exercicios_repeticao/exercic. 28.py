# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

print('''
informe a quantidade de CDs e o valor para em cada um para descobrir:

O valor total investido em sua coleção de CDs
E o valor médio gasto em cada um deles.
''')

QtCDs = int(input("\nInforme a quantidade de CDs de sua coleção: "))
NumeracaoCDs = 0
CD_lista = []

for i in range(QtCDs):
    NumeracaoCDs = NumeracaoCDs + 1
    valor = float(input(f"\nInforme o valor do CD {NumeracaoCDs} em reais: "))
    CD_lista.append(valor)

    while valor < 1:
        valor = float(input(f"\nInforme o valor do CD {NumeracaoCDs} em reais: "))
        CD_lista.append(valor)

somaCDs = sum(CD_lista)
mediaCDs = somaCDs / QtCDs

print(f"\n\nO valor total que foi investido na coleção é de {somaCDs} reais")
print(f"\nA média gasta em cada CD é de {mediaCDs:.1f} reais")