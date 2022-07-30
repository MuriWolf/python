# Faça um Programa para uma loja de tintas
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados,
# e que a tinta é vendida em
# latas de 18 litros que custam R$ 80,00
# ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("\nInforme em metros² a area que será pintada: ")) # ex: 550 metros

while area < 1:
    print("\nDigite um numero maior que 0")
    area = float(input("Informe em metros² a area que será pintada: "))  # ex: 550 metros

# LATA

lata = 0 # / 18 litros = 1 lata / 1 litro = 6 metros² / 1 lata = 108 metros²

area_lata = 0

dinheiro_lata = 0 # 80 reais uma lata

# GALAO

galao = 0

area_galao = 0 # / 3.6 litros = 1 galao / 1 litro = 6 metros² / 1 galao = 21.6 metros²

dinheiro_galao = 0 # 25 reais um galao²


# APENAS LATAS DE 18 LITROS
while area > area_lata:
    lata = lata + 1
    area_lata = area_lata + 108
    dinheiro_lata = dinheiro_lata + 80

print("\nOPÇÃO APENAS LATAS")

if lata > 1:

    print(f"\nQuantidade de latas:\nPara pintar {area} metros² será necessario {lata} latas de tinta de 18 litros.")
    print(f"\nPreço das latas:\nO preço ficará em {dinheiro_lata} reais.\n")

else:
    print(f"\nQuantidade de latas:\nPara pintar {area} metros² será necessario {lata} latas de tinta de 18 litros.")
    print(f"\nPreço das latas:\nO preço ficará em {dinheiro_lata} reais.\n")


# APENAS GALOES DE 3.6 LITROS
while area > area_galao:
    galao = galao + 1
    area_galao = area_galao + 21.6
    dinheiro_galao = dinheiro_galao + 25

print("\nOPÇÃO APENAS GALOES")

if galao > 1:
    print(f"\nQuantidade de galoes:\nPara pintar {area} metros² será necessario {galao} galoes de tinta de 3.6 litros.")
    print(f"\nPreço dos galoes:\nO preço ficará em {dinheiro_galao} reais.\n")

else:
    print(f"\nQuantidade de galoes:\nPara pintar {area} metros² será necessario {galao} galoes de tinta de 3.6 litros.")
    print(f"\nPreço dos galoes:\nO preço ficará em {dinheiro_galao} reais.\n")


# GALOES E LATAS JUNTAS
lata = 0
area_lata = 0
dinheiro_lata = 0
galao = 0
area_galao = 0
dinheiro_galao = 0

while area > area_lata:
    lata = lata + 1
    area_lata = area_lata + 108
    dinheiro_lata = dinheiro_lata + 80

while area_lata > area:
    lata = lata - 1
    area_lata = area_lata - 108
    dinheiro_lata = dinheiro_lata - 80

    galao = galao + 1
    area_galao = area_galao + 21.6
    dinheiro_galao = dinheiro_galao + 25

dinheiro_juntos = dinheiro_galao + dinheiro_lata

print("\nOPÇÃO LATAS E GALOES")

if galao > 1:
    print(f"\nQuantidade de latas e galoes:\nPara pintar {area} metros² será necessario {lata} latas de tinta de 18 litros e {galao} galoes de tinta de 3.6 litros.")
    print(f"\nPreço das latas e galoes:\nO preço ficará em {dinheiro_juntos} reais.")

else:
    print(f"\nQuantidade de latas e galoes:\nPara pintar {area} metros² será necessario {lata} latas de tinta de 18 litros e {galao} galao de tinta de 3.6 litros.")
    print(f"\nPreço das latas e galoes:\nO preço ficará em {dinheiro_juntos} reais.")