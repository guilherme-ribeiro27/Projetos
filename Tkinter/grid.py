from tkinter import *

root = Tk()

myLabel = Label(root,text='Hello World')
myLabel2 = Label(root,text='Eu sou o Guilherme')
myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()