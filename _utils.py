''' Helpful methods for card shuffling '''

from turtle import Turtle
import tkinter
from PIL import ImageGrab

from _constants import (
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
    tooter = Turtle()

    # https://docs.python.org/3/library/turtle.html#turtle-tutorial

    tooter.screen.title('pcs: hello tooter turtle')
    tooter.penup()
    tooter.color('deep pink')
    tooter.goto(0, 30)
    tooter.write(s1, font=style, move=True)
    tooter.goto(50, 30)
    tooter.write(d1, font=style, move=True)
    tooter.hideturtle()

    tooter.screen.mainloop()


def _capture_tkinter(capture_window, offset_area, capture_prefix='shuffled'):
    '''Save an image of the display cards

    Grab the current screen using pillow and crop the area outside of the gui using the tkinter
        window + widget geometry

    Args:
        capture_window (tkinter.Tk): The current tkinter instance to pull geometry from
        offset_area (tkinter.Frame): The widget to ignore when grabbing screenshot
    '''

    capture_window.update_idletasks()

    capture_area_start_x = capture_window.winfo_rootx()
    capture_area_start_y = capture_window.winfo_rooty()
    offset_y = offset_area.winfo_height() + 20
    capture_area_end_x = capture_area_start_x + capture_window.winfo_width()
    capture_area_end_y = capture_area_start_y + capture_window.winfo_height() - offset_y
    capture_filename = "{}.decklist.png".format(capture_prefix)

    # https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
    #
    # bbox determines what region of screen to save
    #
    capture_image = ImageGrab.grab(
        bbox=(capture_area_start_x, capture_area_start_y, capture_area_end_x, capture_area_end_y)
    )

    capture_image.save(capture_filename)

    print("Decklist saved to '{}'".format(capture_filename))


def _capture_tkinter_partial(capture_window, offset_area, capture_prefix='shuffled'):
    ''' Grab screenshot and close window '''

    def _partial_func():
        ''' Passed to the command= param for tkinter button widget and invoked upon click '''

        _capture_tkinter(capture_window, offset_area, capture_prefix)
        capture_window.destroy()

    return _partial_func


def ndo_example():
    ''' Print cards in new deck order: (♠️:A-K, ♦️:A-K, ♣️:K-A, ♥️:K-A) '''

    card_roll, _ = _setup_52()

    rootWindow = tkinter.Tk()
    window_height = int(rootWindow.winfo_screenheight() * 0.63)
    window_width = int(rootWindow.winfo_screenwidth() * 0.63)
    card_font_size = int(window_height * 0.1325)
    control_font_size = int(window_height * 0.033)
    card_font_style = ('Consolas', card_font_size)
    control_font_style = ('Consolas', control_font_size)

    rootWindow.title("pcs: pseudo card shuffle")
    rootWindow.geometry("{}x{}".format(window_width, window_height))
    rootWindow.grid_columnconfigure(0, weight=1)

    cardFrame = tkinter.Frame(rootWindow, bd=0, highlightthickness=0)

    cardFrame.grid()

    controlFrame = tkinter.Frame(rootWindow, bd=0, highlightthickness=0)

    controlFrame.grid()

    tkinter.Button(
        controlFrame, text=chr(int(floppy_code, 16)), font=control_font_style, fg="goldenrod3",
        command=_capture_tkinter_partial(rootWindow, controlFrame, 'ndo'), relief="flat"
    ).pack()

    # tkinter/tcl colors
    # https://www.tcl-lang.org/man/tcl8.5/TkCmd/colors.htm

    for frame_idx, card_info in enumerate(card_roll[:13]):
        tkinter.Label(cardFrame,
            text=chr(int(card_to_utf8.get(card_info), 16)), font=card_font_style, fg='midnight blue'
        ).grid(column=frame_idx, row=0)

    for frame_idx, card_info in enumerate(card_roll[13:26]):
        tkinter.Label(cardFrame,
            text=chr(int(card_to_utf8.get(card_info), 16)), font=card_font_style, fg='firebrick'
        ).grid(column=frame_idx, row=1)

    for frame_idx, card_info in enumerate(card_roll[26:39]):
        tkinter.Label(cardFrame,
            text=chr(int(card_to_utf8.get(card_info), 16)), font=card_font_style, fg='dark olive green'
        ).grid(column=frame_idx, row=2)

    for frame_idx, card_info in enumerate(card_roll[39:]):
        tkinter.Label(cardFrame,
            text=chr(int(card_to_utf8.get(card_info), 16)), font=card_font_style, fg='DarkOrange2'
        ).grid(column=frame_idx, row=3)

    rootWindow.mainloop()


if __name__ == "__main__":
    hello_turtle()
