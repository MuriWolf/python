# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#
# ------------------------------------------------------
#                 Até 5 Kg                Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# ------------------------------------------------------

# Se o cliente comprar mais de 8 Kg em frutas
# ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.

# preco por quilo
maca = float(input("\nInforme a quantidade de maças que sera comprada (em kg): "))

while maca < 1:
    maca = float(input("\nInforme a quantidade de maças que sera comprada (em kg): "))

morango = float(input("\nInforme a quantidade de morango que sera comprada (em kg): "))

while morango < 1:
    morango = float(input("\nInforme a quantidade de morango que sera comprada (em kg): "))

# maça
preco_maca = 1.80 * maca
preco_maca_acima_5 = 1.50 * maca

if maca == 5 or maca < 5:
    print(f"\nPreço da maça: {preco_maca:.2f} reais")

elif maca > 5 and maca < 8 or maca == 8:
    print(f"\nPreço da maça: {preco_maca_acima_5:.2f} reais")

elif preco_maca_acima_5 == 25 or preco_maca_acima_5 > 25 or maca > 8:

    maca_um_porcento = preco_maca_acima_5 / 100
    maca_10_porcento = maca_um_porcento * 10
    preco_maca_acima_5 = preco_maca_acima_5 - maca_10_porcento

    print(f"\nPreço da maça: {preco_maca_acima_5:.2f} reais")

# morango
preco_morango = 2.50 * morango
preco_morango_acima_5 = 2.20 * morango

if morango == 5 or morango < 5:
    print(f"\nPreço do  morango: {preco_morango:.2f} reais")

elif morango > 5 and morango < 8 or morango == 8:
    print(f"\nPreço da morango: {preco_morango_acima_5:.2f} reais")

elif preco_morango_acima_5 == 25 or preco_morango_acima_5 > 25 or morango > 8:

    morango_um_porcento = preco_morango_acima_5 / 100
    morango_dez_porcento = morango_um_porcento * 10
    preco_morango_acima_5 = preco_morango_acima_5 - morango_dez_porcento

    print(f"\nPreço do morango: {preco_morango_acima_5:.2f} reais")