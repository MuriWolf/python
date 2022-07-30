# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
# O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
# e depois informe a média dos saltos conforme a descrição acima informada
# (retirar o melhor e o pior salto e depois calcular a média).
# Faça uso de uma lista para armazenar os saltos.
# Os saltos são informados na ordem da execução, portanto não são ordenados.
# O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
#
# Resultado final:
# Rodrigo Curvêllo: 5.9 m

totalMedias = [] # talvez fazer o ganhador!
nome = ['a']
saltos = []

while len(nome[0]) > 0:
    nome.clear()
    nomeInput = input("\nDigite o nome do atleta: ")
    nome.append(nomeInput)

    if len(nome[0]) > 0:
        print("\nDigite a distancia em metros!")
        saltos.clear()
        for i in range(5):
            salto = float(input(f"\nDigite a distancia do salto {i + 1}: "))
            saltos.append(salto)
        print(f'''
Primeiro salto: {saltos[0]} m
Segundo salto: {saltos[1]} m
Terceiro salto: {saltos[2]} m
Quarto salto: {saltos[3]} m
Quinto salto: {saltos[4]} m

Melhor salto: {max(saltos)} m
Pior salto: {min(saltos)} m
Média dos saltos: {sum(saltos) / 5} m

Resultado final:
{nome[0]}: {sum(saltos) / 5} m
''')

    elif len(nome[0]) == 0:
        print('Ganhador:')
