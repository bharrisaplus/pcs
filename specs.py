import unittest

import _utils as CardShuffleUtils
import _stats as CardShuffleStats
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

        self.assertNotEqual(mixed_up, card_order,
            "The shuffled deck should not be the same as new deck order"
        )

    def test_cut(self):
        swear_mix = [('diamond', 13), ('spade', 10), ('spade', 2), ('heart', 11), ('spade', 8), ('heart', 6), ('heart', 13), ('heart', 9), ('spade', 6), ('spade', 12), ('spade', 3), ('spade', 5), ('diamond', 1), ('diamond', 10), ('spade', 7), ('club', 5), ('club', 4), ('club', 11), ('diamond', 9), ('diamond', 2), ('diamond', 7), ('heart', 2), ('spade', 11), ('spade', 4), ('diamond', 3), ('spade', 1), ('heart', 10), ('heart', 12), ('heart', 8), ('club', 6), ('spade', 13), ('club', 13), ('heart', 4), ('club', 8), ('club', 2), ('diamond', 8), ('spade', 9), ('club', 9), ('diamond', 11), ('club', 7), ('heart', 3), ('diamond', 5), ('club', 12), ('heart', 7), ('club', 3), ('heart', 1), ('heart', 5), ('diamond', 6), ('club', 10), ('club', 1), ('diamond', 4), ('diamond', 12)]
        swear_cut = [('club', 4), ('club', 11), ('diamond', 9), ('diamond', 2), ('diamond', 7), ('heart', 2), ('spade', 11), ('spade', 4), ('diamond', 3), ('spade', 1), ('heart', 10), ('heart', 12), ('heart', 8), ('club', 6), ('spade', 13), ('club', 13), ('heart', 4), ('club', 8), ('club', 2), ('diamond', 8), ('spade', 9), ('club', 9), ('diamond', 11), ('club', 7), ('heart', 3), ('diamond', 5), ('club', 12), ('heart', 7), ('club', 3), ('heart', 1), ('heart', 5), ('diamond', 6), ('club', 10), ('club', 1), ('diamond', 4), ('diamond', 12), ('diamond', 13), ('spade', 10), ('spade', 2), ('heart', 11), ('spade', 8), ('heart', 6), ('heart', 13), ('heart', 9), ('spade', 6), ('spade', 12), ('spade', 3), ('spade', 5), ('diamond', 1), ('diamond', 10), ('spade', 7), ('club', 5)]

        cut_up, cut_spot = CardShuffle.maybe_cut(swear_mix)

        self.assertEqual(len(cut_up), len(swear_mix),
            "The peapod cut deck should retain the same number of cards as before the cut"
        )

        self.assertEqual(cut_spot, swear_mix.index(swear_cut[0]),
            "The peapod cut deck should be cut at the first consecutive pair"
        )

    def test_cut_arbitrary(self):
        swear_mix = [('diamond', 13), ('spade', 10), ('spade', 2), ('heart', 11), ('spade', 8), ('heart', 6), ('heart', 13), ('heart', 9), ('spade', 6), ('spade', 12), ('spade', 3), ('spade', 5), ('diamond', 1), ('diamond', 10), ('spade', 7), ('club', 5), ('club', 4), ('club', 11), ('diamond', 9), ('diamond', 2), ('diamond', 7), ('heart', 2), ('spade', 11), ('spade', 4), ('diamond', 3), ('spade', 1), ('heart', 10), ('heart', 12), ('heart', 8), ('club', 6), ('spade', 13), ('club', 13), ('heart', 4), ('club', 8), ('club', 2), ('diamond', 8), ('spade', 9), ('club', 9), ('diamond', 11), ('club', 7), ('heart', 3), ('diamond', 5), ('club', 12), ('heart', 7), ('club', 3), ('heart', 1), ('heart', 5), ('diamond', 6), ('club', 10), ('club', 1), ('diamond', 4), ('diamond', 12)]

        cut_up, cut_spot = CardShuffle.maybe_cut(swear_mix, isArbitrary=True)

        self.assertEqual(len(cut_up), len(swear_mix),
            "The arbitrary cut deck should retain the same number of cards as before the cut"
        )

        self.assertEqual(cut_spot, swear_mix.index(cut_up[0]),
            "The peapod cut deck should be cut at the first consecutive pair"
        )

