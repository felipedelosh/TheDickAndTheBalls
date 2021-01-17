"""
This is a machine of status of lokoBall


"""
__author__      = "FelipedelosH"

from MachineOfStates import *
from Ball import *
from Target import *

class Game:
    def __init__(self):
        self.gameStatus = MachineOfStates() # say a game status main, gameOPT, 1pvsCp, 1pvs2p
        self.configureGameStatus()
        # Balls
        self.ballTarget = "" # Ball to Hit (white, yellow, red)
        self.ballWhite = Ball()
        self.ballYellow = Ball()
        self.ballRed = Ball() 
        self.balls = [self.ballWhite, self.ballYellow, self.ballRed] # Array with all balls
        # Table
        self.SizeOfTable = 0 # Autoconfigure when the game is run >> L
        # Players
        self.target = Target() # This is a interface usert to hit the ball and configures
        self.Players = []
        

    def configureGameStatus(self):
        """
        Configure a machine of status to control a game
        control if show main title menu or if u play
        if you pause if you enter to options
        """
        self.gameStatus.addNode("main")
        self.gameStatus.addNode("game")
        self.gameStatus.addNode("options")
        self.gameStatus.addNode("pause")
        self.gameStatus.setInitialPointer("main")
        self.gameStatus.addConection("main", "game", 0)
        self.gameStatus.addConection("main", "options", 1)
        self.gameStatus.addConection("game", "game", 1)
        self.gameStatus.addConection("game", "pause", 0)
        self.gameStatus.addConection("pause", "game", 0)
        self.gameStatus.addConection("pause", "options", 1)
        self.gameStatus.addConection("options", "game", 0)
        self.gameStatus.addConection("options", "main", 1)

    def configureBallsInInt(self):
        """
        Put a balls in initial potition
        and put a names
        select a first ball to hit
        Put a target in initial pos
        """
        self.ballTarget = "white"
        self.ballWhite.posx = self.SizeOfTable * 0.3
        self.ballWhite.posy = self.SizeOfTable / 2
        self.ballWhite.name = "white"
        self.ballYellow.posx = self.SizeOfTable * 1.4
        self.ballYellow.posy = self.SizeOfTable / 2
        self.ballYellow.name = "yellow"
        self.ballRed.posx = self.SizeOfTable * 1.7
        self.ballRed.posy = self.SizeOfTable / 2
        self.ballRed.name = "red"
        self.target.targetPosX = self.SizeOfTable
        self.target.targetPosY = self.SizeOfTable/2

    def returnPercentOfPosXPosYOfBalls(self, key):
        """
        return a x y of a ball in %

        The table is Lx2L

        return if the ball.key (white, yellow, red) is in 0.5 x  
        """
        if key == "white":
            x = (self.ballWhite.posx)/(2*self.SizeOfTable)
            y = (self.ballWhite.posy)/self.SizeOfTable
            return [x, y]

        if key == "yellow":
            x = (self.ballYellow.posx)/(2*self.SizeOfTable)
            y = (self.ballYellow.posy)/self.SizeOfTable
            return [x, y]

        if key == "red":
            x = (self.ballRed.posx)/(2*self.SizeOfTable)
            y = (self.ballRed.posy)/self.SizeOfTable
            return [x, y]

    def returnPercentOfPosXPosYOfTarget(self):
        """
        The target is inside of game table
        return a %X %Y of the target
        """
        x = (self.target.targetPosX) / (2*self.SizeOfTable)
        y = (self.target.targetPosY) / self.SizeOfTable

        return [x, y]


    def returnPosXYOfBall(self, key):
        """
        return a [x, y] pos x, y of ball.key (white, yellow, red)
        """
        if key == "white":
            x = self.ballWhite.posx
            y = self.ballWhite.posy
            return [x, y]

        if key == "yellow":
            x = self.ballYellow.posx
            y = self.ballYellow.posy
            return [x, y]

        if key == "red":
            x = self.ballRed.posx
            y = self.ballRed.posy
            return [x, y]