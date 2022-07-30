# Faça um programa para a leitura de duas notas parciais de um aluno
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete
# A mensagem "Reprovado", se a média for menor do que sete
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# pedir nota

nota1 = float(input("Digite a primeria noata do aluno: "))

nota2 = float(input("Digite a segunda nota do aluno: "))

# calcular a media
media = (nota1 + nota2) / 2
print(media)

# aprovar/reprovar
if 7 < media < 10:
    print("aprovado")

elif 10 == media:
    print("Aprovado com distinção")

elif media < 7:
    print("Reprovado")

else:
    print("Verifique se voce digitou certo.")