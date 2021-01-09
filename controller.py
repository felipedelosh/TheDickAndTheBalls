"""
This is a controller for lokoBall

1 - 
"""
__author__      = "FelipedelosH"

from Ball import *
from Game import *

class Controller:
    def __init__(self):
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

    def configureZiseOfTable(self, resolutionW):
        """
        When the program runs i need information to define a size of table
        the table is 2 perfect squares, here only calculate single L for one square
        """
        self.game.SizeOfTable = resolutionW * 0.4

    def configureBallsInInt(self):
        self.game.configureBallsInInt()

    def returnPosXYBallsInPercent(self, key):
        return self.game.returnPercentOfPosXPosYOfBalls(key)

    """
    Methods GAME
    """