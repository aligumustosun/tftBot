import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import re
import time
from modules import *
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


mouse = Controller()

class Options():
    def __init__(self, economyMode, selectedOrigin, selectedClass):
        self.economyMode = economyMode
        self.selectedOrigin = selectedOrigin
        self.selectedClass = selectedClass
        self.board = board.Board()


defaultOptions = Options('aggressive', 'blademaster','celestial')

class Bot():
    def __init__(self, options=defaultOptions):
        botParser.initializeValues(self, options)

    def getInformations(self):
        attrs = vars(self)
        for item in attrs.items():
            print(item[0] + ": " + item[1])   
        
    def start(self):
        self.running = True

#myBot = Bot()
#shop.checkSinergies()

#print(convert.mouseToScreen(mouse.position))
print(sinergy.getSinergies())
#firstSinergy (81,287,181,307)
#second sinergy (81, 337, 181, 357)