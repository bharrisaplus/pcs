# (P)seudo (C)ard (S)huffler
For producing a pseudo-randomized list of playing cards (♠️♦️♣️♥️).

## Usage
Outputs the list of cards to the console and optionally to a file.

### Console output only
```
$ python card_shuffle.py
1) Two of Spade
2) King of Heart
3) Seven of Club
4) Ace of Diamond
....
52) Queen of Heart
```

### Writing to file
```
$ python card_shuffle.py -w,--write
1) Three of Club
2) Ace of Spade
3) Two of Spade
4) King of Heart
....
52) Five of Heart
Decklist written to 'shuffled.decklist.txt'.
```

### Help display
```
$ python card_shuffle.py -h
usage: card_shuffle.py [-h] [-w]

Producing a pseudo-randomized list of playing cards.

options:
  -h, --help   show this help message and exit
  -w, --write  Flag to set for writing output to a file
```