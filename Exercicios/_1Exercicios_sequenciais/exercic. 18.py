# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import PySimpleGUI as sg

class tempo_dowload():
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Informe o tamanho do arquivo para download (em MB)')],
            [sg.Input(size=(10,10), key='tamanho')],
            [sg.Text('\nInforme a velocidade do link de Internet (em Mbps)')],
            [sg.Input(size=(10,10), key='velocidade')],
            [sg.Text('\n')],
            [sg.Button('Confirmar')],
            [sg.Output(size=(70,20))]
        ]

        # janela
        self.janela = sg.Window("Tempo Download").layout(layout)

    def iniciar(self):
        while True:
            # extrair os dados da tela e converter
            self.button, self.values = self.janela.read()

            tamanho = self.values['tamanho']
            intTamanho = int(tamanho)
            velocidade = self.values['velocidade']
            intVelocidade = int(velocidade)

            tempo = (intTamanho / intVelocidade)
            contaMinutos = tempo / 60
            minutos = int(contaMinutos)
            contaSegundos = minutos * 60
            segundos = tempo - contaSegundos
            intSegundos = int(segundos)

            print(f"Tempo aproximado de download: {minutos} minuto(s) e {intSegundos} segundo(s)\n")

tela = tempo_dowload()
tela.iniciar()