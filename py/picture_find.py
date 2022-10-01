import pyautogui
import cv2

found = pyautogui.locateOnScreen("1.png", grayscale=True, confidence=.5)

print(found)

x, y = pyautogui.locateCenterOnScreen("1.png", grayscale=True, confidence=.70)
print(x, y)
pyautogui.click(x, y)


# Tracking mouse position
import sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        
except KeyboardInterrupt:
    print('\n')