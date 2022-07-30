# As Organizações Tabajara resolveram dar um abono
# aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou.
# Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
# Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral,
# chegou-se a seguinte forma de cálculo:

# a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
# a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;
# Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa,
# descontos, impostos ou outras particularidades.
# Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários.
# Um valor de salário igual a 0 (zero) encerra a digitação.
# Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador,
# de acordo com a regra definida acima. Ao final, o programa deverá apresentar:

# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.
# Os valores podem mudar a cada execução do programa.

# Projeção de Gastos com Abono
# == == == == == == == == == == == == == ==

# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0

# Salário    - Abono
# R$ 1000.00 - R$  200.00
# R$  300.00 - R$  100.00
# R$  500.00 - R$  100.00
# R$  100.00 - R$  100.00
# R$ 4500.00 - R$  900.00

# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00

QtdeFuncionarios = 0
salario = 123
salarioMenor500 = []
salarioMaior500 = []

print("\nDigite 0 para encerrar o programa.\n")
# input dos salarios
while salario != 0:
    salario = float(input("Digite seu salário (0-encerra): "))

    if salario == 0:
        break
    while salario < 0:
        # mensagem de erro
        print("\nNao digite numeros negativos!")
        salario = float(input("Digite seu salário (0-encerra): "))

    else:
        QtdeFuncionarios = QtdeFuncionarios + 1
        # descobrir se o numero é maior ou menor 500
        if salario < 501:
            salarioMenor500.append(salario)
        elif salario > 500:
            salarioMaior500.append(salario)

abonosMenor500 = []
abonosMaior500 = []

QtdeValorMinimo = []
maiorValorPago = 0

# descobrir o abono de um numero menor que 500, ver se o abono é o maior que tem.
for i in range(len(salarioMenor500)):
    abonosMenor500.append(100)
    QtdeValorMinimo.append(1)

    if 100 > maiorValorPago:
        maiorValorPago = 100

# descobrir o abono de um numero maior que 500, ver se o abono é o maior que tem.
for i in range(len(salarioMaior500)):
    valorAbono = (salarioMaior500[i] / 100) * 20
    abonosMaior500.append((salarioMaior500[i] / 100) * 20)

    if valorAbono > maiorValorPago:
        maiorValorPago = valorAbono

# print dos salarios menores que 500
for i in range(len(salarioMenor500)):
    # primeiro print
    if i == 0:
        print("\nSalarios com abono igual a 100")
        print("Salário   - Abono")

    if salarioMenor500[i] < 1000:
        print(f"R%  {salarioMenor500[i]} - R$ {abonosMenor500[i]}")
    else:
        print(f"R% {salarioMenor500[i]} - R$ {abonosMenor500[i]}")

#  print dos salarios maiores que 500
for i in range(len(salarioMaior500)):
    # primeiro print
    if i == 0:
        print("\nSalarios com abono maior que 100")
        print("Salário   - Abono")

    if salarioMenor500[i] < 1000:
        print(f"R%  {salarioMaior500[i]} - R$ {abonosMaior500[i]}")
    else:
        print(f"R% {salarioMaior500[i]} - R$ {abonosMaior500[i]}")

totalAbono = [sum(abonosMenor500) + sum(abonosMaior500)]

# print das informaçõe finais
print(f"\nForam processados {QtdeFuncionarios} colaboradores")
print(f"Total gasto com abonos: R$ {sum(totalAbono)}")
print(f"Valor mínimo pago a {sum(QtdeValorMinimo)} colaboradores")
print(f"Maior valor de abono pago: R$ {maiorValorPago}")