from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def click():
    print(ed.text)

def build():
    
    layout = FloatLayout()
    
    ed = TextInput(text="eXcript")
    global ed
    ed.size_hint = None, None   #Reseta a propriedade SizeHint
    ed.height = 300
    ed.width = 400 
    ed.x = 100
    ed.y = 250

    bt = Button(text="Clique aqui")
    bt.size_hint = None, None
    bt.width = 400
    bt.height = 50
    bt.x = 100
    bt.y = 140
    bt.on_press = click

    layout.add_widget(bt)
    layout.add_widget(ed)

    return layout

janela = App()
janela.title = "eXcript"

from kivy.core.window import Window
Window.size = 600, 600

janela.build = build
janela.run()