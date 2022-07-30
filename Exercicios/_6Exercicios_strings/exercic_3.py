# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

# F
# U
# L
# A
# N
# O

nome = str(input("Digite um nome: "))

tamanho =len(nome)

print(f"\nO nome '{nome}' na vertical é:\n")
for i in range(tamanho):
    print(nome[i], end="\n")