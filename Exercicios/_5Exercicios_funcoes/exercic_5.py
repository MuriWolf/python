# Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais:

# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

denovo = ''

while denovo != 'n':
    def somaImposto(taxaImposto, custo):
        return (custo / 100) * taxaImposto + custo

    taxaImposto = float(input("\nDigite a taxa do imposto: "))
    custo = float(input("\nDigite o custo: "))

    print(f"\nValor do custo com o imposto incluido: R$ {somaImposto(taxaImposto, custo)}")

    denovo = input("\n\nDeseja utilizar o programa novamente? [s/n]: ")