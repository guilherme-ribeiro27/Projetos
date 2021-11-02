from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.text('Usário'),sg.Input(key='usuario')],
    [sg.text('Senha'),sg.Input(key='senha',password_char='♥')], 
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de login',layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Guilherme' and valores['senha'] == 'Ribeiro':
            print('Bem vindo!')
