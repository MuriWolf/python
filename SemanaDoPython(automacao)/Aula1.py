# importar bibliotecas
import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 1

# abrir navegador
pyautogui.press('winleft')
pyautogui.write('Chrome')

pyautogui.press('enter')
pyautogui.alert("Vai começar, aperte OK e não mexa em nada")
time.sleep(1.5)

# entrar no drive
link = r'https://drive.google.com/drive/folders/1wRTFw0sUVBjRr4hW5U9LF7DjLixRyxym'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(6)

# baixar o arquivo
pyautogui.click(1059, 359)
pyautogui.click(1161, 199)
time.sleep(1)
pyautogui.click(1012, 562)
time.sleep(5)

# calcular o faturamento e a quantidade de produtos de ontem
df = pd.read_excel(r'C:\Users\Usuario\Downloads\Vendas - Dez.xlsx')
print(df)

faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()

# abrir email
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
pyautogui.press('enter')
time.sleep(8)

# escrever e mandar email
pyautogui.click(66, 192)

time.sleep(1)
pyautogui.write(r'murillop.o06@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')

time.sleep(1)
assunto = r'Relatório de vendas de ontem'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = (f'''
Prezados, bom dia

O faturamento de ontem foi de R${faturamento:,.2f}
A quantidade de produtos foi {qtde_produtos:,}

Abs
MuriWolf
''')

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')