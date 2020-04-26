import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import shopModule
import re
import time
import cropModule
import convertModule
import gold
import roundModule

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

k = 0
selectedClass  = ''
selectedOrigin = ''
while(k>4):
    input()   
    decisions = shopModule.checkSinergies(selectedClass, selectedOrigin)
    selectedClass = decisions[0]
    selectedOrigin = decisions[1]
