# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.
#  Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

import time

class pessoa:
    def __init__(self, nome="unknown", idade=0, peso=0, altura=0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhercer(self):
        decicao = str(input("Deseja envelhecer? [s/n]: "))
        decicao.casefold()

        if decicao == "s":
            anos = int(input("Anos que se passarão: "))

            if self.idade < 21:
                while self.idade < 21 or anos !=0:
                    self.idade = self.idade + 1
                    anos = anos - 1
                    self.altura = self.altura + 0.5
        else:
            pass
        self.idade = self.idade + anos

    def engordar(self):
        decicao = str(input("Deseja engordar? [s/n]: "))
        decicao.casefold()

        if decicao == "s":
            mais_peso = float(input("Quanto de peso ele ira ganhar (em kg): "))
            self.peso = self.peso + mais_peso

    def emagrecer(self):
        decicao = str(input("Deseja emagrecer? [s/n]: "))
        decicao.casefold()

        if decicao == "s":
            menos_peso = float(input("Quanto de peso ele ira perder (em kg): "))

            self.peso = self.peso - menos_peso

    def crescer(self):
        decicao = str(input("Deseja crescer? [s/n]: "))
        decicao.casefold()

        if decicao == "s":
            tamanho = float(input("Quanto de altura ele ira ganhar (em cm): "))

            self.altura = self.altura + tamanho

def main():
    pessoa_01 = pessoa("Joao", 7, 28, 134)
    while True:
        time.sleep(1.5)
        escolha = int(input('''
Digite um dos numeros abaixo para continuar...

1- Envelhecer
2- Engordar
3- Emagrecer
4- Crescer
0- Sair

R: '''))
        if escolha == 1:
            pessoa_01.envelhercer()
        if escolha == 2:
            pessoa_01.engordar()
        if escolha == 3:
            pessoa_01.emagrecer()
        if escolha == 4:
            pessoa_01.crescer()
        if escolha == 0:
            break
        
        time.sleep(1.5)
        print(f"""
Informaçôes atuais da pessoa:

Nome: {pessoa_01.nome}
Idade: {pessoa_01.idade}
Peso: {pessoa_01.peso}
Tamanho: {pessoa_01.altura}        
""")
main()