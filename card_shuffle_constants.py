number_values = range(1,14)
suites = [ 'spade', 'diamond', 'club', 'heart' ]
card_names = [ 'ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king' ]
card_group_a = [suites[0], suites[2]]
card_group_b = [suites[1], suites[3]]

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
# 
# https://docs.python.org/3/library/functions.html#chr
# Use like: print(chr(int('1F0A1', 16)))
card_to_utf8 = {
    ('spade', 1): '1F0A1',
    ('spade', 2): '1F0A2',
    ('spade', 3): '1F0A3',
    ('spade', 4): '1F0A4',
    ('spade', 5): '1F0A5',
    ('spade', 6): '1F0A6',
    ('spade', 7): '1F0A7',
    ('spade', 8): '1F0A8',
    ('spade', 9): '1F0A9',
    ('spade', 10): '1F0AA',
    ('spade', 11): '1F0AB',
    ('spade', 12): '1F0AD',
    ('spade', 13): '1F0AE',
    ('diamond', 1): '1F0B1',
    ('diamond', 2): '1F0B2',
    ('diamond', 3): '1F0B3',
    ('diamond', 4): '1F0B4',
    ('diamond', 5): '1F0B5',
    ('diamond', 6): '1F0B6',
    ('diamond', 7): '1F0B7',
    ('diamond', 8): '1F0B8',
    ('diamond', 9): '1F0B9',
    ('diamond', 10): '1F0BA',
    ('diamond', 11): '1F0BB',
    ('diamond', 12): '1F0BD',
    ('diamond', 13): '1F0BE',
    ('red', 'joker'): '1F0BF',
    ('club', 1): '1F0C1',
    ('club', 2): '1F0C2',
    ('club', 3): '1F0C3',
    ('club', 4): '1F0C4',
    ('club', 5): '1F0C5',
    ('club', 6): '1F0C6',
    ('club', 7): '1F0C7',
    ('club', 8): '1F0C8',
    ('club', 9): '1F0C9',
    ('club', 10): '1F0CA',
    ('club', 11): '1F0CB',
    ('club', 12): '1F0CD',
    ('club', 13): '1F0CE',
    ('black', 'joker'): '1F0CF',
    ('heart', 1): '1F0D1',
    ('heart', 2): '1F0D2',
    ('heart', 3): '1F0D3',
    ('heart', 4): '1F0D4',
    ('heart', 5): '1F0D5',
    ('heart', 6): '1F0D6',
    ('heart', 7): '1F0D7',
    ('heart', 8): '1F0D8',
    ('heart', 9): '1F0D9',
    ('heart', 10): '1F0DA',
    ('heart', 11): '1F0DB',
    ('heart', 12): '1F0DD',
    ('heart', 13): '1F0DE',
    ('white', 'joker'): '1F0DF'
}

save_icon_utf8 = '1F4BE'
