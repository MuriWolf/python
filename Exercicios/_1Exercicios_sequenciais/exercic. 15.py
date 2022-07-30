# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,

# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


# dinheiro bruto ganho no mes
ganho_horas = float(input("\nInforme seu ganho por hora em reais: "))

horas_mes = int(input("\nInforme o numero de horas trabalhadas no mês: "))

salario = ganho_horas * horas_mes


# porcentagem:
salario_porcent = salario / 100

ImpostoRenda_sal  = salario_porcent * 11

INSS_sal = salario_porcent * 8

sindicato_sal = salario_porcent * 5

# salario liquido
salario_liquido = salario - (ImpostoRenda_sal + INSS_sal + sindicato_sal)


# mostrar resultados

# explicaçoes
print('''
OQUE FOI DESCONTADO:

- Imposto de Renda (11%) : R$
- INSS (8%) : R$
- Sindicato (5%) : R$ 

= Salário Liquido : R$
''')

# salario bruto
print(f"\nSALARIO BRUTO:\n{salario} reais\n")

# quanto pagou ao INSS.
print(f"PREÇO PAGO AO INSS:\n{INSS_sal} reais\n")

# quanto pagou ao sindicato.
print(f"PREÇO PAGO AO SINDICATO:\n{sindicato_sal} reais\n")

# o salário líquido.
print(f"SALÁRIO LIQUIDO:\n{salario_liquido} reais")