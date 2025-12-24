import argparse
import turtle
import tkinter
from PIL import ImageGrab

import card_shuffle_constants

def turtle_demo():
    ''' Print card symbols to screen '''
    ace_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 1)), 16))
    ace_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 1)), 16))

    # https://docs.python.org/3/library/turtle.html#turtle-tutorial

    turtle.color('deep pink')
    style = ('Consolas', 45)

    turtle.penup()
    turtle.goto(0,30)
    turtle.write(ace_spade, font=style, move=True)
    turtle.goto(50,30)
    turtle.write(ace_diamond, font=style, move=True)
    turtle.hideturtle()

    turtle.mainloop()

def _capture_tkinter(captureWindow, offsetArea, captureFileName='shuffled'):
    capture_area_start_x = captureWindow.winfo_rootx()
    capture_area_start_y = captureWindow.winfo_rooty()
    offset_y = offsetArea.winfo_height()
    capture_area_end_x = capture_area_start_x + captureWindow.winfo_width()
    capture_area_end_y = capture_area_start_y + captureWindow.winfo_height() - offset_y
    capture_filename = "{}.decklist.png".format(captureFileName)

    # https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
    #
    # bbox determines what region of screen to save
    #
    capture_image = ImageGrab.grab(
        bbox=(capture_area_start_x, capture_area_start_y, capture_area_end_x, capture_area_end_y)
    )

    capture_image.save(capture_filename)

    print("Decklist saved to '{}'".format(capture_filename))

