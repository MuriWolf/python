# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,]
pares = []
impares = []
contagem = 0

for i in range(20):
    if numeros[contagem] % 2 == 0:
        pares.append(numeros[contagem])
    else:
        impares.append(numeros[contagem])
    contagem = contagem + 1

print(f'''
Todos os numeros:
{numeros}

Pares:
{pares}

Impares:
{impares}
''')