# (P)seudo (C)ard (S)huffler
For producing a pseudo-randomized list of playing cards (♠️♦️♣️♥️).

* [Overview](#overview)
* [Usage](#usage)
  * [Console](#console)
    * [Console output only](#console-output-only)
    * [Writing to a file](#writing-to-file)
  * [GUI](#gui)
    * [Demo](#demo)
    * [GUI output](#gui-output)
    * [Writing to image file](#writing-to-image-file)
  * [Help display](#help-display)

## Overview

## Usage
Outputs the list of cards to the console and optionally to a file.

### Console

#### Console output only
```
$ python card_shuffle.py
1) Two of Spade
2) King of Heart
3) Seven of Club
4) Ace of Diamond
....
52) Queen of Heart
```

#### Writing to file
```
$ python card_shuffle.py [-w,--write]
1) Three of Club
2) Ace of Spade
3) Two of Spade
4) King of Heart
....
52) Five of Heart
Decklist written to 'shuffled.decklist.txt'.
```

### GUI
Using tkinter

#### Demo
```
$ python card_shuffle.py [-d, --demo]
```

### GUI output
```
$ python card_shuffle.py [-g,--gui]
```

#### Writing to image file
```
$ python card_shuffle.py [-gi, -g -i, --gui --image]
```

### Help display
```
$ python card_shuffle.py -h
usage: card_shuffle.py [-h] [-w] [-g] [-i] [-d]

Producing a pseudo-randomized list of playing cards.

options:
  -h, --help   show this help message and exit
  -w, --write  Flag to set for writing output to a text file
  -g, --gui    Flag to set for displaying output using tkinter
  -i, --image  Flag to set for writing tkinter window to an image file. Requires -g to be set to take effect.
  -d, --demo   Flag to set for displaying demo using tkinter. Other options are ignored when set.
```