def tkinter_demo():
    ''' Print cards in new deck order: (♠️:A-K, ♦️:A-K, ♣️:K-A, ♥️:K-A) '''
    ace_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 1)), 16))
    two_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 2)), 16))
    three_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 3)), 16))
    four_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 4)), 16))
    five_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 5)), 16))
    six_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 6)), 16))
    seven_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 7)), 16))
    eight_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 8)), 16))
    nine_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 9)), 16))
    ten_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 10)), 16))
    jack_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 11)), 16))
    queen_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 12)), 16))
    king_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 13)), 16))

    ace_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 1)), 16))
    two_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 2)), 16))
    three_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 3)), 16))
    four_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 4)), 16))
    five_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 5)), 16))
    six_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 6)), 16))
    seven_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 7)), 16))
    eight_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 8)), 16))
    nine_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 9)), 16))
    ten_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 10)), 16))
    jack_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 11)), 16))
    queen_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 12)), 16))
    king_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 13)), 16))

    ace_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 1)), 16))
    two_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 2)), 16))
    three_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 3)), 16))
    four_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 4)), 16))
    five_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 5)), 16))
    six_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 6)), 16))
    seven_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 7)), 16))
    eight_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 8)), 16))
    nine_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 9)), 16))
    ten_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 10)), 16))
    jack_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 11)), 16))
    queen_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 12)), 16))
    king_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 13)), 16))

    ace_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 1)), 16))
    two_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 2)), 16))
    three_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 3)), 16))
    four_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 4)), 16))
    five_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 5)), 16))
    six_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 6)), 16))
    seven_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 7)), 16))
    eight_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 8)), 16))
    nine_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 9)), 16))
    ten_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 10)), 16))
    jack_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 11)), 16))
    queen_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 12)), 16))
    king_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 13)), 16))

    cardFontStyle = ('Consolas', 81)

    tkinterWindow = tkinter.Tk()

    tkinterWindow.title("pcs: pseudo card shuffle")
    tkinterWindow.geometry("1036x583")

    cardFrame = tkinter.Frame(
        tkinterWindow, borderwidth=0, padx=22, highlightthickness=0
    )

    cardFrame.grid()

    controlFrame = tkinter.Frame(
        tkinterWindow, borderwidth=0, highlightthickness=0
    )

    controlFrame.grid()

    def saveButtonCommand():
        ''' Grab screenshot and close window '''
        _capture_tkinter(tkinterWindow, controlFrame, 'ndo')
        tkinterWindow.destroy()

    tkinter.Button(
        controlFrame, text=chr(int(card_shuffle_constants.save_icon_utf8, 16)), font=('Consolas', 18), fg="goldenrod3",
        command=saveButtonCommand, relief="flat"
    ).pack()

    # tkinter/tcl colors
    # https://www.tcl-lang.org/man/tcl8.5/TkCmd/colors.htm

    tkinter.Label(cardFrame, text=ace_spade, font=cardFontStyle, fg="midnight blue").grid(column=0, row=0)
    tkinter.Label(cardFrame, text=two_spade, font=cardFontStyle, fg="midnight blue").grid(column=1, row=0)
    tkinter.Label(cardFrame, text=three_spade, font=cardFontStyle, fg="midnight blue").grid(column=2, row=0)
    tkinter.Label(cardFrame, text=four_spade, font=cardFontStyle, fg="midnight blue").grid(column=3, row=0)
    tkinter.Label(cardFrame, text=five_spade, font=cardFontStyle, fg="midnight blue").grid(column=4, row=0)
    tkinter.Label(cardFrame, text=six_spade, font=cardFontStyle, fg="midnight blue").grid(column=5, row=0)
    tkinter.Label(cardFrame, text=seven_spade, font=cardFontStyle, fg="midnight blue").grid(column=6, row=0)
    tkinter.Label(cardFrame, text=eight_spade, font=cardFontStyle, fg="midnight blue").grid(column=7, row=0)
    tkinter.Label(cardFrame, text=nine_spade, font=cardFontStyle, fg="midnight blue").grid(column=8, row=0)
    tkinter.Label(cardFrame, text=ten_spade, font=cardFontStyle, fg="midnight blue").grid(column=9, row=0)
    tkinter.Label(cardFrame, text=jack_spade, font=cardFontStyle, fg="midnight blue").grid(column=10, row=0)
    tkinter.Label(cardFrame, text=queen_spade, font=cardFontStyle, fg="midnight blue").grid(column=11, row=0)
    tkinter.Label(cardFrame, text=king_spade, font=cardFontStyle, fg="midnight blue").grid(column=12, row=0)
    tkinter.Label(cardFrame, text=ace_diamond, font=cardFontStyle, fg="firebrick").grid(column=13, row=0)

    tkinter.Label(cardFrame, text=two_diamond, font=cardFontStyle, fg="firebrick").grid(column=0, row=1)
    tkinter.Label(cardFrame, text=three_diamond, font=cardFontStyle, fg="firebrick").grid(column=1, row=1)
    tkinter.Label(cardFrame, text=four_diamond, font=cardFontStyle, fg="firebrick").grid(column=2, row=1)
    tkinter.Label(cardFrame, text=five_diamond, font=cardFontStyle, fg="firebrick").grid(column=3, row=1)
    tkinter.Label(cardFrame, text=six_diamond, font=cardFontStyle, fg="firebrick").grid(column=4, row=1)
    tkinter.Label(cardFrame, text=seven_diamond, font=cardFontStyle, fg="firebrick").grid(column=5, row=1)
    tkinter.Label(cardFrame, text=eight_diamond, font=cardFontStyle, fg="firebrick").grid(column=6, row=1)
    tkinter.Label(cardFrame, text=nine_diamond, font=cardFontStyle, fg="firebrick").grid(column=7, row=1)
    tkinter.Label(cardFrame, text=ten_diamond, font=cardFontStyle, fg="firebrick").grid(column=8, row=1)
    tkinter.Label(cardFrame, text=jack_diamond, font=cardFontStyle, fg="firebrick").grid(column=9, row=1)
    tkinter.Label(cardFrame, text=queen_diamond, font=cardFontStyle, fg="firebrick").grid(column=10, row=1)
    tkinter.Label(cardFrame, text=king_diamond, font=cardFontStyle, fg="firebrick").grid(column=11, row=1)
    tkinter.Label(cardFrame, text=king_club, font=cardFontStyle, fg="dark olive green").grid(column=12, row=1)
    tkinter.Label(cardFrame, text=queen_club, font=cardFontStyle, fg="dark olive green").grid(column=13, row=1)

    tkinter.Label(cardFrame, text=jack_club, font=cardFontStyle, fg="dark olive green").grid(column=0, row=2)
    tkinter.Label(cardFrame, text=ten_club, font=cardFontStyle, fg="dark olive green").grid(column=1, row=2)
    tkinter.Label(cardFrame, text=nine_club, font=cardFontStyle, fg="dark olive green").grid(column=2, row=2)
    tkinter.Label(cardFrame, text=eight_club, font=cardFontStyle, fg="dark olive green").grid(column=3, row=2)
    tkinter.Label(cardFrame, text=seven_club, font=cardFontStyle, fg="dark olive green").grid(column=4, row=2)
    tkinter.Label(cardFrame, text=six_club, font=cardFontStyle, fg="dark olive green").grid(column=5, row=2)
    tkinter.Label(cardFrame, text=five_club, font=cardFontStyle, fg="dark olive green").grid(column=6, row=2)
    tkinter.Label(cardFrame, text=four_club, font=cardFontStyle, fg="dark olive green").grid(column=7, row=2)
    tkinter.Label(cardFrame, text=three_club, font=cardFontStyle, fg="dark olive green").grid(column=8, row=2)
    tkinter.Label(cardFrame, text=two_club, font=cardFontStyle, fg="dark olive green").grid(column=9, row=2)
    tkinter.Label(cardFrame, text=ace_club, font=cardFontStyle, fg="dark olive green").grid(column=10, row=2)
    tkinter.Label(cardFrame, text=king_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=11, row=2)
    tkinter.Label(cardFrame, text=queen_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=12, row=2)
    tkinter.Label(cardFrame, text=jack_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=13, row=2)

    tkinter.Label(cardFrame, text=ten_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=0, row=3)
    tkinter.Label(cardFrame, text=nine_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=1, row=3)
    tkinter.Label(cardFrame, text=eight_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=2, row=3)
    tkinter.Label(cardFrame, text=seven_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=3, row=3)
    tkinter.Label(cardFrame, text=six_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=4, row=3)
    tkinter.Label(cardFrame, text=five_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=5, row=3)
    tkinter.Label(cardFrame, text=four_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=6, row=3)
    tkinter.Label(cardFrame, text=three_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=7, row=3)
    tkinter.Label(cardFrame, text=two_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=8, row=3)
    tkinter.Label(cardFrame, text=ace_heart, font=cardFontStyle, fg="DarkOrange2").grid(column=9, row=3)

    tkinterWindow.mainloop()

if __name__ == "__main__":
    # Grab arguments

    cardShuffleParser = argparse.ArgumentParser(prog="card_shuffle.py",
        description="Producing a pseudo-randomized list of playing cards."
    )

    cardShuffleParser.add_argument("-k", "--tk", action="store_true",
        help="Flag to set for displaying tkinter demo"
    )

    cardShuffleParser.add_argument("-u", "--turtle", action="store_true", default=True,
        help="Flag to set for displaying turtle demo"
    )

    cardShuffleArgs = cardShuffleParser.parse_args()

    if cardShuffleArgs.tk:
        tkinter_demo()
    else:
        turtle_demo()
