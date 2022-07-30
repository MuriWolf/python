# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

listaNumerosReais = []

print("Informe 10 numeros reais.")

for i in range(10):
    listaNumerosReais.append(float(input('Digite o numero: ' + str(i + 1) + ': ')))

listaNumerosReais.reverse()

print(listaNumerosReais)