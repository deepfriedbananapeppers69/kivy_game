import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class my_grid(Widget):
    nocal = ObjectProperty(None)
    socal = ObjectProperty(None)
    choice = ObjectProperty(None)
    score = ObjectProperty(None)
    
    def btn(self):
        self.numberscore = 0 
        self.number = random.randint(0, 9)
        self.choice.text = str(self.number)
        self.score.text =   
        
class MyApp(App):
    def build(self):
        return my_grid()
            


if __name__ == '__main__':
    MyApp().run()
    