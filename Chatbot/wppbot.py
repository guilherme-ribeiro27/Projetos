#importar as bibliotecas 
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#Navegar até o Web Whatsapp
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Opera(OperaDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)
#Definir contatos e grupos
contatos = ['Wesley']
mensagem = []
#Buscar contatos ou grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    for msg in mensagem:
        enviar_mensagem(msg)
        time.sleep(2)


#Campo de pesquisa 'copyable-text selectable-text'
#campo de mensagem privada 'copyable-text selectable-text'
#Enviar mensagem para contato/grupos