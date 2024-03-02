from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from functools import cached_property
from tkinter import TOP, BOTTOM, W, X, BOTH, LEFT, CENTER, N

from gui.gui_styling_constants import TITLE_FONT, APPLICATION_VERSION, TINY_FONT, PALETTE_COLOR1
from language.obscured_sentence import ObscuredSentence
from language.text_to_speech import TextToSpeech
from utils.functional_utils import do_nothing
from utils.gui_utils import add_label, add_frame, add_button, ParentWidget, remove_all_frame_children, add_entry
from utils.string_utils import french_word_compare


@dataclass
class LanguageLearningGuiContent:
    root: tk
    obscured_sentence: ObscuredSentence
    sentence_frame: tk.Frame

    @staticmethod
    def add_title_label(parent: ParentWidget) -> None:
        add_label(parent=parent,
                  text="French Learning Application",
                  font=TITLE_FONT,
                  dock=TOP,
                  pad_y=20)

    @staticmethod
    def add_credits_label(parent: ParentWidget) -> None:
        add_label(parent=parent,
                  text=f'© Written by Yuval Alfassi, version {APPLICATION_VERSION}',
                  font=TINY_FONT,
                  dock=BOTTOM,
                  anchor=W,
                  pad_x=10,
                  pad_y=5)

    @staticmethod
    def add_content_frames(parent: ParentWidget) -> tk.Frame:
        content_frame = add_frame(parent=parent,
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
                   text='Submit Answer [Enter]',
                   command=self.submit_answer,
                   width=27,
                   background_color=PALETTE_COLOR1,
                   pad_x=5,
                   pad_y=5)
        self.root.bind('<Return>', lambda *_: self.submit_answer())
        add_button(parent=buttons_frame,
                   text='Hear Word in French [Ctrl-F]',
                   command=self.hear_word_in_french,
                   width=27,
                   pad_x=5,
                   pad_y=5)
        self.root.bind('<Control-f>', lambda *_: self.hear_word_in_french())
        add_button(parent=buttons_frame,
                   text='Show Answer [Ctrl-S]',
                   command=self.show_answer,
                   width=27,
                   pad_x=5,
                   pad_y=5)
        self.root.bind('<Control-s>', lambda *_: self.show_answer())
        add_button(parent=buttons_frame,
                   text='Next Sentence [Ctrl-N]',
                   command=do_nothing,
                   width=27,
                   pad_x=5,
                   pad_y=5)
        self.root.bind('<Control-n>', lambda *_: do_nothing())

    @cached_property
    def user_entered_word_string_variable(self) -> tk.StringVar:
        return tk.StringVar(value='')

    def set_obscured_sentence_gui(self) -> None:
        remove_all_frame_children(self.sentence_frame)
        self.user_entered_word_string_variable.set('')

        obscured_sentence_frame = add_frame(parent=self.sentence_frame,
                                            anchor=N,
                                            background_color=PALETTE_COLOR1,
                                            pad_x=20,
                                            pad_y=10)
        translation_frame = add_frame(parent=self.sentence_frame,
                                      anchor=N,
                                      background_color=PALETTE_COLOR1,
                                      pad_x=20,
                                      pad_y=10)
        add_label(parent=translation_frame,
                  text=f'<< {self.obscured_sentence.obscured_word_translation} >> ',
                  dock=LEFT,
                  background_color=PALETTE_COLOR1,
                  anchor=W,
                  pad_x=0)

        for token, is_obscured_word in self.obscured_sentence.all_tokens():
            if is_obscured_word:
                add_entry(parent=obscured_sentence_frame,
                          text_variable=self.user_entered_word_string_variable,
                          dock=LEFT,
                          anchor=W,
                          pad_x=2,
                          width=10)
            else:
                add_label(parent=obscured_sentence_frame,
                          text=f'{token}',
                          dock=LEFT,
                          background_color=PALETTE_COLOR1,
                          anchor=W,
                          pad_x=0)

    @staticmethod
    def initialize_gui(root: tk.Tk) -> LanguageLearningGuiContent:
        LanguageLearningGuiContent.add_title_label(root)
        LanguageLearningGuiContent.add_credits_label(root)
        sentence_frame, buttons_frame = LanguageLearningGuiContent.add_content_frames(root)
        obscured_sentence = ObscuredSentence.generate('word')  # TODO: fix this
        content = LanguageLearningGuiContent(root, obscured_sentence, sentence_frame)
        content.set_obscured_sentence_gui()
        content.add_buttons(buttons_frame)
        return content

    def submit_answer(self) -> None:
        incorrect_characters = french_word_compare(word1=self.obscured_sentence.obscured_french_word,
                                                   word2=self.user_entered_word_string_variable.get())
        if incorrect_characters == 0:
            TextToSpeech.speak('Vous avez raison')
        else:
            TextToSpeech.speak(f'{incorrect_characters} erreurs de caractères')

    def show_answer(self) -> None:
        self.user_entered_word_string_variable.set(self.obscured_sentence.obscured_french_word)
        self.hear_word_in_french()

    def hear_word_in_french(self) -> None:
        TextToSpeech.speak(self.obscured_sentence.obscured_french_word)
