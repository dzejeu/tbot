from bot.attack.checks import is_currently_attacking
from bot.attack.actions import attack_monster
from pyautogui import sleep, alert, failSafeCheck


alert("start attacking")

while True:
    failSafeCheck()
    sleep(0.5)
    if is_currently_attacking():
        sleep(0.5)
        continue
    else:
        attack_monster()
        sleep(0.1)
        if is_currently_attacking():
            continue
