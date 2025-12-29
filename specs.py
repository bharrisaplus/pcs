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
