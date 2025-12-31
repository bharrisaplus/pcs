import turtle
import tkinter
from PIL import ImageGrab

from _constants import (
    suites as card_suites,
    number_values as card_nums,
    save_icon_utf8 as floppy_code,
    card_group_b as red_group,
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

    cardRoll, _ = _setup_52()

    tkinterWindow = tkinter.Tk()
    window_height = int((tkinterWindow.winfo_screenheight() * 0.63) // 1)
    window_width = int((tkinterWindow.winfo_screenwidth() * 0.63) // 1)
    cardFontSize = int(window_height * 0.1325 // 1)
    controlFontSize = int(window_height * 0.033 // 1)
    cardFontStyle = ('Consolas', cardFontSize)
    controlFontStyle = ('Consolas', controlFontSize)

    #print("Screen size: {}x{}".format(tkinterWindow.winfo_screenwidth(), tkinterWindow.winfo_screenheight()))
    #print("Window size: {}x{}".format(window_width, window_height))
    #print("Card font size: {}".format(cardFontSize)) # or 63 min
    #print("Control font: {}".format(controlFontSize)) # or 18 min


    tkinterWindow.title("pcs: pseudo card shuffle")
    tkinterWindow.geometry("{}x{}".format(window_width, window_height))
    tkinterWindow.grid_columnconfigure(0, weight=1)

    cardFrame = tkinter.Frame(tkinterWindow, bd=0, highlightthickness=0)

    cardFrame.grid()

    controlFrame = tkinter.Frame(tkinterWindow, bd=0, highlightthickness=0)

    controlFrame.grid()

    tkinter.Button(
        controlFrame, text=chr(int(floppy_code, 16)), font=controlFontStyle, fg="goldenrod3",
        command=_capture_tkinter_partial(tkinterWindow, controlFrame, 'ndo'), relief="flat"
    ).pack()

    # tkinter/tcl colors
    # https://www.tcl-lang.org/man/tcl8.5/TkCmd/colors.htm

    for frame_idx, card_info in enumerate(cardRoll[:13]):
        card_symbol = chr(int(card_to_utf8.get(card_info), 16))
        tkinter.Label(cardFrame, text=card_symbol, font=cardFontStyle, fg='midnight blue').grid(column=frame_idx, row=0)

    for frame_idx, card_info in enumerate(cardRoll[13:26]):
        card_symbol = chr(int(card_to_utf8.get(card_info), 16))
        tkinter.Label(cardFrame, text=card_symbol, font=cardFontStyle, fg='firebrick').grid(column=frame_idx, row=1)

    for frame_idx, card_info in enumerate(cardRoll[26:39]):
        card_symbol = chr(int(card_to_utf8.get(card_info), 16))
        tkinter.Label(cardFrame, text=card_symbol, font=cardFontStyle, fg='dark olive green').grid(column=frame_idx, row=2)

    for frame_idx, card_info in enumerate(cardRoll[39:]):
        card_symbol = chr(int(card_to_utf8.get(card_info), 16))
        tkinter.Label(cardFrame, text=card_symbol, font=cardFontStyle, fg='DarkOrange2').grid(column=frame_idx, row=3)

    tkinterWindow.mainloop()

if __name__ == "__main__":
    hello_turtle()
