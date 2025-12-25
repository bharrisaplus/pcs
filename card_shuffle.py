import importlib
import random
import os
import argparse

pcs_constants = importlib.import_module("card_shuffle_constants")
pcs_utils = importlib.import_module("card_shuffle_gui-demo")

def shuffle_cards(card_pool, position_pool):
    '''Randomize the order of given cards

    Having a bank of both cards and positions, pick a random card and a random position from their
        respective banks to create a somewhat random order.

    Args:
        card_pool (list[tuple(str, int)]): The cards to randomize. See card_shuffle_constants.py@_setup_52
        position_pool (list[int]): The potential numbered spots cards can be placed in

    Returns:
        list[tuple(str, int)]: cards placed in a pseudo-random order
    '''

    random_cards = random.sample(population = card_pool, k = len(card_pool))
    random_positions = random.sample(population = position_pool, k = len(position_pool))
    random_deck_order = [0] * 52

    for slot in range(len(card_pool)):
        card_idx = random.randrange(len(random_cards))
        card_to_place = random_cards[card_idx]
        position_idx = random.randrange(len(random_positions))
        position_to_use = random_positions[position_idx]

        random_deck_order.insert(position_to_use, card_to_place)

        random_cards.remove(card_to_place)
        random_positions.remove(position_to_use)

    return [maybe_card for maybe_card in random_deck_order if maybe_card != 0]

def display_decklist_in_console(card_roll, toFile=False):
    '''Create a plain-text version of the card order for viewing in the terminal.

    Taking the cards given create a formatted string with each card on it's own line that
    can, optionally, be written to a file.

    Args:
        card_roll (list[tuple(str, int)]): The cards to be shown. See card_shuffle_constants.py@_setup_52
        toFile (bool): Whether or not to create a file. (default: `False`)
    '''

    card_catalog = []

    for card_catalog_idx, card_stuff in enumerate(card_roll, start=1):
        card_name = pcs_constants.card_num_to_name.get(card_stuff[1])

        card_catalog.append("{}) {} of {}".format(card_catalog_idx, card_name, card_stuff[0]))

    print(*card_catalog, sep="\n")

    if toFile:
        file_descriptor = os.open('shuffled.decklist.txt', os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

        with os.fdopen(file_descriptor, mode='w') as out_file:
            out_file.write("\n".join(card_catalog))

        print("\nDecklist written to 'shuffled.decklist.txt'.")

def display_decklist_in_gui(card_roll, toFile=False):
    return

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

    cardShuffleParser.add_argument("-i", "--image", action="store_true",
        help="Flag to set for writing tkinter window to an image file"
    )

    cardShuffleParser.add_argument("-d", "--demo", action="store_true",
        help="Flag to set for displaying demo using tkinter. Other options are ignored when set."
    )

    cardShuffleArgs = cardShuffleParser.parse_args()

    # Get a blank deck and mix it up

    new_deck_order, positions_to_fill = pcs_utils._setup_52()
    mixed_deck_order = shuffle_cards(new_deck_order, positions_to_fill)

    # Show the cards

    if cardShuffleArgs.demo:
        pcs_utils.tkinter_demo()
    else:
        display_decklist_in_console(mixed_deck_order, toFile=cardShuffleArgs.write)

        if cardShuffleArgs.gui:
            display_decklist_in_gui(mixed_deck_order, toFile=cardShuffleArgs.image)
