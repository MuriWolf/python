# Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia entre (0 e 25), (26 e 60) e (maior que 60);
# e então,
# dizer se a turma é (jovem), (adulta) ou (idosa), conforme a média calculada.

QtPessoas = int(input("\nDigite quantas pessoas irão informar suas idades: "))
idades = []

for i in range(QtPessoas):
    idade = float(input("\nInforme sua idade: "))
    idades.append(idade)

media = sum(idades) / QtPessoas

if media > -1 and media < 26:
    print("\nConforme a média calculada, a turma é jovem")

elif media > 25 and media < 61:
    print("\nConforme a média calculada, a turma é adulto")

elif media > 60:
    print("\nConforme a média calculada, a turma é idosa")