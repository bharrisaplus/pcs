import unittest

import _stats as CardShuffleStats
import card_shuffle as CardShuffle

from specs import card_order

class RandomCheck(unittest.TestCase):
    def test_card_shuffle(self):
        mixed_up = CardShuffle.shuffle_cards(card_order, list(range(len(card_order))))

        self.assertEqual(len(mixed_up), len(card_order),
            "The shuffled deck should retain the same number of cards as before the shuffle"
        )

    #def test_card_shuffle_long(self):
