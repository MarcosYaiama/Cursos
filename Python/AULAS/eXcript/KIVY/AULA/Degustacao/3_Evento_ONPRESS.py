from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
a = 0
def muda():
    print("cliquei")

def build():
    
    b1 = Button(text="Liga")
    b1.on_press = muda
    return b1

app = App()
app.build = build
app.run()