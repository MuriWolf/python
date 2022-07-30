# Faça um Programa para leitura de três notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e presentar:

# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota_1 = float(input("\nInforme a primeira nota do aluno: "))

while nota_1 > 10 or nota_1 < 0:
    print("\nDigite apenas de 0 até 10!")
    nota_1 = float(input("Informe a primeira nota do aluno: "))

nota_2 = float(input("\nInforme a segunda nota do aluno: "))

while nota_2 > 10 or nota_2 < 0:
    print("\nDigite apenas de 0 até 10!")
    nota_2 = float(input("Informe a segunda nota do aluno: "))

nota_3 = float(input("\nInforme a terceira nota do aluno: "))

while nota_3 > 10 or nota_3 < 0:
    print("\nDigite apenas de 0 até 10!")
    nota_3 = float(input("Informe a terceira nota do aluno: "))

notas = (f"{nota_1}, {nota_2} e {nota_3}")

media = (nota_1 + nota_2 + nota_3) / 3

if media < 7:
    print(f"\nnotas = {notas}")
    print(f"Media = {media:.1f}")
    print("\nREPROVADO.")

if media == 7 or media > 7 and media < 10:
    print(f"\nnotas = {notas}")
    print(f"Media = {media:.1f}")
    print("\nAPROVADO.")

if media == 10:
    print(f"\nnotas = {notas}")
    print(f"Media = {media:.1f}")
    print("\nPARABENS!")
    print("\nAPROVADO COM DISTINÇÃO.")