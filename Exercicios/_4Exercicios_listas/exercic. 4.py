# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

# perguntar os caracteres

print("Informe 10 caracteres.")

vogais = ('a', 'e', 'i', 'o', 'u')
lista_char = []
consoantes = 0

for i in range(10):
    lista_char.append(input("Informe o caractere " + str(i + 1) + ": "))
    char = lista_char[i]

    if (char not in vogais):
        consoantes += 1

print(consoantes)
