# Passo a passo do projeto
# 
# Passo 1 - Entrar no Sistema da Empresa
#   #   https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui

import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Clicar -> pyautogui.click
# Escrever -> pyautogui.write
# Apertar uma tecla -> pyautogui.press
# Atalho -> pyautogui.hotkey("ctrl" + "x")
# Scroll -> pyautogui.scroll()
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
# Passo 2 - Fazer login
time.sleep(5)
pyautogui.click(x=545, y=412) 
pyautogui.write('teste@gmail.com')
pyautogui.press('tab')
pyautogui.write('minhasenha')
pyautogui.click(x=674, y=572)
# Passo 3 - Importar a base de dados
time.sleep(3)
tabela = pandas.read_csv('produtos.csv')

# Passo 4 - Cadastrar um produto
for linha in tabela.index:
    
    pyautogui.click(x=645, y=289)
    
    #Codigo
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    #Marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    #Tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    #Categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    #Preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    #Custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    #Obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(2000)
# Passo 5 - Repitir isso até acabar a base de dados

