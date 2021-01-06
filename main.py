"""
FelipedelosH dic 2020

this is my vr 0.1 of LokoBall




"""
__author__      = "FelipedelosH"

from controller import *
from tkinter import *
import os # To know path project
import sys # To close APP

class LunarLoko:
    def __init__(self):
        self.pathProject = str(os.path.dirname(os.path.abspath(__file__)))
        self.controller = Controller()
        self.display = Tk() # Show a display
        self.screem = Canvas(self.display, bg="snow") # paint all things
        # Imagenes to background
        self.imgBgMain = PhotoImage(file=self.pathProject+"\\RESOURCES\\IMG\\main.gif")
        # Buttons to controller a main title
        self.btnMainPlayGame = Button(self.screem, text="Play Game")
        self.btnMainOptions = Button(self.screem, text="Options")
        self.btnMainExit = Button(self.screem, text="Exit", command=self.closeProgram)
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
        show a interface from controller.game.gameStatus
        """

        if self.controller.game.gameStatus.pointer == "main":
            self.screem.create_image(0, 0, image=self.imgBgMain, anchor=NW)
            self.btnMainPlayGame.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3)
            self.btnMainOptions.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3 + self.resolutionH*0.1)
            self.btnMainExit.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3 + self.resolutionH*0.2)

        self.screem.after(30, self.refreshDisplay)

    def configureSizeOfDisplay(self):
        resolution = str(self.resolutionW)+"x"+str(self.resolutionH)
        self.display.geometry(resolution)
        self.screem['width'] = self.resolutionW
        self.screem['height'] = self.resolutionH

    def configureGameStatus(self, key):
        """
        Modify a main machine of states:
        The main sructure (Machine of states) to change Main Menu, Pause, Game, Options
        """
        self.controller.game.gameStatus.insertSimbol(key)

    def closeProgram(self):
        """
        End the program and close
        """
        sys.exit()



billar = LunarLoko()
