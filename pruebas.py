import keyboard
from time import sleep
from pynput import keyboard as kb
from pynput.mouse import Button, Controller

i=1

while i>0:
    keyboard.press_and_release('a') 
    sleep(5)
    keyboard.press_and_release('d') 
    sleep(5)
    keyboard.press_and_release('e') 
    sleep(10)