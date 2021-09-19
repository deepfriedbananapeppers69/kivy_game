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

class my_grid(Screen, Widget):
    nocal = ObjectProperty(None)
    socal = ObjectProperty(None)
    desert = ObjectProperty(None)
    vancouver = ObjectProperty(None)
    seattle = ObjectProperty(None)
    other = ObjectProperty(None)
    choicelabel = ObjectProperty(None)
    scorelable = ObjectProperty(None)
    message = ObjectProperty(None)
    wb = load_workbook('MASTEREXCEL.xlsx')
    wsPM = wb["PMCODES"]
    score = 0


    
    
    
    SoCal = []
    for col in wsPM['A']:
        SoCal.append(col.value)
    SoCal = [i for i in SoCal if i != None]

    NoCal = []
    for col in wsPM['B']:
        NoCal.append(col.value)
    NoCal = [i for i in NoCal if i != None]

    Desert = []
    for col in wsPM['C']:
        Desert.append(col.value)
    Desert = [i for i in Desert if i != None]
        
    Vancouver = []
    for col in wsPM['D']:
        Vancouver.append(col.value)
    Vancouver = [i for i in Vancouver if i != None]

    Seattle = []
    for col in wsPM['E']:
        Seattle.append(col.value)
    Seattle = [i for i in Seattle if i != None]

    Other = []
    for col in wsPM['F']:
        Other.append(col.value)
    Other = [i for i in Other if i != None]

    fullList = list(SoCal + NoCal + Desert + Vancouver + Seattle + Other)
    choicevar = random.choice(fullList)
    
        
    def btn(self):
        self.numberscore = 0 
        self.choicevar = random.choice(self.fullList)
        self.choicelabel.text = str(self.choicevar)
    
    def NOCALCHECK (self,):
        answer = self.choicevar
        if answer in self.NoCal:
            self.message.text = "correct"
            self.choicevar = random.choice(self.fullList)
            self.choicelabel.text = str(self.choicevar)
            self.score += 1
            self.scorelabel.text = str(self.score)
        else:
            self.message.text = "wrong"
            self.score -=1
            if self.score < 0:
                self.score = 0
            self.scorelabel.text = str(self.score)
    def SOCALCHECK (self,):
        answer = self.choicevar
        self.score = 0
        if answer in self.SoCal:
            self.message.text = "correct"
            self.choicevar = random.choice(self.fullList)
            self.choicelabel.text = str(self.choicevar)
            self.score += 1
            self.scorelabel.text = str(self.score)
        else:
            self.message.text = "wrong"
            self.score -=1
            if self.score < 0:
                self.score = 0
            self.scorelabel.text = str(self.score)
    def DESERTCHECK (self,):
        answer = self.choicevar
        if answer in self.Desert:
            self.message.text = "correct"
            self.choicevar = random.choice(self.fullList)
            self.choicelabel.text = str(self.choicevar)
            self.score += 1
            self.scorelabel.text = str(self.score)
        else:
            self.message.text = "wrong"
            self.score -=1
            if self.score < 0:
                self.score = 0
            self.scorelabel.text = str(self.score)
    def VANCOUVERCHECK (self,):
        answer = self.choicevar
        if answer in self.Vancouver:
            self.message.text = "correct"
            self.choicevar = random.choice(self.fullList)
            self.choicelabel.text = str(self.choicevar)
            self.score += 1
            self.scorelabel.text = str(self.score)
        else:
            self.message.text = "wrong"
            self.score -=1
            if self.score < 0:
                self.score = 0
            self.scorelabel.text = str(self.score)
    def SEATTLECHECK (self,):
        answer = self.choicevar
        if answer in self.Seattle:
            self.message.text = "correct"
            self.choicevar = random.choice(self.fullList)
            self.choicelabel.text = str(self.choicevar)
            self.score += 1
            self.scorelabel.text = str(self.score)
        else:
            self.message.text = "wrong"
            self.score -=1
            if self.score < 0:
                self.score = 0
            self.scorelabel.text = str(self.score)
    def OTHERCHECK (self,):
        answer = self.choicevar
        if answer in self.Other:
            self.message.text = "correct"
            self.choicevar = random.choice(self.fullList)
            self.choicelabel.text = str(self.choicevar)
            self.score += 1
            self.scorelabel.text = str(self.score)
        else:
            self.message.text = "wrong"
            self.score -=1
            if self.score < 0:
                self.score = 0
            self.scorelabel.text = str(self.score)
    
    





class MyApp(App):
    
    def build(self):
        
        sm = ScreenManager()
        sm.add_widget(my_grid(name='game'))
        sm.add_widget()
        return sm
            


if __name__ == '__main__':
    MyApp().run()
    