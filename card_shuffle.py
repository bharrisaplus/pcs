''' Shuffle a deck of cards and produce the decklist '''

import random
import os
import argparse

from _constants import card_num_to_name as lookup_card
from _utils import _setup_52
from card_shuffle_gui import display_cards as display_decklist_in_gui


def display_example():
    ''' Print cards in new deck order: (♠️:A-K, ♦️:A-K, ♣️:K-A, ♥️:K-A) '''

    example_deck, _ = _setup_52()

    display_decklist_in_gui(example_deck, four_color=True)


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
