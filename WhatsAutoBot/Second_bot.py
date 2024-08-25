#Importando as bibliotecas do selenium 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
#Importando as bibliotecas do pyautogui
import pyautogui as tempoEspera
import pyautogui as teclasTeclado 

#By para trabalhar com os computadores mais recentes 
from selenium.webdriver.common.by import By 

#Importando a bibliotecas do pyautogui para trabalhar com o excel 
from openpyxl import load_workbook

#Pegamos o caminho do arquivo + nome do arquivo que está no computador 
nome_arquivo_contatos = "C:\\Users\\LucasUanderson\\Documents\\GitHub\Python_Advanced_Automation_Suite\\WhatsAutoBot\\whatsapp\\contatos.xlsx"
planilhaDadosContato = load_workbook(nome_arquivo_contatos)

#Selecionamos a sheet de dados
sheet_selecionada = planilhaDadosContato['Dados']


#Emulando navegador do Chrome
navegadorChrome = webdriver.Chrome()
navegadorChrome.get("****")
navegadorChrome.find_element(By.NAME, "username").send_keys("***")
tempoEspera.sleep(1)
navegadorChrome.find_element(By.NAME, "password").send_keys("***")
tempoEspera.sleep(1)
teclasTeclado.press("tab")
tempoEspera.sleep(1)
teclasTeclado.press("enter")
tempoEspera.sleep(1)
teclasTeclado.press("enter")
tempoEspera.sleep(2)

element = navegadorChrome.find_element(By.XPATH, "//div[span[text()='Contatos']]")
element.click()

for linha in range(2, len(sheet_selecionada['A']) + 1):
    
    #Criamos as variaveis nome e mensagem
    nomeContato = sheet_selecionada['A%s' % linha].value
    mensagemContato = sheet_selecionada['B%s' % linha].value
    #Entrando na lupa e pesquisando o numero
    navegadorChrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/input').send_keys(nomeContato)
    tempoEspera.sleep(2)
    #Selecionando o contato para entrar na conversa
    element = navegadorChrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[1]/div/div[5]/div[1]/div/div/div')
    element.click()
    tempoEspera.sleep(2)
    #abrindo o chamado
    element = navegadorChrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]/button')
    element.click()
    tempoEspera.sleep(2)
    #selecionando campo
    element = navegadorChrome.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div/div[2]/div[1]/div[1]')
    element.click()
    teclasTeclado.typewrite("Exames") 
    teclasTeclado.press("enter")
    tempoEspera.sleep(2)
    element = navegadorChrome.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div/footer/button[2]')
    element.click()
    tempoEspera.sleep(2)
    element = navegadorChrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]/form/div/textarea').send_keys(mensagemContato)
    teclasTeclado.press("enter")
    tempoEspera.sleep(2)
    element = navegadorChrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/button')
    element.click() 



    

