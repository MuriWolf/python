# Classe Macaco:

# Desenvolva uma classe Macaco,que possua os 
# atributos nome e bucho (estomago)

# e pelo menos os métodos
# comer(), verBucho() e digerir().
# 
#  Faça um programa ou teste interativamente, criando pelo menos dois macacos,
#  alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
#  Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class macaco:
    def __init__(self, nome="unknown", bucho=[]):
        self.nome = nome
        self.bucho = bucho

    def comer(self):
        alimento = (input("Digite o alimento que sera comido: "))
        self.bucho.append(alimento)
    def verBucho(self):
        print(self.bucho)
    def digerir(self):
        print("Os alimentos estão sendo digeridos")
        self.bucho.clear()

def main():
    macaco_01 = macaco("Jorge")
    while True:
        escolha = int(input("""
1- Comer
2- Ver estomago
3- Digerir
0- Sair
"""))
        if escolha == 1:
            macaco_01.comer()
        elif escolha == 2:
            macaco_01.verBucho()
        elif escolha == 3:
            macaco_01.digerir()
        elif escolha == 0:
            break
        else:
            pass

main()

lista = []

