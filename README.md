# (P)seudo (C)ard (S)huffler
For producing a pseudo-randomized list of playing cards (♠️♦️♣️♥️).

![example_image](example.webp)

* [Overview](#overview)
* [Usage](#usage)
  * [Install dependencies](#install-dependencies)
    * [pip](#pip)
    * [pipenv](#pipenv)
  * [Console](#console)
    * [Writing to a file](#writing-to-file)
  * [GUI](#gui)
    * [NDO Example](#ndo)
  * [Help display](#help-display)

## Overview
Shuffling by taking a random sampling from the available cards and placing them in a position based on a random sampling from available positions in the deck.

## Usage

### Install dependencies
This projects needs tkinter and pillow. Tkinter should be included with most python distributions and pillow is available via pypi
#### pip
To install dependencies globally
```
  pip install pillow
```
#### pipenv
A Pipfile is included for installing dependencies within a virtualenv
```
pipenv install
```
### Console
Outputs the list of cards to the terminal and optionally to a file.
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
Using [tkinter](https://docs.python.org/3/library/tkinter.html) for display and saving to an image with [pillow](https://pillow.readthedocs.io/en/stable/)

```
$ python card_shuffle.py [-g,--gui]
```

#### NDO Example
```
$ python card_shuffle.py [-d, --demo]
```

### Help display
```
$ python card_shuffle.py -h
usage: card_shuffle.py [-h] [-w] [-g] [-f] [-n] [-c] [-a]

Producing a pseudo-randomized list of playing cards.

options:
  -h, --help        show this help message and exit
  -w, --write       Flag to set for writing output to a text file
  -g, --gui         Flag to set for displaying output using tkinter
  -f, --four-color  Flag to set for displaying each suite in a unique color in the tkinter gui window
  -n, --ndo         Flag to set for displaying demo using tkinter. Other options are ignored when set.
  -c, --cut         Flag to set for cutting the deck after the shuffle at a consecutive pair if found.
  -a, --arbitrary   Flag to set for cutting the deck after the shuffle at a random spot.
```