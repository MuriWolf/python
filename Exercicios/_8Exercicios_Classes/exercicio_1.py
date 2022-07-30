# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class bola:
    def __init__(self, cor="unknown", circurf=0, material="unknown"):
        self.cor = cor
        self.circunf = circurf
        self.material = material

    def trocar_cor(self):
        troca = str(input("> Deseja mudar a cor atual? [s/n]: "))
        troca = troca.casefold()

        if troca == "s":
            nova_cor = str(input("> Nova cor: "))
            self.cor = nova_cor
        if troca == "n":
            pass

    def mostrar_cor(self):
        print(f"A cor atual é {self.cor}")

def main():
    bola01 = bola("azul", 3, "metal")

    while True:
        bola01.mostrar_cor()
        bola01.trocar_cor()

        continuar = str(input("Deseja continuar? [s/n]: "))
        if continuar == "n":
            break

main()