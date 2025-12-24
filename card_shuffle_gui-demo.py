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
    two_spade = chr(int(card_shuffle_constants.card_to_utf8.get(('spade', 2)), 16))

    cardFontStyle = ('Consolas', 81)

    tkinterWindow = tkinter.Tk()

    tkinterWindow.title("pcs: pseudo card shuffle")
    tkinterWindow.geometry("1036x583")

    tkinterWindow.mainloop()

if __name__ == "__main__":

    #turtle_demo()
    tkinter_demo()
