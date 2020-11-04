from python_imagesearch.imagesearch import imagesearcharea
from pyautogui import leftClick, moveTo
from bot.cords.point import Point


MONSTERS_BARS_AREA = (Point(530, 275), Point(715, 425))
BATTLE_AREA = (Point(1245, 15), Point(1275, 270))
FIRST_TARGET_ON_BATTLE = Point(1262, 27)
NEUTRAL_POS = Point(200, 200)


def is_monster_around():
    hp_bar_tpl = "templates/hp_bar.png"
    found_cords = Point(
        *imagesearcharea(
            hp_bar_tpl,
            MONSTERS_BARS_AREA[0].x,
            MONSTERS_BARS_AREA[0].y,
            MONSTERS_BARS_AREA[1].x,
            MONSTERS_BARS_AREA[1].y,
            precision=0.9,
        )
    )
    return found_cords != Point(-1, -1)


def is_currently_attacking():
    attack_mark = "templates/attack_battle.png"
    found_cords = Point(
        *imagesearcharea(
            attack_mark,
            BATTLE_AREA[0].x,
            BATTLE_AREA[0].y,
            BATTLE_AREA[1].x,
            BATTLE_AREA[1].y,
            precision=0.6,
        )
    )
    return found_cords != Point(-1, -1)