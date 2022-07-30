# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada

# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = int(input("\nInforme a área a ser pintada em metros quadrados: ")) # ex: 250 metro2

area_lata = 0

lata = 0

preco_lata = 0

while area > area_lata:
    lata = lata + 1
    area_lata = area_lata + 54
    preco_lata = preco_lata + 80

print(f"\nLATAS NECESSARIAS:\nPara pintar {area} metros² irá ser necessario {lata} latas de tinta.")

print(f"\nPREÇO:\nO preço será de {preco_lata} reais.")

