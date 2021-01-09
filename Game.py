"""
This is a machine of status of lokoBall


"""
__author__      = "FelipedelosH"

from MachineOfStates import *
from Ball import *

class Game:
    def __init__(self):
        self.gameStatus = MachineOfStates() # say a game status main, gameOPT, 1pvsCp, 1pvs2p
        self.configureGameStatus()
        # Balls
        self.ballWhite = Ball()
        self.ballYellow = Ball()
        self.ballRed = Ball()
        self.balls = [self.ballWhite, self.ballYellow, self.ballRed]
        # Table
        self.SizeOfTable = 0 # Autoconfigure when the game is run
        # Players
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
        """
        self.ballWhite.posx = self.SizeOfTable * 0.3
        self.ballWhite.posy = self.SizeOfTable / 2
        self.ballWhite.name = "white"
        self.ballYellow.posx = self.SizeOfTable * 1.4
        self.ballYellow.posy = self.SizeOfTable / 2
        self.ballYellow.name = "yellow"
        self.ballRed.posx = self.SizeOfTable * 1.7
        self.ballRed.posy = self.SizeOfTable / 2
        self.ballRed.name = "red"

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