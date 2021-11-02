import random as r

def interface():
    print('----------------------------------------')
    print('             Jogo da sorte              ')
    print('----------------------------------------')

def gerar_numero():
    num = r.randint(0,101)
    return num

def verifica():
    print()

interface()
gerar_numero()