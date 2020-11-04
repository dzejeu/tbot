from imagehash import average_hash
from pyautogui import screenshot, alert, leftClick, sleep, moveTo
from pyscreeze import locate
from cv2 import imread
from bot.cords.point import Point
import os

MINI_MAP_START = Point(1433, 5)
MINI_MAP_CENTER = Point(1485, 60)
MINI_MAP_REGION = (*MINI_MAP_START, 105, 108)
OFFSET = 15


# times = 0

# while True:
#     times += 1
#     alert("take ss")
#     screenshot(f'screens/screen_{times}.png', region=(MINI_MAP_CENTER.x - 15, MINI_MAP_CENTER.y - 15, 30, 30))

def to_global(mini_map_waypoint):
    # TODO: to sth with offset
    global_x = MINI_MAP_START.x + mini_map_waypoint.x + OFFSET
    global_y = MINI_MAP_START.y + mini_map_waypoint.y + OFFSET
    return Point(global_x, global_y)


def locate_on_minimap(waypoint, confidence=0.8):
    return locate(waypoint, screenshot(region=MINI_MAP_REGION), confidence=confidence)


def is_on_waypoint(waypoint):
    cords = locate_on_minimap(waypoint)
    global_cords = to_global(Point(cords.left, cords.top))
    return abs((MINI_MAP_CENTER.x - global_cords.x) + (MINI_MAP_CENTER.y - global_cords.y)) < 8


def wait_for_arrival(waypoint):
    while not is_on_waypoint(waypoint):
        sleep(2)


waypoints = sorted(os.listdir('screens'))

alert("go")

sleep(3)

for wpt in waypoints + [waypoints[0]]:

    waypt = os.path.join('screens', wpt)

    cords = locate_on_minimap(waypt, confidence=0.7)

    if not cords:
        print(f'cant find {wpt}')
        continue

    global_wpt = to_global(Point(cords.left, cords.top))

    leftClick(global_wpt.x, global_wpt.y)
    moveTo(500, 500)

    wait_for_arrival(waypt)

    print(global_wpt)
