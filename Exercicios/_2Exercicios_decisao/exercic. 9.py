# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))


# num3 maior
if num3 > num2 and num3 > num1 and num2 > num1:
    print(num3, num2, num1)

elif num3 > num2 and num3 > num1 and num1 > num2:
    print(num3, num1, num2)

# num2 maior

elif num2 > num1 and num2 > num3 and num1 > num3:
    print(num2, num1, num3 )

elif num2 > num1 and num2 > num3 and num3 > num1:
    print(num2, num3, num1)

# num1 maior

elif num1 > num2 and num1 > num3 and num2 > num3:
    print(num1, num2, num3)

elif num1 > num2 and num1 > num3 and num3 > num2:
    print(num1, num3, num2)