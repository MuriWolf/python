# Faça um programa que, dado um conjunto de N números,
# determine o menor valor,
# o maior valor e a soma dos valores.

numeros = []
quantNum = int(input("\nInforme quantos numeros deseja digitar: "))

for i in range(quantNum):
    num = int(input("\nInfome um numero: "))
    numeros.append(num)

maxNumeros = max(numeros)
minNumeros = min(numeros)
somaNumeros = sum(numeros)

print(f"\nO maior valor entre essa numeros é o {maxNumeros}")
print(f"\nO menor valor entre essa numeros é o {minNumeros}")
print(f"\nO valor da soma desses numeros é {somaNumeros}")