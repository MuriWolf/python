# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel.
# valorLitro
# quantidadeCombustivel

# Possua no mínimo esses métodos:
# abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterarValor( ) – altera o valor do litro do combustível.
# alterarCombustivel( ) – altera o tipo do combustível.
# alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

from time import sleep

class bombaCombustivel:
    def __init__(self, tipo_combustivel="unknown", valor_litro=0, quantidade=0):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade = quantidade
        
    def abastecer_por_litro(self):
        qtde_litro = float(input("> Quantidade de litros a ser colocado: "))
        valor = qtde_litro * self.valor_litro
        print(f"Valor a pagar: R$ {valor:.2f}")
        self.quantidade = self.quantidade - qtde_litro

    def abastecer_por_valor(self):
        qtde_valor = float(input("> Valor a ser colocado: "))
        litros = qtde_valor / self.valor_litro
        print(f"Quantidade litros: {litros:.2f} L")
        self.quantidade = self.quantidade - litros

    def alterar_valor(self):
        novo_valor = float(input(f"> Novo valor do combustivel: "))
        self.valor_litro = novo_valor

    def alterar_combustivel(self):
        novo_combustivel = str(input("> Novo comsutivel: "))
        self.tipo_combustivel = novo_combustivel
        
    def alterar_quantidade_combustivel(self):
        qtde_combustivel = float(input("Nova quantidade de combustivel do tanque: "))
        self.quantidade = qtde_combustivel

def main():
    bomba_combustivel_01 = bombaCombustivel("gasolina", 4.23, 5000)
    while True:
        escolha = int(input(f"""


{'='*40}
Combustivel atual: {bomba_combustivel_01.tipo_combustivel}
Valor do combustivel atual: {bomba_combustivel_01.valor_litro}
Quantidade disponivel no tanque: {bomba_combustivel_01.quantidade:.2f}
{'='*40}
1- Abastecer por litro
2- Abastecer por valor

3- Alterar combustivel
4- Alterar valor do combustivel
5- Alterar quantidade do tanque

0- Sair
{'='*40}
>>> """))
        if escolha == 1:
            bomba_combustivel_01.abastecer_por_litro()
        if escolha == 2:
            bomba_combustivel_01.abastecer_por_valor()
        if escolha == 3:
            bomba_combustivel_01.alterar_combustivel()
        if escolha == 4:
            bomba_combustivel_01.alterar_valor()
        if escolha == 5:
            bomba_combustivel_01.alterar_quantidade_combustivel()
        elif escolha == 0:
            break
        sleep(3)
main()

#formatar o tamanho dos numeros