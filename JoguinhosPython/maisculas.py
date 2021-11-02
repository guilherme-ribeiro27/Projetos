lista = []
while True:
    texto = input('Digita o texto aí gato: \n')
    if texto=='s':
        break
    else:
        lista.append(texto)

for texto in lista:
    print(texto.upper())