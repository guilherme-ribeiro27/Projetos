import PySimpleGUI as sg
import mysql.connector
sg.theme('BluePurple') 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='pythonusers'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT nome,email FROM usuarios")




class Users:
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database='pythonusers'
    )
  def BuscarUsers(self):
    self.mycursor = self.mydb.cursor()
    self.mycursor.execute("SELECT nome,email FROM usuarios")

  def Iniciar():
    layout = [
      [sg.Text('Nomes: ')],
      [sg.Output()],
      [sg.Button('Mostrar nomes'),sg.Button('Sair')]
    ]
    self.tela = sg.Window('Nomes',layout=layout)

    while True:
      self.LerOsValoresDaTela()
      try:
        if self.eventos == 'Mostrar nomes':
          self.BuscarUsers()
          for nomes in names:
            print(nomes)
        elif eventos == 'Sair' or eventos == WIN_CLOSED:
            self.tela.Close()
      except:
        print('Erro')

    def LerOsValoresDaTela(self):
      self.eventos, self.valores = self.tela.Read()
Iniciar()


