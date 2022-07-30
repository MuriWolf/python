# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("\nDigite um numero inteiro de 1 até 7: "))

def dia_da_semana():
    numero = int(input("\nDigite um numero inteiro de 1 até 7: "))

    if numero == 1:
        print("Domingo")

    elif numero == 2:
        print("Segunda-feira")

    elif numero == 3:
        print("Terça-feira")

    elif numero == 4:
        print("Quarta-feira")

    elif numero == 5:
        print("Quinta-feira")

    elif numero == 6:
        print("Sexta-feira")

    elif numero == 7:
        print("Sábado")

while numero != 1 and 2 and 3 and 4 and 5 and 6 and 7:
    dia_da_semana()