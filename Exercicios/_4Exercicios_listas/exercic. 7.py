# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetorList = []

for i in range(5):
    numero = int(input("Digite um numero inteiro: "))
    vetorList.append(numero)

somaVetorList = (sum(vetorList))

multiplicacao = vetorList[0] * vetorList[1] * vetorList[2] * vetorList[3] * vetorList[4]

print(f'''
Numeros:
{vetorList}

Soma:
{somaVetorList}

Multiplicação:
{multiplicacao}
''')