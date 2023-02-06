from imp import reload
import telegram
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
import os

os.system('cls')
        #Por informações do seu bot aqui #.
api_key = '5500529057:AAGaalp4FDKAUPcQIoVOgGv11yCMW8yDK50'
user_id = '-1001753176339'  #double free -1001731978350 / double vip -1001753176339
bot = telegram.Bot(token=api_key)

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options=chrome_options)

WAIT = 15
delta = 0
xx = 0
nav.get('https://blaze.com/pt/games/double')
while True:
    time.sleep(3) 
    girando = nav.find_element(By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    



    if girando == 'Girando...':
        xx = 1
        print('Analisando')
        delta = WAIT
        time.sleep(12)
        pegardados = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text
        tfg = pegardados.split()
        
        def qualnum(x):

            if x == '0':
                return 0

            if x == '1':
                return 1

            if x == '2':
                return 2

            if x == '3':
                return 3

            if x == '4':
                return 4

            if x == '5':
                return 5

            if x == '6':
                return 6

            if x == '7':
                return 7

            if x == '8':
                return 8

            if x == '9':
                return 9

            if x == '10':
                return 10

            if x == '11':
                return 11

            if x == '12':
                return 12

            if x == '13':
                return 13

            if x == '14':
                return 14


        def qualcor(x):

            if x == '0':
                return 'Branco'

            if x == '1':
                return 'Vermelho'

            if x == '2':
                return 'Vermelho'

            if x == '3':
                return 'Vermelho'

            if x == '4':
                return 'Vermelho'

            if x == '5':
                return 'Vermelho'

            if x == '6':
                return 'Vermelho'

            if x == '7':
                return 'Vermelho'

            if x == '8':
                return 'Preto'

            if x == '9':
                return 'Preto'

            if x == '10':
                return 'Preto'

            if x == '11':
                return 'Preto'

            if x == '12':
                return 'Preto'

            if x == '13':
                return 'Preto'

            if x == '14':
                return 'Preto'


        


    if xx == 1:
        xx = 0

        def verificarsaida(num):
                if num == ['Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
💰 Entrada: 🔴
⚠️ Proteger no branco: ⚪️
✅Ate Gale 2 🐓🐓 
💻 🎲

     
                                             💬 
BATEU A META!? VAZA!!!!!!
                ''')
                if num == ['Vermelho']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
💰 Entrada: ⚫
⚠️ Proteger no branco: ⚪️
✅Ate Gale 2 🐓🐓 
💻 🎲 
     
                                             💬 
BATEU A META!? VAZA!!!!!!
                ''')

                if num == ['Branco']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
CANCELAR ENTRADA - SAIU BRANCO
     
                                             💬 
CUIDADO COM O GERENCIAMENTO DA BANCA!!
                ''')

    
    def WinOrLoss(msg):
        time.sleep(10)
        pegarrusltado = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text
        WL = pegarrusltado.split()[0]
        wlcor = qualcor(WL)
        print('O resultado é:', wlcor)

        if msg =='NENHUMA':
            return
        if msg == wlcor:
            return bot.send_message(chat_id=user_id, text="✅WIN✅WIN✅WIN✅")
        
        else:        
            return bot.send_message(chat_id=user_id, text="❌loss❌❌loss❌")
    
    while True:
        
            time.sleep(10)
            pegardados = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text

            dados = pegardados.split()

            pd = dados[0:1]
            mapeando = map(qualnum, pd)
            mapeando2 = map(qualcor, pd)

            finalnum = list(mapeando)
            finalcor = list(mapeando2)

            entrada = verificarsaida(finalcor)
            print("entrada é:", entrada.split()[1])
            time.sleep(15)
            resultadocor = WinOrLoss(entrada.split()[1])
            print(resultadocor)

            print(finalnum)
            print(finalcor)
            testando = verificarsaida(finalcor)
            print(testando)

            time.sleep(180)
            print(time.sleep)
