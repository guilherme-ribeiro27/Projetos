import PySimpleGUI as sg
import mysql.connector
## SIZE É POR LETRA, GUILHERME (x,y) sendo x a quantidade de letras e y a quantidade de linhas
## self.valores é um dicionario python no formato {'valor1':'bla','valor2':'bla2'} que sao os valores lidos na tela
class Tela:
    def __init__(self):
        #Conectar o banco:
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database='pythonusers'
                )
        #layout
        layout = [
            [sg.Button('Cadastrar Usuário',size=(30,0)),sg.Button('Mostrar Usuários',size=(30,0))]
        ]
        #janela
        self.telaMain = sg.Window('Opções',layout=layout)
        self.telaCadastro,self.telaMostra = None,None


    def Iniciar(self):
        #ler
        while True:
            #self.janela,self.eventos, self.valores = sg.read_all_windows()
            self.eventos, self.valores = self.telaMain.Read()
            if self.eventos=='Cadastrar Usuário':
                self.telaCadastro = self.TelaCadastro()
                while True:
                    self.eventos, self.valores = self.telaCadastro.Read()
                    self.telaMain.hide()
            
           
            
    def TelaCadastro(self):
        #layout
        layoutCadastro = [
            [sg.Text('Nome:',size=(7,0),text_color='red'), sg.Input(size=(15,0),key='nome')],
            [sg.Text('Email:',size=(7,0)), sg.Input(size=(15,0),key='email')],
            [sg.Button('Cadastrar Usuário')],
            [sg.Text('Resultado:',size=(10,0)),sg.Output(size=(10,0),key='Resultado')]
        ]
        
        return sg.Window('Dados do Usuário',layout=layoutCadastro,finalize=True)
    
    def TelaMostra(self):
        #layout
        layout = []
        #tela
        self.telaMostra = sg.Window('Usuários',layout=layout, finalize=True)
        return self.telaMostra

tela = Tela()
tela.Iniciar()
