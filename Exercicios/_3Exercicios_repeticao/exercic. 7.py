# Faça um programa que leia 5 números e informe o maior número.

# five_numbers = []

# for i in range(0,5):
#     five_numbers = (input("Digite o numero " + str(i + 1) + ": "))
# max = max(five_numbers)
# print(max)

# another way to do

print("Digite cinco numeros.\n")

lista = []
maximo = 5

while len(lista) < maximo:
    n = int(input("Digite um numero: "))
    lista.append(n)

max_cinco = max(lista)
print(f"O maior numero entre {lista} é o {max_cinco}.")

