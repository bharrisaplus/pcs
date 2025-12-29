import unittest

import _utils as CardShuffleUtils
import card_shuffle as CardShuffle

card_order = [('spade', 1),('spade', 2),('spade', 3),('spade', 4),('spade', 5),('spade', 6),('spade', 7),('spade', 8),('spade', 9),('spade', 10),('spade', 11),('spade', 12),('spade', 13),('diamond', 1),('diamond', 2),('diamond', 3),('diamond', 4),('diamond', 5),('diamond', 6),('diamond', 7),('diamond', 8),('diamond', 9),('diamond', 10),('diamond', 11),('diamond', 12),('diamond', 13),('club', 13),('club', 12),('club', 11),('club', 10),('club', 9),('club', 8),('club', 7),('club', 6),('club', 5),('club', 4),('club', 3),('club', 2),('club', 1),('heart', 13),('heart', 12),('heart', 11),('heart', 10),('heart', 9),('heart', 8),('heart', 7),('heart', 6),('heart', 5),('heart', 4),('heart', 3),('heart', 2),('heart', 1)]

class PCSCheck(unittest.TestCase):
    def test_setup_52(self):
        maybe_new_deck_order = CardShuffleUtils._setup_52()

        self.assertEqual(len(maybe_new_deck_order[0]), 52,
            "The starting deck should contain 52 cards"
        )

        self.assertEqual(maybe_new_deck_order[0], card_order,
            "The starting should be in new deck order"
        )

    def test_shuffle(self):
        mixed_up = CardShuffle.shuffle_cards(card_order, list(range(len(card_order))))

        self.assertEqual(len(mixed_up), len(card_order),
            "The shuffled deck should retain the same number of cards as before the shuffle"
        )

    def test_cut(self):
        swear_mix = [('diamond', 13), ('spade', 10), ('spade', 2), ('heart', 11), ('spade', 8), ('heart', 6), ('heart', 13), ('heart', 9), ('spade', 6), ('spade', 12), ('spade', 3), ('spade', 5), ('diamond', 1), ('diamond', 10), ('spade', 7), ('club', 5), ('club', 4), ('club', 11), ('diamond', 9), ('diamond', 2), ('diamond', 7), ('heart', 2), ('spade', 11), ('spade', 4), ('diamond', 3), ('spade', 1), ('heart', 10), ('heart', 12), ('heart', 8), ('club', 6), ('spade', 13), ('club', 13), ('heart', 4), ('club', 8), ('club', 2), ('diamond', 8), ('spade', 9), ('club', 9), ('diamond', 11), ('club', 7), ('heart', 3), ('diamond', 5), ('club', 12), ('heart', 7), ('club', 3), ('heart', 1), ('heart', 5), ('diamond', 6), ('club', 10), ('club', 1), ('diamond', 4), ('diamond', 12)]
        swear_cut = [('club', 4), ('club', 11), ('diamond', 9), ('diamond', 2), ('diamond', 7), ('heart', 2), ('spade', 11), ('spade', 4), ('diamond', 3), ('spade', 1), ('heart', 10), ('heart', 12), ('heart', 8), ('club', 6), ('spade', 13), ('club', 13), ('heart', 4), ('club', 8), ('club', 2), ('diamond', 8), ('spade', 9), ('club', 9), ('diamond', 11), ('club', 7), ('heart', 3), ('diamond', 5), ('club', 12), ('heart', 7), ('club', 3), ('heart', 1), ('heart', 5), ('diamond', 6), ('club', 10), ('club', 1), ('diamond', 4), ('diamond', 12), ('diamond', 13), ('spade', 10), ('spade', 2), ('heart', 11), ('spade', 8), ('heart', 6), ('heart', 13), ('heart', 9), ('spade', 6), ('spade', 12), ('spade', 3), ('spade', 5), ('diamond', 1), ('diamond', 10), ('spade', 7), ('club', 5)]

        cut_up = CardShuffle.maybe_cut(swear_mix)

        self.assertEqual(len(cut_up), len(swear_mix),
            "The peapod cut deck should retain the same number of cards as before the cut"
        )

    def test_cut_arbitrary(self):
        swear_mix = [('diamond', 13), ('spade', 10), ('spade', 2), ('heart', 11), ('spade', 8), ('heart', 6), ('heart', 13), ('heart', 9), ('spade', 6), ('spade', 12), ('spade', 3), ('spade', 5), ('diamond', 1), ('diamond', 10), ('spade', 7), ('club', 5), ('club', 4), ('club', 11), ('diamond', 9), ('diamond', 2), ('diamond', 7), ('heart', 2), ('spade', 11), ('spade', 4), ('diamond', 3), ('spade', 1), ('heart', 10), ('heart', 12), ('heart', 8), ('club', 6), ('spade', 13), ('club', 13), ('heart', 4), ('club', 8), ('club', 2), ('diamond', 8), ('spade', 9), ('club', 9), ('diamond', 11), ('club', 7), ('heart', 3), ('diamond', 5), ('club', 12), ('heart', 7), ('club', 3), ('heart', 1), ('heart', 5), ('diamond', 6), ('club', 10), ('club', 1), ('diamond', 4), ('diamond', 12)]

        cut_up = CardShuffle.maybe_cut(swear_mix, isArbitrary=True)

        self.assertEqual(len(cut_up), len(swear_mix),
            "The arbitrary cut deck should retain the same number of cards as before the cut"
        )
