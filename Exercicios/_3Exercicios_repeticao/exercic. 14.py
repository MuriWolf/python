# Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

print("\nDigite 10 numeros para descobrir a quantidade de (pares) e (impares)!")

numeros = []
dez_contagem = 10
dez_divisao = -1

pares = 0
impares = 0

for i in range(10):
    numeroNovo = int(input("\nInfome um numero inteiro: "))
    numeros.append(numeroNovo)

    dez_divisao = dez_divisao + 1
    if numeros[dez_divisao] % 2 != 0:
        impares = impares + 1
    elif numeros[dez_divisao] % 2 == 0:
        pares = pares + 1

print(f"\nNumero de pares: {pares}")
print(f"Numero de impares: {impares}")