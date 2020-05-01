from PIL import ImageGrab, Image
import cv2
import numpy as nm
from pynput.mouse import Controller

def getImages(imageType):
    if(imageType == 'shopClasses'):
        return [
        ImageGrab.grab(bbox =(507, 1015, 640, 1035)),
        ImageGrab.grab(bbox =(707, 1015, 840, 1035)),
        ImageGrab.grab(bbox =(907, 1015, 1040, 1035)),
        ImageGrab.grab(bbox =(1107, 1015, 1240, 1035)),
        ImageGrab.grab(bbox =(1307, 1015, 1440, 1035))
        ]
    elif(imageType == 'shopOrigins'):
        return [
        ImageGrab.grab(bbox =(507, 985, 640, 1010)),
        ImageGrab.grab(bbox =(707, 985, 840, 1010)),
        ImageGrab.grab(bbox =(907, 985, 1040, 1010)),
        ImageGrab.grab(bbox =(1107, 985, 1240, 1010)),
        ImageGrab.grab(bbox =(1307, 985, 1440, 1010))
        ]


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



