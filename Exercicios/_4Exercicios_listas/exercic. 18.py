# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo.
# Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos.
# Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++.
# Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
# Um número de jogador igual zero, indica que a votação foi encerrada.
# Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
# Após o final da votação, o programa deverá exibir:

# O total de votos computados;
# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0
#
# Resultado da votação:
#
# Foram computados 8 votos.
#
# Jogador Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

votosAtletas = [0] * 24

voto = 123

print("\nDigite o numero da camisa de quem voce acha que foi o melhor jogador da partida (de 1 até 23) .\n")

# input dos votos
while voto != 0:
    voto = int(input("Numero do jogador (0=fim): "))
    if voto != 0: # erro de voto menor que 0 ou maior que 23
        if voto < 0 or voto > 23:
            print("\nDigite apenas entre 1 e 23!")
        # adicionar os votos numa lista
        else:
            votosAtletas[voto] = votosAtletas[voto] + 1

totalVotos = sum(votosAtletas)
vencedor = [0,0,0]

# printar a primeira parte do resultado mais o total de votos
print(f'''
Resultado da votação: 

Foram computados {totalVotos} votos''')

print(f"\nJogador  Numero de votos  Porcentagem")
atletasComVotos = []

for atleta in range(len(votosAtletas)): # descobrir quem teve votos
    if votosAtletas[atleta] > 0:
        atletasComVotos.append(atleta) # adiconar o numero do atleta

        decimal = votosAtletas[atleta] / totalVotos
        porcentagem = int(decimal * 100) # calcular o valor em porcentagem

        print(f"{atletasComVotos[-1]}          {votosAtletas[atleta]}               {porcentagem}%") # printar as informacoes o jgdr

        if votosAtletas[atleta] > vencedor[1]: # descobir o vencedor
            vencedor = [atletasComVotos[-1], votosAtletas[atleta], porcentagem]

# printar o vencedor
print(f"\nO melhor jogador foi o número {vencedor[0]}, com {vencedor[1]} votos, correspondendo a {vencedor[2]}% do total de votos.")