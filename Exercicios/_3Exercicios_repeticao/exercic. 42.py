# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
# [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

print('''
Olá, nesse programa voce pode digitar qualquer numero inteiro,
e no final descobrir quantos estão entre [0-25], [26-50], [51-75] e [76-100].
Para finalizar o input do programa, digite qualquer numero negativo.
''')

numero = 123 # <- numero aleatorio

zero_vinte = []
vinte_cinquenta = []
cinquenta_setenta = []
setenta_cem = []

while numero >= 0:
    numero = int(input("\nDigite um numero numero positivo: "))

    if numero >= 0 and numero < 26:
        zero_vinte.append(1)
    elif numero >= 26 and numero < 51:
        vinte_cinquenta.append(1)
    elif numero >= 51 and numero < 76:
        cinquenta_setenta.append(1)
    elif numero >= 76 and numero < 101:
        setenta_cem.append(1)

print(f'''
Quantidade de numeros entre 0 e 25:
{sum(zero_vinte)} numero(s)

Quantidade de numeros entre 26 e 50:
{sum(vinte_cinquenta)} numero(s)

Quantidade de numeros entre 51 e 75:
{sum(cinquenta_setenta)} numero(s)

Quantidade de numeros entre 76 e 100:
{sum(setenta_cem)} numero(s)
''')