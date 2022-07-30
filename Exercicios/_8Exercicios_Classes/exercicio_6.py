# classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

from time import sleep

class tv:
    def __init__(self, canal=0, volume=0):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self):
        novo_canal = int(input("\nCanal: "))
        if novo_canal < 1 or novo_canal > 256:
            print("Canal invalido")
        else:
            self.canal = novo_canal

    def mudar_volume(self):
        novo_volume = int(input("\nVolume: "))
        if novo_volume > 100 or novo_volume < 1:
            print("Escolha um volume de 1 a 100")
        else:
            self.volume = novo_volume

def main():
    tv_01 = tv(1, 10)
    while True:
        print(f"Canal atual: {tv_01.canal}\nVolume atual: {tv_01.volume}")

        escolha = int(input('''

1- Mudar canal
2- Mudar volume
3- Desligar

SELECIONAR: '''))

        if escolha == 1:
            tv_01.mudar_canal()
        if escolha == 2:
            tv_01.mudar_volume()
        if escolha == 3:
            print("\nDesligando...")
            break
        sleep(2.5)
        
main()