# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#
# contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print('''
Carnes          Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg''')

print('''
1 - File Duplo
2 - Alcantra
3 - Picanha
''')

def comCartao():
    print(f'''
Tipo da carne
{nome_carne}

Quantidade da carne
{quantidade_carne} kg(s)

Preço total
{preco_total} reais

Tipo do pagamento
{cartao}

Valor do desconto
{porcentagem_desconto}

VALOR A PAGAR
{preco_cartao} reais
''')
        
def semCartao():
    print(f'''
    Tipo da carne
    {tipo_carne}

    Quantidade da carne
    {quantidade_carne} kg(s)

    Preço total
    {preco_total} reais

    Tipo do pagamento
    {sem_cartao}

    Valor do desconto
    {porcentagem_sem_desconto}

    VALOR A PAGAR
    {preco_total} reais
    ''')

cartao = 'Cartão Tajabara'
sem_cartao = 'cartão de Crédito'
porcentagem_desconto = '5%'
porcentagem_sem_desconto = '0%'

tipo_carne = int(input("Informe o tipo de carne que deseja (1, 2 ou 3): "))
while tipo_carne != 1 and tipo_carne != 2 and tipo_carne != 3:
    tipo_carne = int(input("Informe o tipo de carne que deseja (1, 2 ou 3): "))

quantidade_carne = int(input("\nInforme a quantidade em quilos que deseja: "))
while quantidade_carne < 1:
    quantidade_carne = int(input("\nInforme a quantidade em quilos que deseja: "))

opcao_cartao = int(input("\nDeseja usar o cartão Tajabara? (1 p/sim e 2 p/ não): "))
while opcao_cartao != 1 and opcao_cartao != 2:
    opcao_cartao = int(input("\nDeseja usar o cartão Tajabara? (1 p/sim e 2 p/ não): "))

# Tipo de carne (File duplo)
if tipo_carne == 1:
    if quantidade_carne <= 5:
        nome_carne = 'File Duplo'
        preco_carne = 4.90
        preco_total = quantidade_carne * preco_carne
        if opcao_cartao == 1:
            preco_cartao = preco_total - ((preco_total * 5) / 100)
            comCartao()
        elif opcao_cartao == 2:
            semCartao()

    else:
        nome_carne = 'File Duplo'
        preco_carne = 5.80
        preco_total = quantidade_carne * preco_carne
        if opcao_cartao == 1:
            preco_cartao = preco_total - ((preco_total * 5) / 100)
            comCartao()
        elif opcao_cartao == 2:
            semCartao()

# Tipo de carne (Alcatra)
elif tipo_carne == 2:
    if quantidade_carne <= 5:
        nome_carne = 'Alcatra'
        preco_carne = 5.90
        preco_total = quantidade_carne * preco_carne
        if opcao_cartao == 1:
            preco_cartao = preco_total - ((preco_total * 5) / 100)
            comCartao()
        elif opcao_cartao == 2:
            semCartao()

    else:
        nome_carne = 'Alcatra'
        preco_carne = 6.80
        preco_total = quantidade_carne * preco_carne
        if opcao_cartao == 1:
            preco_cartao = preco_total - ((preco_total * 5) / 100)
            comCartao()
        elif opcao_cartao == 2:
            semCartao()

# Tipo de carne (Picanha)
elif tipo_carne == 3:
    if quantidade_carne <= 5:
        nome_carne = 'Picanha'
        preco_carne = 6.90
        preco_total = quantidade_carne * preco_carne
        if opcao_cartao == 1:
            preco_cartao = preco_total - ((preco_total * 5) / 100)
            comCartao()
        elif opcao_cartao == 2:
            semCartao()

    else:
        nome_carne = 'Picanha'
        preco_carne = 7.80
        preco_total = quantidade_carne * preco_carne
        if opcao_cartao == 1:
            preco_cartao = preco_total - ((preco_total * 5) / 100)
            comCartao()
        elif opcao_cartao == 2:
            semCartao()

# maneira "errada" de fazer:

# cartao = 'Cartão Tajabara'
#
# print("ESCOLHA APENAS UM DOS TIPOS DE CARNE EM PREMOÇÃO!")
# escolha = str(input("\nInforme qual dessas carnes será comprada (F, A ou P): "))
#
# # File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg ------------------------------------------------------------
# if escolha == 'F' or escolha == 'f':
#     KgFileDuplo = int(input("\nInfome a quantidade de carne que será comprada (em kg): "))
#
#     # se o peso da carne for até 5 kg
#     if KgFileDuplo == 5 or KgFileDuplo < 5 and KgFileDuplo > 0:
#         print("\n * Comprar com o cartão Tajabara dará 5% de desconto * \n")
#
#         # preco file duplo
#         FileDuploAte5 = 4.90 * KgFileDuplo
#
#         # Desconto cartao Tajabara
#         CartaoTajabara = FileDuploAte5 / 100
#         CartaoTajabara = CartaoTajabara * 5
#
#         # se a escolha do cartão for sim
#         EscolhaCartao = str(input("Comprar com o cartão Tajabara? (S - sim, N -nao): "))
#         if EscolhaCartao == 'S' or EscolhaCartao == 's':
#             PrecoCarneCartao = FileDuploAte5 - CartaoTajabara
#             # tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
#             print(
# f'''
# Tipo
# {F}
#
# Quantidade
# {KgFileDuplo} kg(s)
#
# Preço Total
# {FileDuploAte5} reais
#
# Tipo de pagamento
# {cartao}
#
# Valor do desconto
# 5%
#
# Valor a pagar
# {PrecoCarneCartao} reais
# ''')
#
#         # se a escolha do cartão for não
#         elif EscolhaCartao == 'N' or EscolhaCartao == 'n':
#             print(f'''
# Tipo
# {F}
#
# Quantidade
# {KgFileDuplo} kg(s)
#
# Preço Total
# {FileDuploAte5} reais
#
# Tipo de pagamento
# Cartão de crédito
#
# Valor do desconto
# 0%
#
# Valor a pagar
# {FileDuploAte5} reais
# ''')
#
# # File duplo, kilo maior que 5 ----------------------------------------------------------------------------
#     elif KgFileDuplo > 5:
#         print("\n * Comprar com o cartão Tajabara dará 5% de desconto * \n")
#
#         # preço file duplo acima de 5 kg
#         FileDuploAcima5 = 5.80 * KgFileDuplo
#
#         # Desconto cartao Tajabara
#         CartaoTajabara = FileDuploAcima5 / 100
#         CartaoTajabara = CartaoTajabara * 5
#
#         EscolhaCartao = str(input("Comprar com o cartão Tajabara? (S - sim, N -nao): "))
#
#         # se a escolha do cartão for igual a sim
#         if EscolhaCartao == 'S' or EscolhaCartao == 's':
#             PrecoCarneCartao = FileDuploAcima5 - CartaoTajabara
#             print(f'''
# Tipo
# {F}
#
# Quantidade
# {KgFileDuplo} kg(s)
#
# Preço Total
# {FileDuploAcima5} reais
#
# Tipo de pagamento
# {cartao}
#
# Valor do desconto
# 5%
#
# Valor a pagar
# {PrecoCarneCartao} reais
# ''')
#
#         # se a escolha do cartão for igual a não
#         elif EscolhaCartao == 'N' or EscolhaCartao == 'n':
#             print(f'''
# Tipo
# {F}
#
# Quantidade
# {KgFileDuplo} kg(s)
#
# Preço Total
# {FileDuploAcima5} reais
#
# Tipo de pagamento
# cartao de crédito
#
# Valor do desconto
# 0%
#
# Valor a pagar
# {FileDuploAcima5} reais
# ''')
#
#
#
#
# # Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg ------------------------------------------------------------
# elif escolha == 'A' or escolha == 'a':
#     KgAlcatra = int(input("\nInfome a quantidade de carne que será comprada (em kg): "))
#
#     # se o peso da carne for menor que 5
#     if KgAlcatra == 5 or KgAlcatra < 5 and KgAlcatra > 0:
#         print("\n * Comprar com o cartão Tajabara dará 5% de desconto * \n")
#
#         # preco file duplo
#         AlcatraAte5 = 5.90 * KgAlcatra
#
#         # Desconto cartao Tajabara
#         CartaoTajabara = AlcatraAte5 / 100
#         CartaoTajabara = CartaoTajabara * 5
#
#         # se a escolha do cartão for igual a sim
#         EscolhaCartao = str(input("Comprar com o cartão Tajabara? (S - sim, N -nao): "))
#         if EscolhaCartao == 'S' or EscolhaCartao == 's':
#             PrecoCarneCartao = AlcatraAte5 - CartaoTajabara
#             # tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
#             print(
#                 f'''
# Tipo
# {A}
#
# Quantidade
# {KgAlcatra} kg(s)
#
# Preço Total
# {AlcatraAte5} reais
#
# Tipo de pagamento
# {cartao}
#
# Valor do desconto
# 5%
#
# Valor a pagar
# {PrecoCarneCartao} reais
# ''')
#
#         # se a escolha do cartão for igual a nao
#         elif EscolhaCartao == 'N' or EscolhaCartao == 'n':
#             print(f'''
# Tipo
# {A}
#
# Quantidade
# {KgAlcatra} kg(s)
#
# Preço Total
# {AlcatraAte5} reais
#
# Tipo de pagamento
# Cartão de crédito
#
# Valor do desconto
# 0%
#
# Valor a pagar
# {AlcatraAte5} reais
# ''')
#
# # Alcatra, kilo maior que 5 ----------------------------------------------------------------------------
#     elif KgAlcatra > 5:
#         print("\n * Comprar com o cartão Tajabara dará 5% de desconto * \n")
#
#     # preço file duplo acima de 5 kg
#     AlcatraAcima5 = 6.80 * KgAlcatra
#
#     # Desconto cartao Tajabara
#     CartaoTajabara = AlcatraAcima5 / 100
#     CartaoTajabara = CartaoTajabara * 5
#
#     EscolhaCartao = str(input("Comprar com o cartão Tajabara? (S - sim, N -nao): "))
#
#     # se a escolha do cartão for igual a sim
#     if EscolhaCartao == 'S' or EscolhaCartao == 's':
#         PrecoCarneCartao = AlcatraAcima5 - CartaoTajabara
#         print(f'''
# Tipo
# {A}
#
# Quantidade
# {KgAlcatra} kg(s)
#
# Preço Total
# {AlcatraAcima5} reais
#
# Tipo de pagamento
# {cartao}
#
# Valor do desconto
# 5%
#
# Valor a pagar
# {PrecoCarneCartao} reais
# ''')
#
#     # se a escolha do cartão for igual a nao
#     elif EscolhaCartao == 'N' or EscolhaCartao == 'n':
#         print(f'''
# Tipo
# {A}
#
# Quantidade
# {KgAlcatra} kg(s)
#
# Preço Total
# {AlcatraAcima5} reais
#
# Tipo de pagamento
# Cartão de crédito
#
# Valor do desconto
# 0%
#
# Valor a pagar
# {AlcatraAcima5} reais
# ''')
#
#
#
#
# # Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# elif escolha == 'P' or escolha == 'p':
#     KgPicanha = int(input("\nInfome a quantidade de carne que será comprada (em kg): "))
#
#     # se o peso da carne for menor que 5
#     if KgPicanha == 5 or KgPicanha < 5 and KgPicanha > 0:
#         print("\n * Comprar com o cartão Tajabara dará 5% de desconto * \n")
#
#         # preco picanha
#         PicanhaAte5 = 6.90 * KgPicanha
#
#         # Desconto cartao Tajabara
#         CartaoTajabara = PicanhaAte5 / 100
#         CartaoTajabara = CartaoTajabara * 5
#
#         # se a escolha do cartão for igual a sim
#         EscolhaCartao = str(input("Comprar com o cartão Tajabara? (S - sim, N -nao): "))
#         if EscolhaCartao == 'S' or EscolhaCartao == 's':
#             PrecoCarneCartao = PicanhaAte5 - CartaoTajabara
#             # tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
#             print(
#                 f'''
# Tipo
# {P}
#
# Quantidade
# {KgPicanha} kg(s)
#
# Preço Total
# {PicanhaAte5} reais
#
# Tipo de pagamento
# {cartao}
#
# Valor do desconto
# 5%
#
# Valor a pagar
# {PrecoCarneCartao} reais
# ''')
#
#         # se a escolha do cartão for igual a nao
#         elif EscolhaCartao == 'N' or EscolhaCartao == 'n':
#             print(f'''
# {P}
#
# Quantidade
# {KgPicanha} kg(s)
#
# Preço Total
# {PicanhaAte5} reais
#
# Tipo de pagamento
# Cartão de crédito
#
# Valor do desconto
# 0%
#
# Valor a pagar
# {PicanhaAte5} reais
# ''')
#
#     elif KgPicanha > 5:
#         print("\n * Comprar com o cartão Tajabara dará 5% de desconto * \n")
#
#     # preço file duplo acima de 5 kg
#     PicanhaAcima5 = 7.80 * KgPicanha
#
#     # Desconto cartao Tajabara
#     CartaoTajabara = PicanhaAcima5 / 100
#     CartaoTajabara = CartaoTajabara * 5
#
#     EscolhaCartao = str(input("Comprar com o cartão Tajabara? (S - sim, N -nao): "))
#
#     # se a escolha do cartão for igual a sim
#     if EscolhaCartao == 'S' or EscolhaCartao == 's':
#         PrecoCarneCartao = PicanhaAcima5 - CartaoTajabara
#         print(f'''
# Tipo
# {P}
#
# Quantidade
# {KgPicanha} kg(s)
#
# Preço Total
# {PicanhaAcima5} reais
#
# Tipo de pagamento
# {cartao}
#
# Valor do desconto
# 5%
#
# Valor a pagar
# {PrecoCarneCartao} reais
# ''')
#
#     # se a escolha do cartão for igual a nao
#     elif EscolhaCartao == 'N' or EscolhaCartao == 'n':
#         print(f'''
# Tipo
# {P}
#
# Quantidade
# {KgPicanha} kg(s)
#
# Preço Total
# {PicanhaAcima5} reais
#
# Tipo de pagamento
# Cartão de crédito
#
# Valor do desconto
# 0%
#
# Valor a pagar
# {PicanhaAcima5} reais
# ''')
#
# # End :)