class MetricCheck(unittest.TestCase):
    def test_jaro(self):
        ex_a = 'FARMVILLE'
        ex_b = 'FAREMVIEL'
        solution = CardShuffleStats.get_jaro_edit_distance_from(ex_b, ex_a)

        self.assertEqual(0.8842592592592592, solution[0],
            "jaro similarity between {} and {} should be 0.8842592592592592".format(ex_a, ex_b)
        )

        self.assertEqual(len(solution[1][0]), 8,
            "matched characters in {} and {} should be 8".format(ex_a, ex_b)
        )

        self.assertEqual(len(solution[1][1]), 8,
            "matched characters in {} and {} should be 8".format(ex_a, ex_b)
        )

        self.assertEqual(solution[2], 2/2,
            "transpositions counted in {} and {} should be 1".format(ex_a, ex_b)
        )

    def test_jaro_again(self):
        ex_c = 'HELLO'
        ex_d = 'HEYYA'
        solution = CardShuffleStats.get_jaro_edit_distance_from(ex_c, ex_d)

        self.assertEqual(1.8/3, solution[0],
            "jaro similarity between {} and {} should be 0.6".format(ex_c, ex_d)
        )

        self.assertEqual(len(solution[1][0]), 2,
            "matched characters in {} and {} should be 2".format(ex_c, ex_d)
        )

        self.assertEqual(len(solution[1][1]), 2,
            "matched characters in {} and {} should be 2".format(ex_c, ex_d)
        )

        self.assertEqual(solution[2], 0,
            "transpositions counted in {} and {} should be 0".format(ex_c, ex_d)
        )

    def test_jaro_again_again(self):
        ex_e = 'XLNGXATCXR'
        ex_f = 'FYJLHDRQDM'
        solution = CardShuffleStats.get_jaro_edit_distance_from(ex_e, ex_f)

        self.assertEqual(abs(1.4/3), solution[0],
            "jaro edit distance between {} and {} should be ~0.4667".format(ex_e, ex_f)
        )

        self.assertEqual(len(solution[1][0]), 2,
            "matched characters in {} and {} should be ".format(ex_e, ex_f)
        )

        self.assertEqual(len(solution[1][1]), 2,
            "matched characters in {} and {} should be ".format(ex_e, ex_f)
        )

        self.assertEqual(solution[2], 0,
            "transpositions counted in {} and {} should be ".format(ex_e, ex_f)
        )

    def test_peapod(self):
        ex_g = [16,18,13,15,11,12,14,10,17]
        ex_h = [10,11,12,13,14,15,16,17,18]

        solution = CardShuffleStats.count_peapods_from(ex_g, ex_h)

        self.assertEqual(solution[0], 1, "Should be 1 ripe peapod in {}".format(ex_g))
        self.assertEqual(solution[1], 15, "Should be 15 green peapods in {}".format(ex_h))

    def test_peapod_agin(self):
        ex_i = [24,25,19,18,23,21,22,26,20]
        ex_j = [18,19,20,21,22,23,24,25,26]

        solution = CardShuffleStats.count_peapods_from(ex_i, ex_j)

        self.assertEqual(solution[0], 3, "Should be 3 ripe peapods in {}".format(ex_i))
        self.assertEqual(solution[1], 13, "Should be 13 green peapods in {}".format(ex_j))

    def test_peapod_again_again(self):
        ex_k = [6,2,4,1,7,5,8,3]
        ex_l = [1,2,3,4,5,6,7,8]

        solution = CardShuffleStats.count_peapods_from(ex_k, ex_l)

        self.assertEqual(solution[0], 0, "Should be 0 ripe peapods in {}".format(ex_k))
        self.assertEqual(solution[1], 14, "Should be 13 green peapods in {}".format(ex_l))