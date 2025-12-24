import argparse
import turtle
import tkinter

import card_shuffle_constants

def turtle_demo():
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

def tkinter_demo():
    ace_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 1)), 16))
    ace_diamond = chr(int(card_shuffle_constants.card_to_utf8.get(('diamond', 1)), 16))
    ace_club = chr(int(card_shuffle_constants.card_to_utf8.get(('club', 1)), 16))
    ace_heart = chr(int(card_shuffle_constants.card_to_utf8.get(('heart', 1)), 16))

    cardFontStyle = ('Consolas', 81)

    tkinterWindow = tkinter.Tk()

    tkinterWindow.title("pcs: pseudo card shuffle")
    tkinterWindow.geometry("1036x583")

    cardFrame = tkinter.Frame(
        tkinterWindow, borderwidth=0, padx=22, highlightthickness=0
    )

    cardFrame.grid()

    # tkinter/tcl colors
    # https://www.tcl-lang.org/man/tcl8.5/TkCmd/colors.htm

    tkinter.Label(cardFrame, text=ace_spade, font=cardFontStyle, fg="midnight blue").grid(column=0, row=0)
    tkinter.Label(cardFrame, text=ace_diamond, font=cardFontStyle, fg="firebrick").grid(column=1, row=0)
    tkinter.Label(cardFrame, text=ace_heart, font=cardFontStyle, fg="dark olive green").grid(column=2, row=0)
    tkinter.Label(cardFrame, text=ace_club, font=cardFontStyle, fg="DarkOrange2").grid(column=3, row=0)

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
