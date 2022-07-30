# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

denovo = 'abc'

def Positiv_Negativ(a):
    if a >= 0:
        print(f"\nO numero {a} é positivo.")
    elif a < 0:
        print(f"\nO numero {a} é negativo.")

print("\nPositivo ou Negativo")
while denovo != 'n':
    a = float(input("\nDigite um numero: "))
    Positiv_Negativ(a)

    denovo = input("\nDeseja usar o programa denovo? [s/n]: ")