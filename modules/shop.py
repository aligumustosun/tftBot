from difflib import SequenceMatcher
from .static.classes import getClasses
from .static.origins import getOrigins
from . import crop, convert
from pynput.mouse import Button, Controller
import time

origins = getOrigins()
classes = getClasses()
mouse = Controller()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def produceSimiliarTexts(text):
    lowerText = text.lower()
    texts = []
    for i in range(6):
        if(i>2):
            texts.append(lowerText[0:i+1])
    return texts

exceptionOrigins = ["dark", "space", "star", "void"]


def checkSinergies(selectedOrigin, selectedClass):
    try:
        classImages = crop.getImages('shopClasses')
        i = 0
        for image in classImages:
            classText = convert.imageToText(image) 
            foundClass = checkClass(classText, 0, 0)
            if(selectedClass == foundClass):
                buy(i)
            i+=1        
            time.sleep(1)
            print("foundClass: " + foundClass)
        originImages = crop.getImages('shopOrigins')
        i = 0
        for image in originImages:
            originText = convert.imageToText(image)
            foundOrigin = checkOrigin(originText, 0, 0)
            if(selectedOrigin == foundOrigin):
                buy(i)    
            i+=1
            time.sleep(1)
            print("foundOrigin: " + foundOrigin)
        return [foundClass, foundOrigin]
    except NameError:
        print("Error when trying to check sinergies: "+ NameError)
        return 0

def checkOrigin(originText, classText, callTime):
    print("originText: " + originText)
    if(originText == ''):
        return 'None'
    if(callTime == 1):
        return classText
    texts = originText.lower().split(" ")
    texts = originText
    similarities = []
    for origin in origins:
        halfLength = int(len(origin)/2)
        parsedOrigins = [origin[0:halfLength], origin[halfLength:len(origin)-1] ]
        if(len(texts) == 2):
            similarities.append(similar(parsedOrigins[0], texts[0]) + similar(parsedOrigins[1], texts[1]))
        else:
            similarities.append(similar(origin, originText))
        if(max(similarities)>0.4):        
            return origins[similarities.index(max(similarities))]    
    else:
        return checkClass(originText, origins[similarities.index(max(similarities))], 1)

def checkClass(classText, originText, callTime):
    if(classText == ''):
        return 'None'
    if(callTime == 1):
        return originText
    texts = classText.lower().split(" ")
    similarities = []
    for heroClass in classes:
        if(len(texts) == 2):
            similarities.append(similar(heroClass, texts[0]) + similar(heroClass, texts[1]))
        else:
            similarities.append(similar(heroClass, texts[0]))
    if(max(similarities)>0.4):    
        return classes[similarities.index(max(similarities))]
    else:
        return checkOrigin(classText, classes[similarities.index(max(similarities))], 1)        


def buy(heroIndex):
    print("time to buy")
    mouse.position = (530+heroIndex*160, 750)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.position = (530+heroIndex*160, 600)
    time.sleep(0.1)
    mouse.release(Button.left)

