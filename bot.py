import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import re
import time
from modules import *
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



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
        while(self.running):
            checked = shop.checkSinergies(self.selectedClass, self.selectedOrigin)
            if(checked == 0):
                time.sleep(1)
            else:
                time.sleep(round.getSeconds()+1)
    def stop(self):
        self.running = False

    def checkMouse(self):
        if(Controller().position == (0,0)):
            self.stop()
        elif(Controller().position == (1535,863)):
            self.start()    


myBot = Bot()
#myBot.start()
#Controller().position = (530, 750)
#benchPositions = [(340,630), (430, 630), (520,630)]
#myBot.board.getClassImages()[0].show()
#Contoller().position = (430, 360)