from tkinter import *
from typing import ValuesView

root = Tk(screenName='Tela do Gui')

def myClick():
    myClick = Label(root,text=myInput.get())
    myClick.pack()

myInput = Entry(root,width=50) #bg e fg também funcionam aqui

myButton = Button(root,text='Inserir dados',padx=50, pady=10,command= myClick, fg='yellow',bg='black') # state = DISABLED
myInput.pack() 
myButton.pack()


root.mainloop()