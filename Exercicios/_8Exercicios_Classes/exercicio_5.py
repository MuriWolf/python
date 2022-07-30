# Classe Conta Corrente:
# Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

from time import sleep

class contaCorrente:
    def __init__(self, numeroConta=0, nomeCorrentista="unknown", saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self):
        confirmacao = str(input("\nDeseja mudar o nome? [s/n]: "))

        if confirmacao == 's':
            novo_nome = str(input("Novo nome: "))
            self.nomeCorrentista = novo_nome

    def deposito(self):
        confirmacao = str(input("\nDeseja depositar dinheiro? [s/n]: "))
        if confirmacao == 's':
            valor_deposito = float(input("Valor do deposito: "))
            self.saldo = self.saldo + valor_deposito

    def saque(self):
        confirmacao = str(input("\nDeseja sacar dinheiro? [s/n]: "))

        if confirmacao == 's':
            valor_saque = float(input("Valor do saque: "))
            self.saldo = self.saldo - valor_saque

def main():
    conta_01 = contaCorrente(213, "random", 0)
    while True:
        sleep(1.5)
        escolha = int(input("""
Lista de opções

1- Alterar nome
2- Depositar
3- Sacar 
4- Ver saldo e informações
0- Sair

R: """))
        if escolha == 1:
            conta_01.alterarNome()
        if escolha == 2:    
            conta_01.deposito()
        if escolha == 3:
            conta_01.saque()
        if escolha == 4:
            print(f"\nNome conta: {conta_01.nomeCorrentista}\nNumero conta: {conta_01.numeroConta}\nSaldo: {conta_01.saldo}")
        if escolha == 0:
            break
main()