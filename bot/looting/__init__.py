from bot.cords.point import Point
from bot.cords.utils import adjacent_tiles
from pyautogui import rightClick, moveTo


def loot_all_around(char_pos: Point):
    tiles = adjacent_tiles(char_pos, 50)
    for tile in tiles:
        moveTo(char_pos.x, char_pos.y)
        rightClick(tile.x, tile.y)
