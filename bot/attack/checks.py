from pyautogui import screenshot, alert
from bot.cords.point import Point


BATTLE_AREA_START = Point(1252, 15)
BATTLE_AREA_END = Point(1253, 160)
BATTLE_AREA_REGION = (
    *BATTLE_AREA_START,
    BATTLE_AREA_END.x - BATTLE_AREA_START.x,
    BATTLE_AREA_END.y - BATTLE_AREA_START.y
)


def _is_red(color, threshold=30):
    return abs(255 - color[0]) < threshold and color[1] < threshold and color[2] < threshold


def is_currently_attacking():
    battle_ss = screenshot(region=BATTLE_AREA_REGION)
    colors = battle_ss.getcolors()
    top_5_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:min(len(colors), 5)]
    for col in top_5_colors:
        if _is_red(col[1]):
            return True
    return False
