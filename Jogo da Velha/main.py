
#print(quadro)
#print("Qual linha e qual coluna vc vai jogar?")
#linha = int(input("Linha: "))
#coluna = int(input("Coluna: "))

#quadro[linha-1][coluna-1] = "X"
#print(quadro)
#col1 = (quadro[0][0],quadro[1][0],quadro[2][0])
#col2 = ()
#col3 = ()

def verifica(col1):
    if primeira_vez == False:
        return False
    #Coluna 1
    if col1 == ('X','X','X') or col1 == ('O','O','O'):    #Começa a verificar as colunas
        return True
    elif col2 == ('X','X','X') or col2 == ('O','O','O'):
        return True
    elif col3 == ('X','X','X') or col3 == ('O','O','O'):   
        return True                                       #Termina a verificar as colunas
    elif linha1 == ('X','X','X') or linha1 == ('O','O','O'):
        return True
    elif linha2 == ('X','X','X'):
        return
quadro = [[0,0,0],
          [0,0,0],
          [0,0,0]]
primeira_vez = True 
col1 = (quadro[0][0],quadro[1][0],quadro[2][0])
col2 = (quadro[0][1],quadro[1][1],quadro[2][1])
col3 = (quadro[0][2],quadro[1][2],quadro[2][2])
jogador1 = 'X'
jogador2 = 'O'
numJogadas = 1   
while verifica(col1)!= True:
        print(quadro)
        print("Qual linha e qual coluna vc vai jogar?")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        numJogadas += 1
        if numJogadas %2 == 0:           
            quadro[linha-1][coluna-1] = jogador1
        else:
            quadro[linha-1][coluna-1] = jogador2
        print(col1)
        col1 = (quadro[0][0],quadro[1][0],quadro[2][0])
        col2 = (quadro[0][1],quadro[1][1],quadro[2][1])
        col3 = (quadro[0][2],quadro[1][2],quadro[2][2])
        linha1 = (quadro[0])
        linha2 = (quadro[1])
        linha3 = (quadro[2])      
        diag1 = (quadro[0][0],quadro[1][1],quadro[2][2])
        diag2 = (quadro[0][2],quadro[1][1],quadro[2][0])  
        if verifica(col1,col2,col3,linha1,linha2,linha3,diag1,diag2):
            print("Jogador X ganhou")
            break
        continue
