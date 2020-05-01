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