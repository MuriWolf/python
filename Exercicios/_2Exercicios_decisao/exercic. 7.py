# Faça um Programa que leia três números e mostre o maior e o menor deles.

numeros = []

for i in range(0,3):
    n = int(input("Digite um numero: "))
    numeros.append(n)

minimo = min(numeros)

print(f"O menor numero entre {numeros} é o {minimo}.")