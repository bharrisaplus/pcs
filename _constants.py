''' Data for describing the card shuffle '''

card_suites: list[str] = [ 'spade', 'diamond', 'club', 'heart' ]
card_names: list[str] = [ 'ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king' ]

#
# Cards are represented in the UTF-8 block 'Playing Cards'.
#   https://unicode.org/charts/nameslist/n_1F0A0.html
# Use like: print(chr(int('1F0A1', 16)))
#
# The codes here are in ndo
card_utf8_codes: list[str] = [ '1F0A1', '1F0A2', '1F0A3', '1F0A4', '1F0A5', '1F0A6', '1F0A7', '1F0A8', '1F0A9', '1F0AA', '1F0AB', '1F0AD', '1F0AE', '1F0C1', '1F0C2', '1F0C3', '1F0C4', '1F0C5', '1F0C6', '1F0C7', '1F0C8', '1F0C9', '1F0CA', '1F0CB', '1F0CD', '1F0CE', '1F0DE', '1F0DD', '1F0DB', '1F0DA', '1F0D9', '1F0D8', '1F0D7', '1F0D6', '1F0D5', '1F0D4', '1F0D3', '1F0D2', '1F0D1', '1F0BE', '1F0BD', '1F0BB', '1F0BA', '1F0B9', '1F0B8', '1F0B7', '1F0B6', '1F0B5', '1F0B4', '1F0B3', '1F0B2', '1F0B1' ]

# 💾
save_icon_utf8: list[str] = '1F4BE'


type boundingBoxType = tuple[int,int,int,int]
