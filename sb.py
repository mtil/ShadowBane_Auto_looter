from pywinauto.application import Application
from pywinauto.findwindows import find_window
from pywinauto.keyboard import SendKeys
import pywinauto
import time
import threading


def lootGold():
    hello = find_window(best_match='Shadowbane')
    app = Application().connect(handle=hello)
    win = app.window(title='Shadowbane')

    timeToKill = 20
    respawnTimer = 120


    win.set_focus()
    time.sleep(timeToKill)
    print('attempting to click body')
    pywinauto.mouse.click(button='left', coords=(930, 600))
    time.sleep(1)
    print('sending o command')
    win.type_keys('{o}')
    time.sleep(1)
    print('sending mouse click')
    pywinauto.mouse.click(button='left', coords=(850, 392))


while True:

    lootGold()
    time.sleep(1)



