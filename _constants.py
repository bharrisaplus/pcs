''' Data for describing the card shuffle '''

number_values = range(1, 14)
suites = [ 'spade', 'diamond', 'club', 'heart' ]
card_names = [ 'ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king' ]
card_group_a = [suites[0], suites[2]]
card_group_b = [suites[1], suites[3]]

card_utf8_codes = [ '1F0A1', '1F0A2', '1F0A3', '1F0A4', '1F0A5', '1F0A6', '1F0A7', '1F0A8', '1F0A9', '1F0AA', '1F0AB', '1F0AD', '1F0AE', '1F0C1', '1F0C2', '1F0C3', '1F0C4', '1F0C5', '1F0C6', '1F0C7', '1F0C8', '1F0C9', '1F0CA', '1F0CB', '1F0CD', '1F0CE', '1F0DE', '1F0DD', '1F0DB', '1F0DA', '1F0D9', '1F0D8', '1F0D7', '1F0D6', '1F0D5', '1F0D4', '1F0D3', '1F0D2', '1F0D1', '1F0BE', '1F0BD', '1F0BB', '1F0BA', '1F0B9', '1F0B8', '1F0B7', '1F0B6', '1F0B5', '1F0B4', '1F0B3', '1F0B2', '1F0B1' ]

card_num_to_name = {}
card_num_to_name[number_values[0]] = card_names[0]
card_num_to_name[number_values[1]] = card_names[1]
card_num_to_name[number_values[2]] = card_names[2]
card_num_to_name[number_values[3]] = card_names[3]
card_num_to_name[number_values[4]] = card_names[4]
card_num_to_name[number_values[5]] = card_names[5]
card_num_to_name[number_values[6]] = card_names[6]
card_num_to_name[number_values[7]] = card_names[7]
card_num_to_name[number_values[8]] = card_names[8]
card_num_to_name[number_values[9]] = card_names[9]
card_num_to_name[number_values[10]] = card_names[10]
card_num_to_name[number_values[11]] = card_names[11]
card_num_to_name[number_values[12]] = card_names[12]

# https://unicode.org/charts/nameslist/n_1F0A0.html
# https://docs.python.org/3/library/functions.html#chr
#
# Use like: print(chr(int('1F0A1', 16)))
#

card_to_utf8 = {
    ('spade', 1): card_utf8_codes[0],
    ('spade', 2): card_utf8_codes[1],
    ('spade', 3): card_utf8_codes[2],
    ('spade', 4): card_utf8_codes[3],
    ('spade', 5): card_utf8_codes[4],
    ('spade', 6): card_utf8_codes[5],
    ('spade', 7): card_utf8_codes[6],
    ('spade', 8): card_utf8_codes[7],
    ('spade', 9): card_utf8_codes[8],
    ('spade', 10): card_utf8_codes[9],
    ('spade', 11): card_utf8_codes[10],
    ('spade', 12): card_utf8_codes[11],
    ('spade', 13): card_utf8_codes[12],
    ('diamond', 1): card_utf8_codes[13],
    ('diamond', 2): card_utf8_codes[14],
    ('diamond', 3): card_utf8_codes[15],
    ('diamond', 4): card_utf8_codes[16],
    ('diamond', 5): card_utf8_codes[17],
    ('diamond', 6): card_utf8_codes[18],
    ('diamond', 7): card_utf8_codes[19],
    ('diamond', 8): card_utf8_codes[20],
    ('diamond', 9): card_utf8_codes[21],
    ('diamond', 10): card_utf8_codes[22],
    ('diamond', 11): card_utf8_codes[23],
    ('diamond', 12): card_utf8_codes[24],
    ('diamond', 13): card_utf8_codes[25],
    ('club', 13): card_utf8_codes[26],
    ('club', 12): card_utf8_codes[27],
    ('club', 11): card_utf8_codes[28],
    ('club', 10): card_utf8_codes[29],
    ('club', 9): card_utf8_codes[30],
    ('club', 8): card_utf8_codes[31],
    ('club', 7): card_utf8_codes[32],
    ('club', 6): card_utf8_codes[33],
    ('club', 5): card_utf8_codes[34],
    ('club', 4): card_utf8_codes[35],
    ('club', 3): card_utf8_codes[36],
    ('club', 2): card_utf8_codes[37],
    ('club', 1): card_utf8_codes[38],
    ('heart', 13): card_utf8_codes[39],
    ('heart', 12): card_utf8_codes[40],
    ('heart', 11): card_utf8_codes[41],
    ('heart', 10): card_utf8_codes[42],
    ('heart', 9): card_utf8_codes[43],
    ('heart', 8): card_utf8_codes[44],
    ('heart', 7): card_utf8_codes[45],
    ('heart', 6): card_utf8_codes[46],
    ('heart', 5): card_utf8_codes[47],
    ('heart', 4): card_utf8_codes[48],
    ('heart', 3): card_utf8_codes[49],
    ('heart', 2): card_utf8_codes[50],
    ('heart', 1): card_utf8_codes[51],
}

save_icon_utf8 = '1F4BE'
