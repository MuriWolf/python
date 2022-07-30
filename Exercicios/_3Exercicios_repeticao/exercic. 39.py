# Faça um programa que leia dez conjuntos de dois valores,
# o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
# Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas

maisAlto = [0, 0]

for i in range(3):
    codigo = float(input("\nDigite seu código: "))
    altura = float(input("Digite sua altura (em centimetros): "))

    if altura > maisAlto[1]:
        del maisAlto[0]
        maisAlto.insert(0, codigo)
        del maisAlto[1]
        maisAlto.insert(1, altura)

print(f'''
Informações do aluno mais alto:

Codigo: {maisAlto[0]}
Altura: {maisAlto[1]} centimetros
''')

