from bot.attack.checks import is_currently_attacking
from bot.attack.actions import attack_monster
from pyautogui import sleep, failSafeCheck
import os

while True:
    if not os.path.exists("../sync.txt"):
        continue
    with open("../sync.txt", 'r') as fd:
        status = fd.read()
        if status == "running":
            break
        else:
            sleep(2)

while True:
    failSafeCheck()
    sleep(0.2)
    if is_currently_attacking():
        sleep(0.2)
        continue
    else:
        attack_monster()
        sleep(0.1)
        if is_currently_attacking():
            continue
