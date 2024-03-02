from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple, Iterable

from utils.string_utils import remove_non_alphabetic_characters


@dataclass
class ObscuredSentence:
    sentence: str
    obscured_french_word: str
    obscured_word_translation: str

    def all_tokens(self) -> Iterable[Tuple[str, bool]]:
        for token in self.sentence.split(' '):
            is_obscured_word = self.obscured_french_word == remove_non_alphabetic_characters(token)
            yield token, is_obscured_word

    @staticmethod
    def generate(french_word: str) -> ObscuredSentence:
        return ObscuredSentence(sentence='j\'ai vu un chien dans la rue',
                                obscured_french_word='chien',
                                obscured_word_translation='A dog')
