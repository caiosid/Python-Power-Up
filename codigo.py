# pip install pyautogui

import pyautogui

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
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')