# Faça um programa que leia 5 números e informe a soma e a média dos números.

lista_cinco = []

print("Digite cinco numeros.\n")

for i in range (0,5):
    n = int(input("Digite um numero: "))
    lista_cinco.append(n)

soma = sum(lista_cinco)

media = soma / 5

print(f"\nA soma de {lista_cinco} é {soma}\n")

print(f"A media de {lista_cinco} é {media}")