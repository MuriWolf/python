# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math


# perguntar metros ou centimetros
metro_cent = (input("Digite 'm' se for digitar em metros ou 'c' se for digitar em centimetros: "))

while (metro_cent != 'm') and (metro_cent != 'c'):
    print("Digite 'm' ou 'c'!")
    metro_cent = (input("Digite 'm' se for digitar em metros ou 'c' se for digitar em centimetros: "))


# raio e conta
raio = float(input("Digite o raio do circulo: "))

conta = math.pi * (raio ** 2)


# resultado
if metro_cent == 'm':
    print(f"{conta} metros.")

elif metro_cent == 'c':
    print(f"{conta} centimetros.")
