# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

# Crie um programa que utilize esta classe.
# Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

import time

class retangulo:
    def __init__(self, lado_a=0, lado_b=0):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lado(self):
        troca = str(input("\n> Deseja mudar os lados do retangulo? [s/n]: "))
        troca = troca.casefold()

        if troca == "s":
            lado_a = int(input("\n> Valor lado A: "))
            lado_b = int(input("> Valor lado B: "))

            self.lado_a = lado_a
            self.lado_b = lado_b
        else:
            pass

    def retornar_valor_lados(self):
        print(f"\nValor lado A: {self.lado_a}\nValor lado B: {self.lado_b}")

    def calcular_area(self):
        print(f"\nValor area do retangulo: {self.lado_a * self.lado_b}")

    def calcular_perimetro(self):
        print(f"\nValor perimetro do retangulo: {(self.lado_a*2) + (self.lado_b*2)}")

def main():
    retangulo_01 = retangulo(0, 0)
    lado_lugar_A = 0
    lado_lugar_B = 0
    pisos = 0
    rodapes = 0
    while True:
        pergunta = int(input('''
LISTA DE AÇOES

1- Mudar lados do retangulo
2- Calcular área
3- Calcular perimetro   
4- Mudar lados do lugar
0- sair

R: '''))

        if pergunta == 1:
            retangulo_01.mudar_lado()
        if pergunta == 2:
            retangulo_01.calcular_area()
        if pergunta == 3:
            retangulo_01.calcular_perimetro()
        if pergunta == 4:
            lado_lugar_A = int(input("> Lado A: "))
            lado_lugar_B = int(input("> Lado B: "))
        if pergunta == 0:
            break    
        
        if lado_lugar_A != 0:
            pisos = (lado_lugar_A * lado_lugar_B) / (retangulo_01.lado_a * retangulo_01.lado_b) 
            rodapes = ((lado_lugar_A * 2) + (lado_lugar_B * 2)) / (retangulo_01.lado_a * retangulo_01.lado_b) 
        
        else:
            pass
        
        time.sleep(1.5)
        print(f'''
INFORMAÇÕES                                         

Lado A retangulo: {retangulo_01.lado_a}
Lado B retangulo: {retangulo_01.lado_b}

Lado A lugar: {lado_lugar_A}                    
Lado B lugar: {lado_lugar_B}                
                                                        
Total de pisos: {pisos}                            
Total de rodapes: {rodapes}''')             

main()                              