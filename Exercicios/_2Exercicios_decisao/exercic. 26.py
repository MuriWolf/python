# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro

# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
# o preço do litro do álcool é R$ 1,90.

alcool = 1.90
galolina = 2.50

desconto_alcool = (alcool / 100) * 3
desconto_alcool_maior_20 = (alcool / 100) * 5

desconto_gasolina = (galolina / 100) * 4
desconto_gasolina_maior_20 = (galolina / 100) * 6

print("\nA - Alcool   (R$ 1,90)\nG - Gasolina (R$ 2,50)")

quest = str(input("\nInforme qual combustivel será comprado (A ou G): "))

while quest != 'A' and quest != 'G' and quest != 'a' and quest != 'g':
        quest = str(input("\nInforme qual combustivel será comprado (A ou G): "))


if quest == 'A' or quest == 'a':
    litros_alcool = float(input("\nInforme a quantidade de alcool que deseja (em litros): "))

    while litros_alcool < 1:
        litros_alcool = float(input("\nInforme a quantidade de alcool que deseja (em litros): "))

    if litros_alcool < 20 or litros_alcool == 20:
        valor_alcool = (litros_alcool * alcool) - (desconto_alcool * litros_alcool)
        print(f"\nValor a ser pago: {valor_alcool} reais")

    elif litros_alcool > 20:
        valor_alcool = (litros_alcool * alcool) - (desconto_alcool_maior_20 * litros_alcool)
        print(f"\nValor a ser pago: {valor_alcool} reais")


elif quest == 'g' or quest == 'G':
    litros_gasolina = float(input("\nInforme a quantidade de gasolina que deseja (em litros): "))

    while litros_gasolina < 1:
        litros_gasolina = float(input("\nInforme a quantidade de gasolina que deseja (em litros): "))

    if litros_gasolina < 20 or litros_gasolina == 20:
        valor_gasolina = (litros_gasolina * galolina) - (desconto_gasolina * litros_gasolina)
        print(f"\nValor a ser pago: {valor_gasolina} reais")

    elif litros_gasolina > 20:
        valor_gasolina = (litros_gasolina * galolina) - (desconto_gasolina_maior_20 * litros_gasolina)
        print(f"\nValor a ser pago: {valor_gasolina} reais")






