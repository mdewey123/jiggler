import pyautogui, time, random, sys

pyautogui.FAILSAFE = True

def get_cordinates():
    display = pyautogui.size()
    width = [0]
    height = [1]
    
    return(width, height)
    
def wiggle_mouse():
    get_cordinates()
    x_dest = random.randint(10, int(width)-10)
    y_dest = random.randint(10, int(height)-10)
    pyautogui.moveTo(x_dest, y_dest, duration=6.9)

def shutdown()
