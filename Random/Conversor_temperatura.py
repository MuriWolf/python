import PySimpleGUI as sg

class Conversor_temperatura:
    def __init__(self):
        sg.change_look_and_feel('BlueMono')
        # layout
        layout = [
            [sg.Text('( INFORME UM NUMERO EM CELSIUS PARA TRANSFORMA-LO EM FAHRENHEIT E VICE VERSA )\n')],
            [sg.Text('Informe em Qual Unidade de Temperatura Voce Deseja Digitar:')],
            [sg.Radio('Fahrenheit', 'medidas', key='Fahrenheit'), sg.Radio('Celsius', 'medidas', key='Celsius')],
            [sg.Text('\nInforme a Temperatura:\n\n', size=(10, 0)), sg.Input(size=(5, 10), key='temperatura')],
            [sg.Button('Converter')],
            [sg.Output(size=(85, 10))]
        ]
        # janela
        self.janela = sg.Window("Conversor de Temperatura").layout(layout)

    def iniciar(self):
        while True:
            # extrair os dados da tela e converter
            self.button, self.values = self.janela.read()

            temperatura = self.values['temperatura']
            intTemp = int(temperatura)
            Celsius = self.values['Celsius']
            Fahrenheit = self.values['Fahrenheit']

            if Celsius == True:
                celConta = (intTemp * 1.8) + 32
                intCel = float(celConta)
                print(f"{temperatura}° Celsius = {intCel:.1f}° graus Fahrenheit.\n")

            elif Celsius == False:
                fahconta = (intTemp - 32) / 1.8
                intFah = float(fahconta)
                print(f"{temperatura}° Fahrenheit = {intFah:.1f}° graus Celsius.\n")

tela = Conversor_temperatura()
tela.iniciar()