# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = 2
nLista = []

um= 1
while n < 16:
    if n == 2:
        print(f"H = 1 + {um}/{n} + ", end='')
        n = n + 1
        nLista.append(n)
    else:
        print(f"{um}/{n} + ", end='')
        n = n + 1
        nLista.append(n)

print(f"{um}/{n} = 1 + {1}/{sum(nLista)}")