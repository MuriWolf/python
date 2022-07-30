# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

#lista = [4, 8, 16, 32, 64]

#i = 0

#while i < (len(lista)):
#    print(lista[i])
#    i = i + 1

lista_cinco = []

print("Digite 5 numeros inteiros.")
for i in range(5):
    lista_cinco.append(int(input("Digite o numero " + str(i + 1) + ": ")))

print(lista_cinco)