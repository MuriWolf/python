# Numa eleição existem três candidatos.
# Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

QtCandidato1 = 0
QtCandidato2 = 0
QtCandidato3 = 0

QtEleitores = int(input("\nInforme a quantidade de eleitores: "))

print('''
---------------------------------------
Numero equivalente para cada candidato

Cantidato 1 = ( 1 )
Candidato 2 = ( 2 )
Cantidato 3 = ( 3 )
---------------------------------------''')

print("\n                       !!! AVISO !!!\n\nCaso o eleitor não digite (1, 2 ou 3), seu voto não será contado.")

for i in range(QtEleitores):
    voto = int(input("\nInforme qual canditato sera votado (1, 2 ou 3): "))

    if voto == 1:
        QtCandidato1 = QtCandidato1 + 1
    elif voto == 2:
        QtCandidato2 = QtCandidato2 + 1
    elif voto == 3:
        QtCandidato3 = QtCandidato3 + 1

print(f'''
---------------------------------------
Quantidade de votos para cada candidato

Candidato 1: {QtCandidato1} votos
Candidato 2: {QtCandidato2} votos
Candidato 3: {QtCandidato3} votos
---------------------------------------
''')