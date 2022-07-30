# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
#
# O algoritmo deve mostrar na tela as notas, a média,
# o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
# ou “REPROVADO” se o conceito for D ou E.

print("\nDIGITE APENAS DE 1 ATÉ 10.")

nota_1 = float(input("\nDigite a primeira nota do aluno: "))

while nota_1 < 0 or nota_1 > 10:
    nota_1 = float(input("\nDigite a primeira nota do aluno: "))

nota_2 = float(input("\nDigite a segunda nota do aluno: "))

while nota_2 < 0 or nota_2 > 10:
    nota_2 = float(input("\nDigite a segunda nota do aluno: "))

nota_3 = float(input("\nDigite a terceira nota do aluno: ")) # nota extra que eu quis colocar :P

while nota_3 < 0 or nota_3 > 10:
    nota_3 = float(input("\nDigite terceira nota do aluno: "))

media_aluno = (nota_1 + nota_2 + nota_3) / 3


if media_aluno >-1 and media_aluno <= 3.9:
    conceito = 'E'
    print(f"\nMEDIA ALUNO\n{media_aluno:.1f}") # melhor jeito
    print(f"\nCONCEITO\n{conceito}\n\nRESULTADD FINAL\nReprovado.")

elif media_aluno > 3.9 and media_aluno <= 5.9:
    conceito = 'D'
    print("\nMEDIA ALUNO\n{:.1f}".format(media_aluno)) # pior jeito, mas funciona
    print(f"\nCONCEITO\n{conceito}\n\nRESULTADD FINAL\nReprovado.")


elif media_aluno > 5 and media_aluno < 7.4:
    conceito = 'C'
    print("\nMEDIA ALUNO\n{:.1f}".format(media_aluno))
    print(f"\nCONCEITO\n{conceito}\n\nRESULTADD FINAL\nAprovado.")


elif media_aluno > 7.4 and media_aluno < 8.9:
    conceito = 'B'
    print("\nMEDIA ALUNO\n{:.1f}".format(media_aluno))
    print(f"\nCONCEITO\n{conceito}\n\nRESULTADD FINAL\nAprovado.")


elif media_aluno > 9 and media_aluno < 10.1:
    conceito = 'A'
    print(f"\nMEDIA ALUNO\n{media_aluno:.1f}")
    print(f"\nCONCEITO\n{conceito}\n\nRESULTADD FINAL\nAprovado.")

# esses dois jeitos funcionam, mas o primeiro é melhor

# print(f"\nMEDIA ALUNO\n{media_aluno:.2f}")
#
# print("\nMEDIA ALUNO\n{:.1f}".format(media_aluno))




