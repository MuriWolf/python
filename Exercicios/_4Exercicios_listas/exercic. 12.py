# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

# teste 7 alunos
idades = [13, 14, 15, 13, 12, 15, 14]
tamanhos = [1.60, 1.67, 1.64, 1.71, 1.69, 1.65, 1.68]

mediaTamanhos = (sum(tamanhos) / len(tamanhos))
menor13Anos = []

for i in range(len(idades)): # no caso esse len representa o 7
    if tamanhos[i] < mediaTamanhos and idades[i] > 13:
        menor13Anos.append(1)

print(f'''
Quntidade de alunos maiores de 13 anos,
que são menores que a média de altura da turma:

{sum(menor13Anos)} alunos
''')