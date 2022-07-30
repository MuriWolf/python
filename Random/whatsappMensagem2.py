import pywhatkit
import keyboard
import time
from datetime import datetime

# definir contatos que serão enviadas mensagens
contatos = ['+55 18 98814-8206']

# definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'teste enviar mensagem', datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(15)
    keyboard.press_and_release('ctrl + w')
