''' Show a deck of cards '''

from turtle import Turtle
from functools import partial
from tkinter import (
    Frame as tkFrame,
    Canvas as tkCanvas,
    Button as tkButton,
    EventType as tkEvent,
    Tk
)

from _constants import (
    save_icon_utf8 as floppy_code,
    boundingBoxType as boundingBox,
)

from _utils import (
    _capture_tkinter as screen_grab,
    get_card_color,
    get_card_symbol
)

# https://www.tcl-lang.org/man/tcl8.6/TkCmd/colors.htm
tkinter_card_colors = ['midnight blue', 'firebrick', 'dark olive green', 'DarkOrange3']
tkinter_bg_color = "Ivory2"


def hello_turtle() -> None:
    ''' Print card symbols to screen '''

    s1 = get_card_symbol(0)
    d1 = get_card_symbol(13)
    turtle_colors = ['deep pink', 'maroon']
    style = ('Consolas', 45)
    tooter = Turtle()

    # https://docs.python.org/3/library/turtle.html#turtle-tutorial

    tooter.screen.title('pcs: hello tooter turtle')
    tooter.penup()
    tooter.color(turtle_colors[get_card_color(0)])
    tooter.goto(0, 30)
    tooter.write(s1, font=style, move=True)
    tooter.color(turtle_colors[get_card_color(13)])
    tooter.goto(50, 30)
    tooter.write(d1, font=style, move=True)
    tooter.hideturtle()

    tooter.screen.mainloop()


def _get_capture_coordinates(capture_window: Tk) -> boundingBox:
    ''' Determine where to capture screen at. Helper for card_shuffle_gui.py@_save_command '''

    _child = capture_window.nametowidget("control_frame")

    capture_area_start_x = capture_window.winfo_rootx()
    capture_area_start_y = capture_window.winfo_rooty()
    offset_y = _child.winfo_height()
    capture_area_end_x = capture_area_start_x + capture_window.winfo_width()
    capture_area_end_y = capture_area_start_y + capture_window.winfo_height() - offset_y

    return (capture_area_start_x, capture_area_start_y, capture_area_end_x, capture_area_end_y)


def _save_command(capture_window: Tk, capture_prefix: str) -> None:
    ''' Click handler to grab screenshot then close window '''

    capture_window.update_idletasks()

    capture_coordinates = _get_capture_coordinates(capture_window)

    screen_grab(capture_bounds=capture_coordinates, capture_prefix=capture_prefix)
    capture_window.destroy()


def display_cards(card_roll: list[int], four_color: bool = False, capture_filename: str = 'shuffled') -> None:
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

        When clicked, the saveButton will create an image file of the rootWindow and cardFrame
    '''

    _last_tilt_event = None
    _last_untilt_event = None
    card_tag = 'card'

    def _handle_enterleave_tilt(_event: tkEvent):
        ''' Create effect where cards move as mouse hovers over '''

        nonlocal _last_tilt_event, _last_untilt_event

        _item_id = _event.widget.find_withtag("current")
        _tilt_queue = _last_tilt_event if _event.type == tkEvent.Enter else _last_untilt_event
        angle = 2.8125 if _event.type == tkEvent.Enter else 0

        if _tilt_queue:
            _event.widget.after_cancel(_tilt_queue)

        _tilt_queue = _event.widget.after_idle(
            lambda: _event.widget.itemconfig(_item_id, angle=angle) if _item_id else None
        )

    rootWindow = Tk()
    window_height = int((rootWindow.winfo_screenheight() * 0.63) // 1)
    window_width = int((rootWindow.winfo_screenwidth() * 0.63) // 1)
    cardFontStyle = ('Consolas', int(window_height * 0.1325 // 1))
    controlFontStyle = ('Consolas', int(window_height * 0.033 // 1))

    rootWindow.title("pcs: pseudo card shuffle")
    rootWindow.geometry("{}x{}".format(window_width, window_height))
    rootWindow.grid_columnconfigure(0, weight=1)
    rootWindow.configure(bg=tkinter_bg_color)

    cardCanvas_width = (window_width * 0.85) // 1
    cardCanvas_height = (window_height * 0.85) // 1
    cardCanvas = tkCanvas(
        rootWindow, bd=0, highlightthickness=0, bg=tkinter_bg_color,
        width=cardCanvas_width, height=cardCanvas_height
    )

    cardCanvas.grid()

    controlFrame = tkFrame(
        rootWindow, name="control_frame", bd=0, highlightthickness=0, pady=9, bg=tkinter_bg_color
    )

    controlFrame.grid()

    tkButton(
        controlFrame, text=chr(int(floppy_code, 16)), font=controlFontStyle, fg="dim gray",
        relief="flat", bg=tkinter_bg_color, activebackground=tkinter_bg_color,
        command=partial(_save_command, capture_window=rootWindow, capture_prefix=capture_filename)
    ).pack()

    cardCanvas.tag_bind(card_tag, "<Enter>", _handle_enterleave_tilt)
    cardCanvas.tag_bind(card_tag, "<Leave>", _handle_enterleave_tilt)

    for row_idx in range(4):
        for column_idx, card_info in enumerate(card_roll[row_idx*13:(row_idx+1)*13]):
            pos_x = column_idx * (cardCanvas_width // 13)
            pos_y = row_idx * (cardCanvas_height // 4)

            cardCanvas.create_text(
                pos_x, pos_y, anchor="nw", text=get_card_symbol(card_info), font=cardFontStyle,
                fill=tkinter_card_colors[get_card_color(card_info, four_color)], tags=card_tag
            )

    rootWindow.mainloop()


if __name__ == "__main__":
    hello_turtle()
