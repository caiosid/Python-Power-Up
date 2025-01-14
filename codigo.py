# pip install pyautogui

import pyautogui
import time 
import pandas
pyautogui.PAUSE = 0.5

#pyautogui.click -> clicar
#pyautogui.press -> pressinar uma tecla
#pyautogui.write -> escrever 

# Passo 1: Abrir o sistema da empresa 

# abrir o google chrome
# apertar a tecla win
pyautogui.press('win')

# digitar o texto chrome
pyautogui.write('chrome')

# apertar enter
pyautogui.press('enter')

#https://dlp.hashtagtreinamentos.com/python/intensivao/login
time.sleep(0.5)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Passo 2 : Fazer login 
time.sleep(0.5)
pyautogui.click(x=624, y=409)
pyautogui.write('caiosidartha8@gmail.com')

pyautogui.click(x=807, y=514)
pyautogui.write('1234567890')

pyautogui.click(x=671, y=569)
pyautogui.click(x=597, y=288)

# Passo 3 : Importar a base de dados dos produtos 

tabela = print(pandas.read_csv('produtos.csv'))

#codigo 
pyautogui.write('MOLO000251')
pyautogui.press('tab')

#marca
pyautogui.write('Logitech')
pyautogui.press(tab)

#MOLO000251,Logitech,Mouse,1,25.95,6.50,
