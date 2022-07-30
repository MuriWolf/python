# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

import time

class quadrado:
    def __init__(self, tamanho=0):
        self.tamanho = tamanho

    def mudar_lado(self):
        troca = str(input("\n> Deseja mudar o tamanho atual? [s/n]: "))
        troca = troca.casefold()

        if troca == "s":
            novo_tamanho = int(input("\n> Novo tamanho do lado: "))
            self.tamanho = novo_tamanho
        else:
            pass
        
    def retornar_lado(self):
        print(f"\nLado do quadrado: {self.tamanho}")

    def calcular_area(self):
        print(f"\nArea do quadrado: {self.tamanho * self.tamanho}")
    

def main():
    quadrado_01 = quadrado(5)

    while True:
        time.sleep(1.5)
        pergunta = int(input('''
Digite o numero para realizar o comando

1- mudar valor do lado
2- Retornar valor do lado
3- calcular área
0- sair

R:'''))
        if pergunta == 1:
            quadrado_01.mudar_lado()
        if pergunta == 2:
            quadrado_01.retornar_lado()
        if pergunta == 3:
            quadrado_01.calcular_area()
        if pergunta == 0:
            break

main()