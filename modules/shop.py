from .crop import *
from .convert import *
from pynput.mouse import Button, Controller
from .classes import * 
from .origins import *
from .match   import *
import cv2

import time

mouse = Controller()

def produceSimiliarTexts(text):
    lowerText = text.lower()
    texts = []
    for i in range(6):
        if(i>2):
            texts.append(lowerText[0:i+1])
    return texts

exceptionOrigins = ["dark", "space", "star", "void"]

def checkSinergies():
    try:
        i = 0
        for i in range(5):
            images = getShopCardImages(i)
            classText = imageToText(images[0])
            originText = imageToText(images[1])
            heroName = imageToText(images[2])
            matchedClass = matchClass(classText)
            matchedOrigin = matchOrigin(originText)
            print(heroName + ":")
            print(matchedClass)
            print(matchedOrigin)
            matchedClass.increaseShopCount()
            matchedOrigin.increaseShopCount()
    except :
        print("Error when trying to check sinergies: ")
        return 0

def checkOrigin(originText):
    return
def checkClass(classText, originText, callTime):
    return


def buy(heroIndex):
    print("time to buy")
    mouse.position = (530+heroIndex*160, 750)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.position = (530+heroIndex*160, 600)
    time.sleep(0.1)
    mouse.release(Button.left)

