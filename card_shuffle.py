''' Shuffle a deck of cards and produce the decklist '''

import random
import os
import argparse
import tkinter

from _constants import (
    card_num_to_name as lookup_card,
    save_icon_utf8 as floppy_code,
    card_group_a,
    card_group_b,
    card_to_utf8
)

from _utils import (
    _capture_tkinter_partial as screen_grab,
    ndo_example as display_example,
    _setup_52
)


def shuffle_cards(card_pool, position_pool):
    '''Randomize the order of given cards and place at random in a new deck

    Having a bank of both cards and positions, pick a random card and a random position from their
        respective banks to create a new order.

    Args:
        card_pool (list[tuple(str, int)]): The cards to randomize. See _constants.py@_setup_52
        position_pool (list[int]): The potential numbered spots cards can be placed in

    Returns:
        list[tuple(str, int)]: cards placed in a pseudo-random order
    '''

    position_count = len(position_pool)
    random_cards = random.sample(population=card_pool, k=len(card_pool))
    random_positions = random.sample(population=position_pool, k=position_count)
    random_deck_order = [0] * position_count

    for _ in range(position_count):
        card_idx = random.randrange(len(random_cards))
        card_to_place = random_cards[card_idx]
        position_idx = random.randrange(len(random_positions))
        position_to_use = random_positions[position_idx]

        random_deck_order[position_to_use] = card_to_place

        random_cards.remove(card_to_place)
        random_positions.remove(position_to_use)

    return random_deck_order


def maybe_cut(card_block, is_arbitrary=False):
    '''Rearrange the deck at a determined point

    From the determined point take every card before the point and move it to the back of the list.
        The determined point can be picked by:
            * arbitrary: index from one of 1-3 randomly selected cards from the deck
            * peapod: index of card found next to new deck order neighbor

    Args:
        card_block (list[tuple(str, int)]): The cards to rearrange. See _constants.py@_setup_52
        is_arbitrary (bool): See above (default: False)
    '''

    previous_info = None
    cut_position = None
    cutting_block = None

    if is_arbitrary:
        possible_cut = random.sample(population=card_block, k=random.randrange(1, 4))
        cut_position = card_block.index(random.sample(possible_cut, k=1)[0])

    else:
        for idx_info, info in enumerate(card_block):
            if previous_info is None:
                previous_info = info
                continue

            if info[0] == previous_info[0] and (
                info[1] == previous_info[1] - 1 or
                info[1] == previous_info[1] + 1
            ):

                cut_position = idx_info
                break

            previous_info = info

    if cut_position:
        cutting_block = card_block[cut_position:] + card_block[:cut_position]

    return cutting_block or card_block, cut_position


