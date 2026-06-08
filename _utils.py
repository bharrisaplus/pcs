''' Helpful methods for card shuffling '''

from os import urandom as os_urandom
from copy import copy as ccopy
from math import (
    ceil as mceil,
    floor as mfloor
)

from PIL import ImageGrab

from _constants import (
    boundingBoxType as boundingBox,
    card_suites,
    card_names,
    card_utf8_codes
)


def _setup_52() -> tuple[list[int], list[int]]:
    '''Get a deck of cards and positions to fill for the new deck

    This facilitates the default of taking 52 cards then shuffling them into a new arrangement

    Previously, the deck of cards was modeled as list of tuples to represent suite and card value
        but now is a list of integers which represent the cards original position in new deck order:

        before = [('spade', 1), ('diamond', 1), ('club', 1), ('heart', 1)]

        now = [0,13,38,51]
    '''

    return list(range(52)), list(range(52))


def get_card_title(card_index: int) -> str:
    '''The full name of a card

    The card suite and number in english: "jack of club"
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


def get_card_symbol(card_index: int) -> chr:
    ''' The glyph/pictograph/icon of the card '''

    return chr(int(card_utf8_codes[card_index], 16))


def get_card_color(card_index: int, four_color: bool = False) -> int:
    '''Determine what color for each card suite

    With the options for card colors as a list like below, pick which option the card suit
        should use so that different color names can be used for different targets:

        ['red', 'blue', 'green', 'purple]
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


def _capture_tkinter(capture_bounds: boundingBox, capture_prefix: str) -> None:
    '''Save an image of the display cards

    Grab the current screen using pillow and crop the area outside of the gui
    '''

    capture_filename = "{}.decklist.png".format(capture_prefix)

    # https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
    #
    capture_image = ImageGrab.grab(
        bbox=(capture_bounds[0], capture_bounds[1], capture_bounds[2], capture_bounds[3])
    )

    capture_image.save(capture_filename)

    print("Decklist saved to '{}'".format(capture_filename))


def jitter_bugs(max_cap: int = 52, upper_bound: int = 13) -> list[int]:
    ''' get random numbers to use for pre-shuffle '''

    result = []
    bucket_one = list(os_urandom(mceil(upper_bound / 4)))
    bucket_two = list(os_urandom(mceil(upper_bound / 4)))
    bucket_three = list(os_urandom(mceil(upper_bound / 4)))
    bucket_four = list(os_urandom(mceil(upper_bound / 4)))

    def jitter_filter(_seed: int) -> bool:
        return (_seed <= max_cap or (mfloor(_seed / 10) <= max_cap))

    def jitter_map(_seed: int) -> int:
        return (
            _seed
            if _seed < max_cap
            else mfloor(_seed / max_cap)
        )

    result = bucket_one + bucket_two + bucket_three + bucket_four

    result = list(filter(jitter_filter, result))
    result = list(map(jitter_map, result))

    return list(dict.fromkeys(result))


def ndpf(signal_list: list[int], seed_list: list[int]) -> list[int]:
    ''' separate noise '''

    result = []
    lucky_nums = []

    if len(signal_list) == 0:
        return result

    result = list(signal_list)
    lucky_nums = list(dict.fromkeys(seed_list))

    for _idx in range(0, len(lucky_nums), 2):
        pivot = ccopy(lucky_nums[_idx])
        nxt_pivot = ccopy(lucky_nums[_idx + 1]) if _idx < (len(lucky_nums) - 1) else None
        hold = None

        try:
            hold = ccopy(result[pivot])
        except IndexError:
            print(result)
            print(seed_list)
            print(pivot)

        if _idx < (len(lucky_nums) - 1):
            try:
                result[pivot] = ccopy(result[nxt_pivot])
            except IndexError:
                print(result)
                print(nxt_pivot)

            result[nxt_pivot] = hold
        else:
            result[pivot] = ccopy(result[0])
            result.pop(0)
            result.insert(0, hold)

    return result
