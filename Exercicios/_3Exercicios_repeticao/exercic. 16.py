# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

quantos = int(input("\nInforme quantos Fibonacci deseja ver: "))

anterior = 0
proximo = 1
fibo = []

for i in range(quantos):

    # apenas esse while foi adicionado ao código
    while anterior < 500:
        fibo.append(anterior)
        anterior, proximo = proximo, anterior + proximo

print(f"\n{fibo}")