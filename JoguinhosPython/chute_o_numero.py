import random
import math
import PySimpleGUI as sg
sg.theme('DarkAmber') 
class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        #layout
        layout = [
            [sg.Text("Seu chute:",size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!'),sg.Exit('Sair')],
            [sg.Output(size=(39,10))],
            
        ]
        #criar janela
        self.janela = sg.Window('Chute o Número',layout=layout)
        self.GerarNumeroAleatorio()
        qtd_chute = 1
        try:
            while True:
                #receber os valores
                self.LerOsValoresDaTela()
                #fazer alguma coisa com esses valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute)>self.valor_aleatorio:
                            print(f'Chute um valor mais baixo do que {self.valor_do_chute}')
                            qtd_chute+=1
                            break
                        elif int(self.valor_do_chute)<self.valor_aleatorio:
                            print(f'Chute um valor mais alto do que {self.valor_do_chute}')
                            qtd_chute+=1
                            break
                        else: 
                            self.tentar_novamente = False
                            print(f'Você acertou, com um total de: {qtd_chute} chutes')
                            print('Clique em sair para fechar!')
                            break
                elif self.evento == sg.WIN_CLOSED or self.evento == 'Sair':
                    break
                    
                    
        except:
            print("Ocorreu um erro!")
            self.Iniciar()

    
    def LerOsValoresDaTela(self):
        self.evento, self.valores = self.janela.Read()

   
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = (random.randint(self.valor_minimo, self.valor_maximo))


chute = ChuteONumero()
chute.Iniciar()