from . import crop, convert

def getRound():
    roundText = '5-4'
    return roundText

def getSeconds(callDepth=0):
    try:
        if(callDepth==2):
            return 0
        roundTimeSingle = convert.imageToText(crop.getImage('roundTimeSingle'))
        if(roundTimeSingle == ''):
            roundTimeDouble = convert.imageToText(crop.getImage('roundTime'))[0:2]
            if(allDigit(roundTimeDouble)):
                return int(roundTimeDouble)
            else:
                return getSeconds(callDepth+1)    
        elif(allDigit(roundTimeSingle[0])):
            return int(roundTimeSingle[0])
        else:
            return (getSeconds(callDepth+1))    
    except:
        print("Error when reading seconds left")
        return 0

def allDigit(string):
    for char in string:
        if(not char.isdigit()):
            return False
    return True            
