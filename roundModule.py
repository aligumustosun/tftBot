import cropModule
import convertModule

def getRound():
    roundText = '5-4'
    return roundText

def getSecondsLeft():
    roundTimeSingle = convertModule.imageToText(cropModule.getImage('roundTimeSingle'))
    if(roundTimeSingle == ''):
        roundTimeDouble = convertModule.imageToText(cropModule.getImage('roundTime'))[0:2]
        if(allDigit(roundTimeDouble)):
            return roundTimeDouble
        else:
            return getSecondsLeft()    
    elif(allDigit(roundTimeSingle[0])):
        return roundTimeSingle[0]
    else:
        return getSecondsLeft()    

def allDigit(string):
    for char in string:
        if(not char.isdigit()):
            return False
    return True            
