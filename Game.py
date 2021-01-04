"""
This is a machine of status of lokoBall


"""
__author__      = "FelipedelosH"

from MachineOfStates import *

class Game:
    def __init__(self):
        self.gameStatus = MachineOfStates() # say a game status main, gameOPT, 1pvsCp, 1pvs2p
        self.Players =[]

    def configureGameStatus(self):
        self.gameStatus