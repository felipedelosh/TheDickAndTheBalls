"""
This is a controller for lokoBall

1 - 
"""
__author__      = "FelipedelosH"

from Ball import *
from Game import *

class Controller:
    def __init__(self):
        #Exists Table
        #Exists 3 ball
        
        self.ballA = Ball()
        self.ballB = Ball()
        self.ballC = Ball()

        self.game = Game()

    """
    Methods GAME
    """
    def gameStatus(self):
        """
        This mothod return a status of the game
        Main, GameConfig, GamePlay
        """
        return self.game.gameStatus

    """
    Methods GAME
    """