# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice"
# 5 como "Assassino".

# Caso contrário, ele será classificado como "Inocente".

print("\nResponda as perguntas com sim ou não.")
print("\nS - sim\nN - não")

lista_sim = 0

quest1 = str(input("\nTelefonou para a vítima? "))
quest2 = str(input("\nEsteve no local do crime? "))
quest3 = str(input("\nMora perto da vítima? "))
quest4 = str(input("\nDevia para a vítima? "))
quest5 = str(input("\nJá trabalhou com a vítima? "))

if quest1 == 's' or quest1 == 'S':
    lista_sim = lista_sim + 1
if quest2 == 's' or quest2 == 'S':
    lista_sim = lista_sim + 1
if quest3 == 's' or quest3 == 'S':
    lista_sim = lista_sim + 1
if quest4 == 's' or quest4 == 'S':
    lista_sim = lista_sim + 1
if quest5 == 's' or quest5 == 'S':
    lista_sim = lista_sim + 1

if lista_sim == 2:
    print("\nVoce esta classificado como: Suspeito(a).")

elif lista_sim == 3 or lista_sim == 4:
    print("\nVoce esta classificado como: Cúmplice")

elif lista_sim == 5:
    print("\nVoce esta classificado como: Assassino(a).")

elif lista_sim == 0:
    print("\nVoce esta classificado como: Inocente.")