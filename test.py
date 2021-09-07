import random
from ctypes import string_at
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class my_grid(Widget):
    pass
    '''
    def __init__(self, **kwargs):
        super(my_grid, self).__init__(**kwargs)
        self.cols = 1 
        self.inside = GridLayout()
        self.inside.cols = 2
        self.string1 = "vbhjvba"
        self.label1 = Label()
        self.inside.add_widget(self.label1)
        self.name = TextInput()
        self.inside.add_widget(self.name)
              
        
        self.add_widget(self.inside)
        
        self.sumbit = Button(text="ljknakjfj", font_size=40) 
        self.sumbit.bind(on_press=self.pressed)
        self.add_widget(self.sumbit)
        
    def pressed(self, instance):
        self.number = random.randint(0,5)       
        text = self.name.text
        print(text)
        self.name.text = ""
        self.label1.text = str(self.number)
    
    def changelabel(self, instance):
        self.string1 = "hello"
        self.label1 = self.label1
     '''      
        
        
class MyApp(App):
    def build(self):
        return my_grid()
            


if __name__ == '__main__':
    MyApp().run()
    