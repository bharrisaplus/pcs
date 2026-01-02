import unittest
import statistics as PyStat
import math

import _stats as CardShuffleStats
import card_shuffle as CardShuffle

from specs import card_order

class RandomCheck(unittest.TestCase):
    '''How random is the pcs shuffle

    Starting with the jaro similarity as a sanity test and looking at Fisher-Yates (FY) shuffle and the
        Gilbert-Shannon-Reeds (GSR) riffle shuffle models for 10,000 shuffles:
            +---------+--------+--------+--------+---------+
            | Shuffle |  jaro  |  +/-   | lowest | highest |
            +---------+--------+--------+--------+---------+
            | FY      | 0.6676 | 0.0368 | 0.5316 |  0.7890 |
            | GSR     | 0.6662 | 0.0363 | 0.5252 |  0.8017 |
            +---------+--------+--------+--------+---------+

    Next looking at 'peapods' or pairs of cards that are consecutive or matching their positions in
        new deck order.
    '''

    def setUp(self):
        self.new_deck_order_positions = list(range(len(card_order)))

    def debug_report_jaro_long_stats(self, _mean, _std, _min, _max):
        print("\nThe mean for the data: {}".format(_mean))
        print("The standard deviation for the data: {}".format(_std))
        print("The Data ranged between {} and {}".format(_min, _max))
        print("\nThe mean compared to Fishe-Yates: {} +- {} vs {}".format(_mean, _std, 0.6676))
        print("The mean compared to Gilber-Shannon-Reeds: {} +- {} vs {}".format(_mean, _std, 0.6662))


    def debug_report_peapod_long_stats(self, _mean, _std, _min, _max):
        print("\nThe mean for the data: {}".format(_mean))
        print("The standard deviation for the data: {}".format(_std))
        print("The Data ranged between {} and {}".format(_min, _max))
        print("\nThe mean compared to accpated value: {} +- {} vs {}".format(_mean, _std, 2.0))

    @unittest.skip("one long test at a time")
    def test_card_shuffle_long(self):
        jaro_measurement = [0] * 10000

        for text_idx in range(len(jaro_measurement)):
            mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
            jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(mixed_up, card_order)

            jaro_measurement[text_idx] = jaro_similarity[0]

        sample_mean = PyStat.mean(jaro_measurement)
        sample_std = PyStat.stdev(jaro_measurement, sample_mean)

        acceptance_check_passed = (
            math.isclose(sample_mean - sample_std, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean + sample_std, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean - sample_std, 0.6662, rel_tol=0.05) or
            math.isclose(sample_mean, 0.6662, rel_tol=0.05) or
            math.isclose(sample_mean + sample_std, 0.6662, rel_tol=0.05)
        )

        self.debug_report_jaro_long_stats(sample_mean, sample_std, min(jaro_measurement), max(jaro_measurement))

        self.assertTrue(acceptance_check_passed,
            "The mean jaro similarity observed of the PCS should be close to that of the FY and GSR shuffles"
        )

    @unittest.skip("one long test at a time")
    def test_card_shuffle_cut_long(self):
        jaro_measurement = [0] * 10000

        for text_idx in range(len(jaro_measurement)):
            mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
            maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up)
            jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(maybe_cut_up, card_order)

            jaro_measurement[text_idx] = jaro_similarity[0]

        sample_mean = PyStat.mean(jaro_measurement)
        sample_std = PyStat.stdev(jaro_measurement, sample_mean)

        acceptance_check_passed = (
            math.isclose(sample_mean - sample_std, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean + sample_std, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean - sample_std, 0.6662, rel_tol=0.05) or
            math.isclose(sample_mean, 0.6662, rel_tol=0.05) or
            math.isclose(sample_mean + sample_std, 0.6662, rel_tol=0.05)
        )

        self.debug_report_jaro_long_stats(sample_mean, sample_std, min(jaro_measurement), max(jaro_measurement))

        self.assertTrue(acceptance_check_passed,
            "The mean jaro similarity observed of the PCS should be close to that of the FY and GSR shuffles"
        )

    @unittest.skip("one long test at a time")
    def test_card_shuffle_arbitrary_cut_long(self):
        jaro_measurement = [0] * 10000

        for text_idx in range(len(jaro_measurement)):
            mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
            maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up, is_arbitrary=True)
            jaro_similarity = CardShuffleStats.get_jaro_edit_distance_from(maybe_cut_up, card_order)

            jaro_measurement[text_idx] = jaro_similarity[0]

        sample_mean = PyStat.mean(jaro_measurement)
        sample_std = PyStat.stdev(jaro_measurement, sample_mean)

        acceptance_check_passed = (
            math.isclose(sample_mean - sample_std, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean + sample_std, 0.6676, rel_tol=0.05) or
            math.isclose(sample_mean - sample_std, 0.6662, rel_tol=0.05) or
            math.isclose(sample_mean, 0.6662, rel_tol=0.05) or
            math.isclose(sample_mean + sample_std, 0.6662, rel_tol=0.05)
        )

        self.debug_report_jaro_long_stats(sample_mean, sample_std, min(jaro_measurement), max(jaro_measurement))

        self.assertTrue(acceptance_check_passed,
            "The mean jaro similarity observed of the PCS should be close to that of the FY and GSR shuffles"
        )

    @unittest.skip("one long test at a time")
    def test_card_shuffle_for_peapod_long(self):
        peapod_measurement = [0] * 10000

        for text_idx in range(len(peapod_measurement)):
            mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
            peapod_count = CardShuffleStats.count_peapods_from(mixed_up, card_order)

            peapod_measurement[text_idx] = peapod_count[0]

        sample_mean = PyStat.mean(peapod_measurement)
        sample_std = PyStat.stdev(peapod_measurement, sample_mean)

        acceptance_check_passed = (
            math.isclose(sample_mean - sample_std, 2, rel_tol=0.5) or
            math.isclose(sample_mean, 2, rel_tol=0.5) or
            math.isclose(sample_mean + sample_std, 2, rel_tol=0.5)
        )

        self.debug_report_peapod_long_stats(
            sample_mean, sample_std, min(peapod_measurement), max(peapod_measurement)
        )

        self.assertTrue(acceptance_check_passed, "The number of consecutive pairs should be around 2")
    
    @unittest.skip("one long test at a time")
    def test_card_shuffle_cut_for_peapod_long(self):
        peapod_measurement = [0] * 10000

        for text_idx in range(len(peapod_measurement)):
            mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
            maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up)
            peapod_count = CardShuffleStats.count_peapods_from(maybe_cut_up, card_order)

            peapod_measurement[text_idx] = peapod_count[0]

        sample_mean = PyStat.mean(peapod_measurement)
        sample_std = PyStat.stdev(peapod_measurement, sample_mean)

        acceptance_check_passed = (
            math.isclose(sample_mean - sample_std, 2, rel_tol=0.5) or
            math.isclose(sample_mean, 2, rel_tol=0.5) or
            math.isclose(sample_mean + sample_std, 2, rel_tol=0.5)
        )

        self.debug_report_peapod_long_stats(
            sample_mean, sample_std, min(peapod_measurement), max(peapod_measurement)
        )

        self.assertTrue(acceptance_check_passed, "The number of consecutive pairs should be around 2")

    @unittest.skip("one long test at a time")
    def test_card_shuffle_arbitrary_cut_for_peapod_long(self):
        peapod_measurement = [0] * 10000

        for text_idx in range(len(peapod_measurement)):
            mixed_up = CardShuffle.shuffle_cards(card_order, self.new_deck_order_positions)
            maybe_cut_up, _ = CardShuffle.maybe_cut(mixed_up, is_arbitrary=True)
            peapod_count = CardShuffleStats.count_peapods_from(maybe_cut_up, card_order)

            peapod_measurement[text_idx] = peapod_count[0]

        sample_mean = PyStat.mean(peapod_measurement)
        sample_std = PyStat.stdev(peapod_measurement, sample_mean)

        acceptance_check_passed = (
            math.isclose(sample_mean - sample_std, 2, rel_tol=0.5) or
            math.isclose(sample_mean, 2, rel_tol=0.5) or
            math.isclose(sample_mean + sample_std, 2, rel_tol=0.5)
        )

        self.debug_report_peapod_long_stats(
            sample_mean, sample_std, min(peapod_measurement), max(peapod_measurement)
        )

        self.assertTrue(acceptance_check_passed, "The number of consecutive pairs should be around 2")
