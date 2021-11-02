import os 
inscritos = ['Guilherme Ribeiro','João qualquer','Maria qualquer','Larissa qualquer']
with open('inscritos.txt','w',newline='') as file:
    for line in inscritos:
        file.write(line + os.linesep)