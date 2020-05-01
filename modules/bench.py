from pynput.mouse import Controller as mouseController, Button
from pynput.keyboard import Controller as keyboardController, Key
import time

mouse = mouseController()
keyboard = keyboardController()

#benchPositions = [(340,630), (430, 630), (520,630)]

benchCells = []

for i in range(9):
    benchCells.append((340+94*i, 630))

def sellAll():
    for cell in benchCells:
        mouse.position = cell
        keyboard.press('e')
        time.sleep(0.2)
time.sleep(2)