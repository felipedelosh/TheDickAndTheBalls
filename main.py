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
        self.btnMainPlayGame = Button(self.screem, text="Play Game", command=lambda : self.configureGameStatus(0))
        self.btnMainOptions = Button(self.screem, text="Options")
        self.btnMainExit = Button(self.screem, text="Exit", command=self.closeProgram)
        # Vars to configure a size of display
        self.resolutionW = 720
        self.resolutionH = 480
        # Vars
        self.needToPaintInterface = True # Control if i need paints elements or buttons... in screem
        self.posOfTable = [0, 0, 0, 0] # Sayme a point x0, y0, x, y to the game table
        # Send info about size of table
        self.controller.configureZiseOfTable(self.resolutionH)
        # Puts balls in init
        self.controller.configureBallsInInt()
        
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
        if self.controller.game.gameStatus.pointer == "main" and self.needToPaintInterface:
            self.screem.create_image(0, 0, image=self.imgBgMain, anchor=NW, tags="main")
            self.btnMainPlayGame.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3)
            self.btnMainOptions.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3 + self.resolutionH*0.1)
            self.btnMainExit.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3 + self.resolutionH*0.2)
            self.needToPaintInterface = False

        if self.controller.game.gameStatus.pointer == "game" and self.needToPaintInterface:
            # Create a line to divide main screem
            self.screem.create_line(self.resolutionW*0.01, self.resolutionH*0.2, self.resolutionW*0.99, self.resolutionH*0.2)
            # Create a Player Status, Ball Effect, Emotions
            # Need H y W to rectangles
            H = self.resolutionH * 0.18
            W = self.resolutionW * 0.3
            K = self.resolutionH * 0.1
            for i in range(0, 3):
                self.screem.create_rectangle(((i*W)+K), (self.resolutionH*.01), ((i+1)*W), (H), tags="game")

            # Paint a table
            """
            A = L1
            B = L1
            L <=> l because a screem is HW
            table = A+B
            """
            L = self.resolutionW * 0.45
            l = self.resolutionH * 0.88
            K = self.resolutionH * 0.12
            # Update a register to controller a post of table
            self.posOfTable = [(K), (self.resolutionH*0.3), (2*L), (l)]

            self.screem.create_rectangle((K), (self.resolutionH*0.3), (2*L), (l), fill="green", tags="table")
            
            # Paint balls
            self.paintBalls()

            self.needToPaintInterface = False

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
        self.clearScreem()
        self.controller.game.gameStatus.insertSimbol(key)

    def clearScreem(self):
        """
        This metohods delete and hide all elemetns in the screem
        """
        self.screem.delete("main")
        self.screem.delete("game")
        self.screem.delete("balls")
        self.needToPaintInterface = True
        self.btnMainPlayGame.place_forget()
        self.btnMainOptions.place_forget()
        self.btnMainExit.place_forget()

    def closeProgram(self):
        """
        End the program and close
        """
        sys.exit()

    def paintBalls(self):
        """
        Paint a balss in a table
        """
        for i in self.controller.game.balls:
            xy = self.controller.returnPosXYBallsInPercent(i.name)
            x0 = (self.posOfTable[2] - self.posOfTable[0])*xy[0]
            y0 = self.posOfTable[1]+((self.posOfTable[3] - self.posOfTable[1])*xy[1])
            
            self.screem.create_oval(x0, y0, x0+20, y0+20, fill=i.name, tags="balls")



billar = LunarLoko() # Andre's Felipe Herna'ndes 