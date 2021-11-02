import win32com.client as win32

outlook = win32.Dispatch('outlook.application') #integração com Outlook

#criar um email
email = outlook.createItem(0)

#configurar as informações do seu email
email.To = ""
email.Subject = "Email Automático"
email.HTMLbody = """<p><b>Olá Guilherme, aqui é o código pyhton</b></p>
<p>BLA BLA BLA
BLALBLABLA </p>
"""
email.send()