import pyautogui, threading, random, sys, keyboard

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 3


def get_coordinates():
    display = pyautogui.size()
    width = display[0]
    height = display[1]
    return width, height
    
def wiggle_mouse():
    width, height = get_coordinates()
    
    for i in range(random.randint(1, 6)):
        x_dest = random.randint(10, width-10)
        y_dest = random.randint(10, height-10)
        pyautogui.moveTo(x_dest, y_dest, duration=6.9)
    
    shutdown()
    
    
def shutdown():
    def timeout():
        nonlocal result
        result = 'Continue'
    
    result = None
    timer = threading.Timer(30, timeout)
    timer.start()
    
    try:
        result = pyautogui.confirm(
            text='Do you want to cancel the wiggler?', 
            title='Finished?', 
            buttons=['Finish', 'Continue']
        )
    
    finally:  
        timer.cancel()
        
    if result == "Finish":
        print("Wiggler is going to take a break now")
        sys.exit()
    elif result == 'Continue':
        print("Wiggler is doing his best!")
        wiggle_mouse()
    
def listen_4p():
    while True:
        if keyboard.is_pressed('shift+p'):
            print('Wiggler is going to take a break now.')
            sys.exit()

listener_thread = threading.Thread(target=listen_4p, daemon=True)
listener_thread.start()
    
wiggle_mouse()
