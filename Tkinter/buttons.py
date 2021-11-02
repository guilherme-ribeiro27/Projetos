from tkinter import *

root = Tk(screenName='Tela do Gui')

def myClick():
    myClick = Label(root,text="Você clicou")
    myClick.grid(row=3,column=0)

myLabel = Label(root,text='Olá ')
myLabel2 = Label(root,text='Estou testando Buttons')
myButton = Button(root,text='Clique!',padx=50, pady=10,command=myClick, fg='yellow',bg='black') # state = DISABLED

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=0)
root.mainloop()