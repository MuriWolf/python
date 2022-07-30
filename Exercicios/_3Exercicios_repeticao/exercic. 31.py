# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar.
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra.
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco.
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

# A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00

print('''
Informe o valor dos produtos,
Digite 0 para finalizar a compra.
''')

produtos = []
produto = 4332 # <-- numero qualquer
numeracao = 0

while produto != 0:
    numeracao = numeracao + 1
    produto = int(input(f"\nInforme o valor do produto {numeracao} (em reais): "))
    if produto > 0:
        produtos.append(produto)
    elif produto < 0:
        print("\nDigite apenas numeros acima de 0 ou 0 para encerrar.")

total = sum(produtos)
dinheiro = float(input("\nInforme o dinheiro que sera dado: "))
troco = dinheiro - total

# A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara
print("\nLojas Tajabara\n")

# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
numeracaoWhile = -1
while numeracaoWhile + 1 < len(produtos):
    numeracaoWhile = numeracaoWhile + 1
    print(f"PRODUTO {numeracaoWhile + 1}...R$ {produtos[numeracaoWhile]}")

# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
print(f'''TOTAL.......R$ {total}
DINHEIRO....R$ {dinheiro}
TROCO.......R$ {troco}
''')                    # linha 40 do codigo