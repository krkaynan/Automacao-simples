import pyautogui
import time

pyautogui.PAUSE = 0.3

time.sleep(3)

pyautogui.moveTo(x=424, y=1062, duration=1)

pyautogui.click(x=424, y=1062)

pyautogui.moveTo(x=344, y=52, duration=1)

pyautogui.write('youtube.com', interval=0.25)

time.sleep(1.5)

pyautogui.press('Enter')

time.sleep(2.5)

pyautogui.moveTo(x=886, y=94, duration=0.7)

pyautogui.click(x=886, y=94)

pyautogui.write('Aula automação python', interval=0.25)

time.sleep(0.5)

pyautogui.press('Enter')

time.sleep(0.5)

pyautogui.moveTo(x=733, y=842, duration=0.7)

time.sleep(0.5)

pyautogui.click(x=733, y=842)

time.sleep(0.3)

pyautogui.moveTo(x=1344, y=841, duration=0.7)

time.sleep(0.2)

pyautogui.click(x=1344, y=841)