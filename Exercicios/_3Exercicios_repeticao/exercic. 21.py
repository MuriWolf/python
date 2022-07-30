# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

# Numeros primos de 1 até 100:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 e 97

print("\nDigite um numero para descobrir se ele é primo ou não.")

contagem = 10
contDivisao = 1

listaDivisiveis = []
listaNaoDivisiveis = []

numero = int(input("\nInforme um numero inteiro: "))

if numero < 8:
    if numero != 2 and numero != 3 and numero != 5 and numero != 7:
        print(f"\nOnumero {numero} não é primo.")
    else:
        print(f"\nO numero {numero} é primo.")

elif numero > 7:
    for i in range(8):
        contDivisao = contDivisao + 1

        divisao = numero % contDivisao
        divisaoFloat = float(numero) % contDivisao

        if divisao == 0:
            listaDivisiveis.append(1)
        elif divisao != 0:
            listaNaoDivisiveis.append(1)

    if len(listaDivisiveis) == 0:
        print(f"\nO numero {numero} é primo")
    elif len(listaDivisiveis) > 0:
        print(f"\nO numero {numero} não é primo")