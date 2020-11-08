from pyautogui import sleep, failSafeCheck, alert
from bot.heal.checks import health_percentage, mana_percentage
from bot.heal.actions import light_heal, intense_heal, mana

alert("start healing")

while True:
    hp = health_percentage()
    if hp < 60:
        intense_heal()
    elif hp < 80:
        light_heal()

    mp = mana_percentage()
    if mp < 70:
        mana()
    sleep(0.5)
    failSafeCheck()
