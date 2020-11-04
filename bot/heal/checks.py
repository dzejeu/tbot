from bot.cords.point import Point
from pyautogui import screenshot

HEALTH_BAR_AREA = (Point(1450, 286), Point(1535, 288))
MANA_BAR_AREA = (Point(1450, 298), Point(1535, 300))

(hp_start, hp_end) = HEALTH_BAR_AREA
hp_screen_region = (*hp_start, hp_end.x - hp_start.x, hp_end.y - hp_start.y)

(mp_start, mp_end) = MANA_BAR_AREA
mp_screen_region = (*mp_start, mp_end.x - mp_start.x, mp_end.y - mp_start.y)


def _is_color(rgb_pos, color, threshold=30):
    return all(abs(100 - color[i]) < threshold if i != rgb_pos else abs(240 - color[i]) < threshold for i in range(3))


def _pixels_to_percentage_fn(other_pixels_contribution):
    x = other_pixels_contribution
    return 311 * x**2 - 321 * x + 99.8


def bar_percentage(screen_region, rgb_color_pos):
    img = screenshot(region=screen_region)
    colors = img.getcolors()
    top_five = sorted(colors, key=lambda x: x[0], reverse=True)[:min(len(colors), 5)]
    main = 0.1
    other = 0.1
    for col in top_five:
        if _is_color(rgb_color_pos, col[1]):
            main += col[0]
        else:
            other += col[0]
    contribution = other / (other + main)
    return _pixels_to_percentage_fn(contribution)


def health_percentage():
    return bar_percentage(hp_screen_region, 0)


def mana_percentage():
    return bar_percentage(mp_screen_region, 2)