def display_decklist_in_console(card_roll, to_file=False):
    '''Create a plain-text version of the card order for viewing in the terminal.

    Taking the cards given create a formatted string with each card on it's own line that
    can, optionally, be written to a file.

    Args:
        card_roll (list[tuple(str, int)]): The cards to be shown. See _constants.py@_setup_52
        to_file (bool): Whether or not to create a file. (default: False)
    '''

    card_catalog = []

    for card_catalog_idx, card_stuff in enumerate(card_roll, start=1):
        card_catalog.append("{}) {} of {}".format(
            card_catalog_idx,
            lookup_card.get(card_stuff[1]).capitalize(),
            card_stuff[0].capitalize()
        ))

    print(*card_catalog, sep="\n")

    if to_file:
        file_descriptor = os.open('shuffled.decklist.txt', os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

        with os.fdopen(file_descriptor, mode='w') as out_file:
            out_file.write("\n".join(card_catalog))

        print("\nDecklist written to 'shuffled.decklist.txt'.")


def display_decklist_in_gui(card_roll, four_color=False):
    '''Show the cards using utf-8 symbols

    Create a layout in tkinter with the following layout
        rootWindow
            cardFrame:
                [{Cards 1 - 13}]
                [{Cards 14 - 26}]
                [{Cards 27 - 39}]
                [{Cards 40 - 52}]
            controlFrame:
                [{saveButton}]

        When clicked, the saveButton will create an image file of the rootWindow and cardFrame only.

    Args:
        card_roll (list[tuple(str, int)]): The cards to be shown. See _constants.py@_setup_52
        four_color (bool): Whether to use one color pre suite when displaying cards (default: False)
    '''

    def get_card_color(card_suite):
        suite_color = None

        if card_suite in card_group_a:
            suite_color = 'midnight blue'

            if four_color and card_suite == card_group_a[1]:
                suite_color = 'dark olive green'

        if card_suite in card_group_b:
            suite_color = 'firebrick'

            if four_color and card_suite == card_group_b[1]:
                suite_color = 'DarkOrange2'

        return suite_color

    rootWindow = tkinter.Tk()
    window_height = int((rootWindow.winfo_screenheight() * 0.63) // 1)
    window_width = int((rootWindow.winfo_screenwidth() * 0.63) // 1)
    cardFontStyle = ('Consolas', int(window_height * 0.1325 // 1))
    controlFontStyle = ('Consolas', int(window_height * 0.033 // 1))

    rootWindow.title("pcs: pseudo card shuffle")
    rootWindow.geometry("{}x{}".format(window_width, window_height))
    rootWindow.grid_columnconfigure(0, weight=1)

    cardFrame = tkinter.Frame(rootWindow, bd=0, highlightthickness=0)

    cardFrame.grid()

    controlFrame = tkinter.Frame(rootWindow, bd=0, highlightthickness=0)

    controlFrame.grid()

    tkinter.Button(
        controlFrame, text=chr(int(floppy_code, 16)), font=controlFontStyle, fg="goldenrod3",
        command=screen_grab(rootWindow, controlFrame), relief="flat"
    ).pack()

    for frame_idx, card_info in enumerate(card_roll[:13]):
        tkinter.Label(
            cardFrame, text=chr(int(card_to_utf8.get(card_info), 16)), font=cardFontStyle,
            fg=get_card_color(card_info[0])
        ).grid(column=frame_idx, row=0)

    for frame_idx, card_info in enumerate(card_roll[13:26]):
        tkinter.Label(
            cardFrame, text=chr(int(card_to_utf8.get(card_info), 16)), font=cardFontStyle,
            fg=get_card_color(card_info[0])
        ).grid(column=frame_idx, row=1)

    for frame_idx, card_info in enumerate(card_roll[26:39]):
        tkinter.Label(
            cardFrame, text=chr(int(card_to_utf8.get(card_info), 16)), font=cardFontStyle,
            fg=get_card_color(card_info[0])
        ).grid(column=frame_idx, row=2)

    for frame_idx, card_info in enumerate(card_roll[39:]):
        tkinter.Label(
            cardFrame, text=chr(int(card_to_utf8.get(card_info), 16)), font=cardFontStyle,
            fg=get_card_color(card_info[0])
        ).grid(column=frame_idx, row=3)

    rootWindow.mainloop()


if __name__ == "__main__":
    # Grab arguments

    cardShuffleParser = argparse.ArgumentParser(prog="card_shuffle.py",
        description="Producing a pseudo-randomized list of playing cards."
    )

    cardShuffleParser.add_argument("-w", "--write", action="store_true",
        help="Flag to set for writing output to a text file"
    )

    cardShuffleParser.add_argument("-g", "--gui", action="store_true",
        help="Flag to set for displaying output using tkinter"
    )

    cardShuffleParser.add_argument("-f", "--four-color", action="store_true",
        help="Flag to set for displaying each suite in a unique color in the tkinter gui window"
    )

    cardShuffleParser.add_argument("-n", "--ndo", action="store_true",
        help="Flag to set for displaying demo using tkinter. Other options are ignored when set."
    )

    cardShuffleParser.add_argument("-c", "--cut", action="store_true",
        help="Flag to set for cutting the deck after the shuffle at a consecutive pair if found."
    )

    cardShuffleParser.add_argument("-a", "--arbitrary", action="store_true",
        help="Flag to set for cutting the deck after the shuffle at a random spot."
    )

    cardShuffleArgs = cardShuffleParser.parse_args()

    if cardShuffleArgs.ndo:
        display_example()
    else:
        new_deck_order, positions_to_fill = _setup_52()
        mixed_deck = shuffle_cards(new_deck_order, positions_to_fill)
        cut_deck = None

        if cardShuffleArgs.cut:
            cut_deck, cut_spot = maybe_cut(mixed_deck, is_arbitrary=cardShuffleArgs.arbitrary)

            if cut_spot:
                print("Cut deck @ {}".format(cut_spot))

        final_deck = cut_deck or mixed_deck

        display_decklist_in_console(final_deck, to_file=cardShuffleArgs.write)

        if cardShuffleArgs.gui:
            display_decklist_in_gui(final_deck, four_color=cardShuffleArgs.four_color)
