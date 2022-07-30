# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

# Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# O consumo é especificado no construtor e o nível de combustível inicial é 0.
# Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
# Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

# meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
# meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
# meuFusca.andar(100);            # anda 100 quilômetros.
# meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.

import time 

class carro:
    def __init__(self, consumo_por_km=0, combustivel=0):
        self.consumo_por_km = consumo_por_km
        self.combustivel = combustivel

    def andar(self):
        quilometros = int(input(f"Quilometros que serao andados: "))

        gasolina_gasta = quilometros * (self.consumo_por_km)

        if self.combustivel - gasolina_gasta < 0:
            print("Falta combustivel para essa viagem, tente encher o tanque")
        elif self.combustivel - gasolina_gasta >= 0:
            self.combustivel = self.combustivel - gasolina_gasta
            print('Andando...')
            time.sleep(quilometros / 3)
            print('Voce chegou no destino!')

    def adicionarGasolina(self):
        qtde_combustivel = int(input("Quantidade de combustivel (em litros): "))
        self.combustivel = self.combustivel + qtde_combustivel

    def obterGasolina(self):
        print(f"O tanque tem {self.combustivel} litros de combsutivel")


def main():
    carro_01 = carro(4, 100)
    while True:
        escolha = int(input(f"""
{'='*40}
1- Andar
2- Adicionar combustivel
3- Ver combustivel

0- Desligar o carro
{'='*40}
>>> """))
        if escolha == 1:
            carro_01.andar()
        if escolha == 2:
            carro_01.adicionarGasolina()
        if escolha == 3:
            carro_01.obterGasolina()
        if escolha == 0:
            print('Desligando o motor...')
            break 

main()