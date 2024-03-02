
import tkinter as tk
from tkinter import TOP, CENTER, NONE
from typing import Union, Callable, Optional

from gui.gui_styling_constants import REGULAR_FONT, BACKGROUND_COLOR
from utils.functional_utils import do_nothing


ParentWidget = Union[tk.Tk, tk.Widget]


def add_label(parent: ParentWidget,
              text: str,
              font: (str, int) = REGULAR_FONT,
              dock: str = TOP,
              anchor: str = CENTER,
              background_color: str = BACKGROUND_COLOR,
              pad_x: int = 0,
              pad_y: int = 0) -> tk.Label:
    label = tk.Label(master=parent,
                     text=text,
                     font=font,
                     background=background_color)
    label.pack(padx=pad_x,
               pady=pad_y,
               side=dock,
               anchor=anchor)
    return label


def add_button(parent: ParentWidget,
               text: str,
               command: Callable[[], None] = do_nothing,
               font: (str, int) = REGULAR_FONT,
               dock: str = TOP,
               anchor: str = CENTER,
               width: Optional[int] = None,
               background_color: str = BACKGROUND_COLOR,
               pad_x: int = 0,
               pad_y: int = 0) -> tk.Button:
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


def add_frame(parent: ParentWidget,
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


def remove_all_frame_children(frame: tk.Frame) -> None:
    for widget in frame.winfo_children():
        widget.destroy()


def add_entry(parent: tk.Widget,
              text_variable: tk.StringVar,
              dock: str = tk.TOP,
              anchor: str = tk.CENTER,
              font: (str, int) = REGULAR_FONT,
              background_color: str = BACKGROUND_COLOR,
              pad_x: int = 0,
              pad_y: int = 0,
              width: int = 20,
              text_justification: str = CENTER) -> tk.Entry:
    entry = tk.Entry(master=parent,
                     textvariable=text_variable,
                     background=background_color,
                     width=width,
                     font=font,
                     justify=text_justification)
    entry.pack(padx=pad_x,
               pady=pad_y,
               side=dock,
               anchor=anchor)
    return entry
