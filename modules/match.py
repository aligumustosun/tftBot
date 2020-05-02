from difflib import SequenceMatcher
from .classes import classList
from .origins import originList
from .origins import *
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()



def matchClass(text):
    values = []
    for heroClass in classList:
        values.append(similar(heroClass.name, text))
    return classList[values.index(max(values))]

def matchOrigin(text):
    if(text[0:4].lower() == 'star'):
        return starGuardian
    values = []
    for origin in originList:
        values.append(similar(origin.name, text))
    return originList[values.index(max(values))]

def matchSinergy(text):
    originValues=[]
    classValues =[]
    if(text[0:4].lower() == 'star'):
        return starGuardian
    for origin in originList:
        originValues.append(similar(origin.name, text))
    for heroClass in classList:
        classValues.append(similar(heroClass.name, text))
    if(max(classValues) > max(originValues)):
        return classList[classValues.index(max(classValues))]
    else:
        return originList[originValues.index(max(originValues))]

