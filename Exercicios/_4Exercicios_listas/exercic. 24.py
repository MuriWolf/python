# Faça um programa que simule um lançamento de dados.
# Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

lados = [0] * 6

for i in range(100):
    lancamento = random.randint(1, 6)

    for i in range(6):
        if lancamento == i+1:
            lados[i] = lados[i] + 1

ladoMaisCaiu = [0,0]

for i in range(6):
    print(f"\nLado {i+1} caiu {lados[i]} vezes")
    if lados[i] > ladoMaisCaiu[1]:
        ladoMaisCaiu[0] = i+1
        ladoMaisCaiu[1] = lados[i]

print(f"\nO lado que mais caiu foi o {ladoMaisCaiu[0]} com {ladoMaisCaiu[1]} vezes")