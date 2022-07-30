# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

products = []

print("Digite o preço de 3 produtos.\n")
for i in range(0,3):
    product = float(input("Digite o preço do produto " + str(i + 1) + ": "))
    products.append(product)

minimum_products = min(products)

print(f"\nEntre os preços desses produtos {products},\nO mais barato é o que custa {minimum_products}.")