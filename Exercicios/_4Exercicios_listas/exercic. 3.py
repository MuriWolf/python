# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# perguntar as notaa
lista_notas_1AnoA_EM = []

print("Digite as 4 notas do aluno.\n")
for i in range(4):
    lista_notas_1AnoA_EM.append(float(input('digite a nota ' + str(i + 1) + ': ')))

# mostrar/somar/dividir as notas
print(f"Notas: {lista_notas_1AnoA_EM}\n")

media_aluno = sum(lista_notas_1AnoA_EM) / 4

print(f"Media das notas: {media_aluno}")