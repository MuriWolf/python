# Os números primos possuem várias aplicações dentro da Computação,
# por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

letras = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','S','T','U','V','W','X','Y','Z')

numero = (input('\nEscreve um numero ai mano: '))
while numero in letras:
    print("\nErrou parceiro")
    numero = (input('Escreve um numero ai mano: '))

numero = int(numero)
numeroDiv = 2

lista = []
listaPrimos1ate10 = [2, 3, 5, 7]

if numero < 8:
    if numero in listaPrimos1ate10:
        print(f'\n{numero} é um número primo!')
    elif numero not in listaPrimos1ate10:
        print(f'\n{numero} não é um número primo :(')

elif numero > 7:
    for i in range(8):
        conta = numero % numeroDiv
        numeroDiv = numeroDiv + 1
        if conta == 0:
            lista.append(1)

    if len(lista) == 0:
            print(f"\n{numero} é um número primo!")

    else:
        print(f'\n{numero} não é um número primo :(')