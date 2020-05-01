from pynput.mouse import Controller as mouseController, Button
from pynput.keyboard import Controller as keyboardController, Key
mouse = mouseController()
keyboard = keyboardController()
from PIL import ImageGrab
import time


def mouseToScreen(position):
    x,y = position
    return (int(x*xRatio), int(y*yRatio))

def screenToMouse(position):
    x,y = position
    return (int(x/xRatio), int(y/yRatio))

class Board():
    def __init__(self):
        self.checkCells()

    def checkCells(self):
        boardCells = [] 
        originImages = []
        classImages = []
        for i in range(4):
            halfCell = i%2 * 50 
            for k in range(7):
                mouseDifference = (100*k+halfCell, 60*i)
                mouseXDiff, mouseYDiff = mouseDifference
                screenDifference = mouseToScreen(mouseDifference)
                screenXDiff, screenYDiff = screenDifference
                posX = 430 + mouseXDiff
                posY = 360 + mouseYDiff
                boardCells.append((posX, posY))
                originImages.append(ImageGrab.grab(bbox =(635+screenXDiff, 360+screenYDiff, 710+screenXDiff, 380+screenYDiff)))
                classImages.append(ImageGrab.grab(bbox =(635+screenXDiff, 395+screenYDiff, 710+screenXDiff, 410+screenYDiff)))    
        self.boardCells = boardCells
        self.originImages = originImages
        self.classImages = classImages

    def getSinergies(self):
        for i in range(len(self.boardCells)):
            return
    
    def getClassImages(self):
        return self.classImages
        
    def getOriginImages(self):
        return self.originImages
        
xRatio = 1.2508143322475571
yRatio = 1.2514484356894555

