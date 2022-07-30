# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

numero = int(input("\nInforme um numero inteiro para descobrir seu fatorial: "))

numeroConta = numero
numeroMenor = numero - 1
conta = numeroConta * numeroMenor

fatorial = []

for i in range(numero - 2):
    numeroMenor = numeroMenor - 1
    conta = conta * numeroMenor
    fatorial.append(conta)

numeroPrint = numero + 1
Numero_ate_1 = []

for i in range(numeroPrint - 1):
    numeroPrint = numeroPrint - 1
    Numero_ate_1.append(numeroPrint)

print(f"\n{numero} = {Numero_ate_1} = {fatorial[-1]}")