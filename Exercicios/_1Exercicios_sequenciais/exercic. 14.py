# toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
# do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.

# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos
# além do limite e na variável multa o valor da multa que João deverá pagar.

# Imprima os dados do programa com as mensagens adequadas.

peso = int(input("\nInforme o peso da pesca em kilos: "))

max_quilos = 50

preco_pagar = 0

peso_extra = 0

if max_quilos >= peso:
    print("\nNao será necesario pagar multa.")

while peso > max_quilos:
    peso = peso - 1
    preco_pagar = preco_pagar + 4
    peso_extra = peso_extra + 1

    print(f"\nPESO EXTRA:\nO peso extra é de {peso_extra} kg.\n")

    print(f"PREÇO A SE PAGAR:\nO Preço a se pagar é de {preco_pagar} reais.")