from tkinter import *
from PIL import ImageTk,Image

tela = Tk()
tela.title('Frames')

frame = LabelFrame(tela, text="Isso é um Frame...",padx=5, pady=5)
frame.pack(padx=10,pady=10)

b = Button(frame, text='Não clique aqui!')
b2 = Button(frame,text='Botão 2')
b3 = Button(frame,text='Botão 3')
b.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
tela.mainloop()