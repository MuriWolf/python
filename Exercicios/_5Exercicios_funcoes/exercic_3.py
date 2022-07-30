# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

denovo = '123'

while denovo != 'n':
    def Soma3(a, b, c):
        soma = a+b+c
        print(f"\nResultado da soma: {soma}")

    a = int(input("Digite um numero inteiro: "))
    b = int(input("Digite um numero inteiro: "))
    c = int(input("Digite um numero inteiro: "))

    Soma3(a,b,c)
    denovo = input("\nDeseja usar o programa denovo? [s/n]: ")