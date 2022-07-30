# Parte 1 (10)
# Faça um programa que receba dois números inteiros
# e gere os números inteiros que estão no intervalo compreendido por eles.

# num1 = int(input("\nDigite um numero inteiro: "))
# num2 = int(input("\nDigite outro numero inteiro: "))
#
# num1Real = num1
# num2Real = num2
#
# numerosInteiro = 0
#
# # num1 10, num2 num 1
# if num1 > num2:
#     while num1 > num2:
#         num1 = num1 - 1
#         numerosInteiro = numerosInteiro + 1
#     print(f"\nQuntidade de numeros entre {num1Real} e {num2}: {numerosInteiro}")
#
# if num2 > num1:
#     while num2 > num1:
#         num2 = num2 - 1
#         numerosInteiro = numerosInteiro + 1
#     print(f"\nQuntidade de numeros entre {num1} e {num2Real}: {numerosInteiro}")

# Parte 2 (11)
# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("\nDigite um numero inteiro: "))
num2 = int(input("\nDigite outro numero inteiro: "))

num1Real = num1
num2Real = num2

numerosInteiro = 0
adicao = 0

# num1 10, num2 num 1
if num1 > num2:
    while num1 > num2:
        num1 = num1 - 1
        numerosInteiro = numerosInteiro + 1
    adicao = adicao + num1Real + num2Real + numerosInteiro
    print(f"\nQuntidade de numeros entre {num1Real} e {num2}: {numerosInteiro}")
    print(f"\nResultado da adição dos numeros: {adicao}")

if num2 > num1:
    while num2 > num1:
        num2 = num2 - 1
        numerosInteiro = numerosInteiro + 1
    adicao = adicao + num1Real + num2Real + numerosInteiro
    print(f"\nQuntidade de numeros entre {num1Real} e {num2}: {numerosInteiro}")
    print(f"\nResultado da adição dos numeros: {adicao}")
