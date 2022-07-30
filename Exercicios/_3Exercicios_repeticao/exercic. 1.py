#Exercicio 1

# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido,
# continue pedindo até que o usuário informe um valor válido.

ask = int(input("Digite uma nota entre 0 e 10: "))

while (ask>10) or (0>ask):
    print("Voce digitou um numero errado")
    ask = int(input("Digite uma nota entre 0 e 10: "))







