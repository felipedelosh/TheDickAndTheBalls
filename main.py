"""
FelipedelosH dic 2020

this is my vr 0.1 of LokoBall




"""
__author__      = "FelipedelosH"

from controller import *
from tkinter import *

class LunarLoko:
    def __init__(self):
        self.controller = Controller()
        self.display = Tk() # Show a display
        self.screem = Canvas(self.display, bg="snow") # paint all things

        

        # Vars to configure a size of display
        self.resolutionW = 720
        self.resolutionH = 480 
        

        self.showDisplay()

    def showDisplay(self):
        self.display.title("Billar By Loko")
        self.configureSizeOfDisplay()
        self.screem.place(x=0, y=0)
        

        self.display.after(0, self.refreshDisplay())
        self.display.mainloop()

    def refreshDisplay(self):
        """
        Refresh a screem every 30 ms
        """
        


        self.screem.after(30, self.refreshDisplay)

    def configureSizeOfDisplay(self):
        resolution = str(self.resolutionW)+"x"+str(self.resolutionH)
        self.display.geometry(resolution)
        self.screem['width'] = self.resolutionW
        self.screem['height'] = self.resolutionH



billar = LunarLoko()
