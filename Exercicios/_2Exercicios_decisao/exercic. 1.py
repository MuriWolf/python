# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite um numero: "))

num2 = int(input("Digite outro numero: "))

if num1 > num2:
    print(f"O numero {num1} é maior que o {num2}.")

elif num2 > num1:
    print(f"O numero {num2} é maior que o {num1}.")

else:
    print(f"O numero {num1} é igual ao {num2}.")