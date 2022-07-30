# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?",
            "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]

sim = []
nao = []

print("\nResponda as perguntas com sim[s] ou nao[n]!\n")
for i in range(5):
    resposta = (input(f"{perguntas[i]} [s/n]: "))

    while resposta !='s' and resposta !='n':
        resposta = (input(f"{perguntas[i]} [s/n]: "))
    if resposta == 's':
        sim.append(1)
    elif resposta == 'n':
        nao.append(1)

if len(sim) == 2:
    print("\nSuspeito")
elif len(sim) == 3 or len(sim) == 4:
    print("\nCumplice")
elif len(sim) == 5:
    print("\nAssassino")
else:
    print("\nInocente")

