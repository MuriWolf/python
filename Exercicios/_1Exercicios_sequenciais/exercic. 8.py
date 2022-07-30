# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

horas = float(input("Informe o quanto voce ganha por hora: "))

hora_mes = float(input("Informe o numero de horas trabalhadas no mês: "))



salario = horas * hora_mes

print(f"{salario} reais")