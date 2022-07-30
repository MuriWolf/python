# Classe Funcionário:
#  Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double)
# Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
#  Escreva um pequeno programa que teste sua classe.

# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
# Exemplo de uso:
#   harry=funcionário("Harry",25000)
#   harry.aumentarSalario(10)

from time import sleep

class funcionarios:
    def __init__(self, funcionarios={}):
        self.funcionarios = funcionarios

    def adicionar_funcionario(self):
        nome= str(input("Nome: "))
        salario= float(input("Salario: "))
        self.funcionarios[nome] = salario
        
    def mostrar_funcionarios(self):
        print(f"Funcionarios: {self.funcionarios}")
        sleep(3)

    def media_salarios(self):
        media = sum(self.funcionarios.values()) / len(self.funcionarios.values())
        print(f"Media: R${media:.2f}")
        sleep(3)

    def alterar_salario(self):
        nome = str(input("Digite o nome o funcionario que deseja mudar o salario [1- Ver nomes, 2- voltar]: "))
        if nome == "1":
            print(self.funcionarios)
        elif nome == "2":
            pass

        else:
            achar_nome = self.funcionarios.get(nome, "Nome nao achado")
            if achar_nome == "Nome nao achado":
                pass
            else:
                print(self.funcionarios.get(nome))
                aumentar_diminuir = int(input("Deseja aumentar ou diminuir o salario? [1- aumentar, 2- dimuir]: "))
                porcentagem= float(input("Digite a porcentagem de mudança: "))

                if aumentar_diminuir == 1:
                    self.funcionarios[nome] = ((self.funcionarios[nome] / 100) * porcentagem) + self.funcionarios[nome]
                elif aumentar_diminuir == 2:
                    self.funcionarios[nome] = self.funcionarios[nome] - ((self.funcionarios[nome] / 100) * porcentagem)

def main():
    funcionarios_01 = funcionarios()
    while True:
        escolha=int(input(f"""
{"="*50}
1- Adicionar funcionario
2- Ver funcionarios/salarios
3- Ver média de salarios
4- Alterar salario 
0- Sair
{"="*50}
>>> """))
        if escolha == 1:
            funcionarios_01.adicionar_funcionario()
        elif escolha == 2:
            funcionarios_01.mostrar_funcionarios()
        elif escolha == 3:
            funcionarios_01.media_salarios()
        elif escolha == 4:
            funcionarios_01.alterar_salario()
        elif escolha == 0:
            break
        else:
            pass
main()


 