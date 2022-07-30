# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,

# o programa deve perguntar ao aluno a resposta de cada questão,
# e ao final comparar com o gabarito da prova e assim calcular o total de acertos
# e a nota (atribuir 1 ponto por resposta certa).

# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
# Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.

# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# Após concluir isto você poderia incrementar o programa
# permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

opcoes = ['A','B','C','D','E','a','b','c','d','e']
gabarito = []
respostas_alunos = []
notas = []

# professor cria o gabarito
print("Professor: ")
for i in range(10):
    print("\nquestao:", i + 1)
    resposta_certa = (input("Digite a resposta correta: "))
    while resposta_certa not in opcoes:
        resposta_certa = (input("Digite a resposta correta: "))
    gabarito.append(resposta_certa)

continuar = 123
numAluno = 0

# todo esse codigo esta dentro do while, isso significa que algo no meio/final muda tambem o começo.
# começa o while, printa o numero do aluno
while continuar != 'n':
    numAluno = numAluno + 1
    print(f"\n\n\nAluno n°{numAluno}")
    respostas_alunos.clear()

    # pergunta as respostas
    for i in range(10):
        print("\nquestao:", i + 1)
        resposta_alunos = input("Escolha a alternativa: ")
        respostas_alunos.append(resposta_alunos)
    nota = 0

    # verifica se as respostas estao corretas
    for i in range(10):
        if respostas_alunos[i] == gabarito[i]:
            nota = nota + 1
    notas.append(nota)
    # pergunta se ira ser usado de novo o programa
    continuar = (input("\nOutro aluno ira ultilizar o sistema? [s/n]: "))
    if continuar == 'n' or continuar == 'N':

        print(f'''
alunos que ultilizaram o sistema: {len(notas)} 

A maior nota tirada foi: {max(notas)}
A menor nota tirada foi: {min(notas)}

A media de nota da turma é: {(sum(notas)) / (len(notas))} 
''')