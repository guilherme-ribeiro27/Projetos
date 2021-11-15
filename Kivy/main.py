from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.graphics import Color,Ellipse,Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    def confirmacao(self,*args):
        pop = Popup(title='Deseja mesmo sair?', content=box,size_hint=(None,None),size=(300,180))

        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10,spacing=10)

        sim = Botao(text='Sim',on_release=App.get_running_app().stop)
        nao = Botao(text='Não',on_release=pop.dismiss)
        botoes.add_widget(sim)
        botoes.add_widget(nao)
        atencao = Image(source='./images/atencao.png')
        box.add_widget(atencao)
        box.add_widget(botoes)

        pop.open()

class Botao(ButtonBehavior,Label):
    cor = ListProperty([0.1,0.5,0.7,1])
    cor_on_press = ListProperty([0.1,0.1,0.1,1])
    def __init__(self, **kwargs):
        super(Botao, self).__init__(**kwargs)
        self.atualizar()
    
    def on_press(self,*args):
            self.cor, self.cor_on_press = self.cor_on_press, self.cor
        
    def on_release(self):
        self.cor, self.cor_on_press = self.cor_on_press, self.cor

    def on_cor(self,*args):
        self.atualizar()

    def on_pos(self,*args):
        self.atualizar()

    def on_size(self,*args):
        self.atualizar()
    
    def atualizar(self,*args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height,self.height),
                    pos=self.pos)
            Ellipse(size=(self.height,self.height),
                    pos=(self.x+self.width-self.height,self.y))
            Rectangle(size=(self.width-self.height,self.height),
                    pos=(self.x+(self.height/2.0),self.y))

class Tarefas(Screen):
    def __init__(self, tarefas = [],**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text= tarefa))
    
    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key==27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

        
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ''
        
class Tarefa(BoxLayout):
    def __init__(self,text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test(App):
    def build(self):
        return Gerenciador()
        
Test().run()