# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
#
# As possíveis respostas são:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados,
# o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
# O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

WindowsServer = 0
Unix = 0
Linux = 0
Netware = 0
MacOS = 0
Outro = 0
pergunta = 123

print('''
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

0- Encerrar
''')

print("\n! Vote usando o digito [1, 2, 3, 4, 5, 6 ou 0 para encerrar] !\n")
while pergunta != 0:
    pergunta = int(input("Qual o melhor Sistema Operacional para uso em servidores? "))

    if pergunta == 0:
        break
    else:
        if pergunta < 0 or pergunta > 6:
            print("\nDigite apenas de 0 até 6.")

        else:
            if pergunta == 1:
                WindowsServer = WindowsServer +  1
            elif pergunta == 2:
                Unix = Unix + 1
            elif pergunta == 3:
                Linux = Linux + 1
            elif pergunta == 4:
                Netware = Netware + 1
            elif pergunta == 5:
                MacOS = MacOS + 1
            elif pergunta == 6:
                Outro = Outro + 1

total = (WindowsServer + Unix + Linux + Netware + MacOS + Outro)
Total1PorCento = total / 100

print(f'''
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server            {WindowsServer}    {int((WindowsServer / total) * 100)}%
Unix                      {Unix}    {int((Unix / total) * 100)}%
Linux                     {Linux}    {int((Linux / total) * 100)}%
Netware                   {Netware}    {int((Netware / total) * 100)}%
Mac OS                    {MacOS}    {int((MacOS / total) * 100)}%
Outro                     {Outro}    {int((Outro / total) * 100)}%
-------------------     -----
Total                    {total}
''')