import random
import os
import argparse

import card_shuffle_constants

def _setup_52():
    number_values = range(1,14)
    suites = [ 'spade', 'diamond', 'club', 'heart' ]
    card_bank = []

    for suite in suites:
        if suite in ['spade', 'diamond']:
            for idx in number_values:
                card_bank.append((suite, idx))
        else:
            for idx in reversed(number_values):
                card_bank.append((suite, idx))

    return card_bank, list(range(len(card_bank)))

def shuffle_cards(card_pool, position_pool):
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

def get_cards_for_display(card_deck):
    card_catalog = []

    for card_catalog_idx, card_stuff in enumerate(card_deck, start=1):
        card_name = card_shuffle_constants.card_num_to_name.get(card_stuff[1])

        card_catalog.append("{}) {} of {}".format(card_catalog_idx, card_name, card_stuff[0]))

    return card_catalog

def output_decklist(card_roll, toFile=False):
    print(*card_roll, sep="\n")

    if toFile:
        file_descriptor = os.open('shuffled.decklist.txt', os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

        with os.fdopen(file_descriptor, mode='w') as out_file:
            out_file.write("\n".join(card_roll))

        print("\nDecklist written to 'shuffled.decklist.txt'.")

if __name__ == "__main__":
    cardShuffleParser = argparse.ArgumentParser(prog="card_shuffle.py",
        description="Producing a pseudo-randomized list of playing cards."
    )

    cardShuffleParser.add_argument("-w", "--write", action="store_true",
        help="Flag to set for writing output to a file"
    )

    cardShuffleArgs = cardShuffleParser.parse_args()
    new_deck_order, positions_to_fill = _setup_52()
    mixed_deck_order = shuffle_cards(new_deck_order, positions_to_fill)
    card_display_list = get_cards_for_display(mixed_deck_order)

    output_decklist(card_display_list, toFile=cardShuffleArgs.write)
