import turtle
import tkinter
from PIL import ImageGrab

from card_shuffle_constants import (
    suites as card_suites,
    number_values as card_nums,
    save_icon_utf8 as floppy_code,
    card_to_utf8
)

def _setup_52():
    '''Arrange playing cards in new deck order (♠️:A-K, ♦️:A-K, ♣️:K-A, ♥️:K-A).

    Returns:
        (tuple[ tuple(str, int)], list[int] ]): The arranged cards and the positions to fill in:
            * tuple(str, int): model representing the cards
                * str: The suite of the card. See card_shuffle_constants.py:suites
                * int: The number value of the card. See card_shuffle_constants.py:number_values
            * list[int]: The numbered spots where cards can go
    '''

    card_bank = []

    for suite in card_suites:
        if suite in card_suites[:2]:
            for idx in card_nums:
                card_bank.append((suite, idx))
        else:
            for idx in reversed(card_nums):
                card_bank.append((suite, idx))

    return card_bank, list(range(len(card_bank)))

def hello_turtle():
    ''' Print card symbols to screen '''

    s1 = chr(int(card_to_utf8.get(('spade', 1)), 16))
    d1 = chr(int(card_to_utf8.get(('diamond', 1)), 16))
    style = ('Consolas', 45)

    # https://docs.python.org/3/library/turtle.html#turtle-tutorial

    turtle.color('deep pink')

    turtle.penup()
    turtle.goto(0,30)
    turtle.write(s1, font=style, move=True)
    turtle.goto(50,30)
    turtle.write(d1, font=style, move=True)
    turtle.hideturtle()

    turtle.mainloop()

def _capture_tkinter(captureWindow, offsetArea, captureFileName='shuffled'):
    '''Save an image of the display cards

    Grab the current screen using pillow and crop the area outside of the gui using the tkinter
        window + widget geometry

    Args:
        captureWindow (tkinter.Tk): The current tkinter instance to pull geometry from
        offsetArea (tkinter.Frame): The widget to ignore when grabbing screenshot
    '''

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

def _capture_tkinter_partial(captureWindow, offsetArea, captureFileName='shuffled'):
    ''' Grab screenshot and close window '''

    def _partialFunc():
        ''' Passed to the command= param for tkinter button widget and invoked upon click '''

        _capture_tkinter(captureWindow,offsetArea, captureFileName)
        captureWindow.destroy()

    return _partialFunc

