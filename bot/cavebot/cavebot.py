from bot.cavebot.minimap import is_on_waypoint, to_global_centralized, locate_on_minimap, Point
from pyautogui import sleep, alert, leftClick, moveTo, failSafeCheck
# from bot.attack.actions import attack_monster
# from bot.attack.checks import is_currently_attacking
import os
import pyautogui as pgi

NEUTRAL_MOUSE_POS = Point(500, 500)

pgi.FAILSAFE = True


def wait_for_arrival(waypoint):
    times = 0
    while not is_on_waypoint(waypoint):
        failSafeCheck()
        times += 1
        if times > 2:
            return False
        sleep(2)
    return True


def move_to_point(point):
    leftClick(*point)
    moveTo(*NEUTRAL_MOUSE_POS)


SUBFOLDER = "mt-ghule"

if not SUBFOLDER:
    raise AttributeError("Set subfolder (cave) for which bot should be running")


waypoints = [
    os.path.join("screens", SUBFOLDER, w)
    for w in sorted(os.listdir(f"screens/{SUBFOLDER}/"), key=lambda x: int(x.split("_")[1].replace(".png", "")))
]

print(waypoints)

alert("start cave bot")

# tell other processes to start running
with open("../sync.txt", "w") as fd:
    fd.write("running")

next_pos = 0

sleep(3)

while True:
    print(f"Next wpt: {waypoints[next_pos]}")
    failSafeCheck()
    wpt = waypoints[next_pos]
    next_pos = (next_pos + 1) % len(waypoints)

    cords = None

    for attempt in range(5):
        cords = locate_on_minimap(wpt, confidence=0.85)
        if cords:
            break
        else:
            sleep(1)

    if not cords:
        print(f'Could not find {wpt}')
        continue

    global_wpt = to_global_centralized(Point(cords.left, cords.top))
    move_to_point(global_wpt)
    if not wait_for_arrival(wpt):
        next_pos = (next_pos - 1) % len(waypoints)
