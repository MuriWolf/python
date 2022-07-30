# O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

print('''
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00      
''')

pedido = 123

tipos = [0, 100, 101, 102, 103, 104, 105]
CachorroQuente = []
BauruSimple = []
BauruComOvo = []
Hamburguer = []
Cheeseburguer = []
Refrigerante = []
total = []

print("Digite (0) na area de informar o código do pedido para encerrar")

while pedido != 0:
    pedido = int(input("\nInforme o código de qual pedido voce deseja (0 para encerrar): "))
    if pedido == 0:
        pass
    else:
        while pedido not in tipos:
            pedido = int(input("\nInforme o código de qual pedido voce deseja (0 para encerrar): "))
        quantidade = int(input("Informe qual a quantidade que voce deseja desse item: "))

        if pedido == 100:
            conta = quantidade * 1.20
            CachorroQuente.append(conta)
            total.append(conta)
        elif pedido == 101:
            conta = quantidade * 1.30
            BauruSimple.append(conta)
            total.append(conta)
        elif pedido == 102:
            conta = quantidade * 1.50
            BauruComOvo.append(conta)
            total.append(conta)
        elif pedido == 103:
            conta = quantidade * 1.20
            Hamburguer.append(conta)
            total.append(conta)
        elif pedido == 104:
            conta = quantidade * 1.30
            Cheeseburguer.append(conta)
            total.append(conta)
        elif pedido == 105:
            conta = quantidade * 1
            Refrigerante.append(conta)
            total.append(conta)

print(f'''
Produto:            Preço a pagar:
Cachorro Quente    R$ {int(sum(CachorroQuente))}
Bauru Simples      R$ {int(sum(BauruSimple))}
Bauru com ovo      R$ {int(sum(BauruComOvo))}
Hambúrguer         R$ {int(sum(Hamburguer))}
Cheeseburguer      R$ {int(sum(Cheeseburguer))}
Refrigerante       R$ {int(sum(Refrigerante))}

TOTAL:
R$ {sum(total)} 
''')
