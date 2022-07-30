#Classe Conta de Investimento:
#  Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
#  com a diferença de que se adicione um atributo taxaJuros. 
# Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
#  Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
#  Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%
# Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class conta_investimento:
    def __init__(self, nome="unknown", numero=0, tax=0, saldo=0):
        self.nome = nome
        self.numero = numero
        self.taxJuros = tax
        self.saldo = saldo

    def mudar_nome(self, nome):
        self.nome = nome

    def mudar_numero(self, numero):
        self.numero = numero

    def mudar_juros(self, juros):
        self.taxJuros = juros

    def aplicar_juros(self):
        self.saldo = self.saldo + ((self.taxJuros * 0.01) * self.saldo)
        print(f"Saldo resultante: {self.saldo:.2f}")

nome = nome = str(input("Nome: ")).casefold()
numero = int(input("Numero: "))
saldo = float(input("saldo: "))
juros = float(input("Juros: "))

conta_investimento01 = conta_investimento(nome, numero, juros, saldo)

for i in range(5):
    conta_investimento01.aplicar_juros()


