"""
FelipedelosH dic 2020

this is my vr 0.1 of LokoBall


"""
__author__      = "FelipedelosH"

from controller import * 
from tkinter import * # To graphics
import os # To know path project
import sys # To close APP

class LunarLoko:
    def __init__(self):
        self.pathProject = str(os.path.dirname(os.path.abspath(__file__)))
        self.controller = Controller()
        self.display = Tk() # Show a display
        self.screem = Canvas(self.display, bg="snow") # paint all things
        self.screem.bind('<Motion>', self.mouseMotionListener) # Listener to x, y mouse position
        self.screem.bind('<Button-1>', self.mouseClickLister) # If you mouse click this is listener
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
        

        # Configure game Propiertis
        self.configureGameProperties()

        self.showDisplay()

    def configureGameProperties(self):
        self.controller.initGame(self.resolutionH)
        

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
        if self.controller.getGameStatus() == "main" and self.needToPaintInterface:
            self.screem.create_image(0, 0, image=self.imgBgMain, anchor=NW, tags="main")
            self.btnMainPlayGame.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3)
            self.btnMainOptions.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3 + self.resolutionH*0.1)
            self.btnMainExit.place(x=self.resolutionW*0.7-(self.resolutionW*0.1), y=self.resolutionH/3 + self.resolutionH*0.2)
            self.needToPaintInterface = False

        if self.controller.getGameStatus() == "game" and self.needToPaintInterface:
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

        self.paintTarget() # If the game is play: paint a target
        self.screem.after(30, self.refreshDisplay)

    def mouseMotionListener(self, event):
        """
        If game is play the target only refresh:
        - Inside of table
        """
        # Refresh a target position inside table paint else delete
        if self.controller.getGameStatus() == "game":
            if self.mouseIsInsideOfTable(event.x, event.y):
                self.controller.configureTargetXY(event.x, event.y, self.posOfTable[0], self.posOfTable[1], self.posOfTable[2], self.posOfTable[3])
    


    def mouseClickLister(self, event):
        """
        1 -> if the game is play and target is inside of gametable HIT
            > First i take a mouse x and y and recalculate it inside game table
        2 -> 
        """
        print(self.controller.returnBallXYkey("white"))
        print(self.controller.returnTargetXY())
            

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


    def paintBalls(self):
        """
        Paint a balss in a table
        """
        for i in self.controller.getAllBalls():
            xy = self.controller.returnPosXYBallsInPercent(i.name)
            # (Distance tableX * %) + pos init table
            x0 = self.posOfTable[0] + ((self.posOfTable[2] - self.posOfTable[0]) * xy[0])
            # (Distance tableY * %)
            y0 = self.posOfTable[1] + ((self.posOfTable[3] - self.posOfTable[1]) * xy[1])
            self.screem.create_oval(x0, y0, x0+20, y0+20, fill=i.name, tags="balls")




    def paintTarget(self):
        """
        if the game is run need to paint a target to hill the ball (balla nd 2 lines)

        1 - need information:

       
        """
        if self.controller.getGameStatus() == "game":
            self.deleteTarget()# To erase before and paint a new target
            xy = self.controller.returnPosXYTargetInPercent() # Get a target pos%

            # (Distance tableX * %) + pos init table
            x0 = self.posOfTable[0] + ((self.posOfTable[2] - self.posOfTable[0]) * xy[0])
            # (Distance tableY * %)
            y0 = self.posOfTable[1] + ((self.posOfTable[3] - self.posOfTable[1]) * xy[1])
            self.screem.create_oval(x0, y0, x0+20, y0+20, tags="target")
            self.screem.create_line(x0-10, y0+10, x0+30, y0+10, tags="target")
            self.screem.create_line(x0+10, y0-10, x0+10, y0+30, tags="target")
        

    def deleteTarget(self):
        self.screem.delete("target")

        

    def mouseIsInsideOfTable(self, x, y):
        """
        Return if the target is inside table
        """
        return x > self.posOfTable[0] and x < self.posOfTable[2] and y > self.posOfTable[1] and y < self.posOfTable[3]


    def clearScreem(self):
        """
        This metohods delete and hide all elemetns in the screem
        """
        self.screem.delete("main")
        self.screem.delete("game")
        self.screem.delete("balls")
        self.screem.delete("target")
        self.needToPaintInterface = True
        self.btnMainPlayGame.place_forget()
        self.btnMainOptions.place_forget()
        self.btnMainExit.place_forget()

    def closeProgram(self):
        """
        End the program and close
        """
        sys.exit()
        
billar = LunarLoko() # Andre's Felipe Herna'ndes 