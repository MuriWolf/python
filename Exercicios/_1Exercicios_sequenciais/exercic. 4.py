# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Digite 4 notas para o programa calcular a média")
print()

num_1 = int(input("Digite a primera nota: "))

num_2 = int(input("Digite a segunda nota: "))

num_3 = int(input("Digite a terceira nota: "))

num_4 = int(input("Digite a quarta nota: "))

soma = num_1 + num_2 + num_3 + num_3

divisao = soma / 4

print(f"A media desses notas é {divisao}")