from kivy.app import App
from kivy.uix.label import Label
def build():
    return Label(text="Hello World")

aplica = App()
aplica.build = build
aplica.run()