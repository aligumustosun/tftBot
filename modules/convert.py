import numpy as nm
import pytesseract
import cv2


def invertAndConvertGray(img):
    firstData = cv2.bitwise_not(nm.array(img))
    data = cv2.cvtColor(firstData, cv2.COLOR_BGR2GRAY)
    return data

def imageToText(image):
    return pytesseract.image_to_string(
            invertAndConvertGray(image),
            lang =None)


def digitImageToText(image):
    concatImg = cv2.hconcat([nm.array(image), nm.array(image), nm.array(image)])
    cv2.imshow('img', concatImg)
    cv2.waitKey(0)
    string = pytesseract.image_to_string(
            invertAndConvertGray(nm.asarray(concatImg)),
            lang =None)[2]
    if(string[1].isDigit()):
        return int(string[1])
    else:
        return 0            
xRatio = 1.2508143322475571
yRatio = 1.2514484356894555
            
def mouseToScreen(position):
    x,y = position
    return (int(x*xRatio), int(y*yRatio))

def screenToMouse(position):
    x,y = position
    return (int(x/xRatio), int(y/yRatio))
