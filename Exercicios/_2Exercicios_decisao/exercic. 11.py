# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
# lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

# Começo
salario = float(input("\nDigite seu salario em reais: "))

while 0 > salario or salario == 0:
    salario = float(input("\nDigite seu salario em reais: "))

# valor de 1 por cento do salario
salario_1_por_cento = salario / 100


# salários até R$ 280,00 (incluindo) : aumento de 20%
if salario <= 280 and salario > 0:
    valor_20_porcento = (salario_1_por_cento * 20)
    aumento_20_porcento = valor_20_porcento + salario
    porcentagem = 20

    # valor inteiro da porcentagem
    int_20_porcento = int(valor_20_porcento)

    print(f"\nSALARIO ANTIGO\nSeu salario antes do reajuste era: {salario} reais.")
    print(f"\nPERCENTUAL DE AUMENTO APLICADO\nFoi aumentado em {porcentagem}% seu salario.")
    print(f"\nVALOR DO AUMENTO\nO valor do aumento é de {int_20_porcento} reais.")
    print(f"\nNOVO SALARIO\nO valor do novo salario é de {aumento_20_porcento} reais.")


# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
elif salario > 280 and salario < 701:
    valor_15_porcento = salario_1_por_cento * 15
    aumento_15_porcento = valor_15_porcento + salario
    porcentagem = 15

    # valor inteiro da porcentagem
    int_15_porcento = int(valor_15_porcento)

    print(f"\nSALARIO ANTIGO\nSeu salario antes do reajuste era: {salario} reais.")
    print(f"\nPERCENTUAL DE AUMENTO APLICADO\nFoi aumentado em {porcentagem}% seu salario.")
    print(f"\nVALOR DO AUMENTO\nO valor do aumento é de {int_15_porcento} reais.")
    print(f"\nNOVO SALARIO\nO valor do novo salario é de {aumento_15_porcento} reais.")


# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
elif salario > 700 and salario < 1501:
    valor_10_porcento = salario_1_por_cento * 10
    aumento_10_porcento = valor_10_porcento + salario
    porcentagem = 10

    # valor inteiro da porcentagem
    int_10_porcento = int(valor_10_porcento)

    print(f"\nSALARIO ANTIGO\nSeu salario antes do reajuste era: {salario} reais.")
    print(f"\nPERCENTUAL DE AUMENTO APLICADO\nFoi aumentado em {porcentagem}% seu salario.")
    print(f"\nVALOR DO AUMENTO\nO valor do aumento é de {int_10_porcento} reais.")
    print(f"\nNOVO SALARIO\nO valor do novo salario é de {aumento_10_porcento} reais.")


# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
elif salario > 1500:
    valor_5_porcento = salario_1_por_cento * 5
    aumento_5_porcento = valor_5_porcento + salario
    porcentagem = 5

    # valor inteiro da porcentagem
    int_5_porcento = int(valor_5_porcento)

    print(f"\nSALARIO ANTIGO\nSeu salario antes do reajuste era: {salario} reais.")
    print(f"\nPERCENTUAL DE AUMENTO APLICADO\nFoi aumentado em {porcentagem}% seu salario.")
    print(f"\nVALOR DO AUMENTO\nO valor do aumento é de {int_5_porcento} reais.")
    print(f"\nNOVO SALARIO\nO valor do novo salario é de {aumento_5_porcento} reais.")