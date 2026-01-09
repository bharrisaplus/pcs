''' Show a deck of cards '''

from turtle import Turtle
from functools import partial as fpartial
from typing import Callable
from tkinter.ttk import Combobox as tkCombobox
from tkinter import (
    Frame as tkFrame,
    Canvas as tkCanvas,
    Button as tkButton,
    PhotoImage as tkImage,
    EventType as tkEventType,
    Event as tkEvent,
    Tk
)

from _constants import (
    save_icon_utf8 as floppy_code,
    boundingBoxType as boundingBox,
    sqwiggle_b16_path as sqwiggle_b16,
    sqwiggle_b32_path as sqwiggle_b32
)

from _utils import (
    _capture_tkinter as screen_grab,
    get_card_color,
    get_card_symbol
)

# https://www.tcl-lang.org/man/tcl8.6/TkCmd/colors.htm
tkinter_card_colors: list[str] = ['midnight blue', 'firebrick', 'dark olive green', 'DarkOrange3']
tkinter_bg_colors: list[str] = ['ivory2', 'ivory3', 'snow', 'AntiqueWhite2', 'bisque2', 'cornsilk2', 'honeydew2', 'lavender blush', 'LightYellow2']


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


def _handle_select_background(_event: tkEvent, _window: Tk) -> None:
    ''' Upate the colors for various widgets based on user pick '''

    _window.update_idletasks()

    selected_option = _event.widget.get()

    if _window.cget('bg') != selected_option:
        _window.configure(bg=selected_option)

        _canvas = _window.nametowidget("card_canvas")
        _frame = _window.nametowidget("control_frame")
        _button = _frame.nametowidget("save_button")

        if _canvas:
            _canvas.configure(bg=selected_option)
        if _frame:
            _frame.configure(bg=selected_option)
        if _button:
            _button.configure(bg=selected_option)


def _get_capture_coordinates(capture_window: Tk) -> boundingBox:
    ''' Determine where to capture screen at. Helper for card_shuffle_gui.py@_save_command '''

    _child = capture_window.nametowidget("card_canvas")

    capture_area_start_x = capture_window.winfo_rootx()
    capture_area_start_y = capture_window.winfo_rooty()

    capture_area_end_x = capture_area_start_x + capture_window.winfo_width()
    capture_area_end_y = capture_area_start_y + _child.winfo_height()

    return (capture_area_start_x, capture_area_start_y, capture_area_end_x, capture_area_end_y)


def _save_command(capture_window: Tk, capture_prefix: str) -> None:
    ''' Click handler to grab screenshot then close window '''

    capture_window.update_idletasks()

    capture_coordinates = _get_capture_coordinates(capture_window)

    screen_grab(capture_bounds=capture_coordinates, capture_prefix=capture_prefix)
    capture_window.destroy()


def _handle_enterleave_tilt() -> Callable[[tkEvent], None]:
    ''' HOF for Scoped mouse events '''

    _last_tilt_event = None
    _last_untilt_event = None

    def _handle_enterleave_tilt_inner(_event: tkEvent) -> None:
        ''' Create effect where cards move as mouse hovers over '''

        nonlocal _last_tilt_event, _last_untilt_event

        _item_id = _event.widget.find_withtag("current")

        if _event.type == tkEventType.Enter:
            if _last_tilt_event:
                _event.widget.after_cancel(_last_tilt_event)

            _last_tilt_event = _event.widget.after_idle(
                lambda: _event.widget.itemconfig(_item_id, angle=2.8125) if _item_id else None
            )
        else:
            if _last_untilt_event:
                _event.widget.after_cancel(_last_untilt_event)

            _last_untilt_event = _event.widget.after_idle(
                lambda: _event.widget.itemconfig(_item_id, angle=0) if _item_id else None
            )

    return _handle_enterleave_tilt_inner


def display_cards(card_roll: list[int], four_color: bool = False, capture_filename: str = 'shuffled') -> None:
    '''Show the cards using utf-8 symbols

    Create widgets in tkinter based on the layout below:
        rootWindow
            cardCanvas:
                [{Cards 1 - 13}]
                [{Cards 14 - 26}]
                [{Cards 27 - 39}]
                [{Cards 40 - 52}]
            controlFrame:
                [{backgroundDropdown}][{saveButton}]

        When clicked, the saveButton will create an image file of the rootWindow and cardFrame
    '''

    rootWindow = Tk()
    window_height = int((rootWindow.winfo_screenheight() * 0.63) // 1)
    window_width = int((rootWindow.winfo_screenwidth() * 0.63) // 1)
    cardFontStyle = ('Consolas', int(window_height * 0.1325 // 1))
    controlFontStyle = ('Consolas', int(window_height * 0.03 // 1))

    rootWindow.title("pcs: pseudo card shuffle")
    rootWindow.geometry("{}x{}".format(window_width, window_height))
    rootWindow.grid_columnconfigure(0, weight=1)
    rootWindow.configure(bg=tkinter_bg_colors[0])
    rootWindow.wm_iconphoto(True, tkImage(file=sqwiggle_b16), tkImage(file=sqwiggle_b32))

    card_tag = 'card'
    cardCanvas_width = (window_width * 0.85) // 1
    cardCanvas_height = (window_height * 0.85) // 1
    cardCanvas = tkCanvas(rootWindow, name='card_canvas',
        bd=0, highlightthickness=0, bg=tkinter_bg_colors[0],
        width=cardCanvas_width, height=cardCanvas_height
    )

    cardCanvas.grid()

    controlFrame = tkFrame(rootWindow, name="control_frame",
        bd=0, highlightthickness=0, bg=tkinter_bg_colors[0],
        padx=(window_width * 0.025), pady=(window_width * 0.025)
    )

    controlFrame.grid(sticky='ew')

    backgroundDropdown = tkCombobox(controlFrame, values=tkinter_bg_colors, state='readonly')

    backgroundDropdown.pack(side='left')
    backgroundDropdown.current(0)

    tkButton(controlFrame, name='save_button',
        text=chr(int(floppy_code, 16)), font=controlFontStyle, fg="dim gray", relief="flat", bd=0,
        bg=tkinter_bg_colors[0], activebackground=tkinter_bg_colors[0], activeforeground='dim gray',
        command=fpartial(_save_command, capture_window=rootWindow, capture_prefix=capture_filename)
    ).pack(side='right')

    backgroundDropdown.bind('<<ComboboxSelected>>', fpartial(_handle_select_background, _window=rootWindow))
    cardCanvas.tag_bind(card_tag, "<Enter>", _handle_enterleave_tilt())
    cardCanvas.tag_bind(card_tag, "<Leave>", _handle_enterleave_tilt())

    for row_idx in range(4):
        for column_idx, card_info in enumerate(card_roll[row_idx*13:(row_idx+1)*13]):
            pos_x = column_idx * (cardCanvas_width // 13)
            pos_y = row_idx * (cardCanvas_height // 4)

            cardCanvas.create_text(pos_x, pos_y, anchor="nw", tags=card_tag,
                text=get_card_symbol(card_info), font=cardFontStyle,
                fill=tkinter_card_colors[get_card_color(card_info, four_color)]
            )

    rootWindow.mainloop()


if __name__ == "__main__":
    hello_turtle()
