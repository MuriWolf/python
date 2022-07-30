# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

notas = []
mediaMaior7 = []
medias = []

for i in range(3): # 10
    notas.clear()
    nome = (input("Digita o nome do aluno: "))
    for x in range(4):
        nota = float(input(f"Digita a nota {x + 1}: "))
        notas.append(nota)
        if x + 1 == 4:
            conta = sum(notas) / 4
            if conta >= 7:
                mediaMaior7.append(1)
            medias.append(1)

print(f'''
Total de alunos:
{sum(medias)} alunos

Total de alunos com média maior que sete:
{sum(mediaMaior7)} alunos 
''')