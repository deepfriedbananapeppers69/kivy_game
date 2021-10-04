from inspect import FullArgSpec
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from openpyxl import workbook, load_workbook
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import PMGAME

class pong(Screen):
    gamedata = PMGAME.my_grid()
    
    def btn(self):
        #self.choicevarstart = random.choice(self.gamedata.fullList)
        #self.testlabel.text = str(self.choicevar)
        #self.gamedata.choicelabel = str(self.choicevar)
        self.manager.screens[1].ids.choicelabel.text = str(self.gamedata.choicevar)
        self.manager.screens[1].ids.lifelabel.text =  "You have " + str(self.gamedata.lifes) + " left"

class MyApp(App):
    
    def build(self):
        
        sm = ScreenManager()
        
        sm.add_widget(pong(name="main"))
        sm.add_widget(PMGAME.my_grid(name='pm_game'))
        return sm
            


if __name__ == '__main__':
    MyApp().run()
    