# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

print('''
Opcoes de codigos para votar:

1 - Joao 
2 - Lucas 
3 - Jonh 
4 - Jorge

5 - Voto nulo
6 - voto em branco
0 - Encerrar a votação 
''')

voto = 123
tipos = [0,1,2,3,4,5,6]

Votos1 = []
Votos2 = []
Votos3 = []
Votos4 = []
VotosNulo = []
VotosBranco = []
total = []

while voto != 0:
    voto = (int(input("\nInforme em Quem/oque voce votará: ")))
    while voto not in tipos:
        print("\nDigite de 0 até 6!")
        voto = (int(input("Informe em Quem/oque voce votará: ")))
    if voto == 1:
        Votos1.append(1)
        total.append(1)
    elif voto == 2:
        Votos2.append(1)
        total.append(1)
    elif voto == 3:
        Votos3.append(1)
        total.append(1)
    elif voto == 4:
        Votos4.append(1)
        total.append(1)
    elif voto == 5:
        VotosNulo.append(1)
        total.append(1)
    elif voto == 6:
        VotosBranco.append(1)
        total.append(1)

total = sum(total)
porcentagemVotosBranco = (sum(VotosBranco) / total) * 100
porcentagemVotosNulos = (sum(VotosNulo) / total) * 100

print(f'''
Quantidade votos:

Joao:  {sum(Votos1)}
Lucas: {sum(Votos2)}
Jonh:  {sum(Votos3)}
Jorge: {sum(Votos4)}
TOTAL: {total}

Porcentagem votos branco: {int(porcentagemVotosBranco)}%
Porcentagem votos nulo:   {int(porcentagemVotosNulos)}%
''')