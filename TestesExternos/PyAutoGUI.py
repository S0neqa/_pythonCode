import time

import pyautogui
pyautogui.sleep(2)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("youtube.com")
pyautogui.press("enter")
