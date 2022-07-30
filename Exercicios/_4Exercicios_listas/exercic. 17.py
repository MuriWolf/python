# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta
# em seus saltos e depois informe o nome,
# os saltos e a média dos saltos.
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo
# Curvêllo
#
# Primeiro Salto: 6.5m
# Segundo Salto: 6.1m
# Terceiro Salto: 6.2m
# Quarto Salto: 5.4m
# Quinto Salto: 5.3m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

nomeVencedor = 'a'
maiorMedia = 0
saltosVencedor = [0,0,0,0,0]

nome = 'abc'
saltos = [1]

while len(nome) > 0:
    nome = input("\nDigite o nome do atleta: ")

    if len(nome) > 0:
        saltos.clear()
        for i in range(5):
            salto = float(input(f"\nDigite a distancia do salto {i + 1}: "))
            saltos.append(salto)
        media = sum(saltos) / 5

        if media > maiorMedia:
            nomeVencedor = nome
            saltosVencedor = saltos
            maiorMedia = media

print(f"\nResultado Final:\nAtleta: {nomeVencedor}")

for i in range(5):
    # primeiro print
    if i == 0:
        print(f"Saltos: {saltosVencedor[i]} - ", end='')
    if i > 0 and i < 4:
        print(f"{saltosVencedor[i]} - ", end='')
    # ultimo print
    elif i == 4:
        print(f"{saltosVencedor[i]}")

print(f"Média dos saltos: {maiorMedia:.1f} m")