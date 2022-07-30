# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados:

# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999).

# Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

QtVezes = 0

cidades_menos2000 = []
veiculos = []
acidentes = []

maior_indice_acidente = [0,0]
menor_indice_acidente = [999,999]

for i in range(5):
    QtVezes = QtVezes + 1
    codigo = int(input("\nDigite o código da cidade: "))
    # pedir quantidade de veiculos
    NumVeiculosPasseio = int(input("Digite a quantidade de veiculos de passeio (em 1999): "))
    veiculos.append(NumVeiculosPasseio)
    # pedir quantidade de vitimas
    NumAcidentesVitimas = int(input("Digite o numero de acidentes com vitimas (em 1999): "))
    acidentes.append(NumAcidentesVitimas)

    # verificar se o numero de acidentes é maior que a cidade anterior
    if NumAcidentesVitimas > menor_indice_acidente[1]:
        del maior_indice_acidente[0]
        maior_indice_acidente.insert(0, codigo)
        del maior_indice_acidente[1]
        maior_indice_acidente.insert(1, NumAcidentesVitimas)

    # verificar se o numero de acidentes é menor que a cidade anterior
    if NumAcidentesVitimas < menor_indice_acidente[1]:
        del menor_indice_acidente[0]
        menor_indice_acidente.insert(0, codigo)
        del menor_indice_acidente[1]
        menor_indice_acidente.insert(1, NumAcidentesVitimas)

    # verificar se a cidade tem menos que 2000, se sim colocala na lista
    if NumVeiculosPasseio < 2000:
        cidades_menos2000.append(NumVeiculosPasseio)

soma_menos2000 = sum(cidades_menos2000)
media_2000 = soma_menos2000 / QtVezes

print(f'''
Cidade com maior índice de acidentes de carro:
Código: {maior_indice_acidente[0]}
Quantidade de acidentes: {maior_indice_acidente[1]}

Cidade com menor índice de acidentes de carro:
Código: {menor_indice_acidente[0]}
Quantidade de acidentes: {menor_indice_acidente[1]}

Quantidade de veiculos de todas as cidades juntas:
{sum(veiculos)} veiculos

Média de acidentes das cidades com menos de 2000 veiculos:
{media_2000} acidentes
''')
