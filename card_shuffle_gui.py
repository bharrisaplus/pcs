''' Show a deck of cards '''

from turtle import Turtle
import tkinter

from _constants import (
    save_icon_utf8 as floppy_code,
    card_group_a,
    card_group_b,
    card_to_utf8
)

from _utils import (
    _capture_tkinter as screen_grab,
    get_card_color as _get_card_color,
    get_card_symbol
)

def hello_turtle():
    ''' Print card symbols to screen '''

    s1 = get_card_symbol(0)
    d1 = get_card_symbol(13)
    turtle_colors = ['deep pink', 'maroon']
    style = ('Consolas', 45)
    tooter = Turtle()

    # https://docs.python.org/3/library/turtle.html#turtle-tutorial

    tooter.screen.title('pcs: hello tooter turtle')
    tooter.penup()
    tooter.color(turtle_colors[_get_card_color(0)])
    tooter.goto(0, 30)
    tooter.write(s1, font=style, move=True)
    tooter.color(turtle_colors[_get_card_color(13)])
    tooter.goto(50, 30)
    tooter.write(d1, font=style, move=True)
    tooter.hideturtle()

    tooter.screen.mainloop()


def _save_command(capture_window, offset_area, capture_prefix='shuffled'):
    ''' Create wrapper method to grab screenshot and close window '''

    def _partial_func():
        ''' Passed to the command= param for tkinter button widget and invoked upon click '''

        screen_grab(capture_window, offset_area, capture_prefix)
        capture_window.destroy()

    return _partial_func


def get_card_color(card_suite, four_color=False):
    '''Pick the tkinter color for the card suite

    https://www.tcl-lang.org/man/tcl8.6/TkCmd/colors.htm

    Args:
        card_suite (str):
        four_color (bool): Whether to use one color per suite (default: `False`)

    Returns:
        str: tkinter color name
    '''
    suite_color = None

    if card_suite in card_group_a:
        suite_color = 'midnight blue'

        if four_color and card_suite == card_group_a[1]:
            suite_color = 'dark olive green'

    if card_suite in card_group_b:
        suite_color = 'firebrick'

        if four_color and card_suite == card_group_b[1]:
            suite_color = 'DarkOrange2'

    return suite_color


def display_cards(card_roll, four_color=False):
    '''Show the cards using utf-8 symbols

    Create a layout in tkinter with the following layout
        rootWindow
            cardFrame:
                [{Cards 1 - 13}]
                [{Cards 14 - 26}]
                [{Cards 27 - 39}]
                [{Cards 40 - 52}]
            controlFrame:
                [{saveButton}]

        When clicked, the saveButton will create an image file of the rootWindow and cardFrame only.

    Args:
        card_roll (list[tuple(str, int)]): The cards to be shown. See _constants.py@_setup_52
        four_color (bool): Whether to use one color pre suite when displaying cards (default: False)
    '''

    rootWindow = tkinter.Tk()
    window_height = int((rootWindow.winfo_screenheight() * 0.63) // 1)
    window_width = int((rootWindow.winfo_screenwidth() * 0.63) // 1)
    cardFontStyle = ('Consolas', int(window_height * 0.1325 // 1))
    controlFontStyle = ('Consolas', int(window_height * 0.033 // 1))

    rootWindow.title("pcs: pseudo card shuffle")
    rootWindow.geometry("{}x{}".format(window_width, window_height))
    rootWindow.grid_columnconfigure(0, weight=1)

    cardFrame = tkinter.Frame(rootWindow, bd=0, highlightthickness=0)

    cardFrame.grid()

    controlFrame = tkinter.Frame(rootWindow, bd=0, highlightthickness=0, pady=9)

    controlFrame.grid()

    tkinter.Button(
        controlFrame, text=chr(int(floppy_code, 16)), font=controlFontStyle, fg="goldenrod3",
        command=_save_command(rootWindow, controlFrame), relief="flat"
    ).pack()

    for row_idx in range(4):
        for column_idx, card_info in enumerate(card_roll[row_idx*13:(row_idx+1)*13]):
            tkinter.Label(
                cardFrame, text=chr(int(card_to_utf8.get(card_info), 16)), font=cardFontStyle,
                fg=get_card_color(card_info[0], four_color)
            ).grid(column=column_idx, row=row_idx)

    rootWindow.mainloop()


if __name__ == "__main__":
    hello_turtle()
