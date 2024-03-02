from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from tkinter import TOP, BOTTOM, W, X, BOTH

from gui.gui_styling_constants import TITLE_FONT, APPLICATION_VERSION, TINY_FONT, PALETTE_COLOR1
from utils.functional_utils import do_nothing
from utils.gui_utils import add_label, add_frame, add_button


@dataclass
class LanguageLearningGuiContent:
    root: tk

    def generate_sentence(self) -> None:
        pass

    def add_title_label(self) -> None:
        add_label(parent=self.root,
                  text="French Learning Application",
                  font=TITLE_FONT,
                  dock=TOP,
                  pad_y=20)

    def add_credits_label(self) -> None:
        add_label(parent=self.root,
                  text=f'© Written by Yuval Alfassi, version {APPLICATION_VERSION}',
                  font=TINY_FONT,
                  dock=BOTTOM,
                  anchor=W,
                  pad_x=10,
                  pad_y=5)

    def add_content_frames(self) -> tk.Frame:
        content_frame = add_frame(parent=self.root,
                                  expand=True,
                                  fill=BOTH,
                                  pad_x=10,
                                  pad_y=10)
        sentence_frame = add_frame(parent=content_frame,
                                   pad_y=5,
                                   height=100,
                                   fill=X,
                                   expand=True,
                                   background_color=PALETTE_COLOR1)
        buttons_frame = add_frame(parent=content_frame,
                                  pad_y=5)
        return sentence_frame, buttons_frame

    def add_buttons(self, buttons_frame: tk.Frame) -> None:
        add_button(parent=buttons_frame,
                   text='Submit Answer',
                   command=do_nothing,
                   width=20,
                   background_color=PALETTE_COLOR1,
                   pad_x=5,
                   pad_y=5)
        add_button(parent=buttons_frame,
                   text='Hear Word in French',
                   command=do_nothing,
                   width=20,
                   pad_x=5,
                   pad_y=5)
        add_button(parent=buttons_frame,
                   text='Show Answer',
                   command=do_nothing,
                   width=20,
                   pad_x=5,
                   pad_y=5)
        add_button(parent=buttons_frame,
                   text='Next Sentence',
                   command=do_nothing,
                   width=20,
                   pad_x=5,
                   pad_y=5)

    @staticmethod
    def initialize_gui(root: tk.Tk) -> LanguageLearningGuiContent:
        content = LanguageLearningGuiContent(root)
        content.add_title_label()
        content.add_credits_label()
        sentence_frame, buttons_frame = content.add_content_frames()
        content.add_buttons(buttons_frame)

        return content
