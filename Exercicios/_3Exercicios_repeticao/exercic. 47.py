# Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
# Você deve fazer um programa que receba o nome do ginasta
# e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média,
# conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
#
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

notas = []
nome = ['a']
vencedor = [0,0]

while len(nome[0]) > 0:
    # pedir nome
    nome.clear()
    atleta = input("\n\nDigite o nome do atleta: ")
    nome.append(atleta)

    if len(nome[0]) > 0:
        notas.clear()
        # pedir notas
        for i in range(7):
            nota = float(input("\nDigite a nota do atleta: "))
            notas.append(nota)

        # ver a maior/menor nota e fazer a media
        maiorNota = max(notas)
        menorNota = min(notas)
        lista = sorted(notas)
        del lista[-1]
        del lista[-1]
        media = (sum(lista) / 7)

        # verificar quem é o que fez mais pontos
        if media > vencedor[-1]:
            del vencedor[0]
            vencedor.insert(0,nome[0])
            del vencedor[-1]
            vencedor.insert(1, media)

        # printar as informacoes do atleta
        print(f'''
Nota: {notas[0]}
Nota: {notas[1]}
Nota: {notas[2]}
Nota: {notas[3]}
Nota: {notas[4]}
Nota: {notas[5]}
Nota: {notas[6]}
    
Resultado final:
Nome: {nome[0]}
maiorNota: {max(notas)}
menorNota: {min(notas)}
Media: {media:.1f}
''')

    # printar as informacoes do vencedor
    elif len(nome[0]) == 0:
        print(f'''
Vencedor:

Nome:
{vencedor[0]}

Media:
{vencedor[1]:.1f}
''')