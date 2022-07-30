# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas e % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25

# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

divida = float(input("\nInforme o valor de sua divida: "))
umPorCentoDivida = divida / 100

PorcentagemJuros = -10
QtParcelas = -1

# parte 1 print
print("\nValor da Dívida: Valor dos Juros: Quantidade de Parcelas: Valor da Parcela:")

for i in range(5):
    # parte dos juros
    if PorcentagemJuros == -10 or PorcentagemJuros == 0:
        PorcentagemJuros = PorcentagemJuros + 10
        ValorJuros = (PorcentagemJuros * umPorCentoDivida)
        DividaComJuros = ValorJuros + divida
    else:
        PorcentagemJuros = PorcentagemJuros + 5
        ValorJuros = (PorcentagemJuros * umPorCentoDivida)
        DividaComJuros = ValorJuros + divida

    # parte das parcelas + os prints
    if QtParcelas == -1:
        QtParcelas = QtParcelas + 2
        DivisaoParcelas = DividaComJuros / QtParcelas
        print(f"R$ {DividaComJuros}         {ValorJuros}             {QtParcelas}                       R$ {DivisaoParcelas:.2f}")
    elif QtParcelas == 1:
        QtParcelas = QtParcelas + 2
        DivisaoParcelas = DividaComJuros / QtParcelas
        print(f"R$ {DividaComJuros}         {ValorJuros}           {QtParcelas}                       R$ {DivisaoParcelas:.2f}")
    else:
        QtParcelas = QtParcelas + 3
        DivisaoParcelas = DividaComJuros / QtParcelas
        print(f"R$ {DividaComJuros}         {ValorJuros}           {QtParcelas}                       R$ {DivisaoParcelas:.2f}")
