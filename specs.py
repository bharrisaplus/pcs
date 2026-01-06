import unittest
from unittest.mock import patch
import json
from types import SimpleNamespace

import _utils as CardShuffleUtils
import _stats as CardShuffleStats
import card_shuffle as CardShuffle

class PCSCheck(unittest.TestCase):
    def setUp(self):
        self.card_order = list(range(52))
        self.args_json = '{"write": false, "gui": false, "four_color": false, "ndo": false, "cut": false, "arbitrary": false}'

    def test_get_card_name(self):
        expected_1 = ["ace of spade", "ace of diamond", "ace of club", "ace of heart"]
        solution_1 = CardShuffleUtils.get_card_title(0)
        solution_2 = CardShuffleUtils.get_card_title(13)
        solution_3 = CardShuffleUtils.get_card_title(38)
        solution_4 = CardShuffleUtils.get_card_title(51)
        expected_2 = ["king of spade", "king of diamond", "king of club", "king of heart"]
        solution_5 = CardShuffleUtils.get_card_title(12)
        solution_6 = CardShuffleUtils.get_card_title(25)
        solution_7 = CardShuffleUtils.get_card_title(26)
        solution_8 = CardShuffleUtils.get_card_title(39)

        self.assertEqual([solution_1, solution_2, solution_3, solution_4], expected_1,
            "The title of a card should be retrieved based on the ndo position of the card"
        )

        self.assertEqual([solution_5, solution_6, solution_7, solution_8], expected_2,
            "The title of a card should be retrieved based on the ndo position of the card"
        )

    def test_get_card_symbol(self):
        expected_1 = [ '🂡', '🃁', '🃑', '🂱' ]
        solution_1 = CardShuffleUtils.get_card_symbol(0)
        solution_2 = CardShuffleUtils.get_card_symbol(13)
        solution_3 = CardShuffleUtils.get_card_symbol(38)
        solution_4 = CardShuffleUtils.get_card_symbol(51)
        expected_2 = [ '🂮', '🃎', '🃞', '🂾' ]
        solution_5 = CardShuffleUtils.get_card_symbol(12)
        solution_6 = CardShuffleUtils.get_card_symbol(25)
        solution_7 = CardShuffleUtils.get_card_symbol(26)
        solution_8 = CardShuffleUtils.get_card_symbol(39)

        self.assertEqual([solution_1, solution_2, solution_3, solution_4], expected_1,
            "The symbol of a card should be retrieved based on the ndo position of the card"
        )

        self.assertEqual([solution_5, solution_6, solution_7, solution_8], expected_2,
            "The symbol of a card should be retrieved based on the ndo position of the card"
        )

    def test_get_card_color(self):
        expected_1 = [0,1,0,1]
        solution_1 = CardShuffleUtils.get_card_color(0)
        solution_2 = CardShuffleUtils.get_card_color(13)
        solution_3 = CardShuffleUtils.get_card_color(38)
        solution_4 = CardShuffleUtils.get_card_color(51)
        solution_5 = CardShuffleUtils.get_card_color(12)
        solution_6 = CardShuffleUtils.get_card_color(25)
        solution_7 = CardShuffleUtils.get_card_color(26)
        solution_8 = CardShuffleUtils.get_card_color(39)
        expected_2 = [0,1,2,3]
        solution_9 = CardShuffleUtils.get_card_color(0, four_color=True)
        solution_10 = CardShuffleUtils.get_card_color(13, four_color=True)
        solution_11 = CardShuffleUtils.get_card_color(38, four_color=True)
        solution_12 = CardShuffleUtils.get_card_color(51, four_color=True)
        solution_13 = CardShuffleUtils.get_card_color(12, four_color=True)
        solution_14 = CardShuffleUtils.get_card_color(25, four_color=True)
        solution_15 = CardShuffleUtils.get_card_color(26, four_color=True)
        solution_16 = CardShuffleUtils.get_card_color(39, four_color=True)

        self.assertEqual([solution_1, solution_2, solution_3, solution_4], expected_1,
            "The color of a card should be retrieved based on the ndo position of the card"
        )

        self.assertEqual([solution_5, solution_6, solution_7, solution_8], expected_1,
            "The color of a card should be retrieved based on the ndo position of the card"
        )

        self.assertEqual([solution_9, solution_10, solution_11, solution_12], expected_2,
            "The color of a card should be retrieved based on the ndo position of the card"
        )

    def test_shuffle(self):
        position_count = 52
        mixed_up = CardShuffle.shuffle_cards(self.card_order, list(range(position_count)))

        self.assertEqual(len(mixed_up), position_count,
            "The shuffled deck should retain the same number of cards as before the shuffle"
        )

        self.assertNotEqual(mixed_up, self.card_order,
            "The shuffled deck should not be the same as new deck order"
        )

    def test_cut(self):
        swear_mix = [25,9,1,41,7,46,39,43,5,11,2,4,13,22,6,34,35,28,21,14,19,50,10,3,15,0,42,40,44,33,12,26,48,31,37,20,8,30,23,32,49,17,27,45,36,51,47,18,29,38,16,24]
        swear_cut = [35,28,21,14,19,50,10,3,15,0,42,40,44,33,12,26,48,31,37,20,8,30,23,32,49,17,27,45,36,51,47,18,29,38,16,24,25,9,1,41,7,46,39,43,5,11,2,4,13,22,6,34]

        cut_up, cut_spot = CardShuffle.maybe_cut(swear_mix)

        self.assertEqual(len(cut_up), len(swear_mix),
            "The peapod cut deck should retain the same number of cards as before the cut"
        )

        self.assertEqual(cut_spot, swear_mix.index(swear_cut[0]),
            "The peapod cut deck should be cut at the first consecutive pair"
        )

        self.assertEqual(cut_up, swear_cut,
            "The peapod cut deck should be cut at the first consecutive pair"
        )

    def test_cut_arbitrary(self):
        swear_mix = [25,9,1,41,7,46,39,43,5,11,2,4,13,22,6,34,35,28,21,14,19,50,10,3,15,0,42,40,44,33,12,26,48,31,37,20,8,30,23,32,49,17,27,45,36,51,47,18,29,38,16,24]

        cut_up, cut_spot = CardShuffle.maybe_cut(swear_mix, is_arbitrary=True)

        self.assertEqual(len(cut_up), len(swear_mix),
            "The arbitrary cut deck should retain the same number of cards as before the cut"
        )

        self.assertEqual(cut_spot, swear_mix.index(cut_up[0]),
            "The arbitrary cut deck should be cut somwhere in the deck"
        )

    @patch('card_shuffle.display_example')
    @patch('card_shuffle._setup_52')
    @patch('card_shuffle.shuffle_cards')
    @patch('card_shuffle.maybe_cut')
    @patch('card_shuffle.display_decklist_in_console')
    @patch('card_shuffle.display_decklist_in_gui')
    def test_gogogo_simple(self, mock_gui, mock_console, mock_cut, mock_shuffle, mock_setup, mock_example):
        # something like the populated namespace from argparse.ArgumentParser.parse_args()
        mock_args = json.loads(self.args_json, object_hook=lambda dct: SimpleNamespace(**dct))

        mock_setup.return_value = (list(range(52)), list(range(52)))

        assert mock_example is CardShuffle.display_example
        assert mock_setup is CardShuffle._setup_52
        assert mock_shuffle is CardShuffle.shuffle_cards
        assert mock_cut is CardShuffle.maybe_cut
        assert mock_console is CardShuffle.display_decklist_in_console
        assert mock_gui is CardShuffle.display_decklist_in_gui

        CardShuffle._gogogo(mock_args)

        self.assertFalse(mock_example.called, "When no options are passed, ignore example")
        self.assertEqual(mock_setup.call_count, 1, "When no options are passed, get setup lists ")
        self.assertTrue(mock_shuffle.called, "When no options are passed, shuffle cards")
        self.assertFalse(mock_cut.called, "When no options are passed, ignore cut")
        self.assertTrue(mock_console.called, "When no options are passed, write list to stdout ")
        self.assertFalse(mock_gui.called, "When no options are passed, ignore gui ")

    @unittest.skip('not yet')
    def test_gogogo_write(self):
        self.assertEqual(0, 0)

    @unittest.skip('not yet')
    def test_gogogo_gui(self):
        self.assertEqual(0, 0)

    @unittest.skip('not yet')
    def test_gogogo_cut(self):
        self.assertEqual(0, 0)

    @unittest.skip('not yet')
    def test_gogogo_cut_arbitrary(self):
        self.assertEqual(0, 0)


class MetricCheck(unittest.TestCase):
    def test_jaro(self):
        ex_a = ['F','A','R','M','V','I','L','L','E']
        ex_b = ['F','A','R','E','M','V','I','E','L']
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
        ex_c = ['H','E','L','L','O']
        ex_d = ['H','E','Y','Y','A']
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
        ex_e = ['X','L','N','G','X','A','T','C','X','R']
        ex_f = ['F','Y','J','L','H','D','R','Q','D','M']
        solution = CardShuffleStats.get_jaro_edit_distance_from(ex_e, ex_f)

        self.assertEqual(abs(1.4/3), solution[0],
            "jaro edit distance between {} and {} should be ~0.4667".format(ex_e, ex_f)
        )

        self.assertEqual(len(solution[1][0]), 2,
            "matched characters in {} should be 2".format(ex_e)
        )

        self.assertEqual(len(solution[1][1]), 2,
            "matched characters in {} should be 2".format(ex_f)
        )

        self.assertEqual(solution[2], 0,
            "transpositions counted in {} and {} should be 0".format(ex_e, ex_f)
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
