# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário.
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

# (esses dois codigo nao fazem parte do mesmo codigo)
# codigo 1
porcentagem = 1.5
salario_inicial = 1000

for i in range(10):
    porcentagem = porcentagem * 2
    print(f"\nporcenta: {porcentagem}")
    salario = (salario_inicial / 100) * porcentagem + salario_inicial
    print(int(salario))

# codigo 2
salario = 1000
ano = 1996
while ano <= 2020:
    salario = salario * 1.015
    ano = ano + 1
    print(salario)
print(f"{salario:.2f}")