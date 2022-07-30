# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
# que já é um sucesso na sua loja de 1,99.
# Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães,

# a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

preco_inicial = float(input("\nInforme o preço do pão: "))

num_ordem = 0
preco = 0

print("\n----------------------------------------------")
print("Panificadora Pão de Ontem - Tabela de preços\n")

for i in range(50):
    num_ordem = num_ordem + 1
    preco = preco + preco_inicial
    if num_ordem < 10:
        print(f"0{num_ordem} - R$ {preco:.2f}")
    else:
        print(f"{num_ordem} - R$ {preco:.2f}")
print("\n----------------------------------------------")