# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

numero = int(input("\nInforme um numero inteiro: "))

divisao = numero % 2

if divisao == 0:
    print("\nEsse numero é par")

else:
    print("\nEsse numero é impar")