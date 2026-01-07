''' Helpful methods for card shuffling '''

from PIL import ImageGrab

from _constants import (
    card_suites,
    card_names,
    card_utf8_codes
)


def _setup_52():
    '''Get a deck of cards and positions to fill for the new deck

    This facilitates the default of taking 52 cards then shuffling them into a new arrangement
    
    Previously, the deck of cards was modeled as list of tuples to represent suite and card value
        but now is a list of integers which represent the cards original position in new deck order:

        before = [('spade', 1), ('diamond', 1), ('club', 1), ('heart', 1)]

        now = [0,13,38,51]
    '''

    return list(range(52)), list(range(52))

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
    ''' The glyph/pictograph/icon of the card

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


def _capture_tkinter(capture_bounds, capture_prefix):
    '''Save an image of the display cards

    Grab the current screen using pillow and crop the area outside of the gui

    Args:
        capture_bounds (tuple[int,int,int,int]): The bounding box of the crop to make
        capture_prefix (str): What to name the saved file
    '''

    capture_filename = "{}.decklist.png".format(capture_prefix)

    # https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
    #
    capture_image = ImageGrab.grab(
        bbox=(capture_bounds[0], capture_bounds[1], capture_bounds[2], capture_bounds[3])
    )

    capture_image.save(capture_filename)

    print("Decklist saved to '{}'".format(capture_filename))
