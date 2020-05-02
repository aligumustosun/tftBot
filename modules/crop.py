from PIL import ImageGrab, Image
import cv2
import numpy as nm
from pynput.mouse import Controller

xDiff = 201

classXStart = 507
classYStart = 1013
classYEnd = 1032
classXDif = 80

originXStart = 507
originYStart = 987
originYEnd = 1007
originXDif = 60

nameXStart = 482
nameYStart = 1043
nameYEnd = 1064
nameXDif = 90

shopClassImages = []
shopOriginImages = []
shopHeroNameImages = []
for i in range(5):
    classXEnd = classXStart + xDiff*i + classXDif
    originXEnd = originXStart + xDiff*i + originXDif
    nameXEnd = nameXStart + xDiff*i + nameXDif
    shopClassImages.append(
        ImageGrab.grab(bbox = (classXStart+i*xDiff, classYStart, classXEnd , classYEnd))
    )
    shopOriginImages.append(
        ImageGrab.grab(bbox = (originXStart+i*xDiff, originYStart, originXEnd , originYEnd))
    )
    shopHeroNameImages.append(
        ImageGrab.grab(bbox = (nameXStart+i*xDiff, nameYStart, nameXEnd , nameYEnd))
    )
      
def getShopCardImages(i):
    return [shopClassImages[i], shopOriginImages[i], shopHeroNameImages[i]]


sinergyImages = []

#firstSinergy (81,287,181,307)
#second sinergy (81, 337, 181, 357)
sinergyXStart = 81
sinergyXDiff = 100
sinergyYStart = 287
sinergyYDiff = 20
sinergyDiff = 50
countXStart = 58
countYStart = 297
countXDiff = 12
countYDiff = 25
for i in range(3):
    sinergyYEnd = sinergyYStart + i*sinergyDiff + sinergyYDiff
    countYEnd = countYStart + i*sinergyDiff + countYDiff
    sinergyImages.append(
       [
       ImageGrab.grab(bbox = (
           sinergyXStart, sinergyYStart + sinergyDiff * i,
            sinergyXStart+sinergyXDiff , sinergyYEnd)),
       ImageGrab.grab(bbox = (
           countXStart, countYStart + sinergyDiff * i,
            countXStart+countXDiff , countYEnd))       
       ] 
    )

def getSinergyImages(imageCount):
    return sinergyImages[0:imageCount]



def getImage(imageType):
    if(imageType=='goldDouble'):
        img = ImageGrab.grab(bbox =(870,880,930,910))
        concatImg = cv2.hconcat([nm.array(img), nm.array(img)])
        return nm.asarray(concatImg)

    elif(imageType=='goldSingle'):
        img = ImageGrab.grab(bbox =(884,883,898,910))
        concatImg = cv2.hconcat([nm.array(img), nm.array(img), nm.array(img)])
        return nm.asarray(concatImg)
    elif(imageType=='roundTime'):
        img = ImageGrab.grab(bbox =(1132,10,1170,35))
        concatImg = cv2.hconcat([nm.array(img),nm.array(img), nm.array(img)])
        return nm.asarray(concatImg)
    elif(imageType=='roundTimeSingle'):
        img = ImageGrab.grab(bbox =(1140,10,1155,32))
        concatImg = cv2.hconcat([nm.array(img),nm.array(img), nm.array(img)])
        return nm.asarray(concatImg)



bench1Class =  ImageGrab.grab(bbox =(505, 710, 600, 735)) #(340, 630) 
bench1Origin = ImageGrab.grab(bbox =(505, 745, 600, 770))

bench2Class =  ImageGrab.grab(bbox =(625, 710, 720, 735)) #(430, 630)
bench2Origin = ImageGrab.grab(bbox =(625, 745, 720, 770))



