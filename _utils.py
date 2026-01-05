''' Helpful methods for card shuffling '''

from PIL import ImageGrab

from _constants import (
    suites as card_suites,
    number_values as card_nums,
    card_names,
    card_utf8_codes
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


def get_card_title(card_index):
    '''The full name of a card

    The card suite and number in english

    Args:
        card_index (int): The position of the card in ndo

    Returns:
        str: Like "jack of club"
    '''

    if card_index < 13:
        name_idx = card_index
    else:
        name_idx = card_index % 13

    suite_idx = card_index // 13

    if card_index < 26:
        name_lookup = card_names
    else:
        name_lookup = list(reversed(card_names))

    return "{} of {}".format(name_lookup[name_idx], card_suites[suite_idx])


def get_card_symbol(card_index):
    ''' The pictograph of the card

    Cards are represented in the UTF-8 block 'Playing Cards'.
    https://unicode.org/charts/nameslist/n_1F0A0.html

    Args:
        card_index (int): The position of the card in ndo

    Returns:
        chr: The character for the glyph
    '''

    return chr(int(card_utf8_codes[card_index], 16))


def get_card_color(card_index, four_color=False):
    '''color for suite

    With the options for card colors as a list like below, pick which option the card suit should use,
        this allows for different color names to be used for different targets:

        ['red', 'blue', 'green', 'purple]

    Args:
        card_index (int): The position of the card in ndo
        four_color (bool): Whether to use one color per suite (default: False)

    Returns:
        int: The index of the color to use
    '''

    color_option = None

    in_spade_range = card_index <= 12
    in_diamond_range = 13 <= card_index <= 25
    in_club_range = 26 <= card_index <= 38
    in_heart_range = 39 <= card_index <= 51

    if in_spade_range or in_club_range:
        color_option = 0

        if four_color and in_club_range:
            color_option = 2

    if in_diamond_range or in_heart_range:
        color_option = 1

        if four_color and in_heart_range:
            color_option = 3

    return color_option


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
    offset_y = offset_area.winfo_height()
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
