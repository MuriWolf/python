# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade.
# Métodos: Alterar Nome, Fome, Saúde e Idade;
# Retornar Nome, Fome, Saúde e Idade 

# Obs: Existe mais uma informação que devemos levar em consideração,
# o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
#  então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

# ideia PAra o proximo exercicio do tamagushi: mudar a carinha dele conforme seu humor, ex: feliz = \('u')/, medio = |('-')|, triste = [(*=*)], quase morrendo = ~(XoX)~

from time import sleep

def filter(numero):
    """This def is used to force the numbers never be less than zero or plus than one hundred"""
    if numero > 100:
        numero = 100
        return numero
    if numero< 1:
        numero = 1
        return numero
    else:
        return numero

class tamagushi:
    """"Tamagushi is a toy, you can change his hungry, health, name and even his age! Also you can see his humor."""
    def __init__(self, name="unknown", hungry=0, health=100, age=0):
        self.name = name
        self.hungry = hungry
        self.health = health
        self.age = age

    def set_name(self):
        new_name = str(input("> Enter the new name: "))
        self.name = new_name

    def set_age(self):
        new_age = int(input("> Enter the new age: "))
        self.age = filter(new_age)

    def set_hungry(self):
        new_hungry = int(input("> Enter the new hungry level: "))
        self.hungry = filter(new_hungry)

    def set_health(self):
        new_health = int(input("> Enter the new health level: "))
        self.health = filter(new_health)
        
    def humor(self):
        if (self.health + self.hungry) > 149:
            print("I'm so happy!")
        elif 150 > (self.health + self.hungry) > 99:
            print("I'm Ok") 
        elif 100 > (self.health + self.hungry) > 59:
            print("I'm bad")
        else:
            print("H E L P M E") 

    def get_status(self):
        print(f"""
{"="*20}
TAMAGUSHI's STATUS
{"="*20}
Name: {self.name}
Age: {self.age}
Hungry: {self.hungry}
Health: {self.health}
Humor: """, end="")
        self.humor()
        print("="*20)
        sleep(3)

def main():
    tamagushi_01 = tamagushi("unknown", 0, 100, 1)
    while True:
        choice = int(input(f"""
{"="*20}
CHOICES
{"="*20}
1- Change name
2- Change age
3- Change Hungry
4- Change health

5- See the status
0- Exit
{"="*20}

>>> """))
        if choice == 1:
            tamagushi_01.set_name()
        elif choice == 2:
            tamagushi_01.set_age()
        elif choice == 3:
            tamagushi_01.set_hungry()
        elif choice == 4:
            tamagushi_01.set_health()
        elif choice == 5:
            tamagushi_01.get_status()
        elif choice == 0:
            break
        else:
            pass

main()
