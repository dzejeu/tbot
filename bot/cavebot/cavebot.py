from bot.cavebot.minimap import is_on_waypoint, to_global_centralized, locate_on_minimap, Point
from pyautogui import sleep, alert, leftClick, moveTo, failSafeCheck
import os

NEUTRAL_MOUSE_POS = Point(500, 500)


def wait_for_arrival(waypoint):
    times = 0
    while not is_on_waypoint(waypoint):
        times += 1
        if times > 1:
            return False
        sleep(2)
    return True


def move_to_point(point):
    leftClick(*point)
    moveTo(*NEUTRAL_MOUSE_POS)


SUBFOLDER = ...

if not SUBFOLDER:
    raise AttributeError("Set subfolder (cave) for which bot should be running")


waypoints = [os.path.join("screens", SUBFOLDER, w) for w in sorted(os.listdir(f"screens/{SUBFOLDER}/"))]


alert("start bot")

next_pos = 0

sleep(3)

while True:
    failSafeCheck()
    wpt = waypoints[next_pos]
    next_pos = (next_pos + 1) % len(waypoints)
    cords = locate_on_minimap(wpt, confidence=0.7)

    if not cords:
        print(f'Could not find {wpt}')
        continue

    global_wpt = to_global_centralized(Point(cords.left, cords.top))
    move_to_point(global_wpt)
    while not wait_for_arrival(wpt):
        next_pos = (next_pos - 1) % len(waypoints)
