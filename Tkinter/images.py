from tkinter import *
from PIL import ImageTk, Image
tela = Tk()
tela.title('Aprendendo imagens')

my_img = ImageTk.PhotoImage(Image.open('./images/pp.jpg'))
my_label = Label(image=my_img)
my_label.pack()


tela.mainloop()
