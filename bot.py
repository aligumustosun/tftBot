import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import shopModule
import re
import time
import cropModule
import convertModule
import gold

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
mouse = Controller()


def checkSinergies(selectedClass, selectedOrigin):
    classImages = cropModule.getImages('shopClasses')
    i = 0
    for image in classImages:
        classText = convertModule.imageToText(image) 
        foundClass = shopModule.checkClass(classText, 0, 0)
        if(selectedClass == '' and foundClass != 'None'):
            selectedClass = foundClass
            buyFromShop(i)
        elif(selectedClass == foundClass):
            buyFromShop(i)
        i+=1        
        time.sleep(1)
        print("foundClass: " + foundClass)
    originImages = cropModule.getImages('shopOrigins')
    i = 0
    for image in originImages:
        originText = convertModule.imageToText(image)
        foundOrigin = shopModule.checkOrigin(originText, 0, 0)
        if(selectedOrigin == '' and foundClass != 'None'):
            selectedOrigin = foundOrigin
            buyFromShop(i)
        elif(selectedOrigin == foundOrigin):
            buyFromShop(i)    
        i+=1
        time.sleep(1)
        print("foundOrigin: " + foundOrigin)
    return [foundClass, foundOrigin]

        

def buyFromShop(heroIndex):
    mouse.position = (530+heroIndex*160, 750)
    mouse.press(Button.left)
    mouse.release(Button.left)

def procudeSimiliarTexts(text):
    lowerText = text.lower()
    texts = []
    for i in range(len(text)):
        if(i>2):
            texts.append(lowerText[0:i+1])
    print(texts)
    return texts

#print(cropModule.getImages('shopClasses'))
#checkSinergies('','')


k = 0
selectedClass  = ''
selectedOrigin = ''
while(k>4):
    input()   
    decisions = checkSinergies(selectedClass, selectedOrigin)
    selectedClass = decisions[0]
    selectedOrigin = decisions[1]

print(gold.get())