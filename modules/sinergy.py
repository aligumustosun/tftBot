from .crop import *
from .convert import *
from .match import *

def getSinergies():
    sinergyImages = getSinergyImages(3)
    for image in sinergyImages:
        print(matchSinergy(imageToText(image[0])).name)
        print(digitImageToText(image[1]))

