
import tkinter as tk
from tkinter import TOP, CENTER, NONE
from typing import Union, Callable, Optional

from gui.gui_styling_constants import REGULAR_FONT, BACKGROUND_COLOR
from utils.functional_utils import do_nothing


def add_label(parent: Union[tk.Tk, tk.Widget],
              text: str,
              font: (str, int) = REGULAR_FONT,
              dock: str = TOP,
              anchor: str = CENTER,
              pad_x: int = 0,
              pad_y: int = 0) -> tk.Label:
    label = tk.Label(master=parent,
                     text=text,
                     font=font)
    label.pack(padx=pad_x,
               pady=pad_y,
               side=dock,
               anchor=anchor)
    return label


def add_button(parent: Union[tk.Tk, tk.Widget],
               text: str,
               command: Callable[[], None] = do_nothing,
               font=REGULAR_FONT,
               dock=TOP,
               anchor=CENTER,
               width: Optional[int] = None,
               background_color: str = BACKGROUND_COLOR,
               pad_x=0,
               pad_y=0) -> tk.Button:
    button = tk.Button(master=parent,
                       text=text,
                       command=command,
                       font=font,
                       width=width,
                       bg=background_color)
    button.pack(padx=pad_x,
                pady=pad_y,
                side=dock,
                anchor=anchor)
    return button


def add_frame(parent: Union[tk.Tk, tk.Widget],
              dock: str = TOP,
              anchor: str = CENTER,
              background_color: str = BACKGROUND_COLOR,
              height: Optional[int] = None,
              pad_x: int = 0,
              pad_y: int = 0,
              fill: str = NONE,
              expand: bool = False) -> tk.Frame:
    frame = tk.Frame(master=parent,
                     height=height,
                     background=background_color)
    frame.pack(padx=pad_x,
               pady=pad_y,
               side=dock,
               anchor=anchor,
               fill=fill,
               expand=expand)
    return frame
