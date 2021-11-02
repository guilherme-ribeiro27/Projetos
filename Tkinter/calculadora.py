from tkinter import * 

tela = Tk()
tela.title('Calculadora')

myEntry = Entry(tela,width=50)
myEntry.grid(row=0,column=0,columnspan=4,padx=10,pady=20)

def button_click(number):
    #myEntry.delete(0,END)
    atual = myEntry.get()
    myEntry.delete(0,END)
    myEntry.insert(0,str(atual)+str(number))

def button_clear():
    myEntry.delete(0,END)

def button_add():
    n1 = myEntry.get()
    global f_num
    global opc
    opc = "add"
    f_num = int(n1)
    myEntry.delete(0,END)

def button_sub():
    n1 = myEntry.get()
    global f_num
    global opc
    opc = "sub"
    f_num = int(n1)
    myEntry.delete(0,END)

def button_mult():
    n1 = myEntry.get()
    global f_num
    global opc
    opc = "mult"
    f_num = int(n1)
    myEntry.delete(0,END)

def button_div():
    n1 = myEntry.get()
    global f_num
    global opc
    opc = "div"
    f_num = int(n1)
    myEntry.delete(0,END)

def button_equal():
    n2 = myEntry.get()
    myEntry.delete(0,END)
    if opc=='add':
        myEntry.insert(0,f_num+int(n2))
    elif opc=='sub':
        myEntry.insert(0,f_num-int(n2))
    elif opc=='mult':
        myEntry.insert(0,f_num*int(n2))
    elif opc=='div':
        myEntry.insert(0,f_num/int(n2))
    
#==========================================================================================================#
#============================Criando os botões e colocando na tela=========================================#
num7 = Button(tela, text='7',padx=30,pady=30,command=lambda: button_click(7))
num8 = Button(tela, text='8',padx=30,pady=30,command=lambda: button_click(8))
num9 = Button(tela, text='9',padx=30,pady=30,command=lambda: button_click(9))
soma = Button(tela, text='+',padx=30,pady=30,command=button_add)

num4 = Button(tela, text='4',padx=30,pady=30,command=lambda: button_click(4))
num5 = Button(tela, text='5',padx=30,pady=30,command=lambda: button_click(5))
num6 = Button(tela, text='6',padx=30,pady=30,command=lambda: button_click(6))
sub  = Button(tela, text='-',padx=30,pady=30,command=button_sub)

num1 = Button(tela, text='1',padx=30,pady=30,command=lambda: button_click(1))
num2 = Button(tela, text='2',padx=30,pady=30,command=lambda: button_click(2))
num3 = Button(tela, text='3',padx=30,pady=30,command=lambda: button_click(3))
div  = Button(tela, text='/',padx=30,pady=30,command=button_div)

num0 = Button(tela, text='0',padx=30,pady=30,command=lambda: button_click(0))
clear = Button(tela, text='C',padx=30,pady=30,command=button_clear)
mult = Button(tela, text='*',padx=30,pady=30,command=button_mult)
equal = Button(tela, text='=',padx=30,pady=30,command=button_equal)

#==========================================================================================================#
#=====================================COLOCANDO NA GRADE===================================================#

num7.grid(row=1,column=0)
num8.grid(row=1,column=1)
num9.grid(row=1,column=2)
soma.grid(row=1,column=3)

num4.grid(row=2,column=0)
num5.grid(row=2,column=1)
num6.grid(row=2,column=2)
sub.grid(row=2,column=3)

num1.grid(row=3,column=0)
num2.grid(row=3,column=1)
num3.grid(row=3,column=2)
div.grid(row=3,column=3)

num0.grid(row=4,column=0)
clear.grid(row=4,column=1)
mult.grid(row=4,column=2)
equal.grid(row=4,column=3)

#==========================================================================================================#

tela.mainloop()
