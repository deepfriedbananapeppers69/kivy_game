
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class my_grid(GridLayout):
    def __init__(self, **kwargs):
        super(my_grid, self).__init__(**kwargs)
        self.cols = 1 
        
        
        self.inside = GridLayout()
        self.inside.cols = 2
        self.string1 = "vbhjvbajbndf"
        self.inside.add_widget(Label(text=string1))
        self.name = TextInput()
        self.inside.add_widget(self.name)
              
        
        self.add_widget(self.inside)
        
        self.sumbit = Button(text="ljknakjfj", font_size=40) 
        self.sumbit.bind(on_press=self.pressed)
        self.add_widget(self.sumbit)
        
    def pressed(self, instance):
        print("pressed")
        
        
        
class MyApp(App):
    def build(self):
        return my_grid()
            


if __name__ == '__main__':
    MyApp().run()
    