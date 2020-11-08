from pyautogui import screenshot
from pyscreeze import locate
from bot.cords.point import Point

MINI_MAP_START = Point(1433, 5)
MINI_MAP_CENTER = Point(1485, 60)
MINI_MAP_REGION = (*MINI_MAP_START, 105, 108)
OFFSET = 15


def to_global_centralized(mini_map_waypoint):
    """
    Offset is added to global cords in order to perform a click on a center of 30x30 waypoint
    :param mini_map_waypoint:
    :return:
    """
    global_x = MINI_MAP_START.x + mini_map_waypoint.x + OFFSET
    global_y = MINI_MAP_START.y + mini_map_waypoint.y + OFFSET
    return Point(global_x, global_y)


def locate_on_minimap(waypoint, confidence=0.85):
    return locate(waypoint, screenshot(region=MINI_MAP_REGION), confidence=confidence)


def is_on_waypoint(waypoint):
    cords = locate_on_minimap(waypoint)
    if not cords:
        return False
    global_cords = to_global_centralized(Point(cords.left, cords.top))
    return abs((MINI_MAP_CENTER.x - global_cords.x) + (MINI_MAP_CENTER.y - global_cords.y)) < 4
