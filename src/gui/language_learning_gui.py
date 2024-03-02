from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk

from gui.gui_styling_constants import set_application_style, WINDOW_WIDTH, \
    WINDOW_HEIGHT
from gui.language_learning_gui_content import LanguageLearningGuiContent


@dataclass
class LanguageLearningGui:
    gui_content: LanguageLearningGuiContent
    style: ttk.Style

    @staticmethod
    def initialize_gui() -> LanguageLearningGui:
        root = tk.Tk()
        root.title("French Learning Application")
        root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        style = set_application_style(root)
        language_learning_gui_content = LanguageLearningGuiContent.initialize_gui(root)
        return LanguageLearningGui(language_learning_gui_content, style)

    def run(self) -> None:
        self.gui_content.root.mainloop()
