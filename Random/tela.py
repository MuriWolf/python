import PySimpleGUI as sg

class Telapython:
    def __init__(self):
        sg.change_look_and_feel('BlueMono')
        #layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quis Provedores de Email São Aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'),sg.Checkbox('Yahoo', key='yahoo'),sg.Checkbox('Outlook', key='outlook')],
            [sg.Text('Aceita Cartão?')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'),sg.Radio('Nao', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        #janela
        self.janela = sg.Window("Dados do Usuario").layout(layout)

    def iniciar(self):
        while True:
            # extrair os dados da janela
            self.button, self.values = self.janela.read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_yahoo = self.values['yahoo']
            aceita_outlook = self.values['outlook']
            aceitaCartao = self.values['aceitaCartao']
            naoAceitaCartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']

            print("\n-----------------------------------------")
            print(f"\nNome: {nome}")
            print(f"Idade: {idade}")
            print(f"\nAceita Gmail: {aceita_gmail}")
            print(f"Aceita Yahoo: {aceita_yahoo}")
            print(f"Aceita Outlook: {aceita_outlook}")
            print(f"\nAceita Cartao: {aceitaCartao}")
            print(f"Aceita Cartao: {naoAceitaCartao}")
            print(f"\nVelocidade Script: {velocidade_script}")

tela = Telapython()
tela.iniciar()