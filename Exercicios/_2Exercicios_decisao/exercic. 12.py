# Faça um programa para o cálculo de uma folha de pagamento,
# sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
# e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.

# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00


dinheiro_hora = int(input("\nInforme o quanto voce ganha por hora: "))

while dinheiro_hora < 1:
    dinheiro_hora = int(input("\nInforme o quanto voce ganha por hora: "))

horas_mes = int(input("\nInforme seu numero de horas trabalhadas por mês: "))

while horas_mes < 1:
    horas_mes = int(input("\nInforme seu numero de horas trabalhadas por mês: "))

salario = dinheiro_hora * horas_mes

salario_1porcento = salario / 100

# DESCONTOS

# descontos INSS, sempre (10%)
inss_10_porcento = salario_1porcento * 10


# FGTS, sempre (11%) (mas nao conta)
fgts_11_porcento = salario_1porcento * 11


# descontos do IR, (varia dependendo do salario), no caso: (0%)
if salario < 901 and salario > 0:
    pass

    # aplicação dos descontos
    salario_liquido = salario - inss_10_porcento
    porcentagem = 0

    total_descontos = inss_10_porcento

    print(f"\nSALARIO BRUTO\nSalario bruto: {salario} reais\n\nIMPOSTO DE RENDA\nValor do Imposto de renda: 0 reais ({0}%)")
    print(f"\nINSS\nValor do INSS: {inss_10_porcento} reais (10%)\n\nFGTS\nValor do FGTS: {fgts_11_porcento} reais (11%) [esse valor nao será descontado]")
    print(f"\nTOTAL DE DESCONTOS\nValor do total de descontos: {total_descontos} reais")
    print(f"\nSALARIO LIQUIDO\nValor do salario liquido: {salario_liquido} reais")

# descontos do IR, (varia dependendo do salario), no caso: (5%)
elif salario > 900 and salario < 1501:
    ir_5_porcento = salario_1porcento * 5
    porcentagem = 5

    # aplicação dos descontos
    salario_liquido = salario - (inss_10_porcento + ir_5_porcento)

    total_descontos = inss_10_porcento + ir_5_porcento

    print(f"\nSALARIO BRUTO\nSalario bruto: {salario} reais\n\nIMPOSTO DE RENDA\nValor do Imposto de renda: {ir_5_porcento} reais ({porcentagem}%)")
    print(f"\nINSS\nValor do INSS: {inss_10_porcento} reais (10%)\n\nFGTS\nValor do FGTS: {fgts_11_porcento} reais (11%) [esse valor nao será descontado]")
    print(f"\nTOTAL DE DESCONTOS\nValor do total de descontos: {total_descontos} reais")
    print(f"\nSALARIO LIQUIDO\nValor do salario liquido: {salario_liquido} reais")

# descontos do IR, (varia dependendo do salario), no caso: (10%)
elif salario > 1500 and salario < 2500:
    ir_10_porcento = salario_1porcento * 10
    porcentagem = 10

    # aplicação dos descontos
    salario_liquido = salario - (inss_10_porcento + ir_10_porcento)

    total_descontos = inss_10_porcento + ir_10_porcento

    print(f"\nSALARIO BRUTO\nSalario bruto: {salario} reais\n\nIMPOSTO DE RENDA\nValor do Imposto de renda: {ir_10_porcento} reais ({porcentagem}%)")
    print(f"\nINSS\nValor do INSS: {inss_10_porcento} reais (10%)\n\nFGTS\nValor do FGTS: {fgts_11_porcento} reais (11%) [esse valor nao será descontado]")
    print(f"\nTOTAL DE DESCONTOS\nValor do total de descontos: {total_descontos} reais")
    print(f"\nSALARIO LIQUIDO\nValor do salario liquido: {salario_liquido} reais")

# descontos do IR, (varia dependendo do salario), no caso: (20%)
elif salario > 2499:
    ir_20_porcento = salario_1porcento * 20
    porcentagem = 20

    # aplicação dos descontos
    salario_liquido = salario - (inss_10_porcento + ir_20_porcento)

    total_descontos = inss_10_porcento + ir_20_porcento

    print(f"\nSALARIO BRUTO\nSalario bruto: {salario} reais\n\nIMPOSTO DE RENDA\nValor do Imposto de renda: {ir_20_porcento} reais ({porcentagem}%)")
    print(f"\nINSS\nValor do INSS: {inss_10_porcento} reais (10%)\n\nFGTS\nValor do FGTS: {fgts_11_porcento} reais (11%) [esse valor nao será descontado]")
    print(f"\nTOTAL DE DESCONTOS\nValor do total de descontos: {total_descontos} reais")
    print(f"\nSALARIO LIQUIDO\nValor do salario liquido: {salario_liquido} reais")