def ndo_example():
    ''' Print cards in new deck order: (♠️:A-K, ♦️:A-K, ♣️:K-A, ♥️:K-A) '''

    cardFontStyle = ('Consolas', 81)
    s1 = chr(int(card_to_utf8.get(('spade', 1)), 16))
    s2 = chr(int(card_to_utf8.get(('spade', 2)), 16))
    s3 = chr(int(card_to_utf8.get(('spade', 3)), 16))
    s4 = chr(int(card_to_utf8.get(('spade', 4)), 16))
    s5 = chr(int(card_to_utf8.get(('spade', 5)), 16))
    s6 = chr(int(card_to_utf8.get(('spade', 6)), 16))
    s7 = chr(int(card_to_utf8.get(('spade', 7)), 16))
    s8 = chr(int(card_to_utf8.get(('spade', 8)), 16))
    s9 = chr(int(card_to_utf8.get(('spade', 9)), 16))
    s10 = chr(int(card_to_utf8.get(('spade', 10)), 16))
    s11 = chr(int(card_to_utf8.get(('spade', 11)), 16))
    s12 = chr(int(card_to_utf8.get(('spade', 12)), 16))
    s13 = chr(int(card_to_utf8.get(('spade', 13)), 16))

    d1 = chr(int(card_to_utf8.get(('diamond', 1)), 16))
    d2 = chr(int(card_to_utf8.get(('diamond', 2)), 16))
    d3 = chr(int(card_to_utf8.get(('diamond', 3)), 16))
    d4 = chr(int(card_to_utf8.get(('diamond', 4)), 16))
    d5 = chr(int(card_to_utf8.get(('diamond', 5)), 16))
    d6 = chr(int(card_to_utf8.get(('diamond', 6)), 16))
    d7 = chr(int(card_to_utf8.get(('diamond', 7)), 16))
    d8 = chr(int(card_to_utf8.get(('diamond', 8)), 16))
    d9 = chr(int(card_to_utf8.get(('diamond', 9)), 16))
    d10 = chr(int(card_to_utf8.get(('diamond', 10)), 16))
    d11 = chr(int(card_to_utf8.get(('diamond', 11)), 16))
    d12 = chr(int(card_to_utf8.get(('diamond', 12)), 16))
    d13 = chr(int(card_to_utf8.get(('diamond', 13)), 16))

    c1 = chr(int(card_to_utf8.get(('club', 1)), 16))
    c2 = chr(int(card_to_utf8.get(('club', 2)), 16))
    c3 = chr(int(card_to_utf8.get(('club', 3)), 16))
    c4 = chr(int(card_to_utf8.get(('club', 4)), 16))
    c5 = chr(int(card_to_utf8.get(('club', 5)), 16))
    c6 = chr(int(card_to_utf8.get(('club', 6)), 16))
    c7 = chr(int(card_to_utf8.get(('club', 7)), 16))
    c8 = chr(int(card_to_utf8.get(('club', 8)), 16))
    c9 = chr(int(card_to_utf8.get(('club', 9)), 16))
    c10 = chr(int(card_to_utf8.get(('club', 10)), 16))
    c11 = chr(int(card_to_utf8.get(('club', 11)), 16))
    c12 = chr(int(card_to_utf8.get(('club', 12)), 16))
    c13 = chr(int(card_to_utf8.get(('club', 13)), 16))

    h1 = chr(int(card_to_utf8.get(('heart', 1)), 16))
    h2 = chr(int(card_to_utf8.get(('heart', 2)), 16))
    h3 = chr(int(card_to_utf8.get(('heart', 3)), 16))
    h4 = chr(int(card_to_utf8.get(('heart', 4)), 16))
    h5 = chr(int(card_to_utf8.get(('heart', 5)), 16))
    h6 = chr(int(card_to_utf8.get(('heart', 6)), 16))
    h7 = chr(int(card_to_utf8.get(('heart', 7)), 16))
    h8 = chr(int(card_to_utf8.get(('heart', 8)), 16))
    h9 = chr(int(card_to_utf8.get(('heart', 9)), 16))
    h10 = chr(int(card_to_utf8.get(('heart', 10)), 16))
    h11 = chr(int(card_to_utf8.get(('heart', 11)), 16))
    h12 = chr(int(card_to_utf8.get(('heart', 12)), 16))
    h13 = chr(int(card_to_utf8.get(('heart', 13)), 16))

    tkinterWindow = tkinter.Tk()

    tkinterWindow.title("pcs: pseudo card shuffle")
    tkinterWindow.geometry("1036x583")

    cardFrame = tkinter.Frame(tkinterWindow, borderwidth=0, padx=22, highlightthickness=0)

    cardFrame.grid()

    controlFrame = tkinter.Frame(tkinterWindow, borderwidth=0, highlightthickness=0)

    controlFrame.grid()

    tkinter.Button(
        controlFrame, text=chr(int(floppy_code, 16)), font=('Consolas', 18), fg="goldenrod3",
        command=_capture_tkinter_partial(tkinterWindow, controlFrame, 'ndo'), relief="flat"
    ).pack()

    # tkinter/tcl colors
    # https://www.tcl-lang.org/man/tcl8.5/TkCmd/colors.htm

    tkinter.Label(cardFrame, text=s1, font=cardFontStyle, fg="midnight blue").grid(column=0, row=0)
    tkinter.Label(cardFrame, text=s2, font=cardFontStyle, fg="midnight blue").grid(column=1, row=0)
    tkinter.Label(cardFrame, text=s3, font=cardFontStyle, fg="midnight blue").grid(column=2, row=0)
    tkinter.Label(cardFrame, text=s4, font=cardFontStyle, fg="midnight blue").grid(column=3, row=0)
    tkinter.Label(cardFrame, text=s5, font=cardFontStyle, fg="midnight blue").grid(column=4, row=0)
    tkinter.Label(cardFrame, text=s6, font=cardFontStyle, fg="midnight blue").grid(column=5, row=0)
    tkinter.Label(cardFrame, text=s7, font=cardFontStyle, fg="midnight blue").grid(column=6, row=0)
    tkinter.Label(cardFrame, text=s8, font=cardFontStyle, fg="midnight blue").grid(column=7, row=0)
    tkinter.Label(cardFrame, text=s9, font=cardFontStyle, fg="midnight blue").grid(column=8, row=0)
    tkinter.Label(cardFrame, text=s10, font=cardFontStyle, fg="midnight blue").grid(column=9, row=0)
    tkinter.Label(cardFrame, text=s11, font=cardFontStyle, fg="midnight blue").grid(column=10, row=0)
    tkinter.Label(cardFrame, text=s12, font=cardFontStyle, fg="midnight blue").grid(column=11, row=0)
    tkinter.Label(cardFrame, text=s13, font=cardFontStyle, fg="midnight blue").grid(column=12, row=0)
    tkinter.Label(cardFrame, text=d1, font=cardFontStyle, fg="firebrick").grid(column=13, row=0)

    tkinter.Label(cardFrame, text=d2, font=cardFontStyle, fg="firebrick").grid(column=0, row=1)
    tkinter.Label(cardFrame, text=d3, font=cardFontStyle, fg="firebrick").grid(column=1, row=1)
    tkinter.Label(cardFrame, text=d4, font=cardFontStyle, fg="firebrick").grid(column=2, row=1)
    tkinter.Label(cardFrame, text=d5, font=cardFontStyle, fg="firebrick").grid(column=3, row=1)
    tkinter.Label(cardFrame, text=d6, font=cardFontStyle, fg="firebrick").grid(column=4, row=1)
    tkinter.Label(cardFrame, text=d7, font=cardFontStyle, fg="firebrick").grid(column=5, row=1)
    tkinter.Label(cardFrame, text=d8, font=cardFontStyle, fg="firebrick").grid(column=6, row=1)
    tkinter.Label(cardFrame, text=d9, font=cardFontStyle, fg="firebrick").grid(column=7, row=1)
    tkinter.Label(cardFrame, text=d10, font=cardFontStyle, fg="firebrick").grid(column=8, row=1)
    tkinter.Label(cardFrame, text=d11, font=cardFontStyle, fg="firebrick").grid(column=9, row=1)
    tkinter.Label(cardFrame, text=d12, font=cardFontStyle, fg="firebrick").grid(column=10, row=1)
    tkinter.Label(cardFrame, text=d13, font=cardFontStyle, fg="firebrick").grid(column=11, row=1)
    tkinter.Label(cardFrame, text=c1, font=cardFontStyle, fg="dark olive green").grid(column=12, row=1)
    tkinter.Label(cardFrame, text=c2, font=cardFontStyle, fg="dark olive green").grid(column=13, row=1)

    tkinter.Label(cardFrame, text=c3, font=cardFontStyle, fg="dark olive green").grid(column=0, row=2)
    tkinter.Label(cardFrame, text=c4, font=cardFontStyle, fg="dark olive green").grid(column=1, row=2)
    tkinter.Label(cardFrame, text=c5, font=cardFontStyle, fg="dark olive green").grid(column=2, row=2)
    tkinter.Label(cardFrame, text=c6, font=cardFontStyle, fg="dark olive green").grid(column=3, row=2)
    tkinter.Label(cardFrame, text=c7, font=cardFontStyle, fg="dark olive green").grid(column=4, row=2)
    tkinter.Label(cardFrame, text=c8, font=cardFontStyle, fg="dark olive green").grid(column=5, row=2)
    tkinter.Label(cardFrame, text=c9, font=cardFontStyle, fg="dark olive green").grid(column=6, row=2)
    tkinter.Label(cardFrame, text=c10, font=cardFontStyle, fg="dark olive green").grid(column=7, row=2)
    tkinter.Label(cardFrame, text=c11, font=cardFontStyle, fg="dark olive green").grid(column=8, row=2)
    tkinter.Label(cardFrame, text=c12, font=cardFontStyle, fg="dark olive green").grid(column=9, row=2)
    tkinter.Label(cardFrame, text=c13, font=cardFontStyle, fg="dark olive green").grid(column=10, row=2)
    tkinter.Label(cardFrame, text=h1, font=cardFontStyle, fg="DarkOrange2").grid(column=11, row=2)
    tkinter.Label(cardFrame, text=h2, font=cardFontStyle, fg="DarkOrange2").grid(column=12, row=2)
    tkinter.Label(cardFrame, text=h3, font=cardFontStyle, fg="DarkOrange2").grid(column=13, row=2)

    tkinter.Label(cardFrame, text=h4, font=cardFontStyle, fg="DarkOrange2").grid(column=0, row=3)
    tkinter.Label(cardFrame, text=h5, font=cardFontStyle, fg="DarkOrange2").grid(column=1, row=3)
    tkinter.Label(cardFrame, text=h6, font=cardFontStyle, fg="DarkOrange2").grid(column=2, row=3)
    tkinter.Label(cardFrame, text=h7, font=cardFontStyle, fg="DarkOrange2").grid(column=3, row=3)
    tkinter.Label(cardFrame, text=h8, font=cardFontStyle, fg="DarkOrange2").grid(column=4, row=3)
    tkinter.Label(cardFrame, text=h9, font=cardFontStyle, fg="DarkOrange2").grid(column=5, row=3)
    tkinter.Label(cardFrame, text=h10, font=cardFontStyle, fg="DarkOrange2").grid(column=6, row=3)
    tkinter.Label(cardFrame, text=h11, font=cardFontStyle, fg="DarkOrange2").grid(column=7, row=3)
    tkinter.Label(cardFrame, text=h12, font=cardFontStyle, fg="DarkOrange2").grid(column=8, row=3)
    tkinter.Label(cardFrame, text=h13, font=cardFontStyle, fg="DarkOrange2").grid(column=9, row=3)

    tkinterWindow.mainloop()

if __name__ == "__main__":
    hello_turtle()
