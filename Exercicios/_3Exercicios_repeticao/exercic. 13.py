# Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem

print("\nDigite dois numeros, o primeiro será a base e o segundo será o expoente.\nO resultado será o primeiro numero elevado ao segundo")

num1 = int(input("\nDigite o primeiro numero (base): "))
num2 = int(input("\nDigite o segundo numero (expoente): "))

base = 0
resultado = 0
adicao = 0

while num2 > 0:
    num2 = num2 - 1
    adicao = num1 * num1
    resultado = num1 * adicao

print(f"Resultado da elevação: {resultado}")

