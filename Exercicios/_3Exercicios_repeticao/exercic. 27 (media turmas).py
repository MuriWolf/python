# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

print('''
Para calcular o número médio de alunos por turma:

Informe a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
''')

QtTurmas = int(input("\nInforme a quantidade de turmas: "))
NumTurma = 0
turmas = []

for i in range(QtTurmas):
    NumTurma = NumTurma + 1
    alunosTurma = int(input(f"\nInforme a quantidade de alunos da turma {NumTurma}: "))
    turmas.append(alunosTurma)

    while alunosTurma < 1 or alunosTurma > 40:
        print("\nDigite apenas de 1 a 40!")
        alunosTurma = int(input(f"Informe a quantidade de alunos da turma {NumTurma}: "))
        turmas.append(alunosTurma)


mediaTurmas = sum(turmas) / QtTurmas

print(f"\nMedia de alunos dessas turmas: {mediaTurmas}")