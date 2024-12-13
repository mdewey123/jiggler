import pyautogui, time, random, sys

pyautogui.FAILSAFE = True

def get_cordinates():
    display = pyautogui.size()
    width = [0]
    height = [1]
    
    return(display, width, height)
    
def wiggle_mouse():
    pyautogui.moveTo(x, y, duration=num_seconds)

def shutdown()
