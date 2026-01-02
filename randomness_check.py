import unittest

import _stats as CardShuffleStats
import card_shuffle as CardShuffle

from specs import card_order

class RandomCheck(unittest.TestCase):
    def setUp(self):
        self.new_deck_order_positions = list(range(len(card_order)))

    def test_card_shuffle(self):
        mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)

        jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(mixed_up, card_order)

        self.assertTrue(0.50 < jaro_similarity[0] < 0.80,
            "The end positions of cards after a shuffle should be somewhat far from start positions"
        )

    def test_card_shuffle_cut(self):
        mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
        maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up)

        jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(maybe_cut_up, card_order)

        self.assertTrue(0.50 < jaro_similarity[0] < 0.80,
            "The end positions of cards after a shuffle and cut should be somewhat far from start positions"
        )

    def test_card_shuffle_arbitrary_cut(self):
        mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
        maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up, is_arbitrary=True)

        jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(maybe_cut_up, card_order)

        self.assertTrue(0.50 < jaro_similarity[0] < 0.80,
            "The end positions of cards after a shuffle and cut should be somewhat far from start positions"
        )

    def test_card_shuffle_for_peapod(self):
        mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)

        peapod_count = CardShuffleStats.count_peapods_from(mixed_up, card_order)

        self.assertTrue( peapod_count[0] <= 4,
            "There should be around 4 consecutive pairs for any shuffled deck"
        )

        self.assertTrue( peapod_count[0] < peapod_count[1],
            "There should be less consecutive than non-consecutive pairs for any shuffled deck"
        )

    def test_card_shuffle_cut_for_peapod(self):
        mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
        maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up)

        peapod_count = CardShuffleStats.count_peapods_from(maybe_cut_up, card_order)

        self.assertTrue( peapod_count[0] <= 3,
            "There should be around 3 consecutive pairs for any shuffled deck"
        )

        self.assertTrue( peapod_count[0] < peapod_count[1],
            "There should be less consecutive than non-consecutive pairs for any shuffled deck"
        )

    def test_card_shuffle_arbitrary_cut_for_peapod(self):
        mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
        maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up, is_arbitrary=True)

        peapod_count = CardShuffleStats.count_peapods_from(maybe_cut_up, card_order)

        self.assertTrue( peapod_count[0] <= 4,
            "There should be around 3 consecutive pairs for any shuffled deck"
        )

        self.assertTrue( peapod_count[0] < peapod_count[1],
            "There should be less consecutive than non-consecutive pairs for any shuffled deck"
        )
