# EX: 15
# Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, 
# permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
#  Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

# EX: 16
# Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto.
# Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário.
# Dica: acrescente um método especial str() à classe Bichinho.

from time import sleep

def filter(numero):
    """This def is used to force the numbers never be less than zero or plus than one hundred"""
    if numero > 100:
        numero = 100
        return numero
    if numero< 1:
        numero = 0
        return numero
    else:
        return numero

class tamagushi:
    """"Tamagushi is a toy, you can change his hungry, health, name and even his age! Also you can see his humor."""
    def __init__(self, name="unknown", hungry=100, health=100, age=0, face="", humor="", boredom=100):
        self.name = name
        self.hungry = hungry
        self.health = health
        self.age = age
        self.face = face
        self.boredom  = boredom 

    def set_name(self):
        new_name = str(input("> Enter the new name: "))
        self.name = new_name

    def set_age(self):
        new_age = int(input("> Enter the new age: "))
        self.age = filter(new_age)

    def set_hungry(self):
        food = int(input("Enter how much food you will give (1 food = 2 points of hungry): "))
        self.hungry = filter((self.hungry + food) * 2)
        print(f"\nGiving food... /('c.')\ ")
        sleep(2)

    def set_health(self):
        new_health = int(input("> Enter the new health level: "))
        self.health = filter(new_health)

    def play(self):
        playtime = int(input("Enter how much time do you wanna play (1min = 1 point of boredoom): "))
        self.boredom = filter(self.boredom + playtime)
        print("\nPlaying... /( ^ 3 ^)/ o")
        sleep(2)

    def get_status(self):
        print(f"""
{"="*20}
TAMAGUSHI's STATUS
{"="*20}

Name: {self.name}
Age: {self.age}

Hungry: {self.hungry}
Health: {self.health}
boredom: {self.boredom}

humor: {self.face}""")
        sleep(2)

if __name__ == "__main__":
    tamagushi_01 = tamagushi()
    while True:
        # calcula o humor do tamagushi
        if (tamagushi_01.health + tamagushi_01.hungry + tamagushi_01.boredom) > 224:
            tamagushi_01.face = "I'm so happy!  \(^u^)/"

        elif 225 > (tamagushi_01.health +tamagushi_01.hungry) > 149 :
            tamagushi_01.face = "I'm Ok  |('<')| "
            
        # diminui os niveis de tedio e fome (quanto menor pior)
        boredoom = tamagushi_01.boredom - 2
        tamagushi_01.boredom = filter(boredoom)
        
        hungry = tamagushi_01.hungry - 2
        tamagushi_01.hungry = filter(hungry)
        

        sleep(1)
        choice = str(input(f"""
{"="*20}
CHOICES
{"="*20}
1- Change name
2- Change age
3- Give food
4- Change health
5- Play

6- See the status
0- Exit
{"="*20}

>>> """))
        if choice == "1":
            tamagushi_01.set_name()
        elif choice == "2":
            tamagushi_01.set_age()
        elif choice == "3":
            tamagushi_01.set_hungry()
        elif choice == "4":
            tamagushi_01.set_health()   
        elif choice == "5":
            tamagushi_01.play()
        elif choice == "6":
            tamagushi_01.get_status()
        elif choice == "0":
            print("Bye!!")
            break
        elif choice == "1987":
            print("CONGRATS! YOU FOUND AN EASTER EGG!!")
        else:
            pass

        