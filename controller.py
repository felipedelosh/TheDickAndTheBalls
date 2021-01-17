"""
This is a controller for lokoBall

1 - 
"""
__author__  = "FelipedelosH"

from Ball import *
from Game import *
import math

class Controller:
    def __init__(self):
        self.game = Game()

    """
    Methods GAME
    """
    def initGame(self, L):
        """
        When the game is start need to define L >> len of table
        need to put a balls in init
        """
        self.configureZiseOfTable(L)
        self.configureBallsInInt()

    def getGameStatus(self):
        """
        This mothod return a status of the game
        Main, GameConfig, GamePlay
        """
        return self.game.gameStatus.pointer

    def configureZiseOfTable(self, resolutionW):
        """
        When the program runs I need information to define a size of table
        the table is 2 perfect squares, here only calculate single L for one square
        """
        self.game.SizeOfTable = resolutionW

    def configureBallsInInt(self):
        self.game.configureBallsInInt()

    def getAllBalls(self):
        return self.game.balls

    def configureTargetXY(self, xTarget, yTarget, xTable, yTable, x1Table, y1Table):
        """
        The gameTable is out of range to mouse need to calibrate

        1 -> Need to calculate a L to the graphic interface
            L=y1-y0
        2 -> Need calculate a percent to te target inside of interface
        3 -> Calculate a new pos target with a percent to real L

        for decimals obtain +-0.1 values

    
        """
        Li = (y1Table - yTable)

        x = abs(xTarget - xTable)
        y = abs(yTarget - yTable)

        ptx = x/Li
        pty = y/Li

        if ptx >= 2:
            ptx = 2

        if pty > 1:
            pty = 1
        

        self.game.target.targetPosX = self.game.SizeOfTable * ptx
        self.game.target.targetPosY = self.game.SizeOfTable * pty

      

    def distanceBetwenTargetAndBallHit(self, x, y):
        """
        the posxy the target in the table is calculate
        firts enter xy to target inside of table x>0 and x < 2L ; y < L
        D = SQRT(DX2, DY2)
        target and ball to hit (white, red, yellow)
        """
        
        return self.returnBallXYkey(self.game.ballTarget)

    def returnTargetXY(self):
        """
        return mousexy in target
        """
        x = self.game.target.targetPosX
        y = self.game.target.targetPosY
        return [x, y]

    def returnBallXYkey(self, key):
        """
        return xy to ball.key(white, yellow, red)
        """
        return self.game.returnPosXYOfBall(key)


    def returnPosXYBallsInPercent(self, key):
        """
        x > 0 and x < 2L  
        0 < y < L

        return a percent xy to paint
        """
        return self.game.returnPercentOfPosXPosYOfBalls(key)

    def returnPosXYTargetInPercent(self):
        """
        The target xy is inside of table 
        x > 0 and x < 2L  
        0 < y < L

        return a percent xy to paint
        """
        return self.game.returnPercentOfPosXPosYOfTarget()

    """
    Methods GAME
    """