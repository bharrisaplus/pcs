''' Shuffle a deck of cards and produce the decklist '''

import random
import os
import argparse
import supports_color

from _utils import (
    _setup_52,
    get_card_title,
    get_card_color
)

from card_shuffle_gui import display_cards as display_decklist_in_gui

# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
console_colors: list[str] = ['\033[36m', '\033[31m', '\033[32m', '\033[33m']
console_color_reset: str = '\033[0m'


def display_example() -> None:
    ''' Print cards in new deck order: (♠️:A-K, ♦️:A-K, ♣️:K-A, ♥️:K-A) '''

    example_deck, _ = _setup_52()

    display_decklist_in_gui(example_deck, four_color=True, capture_filename='ndo')


def shuffle_cards(card_pool: list[int], position_pool: list[int]) -> list[int]:
    '''Randomize the order of given cards and place at random in a new deck

    Having a bank of both cards and positions, for each position pick a random card and
        a random position from their respective banks to create a new order.
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


def maybe_cut(card_block: list[int], is_arbitrary: bool = False) -> tuple[list[int], int | None]:
    '''Rearrange the deck at a determined point

    From the determined point take every card before the point and move it to the back of the list.
        The determined point can be picked by:
            * arbitrary: index from one of 1-3 randomly selected cards from the deck
            * peapod: index of card found next to new deck order neighbor
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

            if abs(previous_info - info) == 1:

                cut_position = idx_info
                break

            previous_info = info

    if cut_position:
        cutting_block = card_block[cut_position:] + card_block[:cut_position]

    return cutting_block or card_block, cut_position


def display_decklist_in_console(card_roll: list[int], to_file: bool = False, four_color: bool = False) -> None:
    '''Create a plain-text version of the card order for viewing in the terminal.

    Taking the cards given create a formatted string with each card on it's own line that
        can, optionally, be written to a file.
    '''

    console_catalog = []
    file_catalog = []

    for console_catalog_idx, card_stuff in enumerate(card_roll, start=1):
        _line = "{}) {}".format(console_catalog_idx, get_card_title(card_stuff))

        if four_color and supports_color.supportsColor.stdout:
            console_catalog.append("{}{}) {}{}".format(
                console_colors[get_card_color(card_stuff, four_color=True)], console_catalog_idx,
                get_card_title(card_stuff), console_color_reset
            ))
        else:
            console_catalog.append(_line)

        file_catalog.append(_line)

    print(*console_catalog, sep="\n")

    if to_file:
        file_descriptor = os.open('shuffled.decklist.txt', os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

        with os.fdopen(file_descriptor, mode='w') as out_file:
            out_file.write("\n".join(file_catalog))

        print("\nDecklist written to 'shuffled.decklist.txt'.")


def _gogogo(cardShuffleArgs: argparse.Namespace) -> None:
    if cardShuffleArgs.ndo:
        display_example()
    else:
        new_deck_order, positions_to_fill = _setup_52()
        mixed_deck = shuffle_cards(new_deck_order, positions_to_fill)
        cut_deck = None

        if cardShuffleArgs.cut or cardShuffleArgs.arbitrary:
            cut_deck, cut_spot = maybe_cut(mixed_deck, is_arbitrary=cardShuffleArgs.arbitrary)

            if cut_spot:
                print("Cut deck @ {}".format(cut_spot))

        final_deck = cut_deck or mixed_deck

        display_decklist_in_console(final_deck, to_file=cardShuffleArgs.write, four_color=cardShuffleArgs.four_color)

        if cardShuffleArgs.gui:
            display_decklist_in_gui(final_deck, four_color=cardShuffleArgs.four_color)


if __name__ == "__main__":
    # Grab arguments

    cardShuffleParser = argparse.ArgumentParser(prog="card_shuffle.py",
        description="Producing a pseudo-randomized list of playing cards."
    )

    cardShuffleParser.add_argument("-w", "--write", action="store_true",
        help="Flag to set for writing output to a text file."
    )

    cardShuffleParser.add_argument("-g", "--gui", action="store_true",
        help="Flag to set for displaying output using tkinter."
    )

    cardShuffleParser.add_argument("-f", "--four-color", action="store_true",
        help="Flag to set for displaying each suite in a unique color."
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

    _gogogo(cardShuffleParser.parse_args())
