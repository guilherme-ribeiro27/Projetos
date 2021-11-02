import os
def start():
    #Apresentar o Chatbot
    print('Olá! Bem vindo ao chatbot.')
    #Pedir o nome
    nome = input('Digite o seu nome, por favor: ')
    #Pedir o email
    email = input('Digite o seu email: ')
    #Ofertar um menu de opções
    input(f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Python?{os.linesep} [2] - Quanto tempo leva para conseguir um emprego com Python?{os.linesep} ')


if __name__ == '__main__':
    start()