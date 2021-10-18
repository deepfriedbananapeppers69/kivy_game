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
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import PMGAME
import AMGAME

class menu(Screen):
    pmgamedata =  PMGAME.pm_grid()
    amgamedata = AMGAME.am_grid()
    
    def btn(self):
        
        self.manager.screens[3].ids.choicelabel.text = str(self.pmgamedata.choicevar)
        self.manager.screens[3].ids.lifelabel.text =  "You have " + str(self.pmgamedata.lifes) + " left"
        self.manager.screens[4].ids.choicelabel.text = str(self.amgamedata.choicevar)
        self.manager.screens[4].ids.lifelabel.text =  "You have " + str(self.amgamedata.lifes) + " left"

class start_menu(Screen):
    gamedata = PMGAME.pm_grid()
    nametext = ObjectProperty(None)
    
    def submit(self):
        self.name = self.nametext.text
        self.manager.screens[3].ids.namevar.text = self.name
        self.manager.screens[4].ids.namevar.text = self.name
        
    
    
    
class MainApp(App):
    
    
    def build(self):
        
        sm = ScreenManager()
        
        sm.add_widget(start_menu(name="getname"))
        sm.add_widget(menu(name="main"))
        sm.add_widget(PMGAME.pm_grid(name='pm_game'))
        sm.add_widget(AMGAME.am_grid(name='am_game'))
        return sm
            


if __name__ == '__main__':
    MainApp().run()
    