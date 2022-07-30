print("\nAVISO: ESSE PROGRAMA SÓ FUNCIONA SE O CMSP JA ESTIVER ABERTO")
print("\nExemplo se voce digitar 2:\nMurillo Pinheiro / presente 2")
QualPresente = int(input("\nDigite qual numero do presente voce quer (1, 2 ou 3): "))

import pyautogui
import time

def enter_fecharJanela():
    pyautogui.press('enter')
    time.sleep(2.5)
    pyautogui.hotkey('ctrl', 'w')

# abrir o chrome
pyautogui.click(707, 741)
time.sleep(2)
pyautogui.hotkey('ctrl', 't')
time.sleep(1)

# entrar cmsp
pyautogui.click(856, 86)
time.sleep(2.5)
# entrar em turmas
pyautogui.click(1085, 127)
time.sleep(1)
# abrir a turma
pyautogui.click(245, 203)
time.sleep(3)
# entrar na texto
pyautogui.click(935, 708)

if QualPresente == 1:
    pyautogui.write('Murillo Pinheiro / presente 1')
    enter_fecharJanela()
elif QualPresente == 2:
    pyautogui.write('Murillo Pinheiro / presente 2')
    enter_fecharJanela()
elif QualPresente == 3:
    pyautogui.write('Murillo Pinheiro / presente 3')
    enter_fecharJanela()
