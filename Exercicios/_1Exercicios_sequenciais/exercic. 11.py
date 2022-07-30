# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num_one = int(input("Digite um numero inteiro: "))

num_two = int(input("Digite outro numero inteiro: "))

num_three = float(input("Digite um numero real: "))


# o produto do dobro do primeiro com metade do segundo

double_one = num_one * 2

half_two = num_two / 2

conta_final_one = double_one * half_two

print("\nO produto do dobro do primeiro com metade do segundo:")
print(conta_final_one)

# a soma do triplo do primeiro com o terceiro.

triple_one = num_one * 3

conta_final_two = triple_one + num_three

print("\na soma do triplo do primeiro com o terceiro:")
print(conta_final_two)

# o terceiro elevado ao cubo.

cube_three = num_three ** 2

print("\nO terceiro elevado ao cubo:")
print(cube_three)