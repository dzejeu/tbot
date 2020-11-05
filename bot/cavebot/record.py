from pyautogui import screenshot, alert
from bot.cords.point import Point

MINI_MAP_CENTER = Point(1485, 60)
OFFSET = 15
SUBFOLDER = ...

"""
Please create a mark on the waypoint - it is not mandatory, but will help locating waypoint on screen, so it will simply
improve bot's efficiency.
"""

waypoints_recorded = 0


if not SUBFOLDER:
    raise AttributeError('set subfolder for this cave')

print("Kill me when it's done!")

while True:
    waypoints_recorded += 1
    alert("RECORD WAYPOINT")
    screenshot(
        f'screens/{SUBFOLDER}/screen_{waypoints_recorded}.png',
        region=(MINI_MAP_CENTER.x - OFFSET, MINI_MAP_CENTER.y - OFFSET, 30, 30)
    )
