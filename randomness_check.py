import unittest

import _stats as CardShuffleStats
import card_shuffle as CardShuffle

from specs import card_order

class RandomCheck(unittest.TestCase):
    '''How random is the pcs shuffle
    
    Looking at the jaro similarity for Fisher-Yates (FY) shuffle and the
        Gilbert-Shannon-Reeds (GSR) riffle shuffle model. For 10,000 shuffles:
            +---------+--------+--------+--------+---------+
            | Shuffle |  jaro  |  +/-   | lowest | highest |
            +---------+--------+--------+--------+---------+
            | FY      | 0.6676 | 0.0368 | 0.5316 |  0.7890 |
            | GSR     | 0.6662 | 0.0363 | 0.5252 |  0.8017 |
            +---------+--------+--------+--------+---------+
    '''
    def test_card_shuffle(self):
        card_order_len = len(card_order)
        mixed_up = CardShuffle.shuffle_cards(card_order, list(range(card_order_len)))

        jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(mixed_up, card_order)

        self.assertTrue(0.55 < jaro_similarity[0] < 0.75,
            "The end positions of cards after a shuffle should be somewhat far from start positions"
        )

    def test_card_shuffle_peapod_cut(self):
        card_order_len = len(card_order)
        mixed_up = CardShuffle.shuffle_cards(card_order, list(range(card_order_len)))
        maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up)

        jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(maybe_cut_up, card_order)

        self.assertTrue(0.55 < jaro_similarity[0] < 0.75,
            "The end positions of cards after a shuffle and cut should be somewhat far from start positions"
        )

    def test_card_shuffle_arbitrary_cut(self):
        card_order_len = len(card_order)
        mixed_up = CardShuffle.shuffle_cards(card_order, list(range(card_order_len)))
        maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up, isArbitrary=True)

        jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(maybe_cut_up, card_order)

        self.assertTrue(0.55 < jaro_similarity[0] < 0.75,
            "The end positions of cards after a shuffle and cut should be somewhat far from start positions"
        )

    #def test_card_shuffle_long(self):
