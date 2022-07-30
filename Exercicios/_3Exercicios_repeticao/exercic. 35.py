# Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

Qtnumeros = int(input('\nInforme até que numero voce deseja ver onde existe primos: '))

numero = 0
primos = []
primosAte8 = [2,3,5,7]

for i in range(Qtnumeros):
    numero = numero + 1
    if numero == 1:
        pass

    elif numero < 8 and numero in primosAte8:
        primos.append(numero)
    else:
        conta = (numero % 2), (numero % 3), (numero % 5), (numero % 7), (numero % 9)

        if 0 not in conta:
            primos.append(numero)
        else:
            pass

print(f"\nNumeros primos de 1 até {Qtnumeros}:")
print(f"\n{primos}")