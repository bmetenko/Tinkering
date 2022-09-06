import pyautogui
import cv2

found = pyautogui.locateOnScreen("1.png", grayscale=True, confidence=.5)

print(found)

x, y = pyautogui.locateCenterOnScreen("1.png", grayscale=True, confidence=.70)
pyautogui.click(x, y)