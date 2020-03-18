import emoji
import random


def draw_lake(width=5, length=20):
    """
    Draw a rectangular lake.
    Parameters:
        width (int): The width of the lake.
        length (int): The length of the lake.
    """

    if width < 0 or length < 0:
        raise ValueError("width and length must be greater than 0")
    elif width <= 2 or length <= 2:
        return

    fishCoordinateY = int(random.random() * (width - 2) + 1)
    fishCoordinateX = int(random.random() * (length - 2) + 1)

    for i in range(width):
        draw_vertical(False)

        if i == 0 or i == width - 1:
            for j in range(length):
                draw_horizontal()

        elif i == fishCoordinateY:
            for j in range(length):
                if j == fishCoordinateX:
                    draw_fish()
                else:
                    draw_wave()
        else:
            for j in range(length):
                draw_wave()

        draw_vertical(True)
    return


def draw_horizontal():
    """Draw a horizontal fence."""
    print("=", end = '')


def draw_vertical(newline=False):
    """
    Draw a vertical fence.
    Parameter:
        newline (boolean): add a new line after drawing vertical component.
    """
    if not newline:
        print("||", end = '')
    else:
        print("||")


def draw_wave():
    """Draw waves representing water."""
    print("~", end = '')


def draw_fish():
    print(emoji.emojize(':fish:', use_aliases = True), end = '')
