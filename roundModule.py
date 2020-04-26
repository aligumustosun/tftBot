import cropModule
import convertModule

def getRound():
    roundText = '5-4'
    return roundText

def getSecondsLeft(callDepth):
    if(callDepth==2):
        return '0'
    roundTimeSingle = convertModule.imageToText(cropModule.getImage('roundTimeSingle'))
    if(roundTimeSingle == ''):
        roundTimeDouble = convertModule.imageToText(cropModule.getImage('roundTime'))[0:2]
        if(allDigit(roundTimeDouble)):
            return roundTimeDouble
        else:
            return getSecondsLeft(callDepth+1)    
    elif(allDigit(roundTimeSingle[0])):
        return roundTimeSingle[0]
    else:
        return getSecondsLeft(callDepth+1)    

def allDigit(string):
    for char in string:
        if(not char.isdigit()):
            return False
    return True            
