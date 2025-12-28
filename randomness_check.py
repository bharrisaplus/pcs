import unittest

import _stats as staty

card_order = [('spade', 1),('spade', 2),('spade', 3),('spade', 4),('spade', 5),('spade', 6),('spade', 7),('spade', 8),('spade', 9),('spade', 10),('spade', 11),('spade', 12),('spade', 13),('diamond', 1),('diamond', 2),('diamond', 3),('diamond', 4),('diamond', 5),('diamond', 6),('diamond', 7),('diamond', 8),('diamond', 9),('diamond', 10),('diamond', 11),('diamond', 12),('diamond', 13),('club', 13),('club', 12),('club', 11),('club', 10),('club', 9),('club', 8),('club', 7),('club', 6),('club', 5),('club', 4),('club', 3),('club', 2),('club', 1),('heart', 13),('heart', 12),('heart', 11),('heart', 10),('heart', 9),('heart', 8),('heart', 7),('heart', 6),('heart', 5),('heart', 4),('heart', 3),('heart', 2),('heart', 1)]

class EdtDstnc(unittest.TestCase):
    def test_jaro(self):
        ex_a = 'FARMVILLE'
        ex_b = 'FAREMVIEL'
        solution = staty.get_jaro_edit_distance_from(ex_b, ex_a)

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
        solution = staty.get_jaro_edit_distance_from(ex_c, ex_d)

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
        solution = staty.get_jaro_edit_distance_from(ex_e, ex_f)

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

        solution = staty.count_peapods_from(ex_g, ex_h)

        self.assertEqual(solution[0], 1, "Should be one ripe peapod in {}".format(ex_g))
        self.assertEqual(solution[1], 15, "Should be fifteen green peapos in {}".format(ex_h))

    '''
    def test_kendall_agin(self):
        ex_i = [24,25,19,18,10,1,2,17,9,13]
        ex_j = [18,19,20,21,22,23,24,25,26]

    def again_again(self):
        ex_k = [0,2,13,9,7,11,1]
        ex_l = [1,2,3,4,5,6,7,8]
    '''
