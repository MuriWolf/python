# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores. Imprima os três vetores.

import random

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    # gerar valores aleatorios para adicionar nas listas
    lista1.append(random.randint(0,100))
    lista2.append(random.randint(0,100))

    # adicionar os valores das lista 1 e 2 na lista3, uma posição por vez
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f'''
Lista 1:
{lista1}

Lista 2:
{lista2}

Lista 3:
{lista3}
''')