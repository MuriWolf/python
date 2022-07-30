# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.


quantos = int(input("\nInforme quantos Fibonacci deseja ver: "))

anterior = 0
proximo = 1
fibo = []

for i in range(quantos):
    fibo.append(anterior)
    anterior, proximo = proximo, anterior + proximo

print(f"\n{fibo}")