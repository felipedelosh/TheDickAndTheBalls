"""
This is a machine of status of lokoBall


"""
__author__      = "FelipedelosH"

from MachineOfStates import *

class Game:
    def __init__(self):
        self.gameStatus = MachineOfStates() # say a game status main, gameOPT, 1pvsCp, 1pvs2p
        self.configureGameStatus()
        self.Players =[]
        

    def configureGameStatus(self):
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