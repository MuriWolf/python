# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
# o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
#
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

import _pyinstaller_hooks_contrib

denovo = 's'
simNao = ['s','n']

while denovo == 's':
    tabuada = int(input("\nInforme qual tabuada voce deseja ver: "))

    print('''
AVISO!!
    
Posição 1 da tabuada de 10: 10,
Se o numero inicial da posicao dessa tabuada for 3, o primeiro numero será 30.
    
Posição 10 da tabuada de 10: 100,
Se o numero da posicao final dessa tabuada for 15, o ultimo numero será 150.
''')

    numInicial = int(input("\nInforme o numero inicial da posicao dessa tabuada: "))

    # se numero menor que 1
    while numInicial < 1:
        print("\nNao digite um numero menor que 1!")
        numInicial = int(input("\nInforme o numero inicial da posicao dessa tabuada: "))

    numFinal = int(input("\nInforme o numero final da posicao dessa tabuada: "))
    while numFinal < 1:
        print("\nNao digite um numero menor que 1!")
        numFinal = int(input("\nInforme o numero final da posicao dessa tabuada: "))

    # se numero inicial menor que o final
    while numInicial > numFinal:
        print("\nO numero final deve ser maior que o numero inicial!")
        numFinal = int(input("Informe o numero final da sequencia dessa tabuada: "))

    # print da tabuada
    print(f"\nTabuada do {tabuada} de {numInicial} até {numFinal}\n")
    numero = numInicial - 1
    while numero < numFinal:
        numero = numero + 1
        conta = tabuada * numero
        print(f"{tabuada} x {numero} = {conta}")

    # perguntar se deseja executar denovo
    pergunta = input("\nDeseja ver outra tabuada? [s/n]: ")
    while pergunta not in simNao:
        pergunta = input("\nDeseja ver outra tabuada? [s/n]: ")
    if pergunta == 's':
        pass
    elif pergunta == 'n':
        denovo = 'n'