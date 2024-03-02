import tkinter
from tkinter import ttk


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

APPLICATION_VERSION = '1.00'

DEFAULT_FONT_FAMILY = 'Berlin Sans FB'

TITLE_FONT_SIZE = 26
REGULAR_FONT_SIZE = 15
TINY_FONT_SIZE = 13

TITLE_FONT = (DEFAULT_FONT_FAMILY, TITLE_FONT_SIZE)
REGULAR_FONT = (DEFAULT_FONT_FAMILY, REGULAR_FONT_SIZE)
TINY_FONT = (DEFAULT_FONT_FAMILY, TINY_FONT_SIZE)


BACKGROUND_COLOR = 'white'
PALETTE_COLOR1 = '#a3e3d3'


def set_application_style(root: tkinter.Tk) -> ttk.Style:
    style = ttk.Style(root)
    style.theme_use('classic')
    style.configure('.', background=BACKGROUND_COLOR)
    root.option_add('*Background', BACKGROUND_COLOR)
    root.configure(bg='white')
    return style
