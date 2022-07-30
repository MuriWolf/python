# OBJETIVOS:

# Abrir o Spotify, depois abrir o xbox console companion e logo após abrir o chrome
# No Chrome: Abrir o Youtube, Abir os exercicios de python e o instagram

import pyautogui
import time

abrirCMSP = input("\nAbrir o CMSP? [s/n]: ")

# entrar no spotify
pyautogui.click(502, 758)
time.sleep(1)

# entrar no xbox console companion
pyautogui.click((557, 754))
time.sleep(1)

# ir para a area de trabalho
pyautogui.click(1362, 737)
time.sleep(1)
pyautogui.doubleClick(1310, 379)
time.sleep(1)

# entrar no chrome
pyautogui.click(707, 741)
time.sleep(5)

# abrir o whatsapp
pyautogui.write(r'https://web.whatsapp.com/')
pyautogui.press(r'enter')
time.sleep(1.5)

# abir o youtube
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.write(r'https://www.youtube.com/')
pyautogui.press(r'enter')
time.sleep(1)

# abrir o instagram
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.write(r'https://www.instagram.com/')
pyautogui.press('enter')
time.sleep(1)

# abrir o exercicios de python
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.write(r'https://wiki.python.org.br/ListaDeExercicios')
pyautogui.press('enter')
time.sleep(1)

if abrirCMSP == 's':
    # abir o cmsp e logar nele
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.write(r'https://cmspweb.ip.tv/')
    pyautogui.press('enter')
    time.sleep(1)

    # clicar para logar em alunos
    pyautogui.click(675, 477)
    time.sleep(1)

    # clicar para colocar meu IP
    pyautogui.click(740, 398)
    time.sleep(0.5)

    # clicar para colocar dígito
    pyautogui.write('3')
    time.sleep(0.5)

    # clicar para colocar minha senha
    pyautogui.click(626, 459)
    time.sleep(0.5)

    # clicar para selecionar senha
    pyautogui.click(662, 495)
    pyautogui.press('enter')

# aviso :)))
pyautogui.alert('Vai estudar rapa')