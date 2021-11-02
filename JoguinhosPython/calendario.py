import calendar
import PySimpleGUI as sg



#calendario2022 = print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2022))

layout = [
        [sg.Text('Calendário')],
        [sg.Text(calendar.TextCalendar(calendar.SUNDAY).formatyear(2022),size=(100,50))]
    ]
janela = sg.Window('Usuários',layout=layout)
eventos, valores = janela.Read()