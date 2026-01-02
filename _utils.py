''' Helpful methods for card shuffling '''

from PIL import ImageGrab

from _constants import (
    suites as card_suites,
    number_values as card_nums
)


def _setup_52():
    '''Arrange playing cards in new deck order (♠️:A-K, ♦️:A-K, ♣️:K-A, ♥️:K-A).

    Returns:
        (tuple[ tuple(str, int)], list[int] ]): The arranged cards and the positions to fill in:
            * tuple(str, int): model representing the cards
                * str: The suite of the card. See card_shuffle_constants.py:suites
                * int: The number value of the card. See card_shuffle_constants.py:number_values
            * list[int]: The numbered spots where cards can go
    '''

    card_bank = []

    for suite in card_suites:
        if suite in card_suites[:2]:
            for idx in card_nums:
                card_bank.append((suite, idx))
        else:
            for idx in reversed(card_nums):
                card_bank.append((suite, idx))

    return card_bank, list(range(len(card_bank)))


def _capture_tkinter(capture_window, offset_area, capture_prefix='shuffled'):
    '''Save an image of the display cards

    Grab the current screen using pillow and crop the area outside of the gui using the tkinter
        window + widget geometry

    Args:
        capture_window (tkinter.Tk): The current tkinter instance to pull geometry from
        offset_area (tkinter.Frame): The widget to ignore when grabbing screenshot
        capture_prefix (str): What to name the saved file (default: 'shuffled')
    '''

    capture_window.update_idletasks()

    capture_area_start_x = capture_window.winfo_rootx()
    capture_area_start_y = capture_window.winfo_rooty()
    offset_y = offset_area.winfo_height() + 20
    capture_area_end_x = capture_area_start_x + capture_window.winfo_width()
    capture_area_end_y = capture_area_start_y + capture_window.winfo_height() - offset_y
    capture_filename = "{}.decklist.png".format(capture_prefix)

    # https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
    #
    # bbox determines what region of screen to save
    #
    capture_image = ImageGrab.grab(
        bbox=(capture_area_start_x, capture_area_start_y, capture_area_end_x, capture_area_end_y)
    )

    capture_image.save(capture_filename)

    print("Decklist saved to '{}'".format(capture_filename))
