import pyautogui, time, pandas

pyautogui.PAUSE = 0.5

time.sleep(0.5)
pyautogui.press('win')

time.sleep(0.5)
pyautogui.write('chrome')

time.sleep(0.5)
pyautogui.press('enter')

time.sleep(0.5)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(1)
pyautogui.click(x=512, y=407)
pyautogui.write('caiosidartha8@gmail.com')

time.sleep(1)
pyautogui.click(x=807, y=514)
pyautogui.write('1234567890')      

pyautogui.click(x=671, y=569)
pyautogui.click(x=597, y=288)

tabela = pandas.read_csv('produtos.csv')
print(tabela)

time.sleep(2)

for linha in tabela.index:
    pyautogui.click(x=598, y=292)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = tabela.loc[linha,'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    
    obs = str(tabela.loc[linha, 'obs'])
    
    if obs != 'nan':
        pyautogui.write(obs)
    
    pyautogui.press('tab')

    pyautogui.press('enter')

    pyautogui.scroll(10000)


