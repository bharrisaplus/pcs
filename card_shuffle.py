import random
import os
import argparse
import tkinter

from _constants import (
    card_num_to_name as lookup_card,
    save_icon_utf8 as floppy_code,
    card_group_a as blue_group,
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

    random_cards = random.sample(population = card_pool, k = len(card_pool))
    random_positions = random.sample(population = position_pool, k = len(position_pool))
    random_deck_order = [0] * len(position_pool)

    for slot in range(len(position_pool)):
        card_idx = random.randrange(len(random_cards))
        card_to_place = random_cards[card_idx]
        position_idx = random.randrange(len(random_positions))
        position_to_use = random_positions[position_idx]

        random_deck_order[position_to_use] = card_to_place

        random_cards.remove(card_to_place)
        random_positions.remove(position_to_use)

    return random_deck_order

def maybe_cut(card_block, isArbitrary=False):
    '''Rearrange the deck at a determined point
    
    From the determined point take every card before the point and move it to the back of the list.
        The determined point can be picked by:
            * arbitrary: index of a card randly selected from 1-3 randomly selected cards from the deck
            * peapod: index of card found next to new dedk order neighbor

    Args:
        card_block (list[tuple(str, int)]): The cards to possibly rearrange. See _constants.py@_setup_52
        isArbitrary (bool): See above (default: `False`)
    '''

    previous_info = None
    cut_position = None
    cutting_block = None

    if isArbitrary:
        possible_cut = random.sample(population = card_block, k = random.randrange(1,4))
        cut_position = card_block.index(random.sample(possible_cut, k = 1)[0])

    else:
        for idx_info, info in enumerate(card_block):
            if previous_info == None:
                previous_info = info
                continue

            if info[0] == previous_info[0] and info[1] in [ previous_info[1] - 1, previous_info[1] + 1]:
                cut_position = idx_info
                break

            previous_info = info

    if cut_position:
        cutting_block = card_block[cut_position:] + card_block[:cut_position]

    return cutting_block or card_block, cut_position

def display_decklist_in_console(card_roll, toFile=False):
    '''Create a plain-text version of the card order for viewing in the terminal.

    Taking the cards given create a formatted string with each card on it's own line that
    can, optionally, be written to a file.

    Args:
        card_roll (list[tuple(str, int)]): The cards to be shown. See _constants.py@_setup_52
        toFile (bool): Whether or not to create a file. (default: `False`)
    '''

    card_catalog = []

    for card_catalog_idx, card_stuff in enumerate(card_roll, start=1):
        card_name = lookup_card.get(card_stuff[1]).capitalize()

        card_catalog.append("{}) {} of {}".format(card_catalog_idx, card_name, card_stuff[0].capitalize()))

    print(*card_catalog, sep="\n")

    if toFile:
        file_descriptor = os.open('shuffled.decklist.txt', os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

        with os.fdopen(file_descriptor, mode='w') as out_file:
            out_file.write("\n".join(card_catalog))

        print("\nDecklist written to 'shuffled.decklist.txt'.")

def display_decklist_in_gui(card_roll):
    '''Show the cards using utf-8 symbols

    Create a layout in tkinter with the following layout
        rootWindow
            cardFrame:
                [{Cards 1 - 14}]
                [{Cards 15 - 28}]
                [{Cards 29 - 42}]
                [{Cards 43 - 52}]
            controlFrame:
                [{saveButton}]

        When clicked, the saveButton will create an image file of the rootWindow and cardFrame only.

    Args:
        card_roll (list[tuple(str, int)]): The cards to be shown. See _constants.py@_setup_52
    '''

    rootWindow = tkinter.Tk()

    rootWindow.title("pcs: pseudo card shuffle")
    rootWindow.geometry("1036x583")

    cardFrame = tkinter.Frame(rootWindow, bd=0, padx=22, highlightthickness=0)

    cardFrame.grid()

    controlFrame = tkinter.Frame(rootWindow, borderwidth=0)

    controlFrame.grid()

    tkinter.Button(
        controlFrame, text=chr(int(floppy_code, 16)), font=("Consolas", 18), fg="goldenrod3",
        command=screen_grab(rootWindow, controlFrame), relief="flat"
    ).pack()

    # 52 / 14 ~ 4 rows

    for frame_idx, card_info in enumerate(card_roll[:14]):
        card_symbol = chr(int(card_to_utf8.get(card_info), 16))
        card_color = 'midnight blue' if card_info[0] in blue_group else 'firebrick'
        tkinter.Label(cardFrame, text=card_symbol, font=("Consolas", 81), fg=card_color).grid(column=frame_idx, row=0)

    for frame_idx, card_info in enumerate(card_roll[14:28]):
        card_symbol = chr(int(card_to_utf8.get(card_info), 16))
        card_color = 'midnight blue' if card_info[0] in blue_group else 'firebrick'
        tkinter.Label(cardFrame, text=card_symbol, font=("Consolas", 81), fg=card_color).grid(column=frame_idx, row=1)

    for frame_idx, card_info in enumerate(card_roll[28:42]):
        card_symbol = chr(int(card_to_utf8.get(card_info), 16))
        card_color = 'midnight blue' if card_info[0] in blue_group else 'firebrick'
        tkinter.Label(cardFrame, text=card_symbol, font=("Consolas", 81), fg=card_color).grid(column=frame_idx, row=2)

    for frame_idx, card_info in enumerate(card_roll[42:]):
        card_symbol = chr(int(card_to_utf8.get(card_info), 16))
        card_color = 'midnight blue' if card_info[0] in blue_group else 'firebrick'
        tkinter.Label(cardFrame, text=card_symbol, font=("Consolas", 81), fg=card_color).grid(column=frame_idx, row=3)

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

    # Get a blank deck, mix it up and possibly cut

    new_deck_order, positions_to_fill = _setup_52()
    mixed_deck_order = shuffle_cards(new_deck_order, positions_to_fill)
    maybe_cut_order = None

    if cardShuffleArgs.cut:
        maybe_cut_order, maybe_cut_spot = maybe_cut(mixed_deck_order, isArbitrary=cardShuffleArgs.arbitrary)

        if maybe_cut_spot:
            print("Cut deck @ {}".format(maybe_cut_spot))

    final_deck_order = maybe_cut_order or mixed_deck_order

    # Show the cards

    if cardShuffleArgs.ndo:
        display_example()
    else:
        display_decklist_in_console(final_deck_order, toFile=cardShuffleArgs.write)

        if cardShuffleArgs.gui:
            display_decklist_in_gui(final_deck_order)
