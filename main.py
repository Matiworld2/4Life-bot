from pyautogui import locateAllOnScreen, press, click
from time import sleep

cc = 0.9

while True:
    sleep(0.5)
    if var == 4:
        click(button='left')
        var=1

    if locateAllOnScreen("samo_q.png", confidence=cc)!=None:
        press('q')
        var=var+1

    elif locateAllOnScreen("samo_e.png", confidence=cc)!=None:
        press('e')
        var=var+1
    else:
        print("I can't find your picture")