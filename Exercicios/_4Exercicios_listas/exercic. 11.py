# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

import random

lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(10):
    # gerar valores aleatorios para adicionar nas listas
    lista1.append(random.randint(0,100))
    lista2.append(random.randint(0,100))
    lista3.append(random.randint(0,100))

    # adicionar os valores das lista 1 e 2 na lista3, uma posição por vez
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print(f'''
Lista 1:
{lista1}

Qtde Numeros: {len(lista1)}

Lista 2:
{lista2}

Qtde Numeros: {len(lista2)}

Lista 3:
{lista3}

Qtde Numeros: {len(lista3)}

Lista 4:
{lista4}

Qtde Numeros: {len(lista4)}
''')