import re
from enum import Enum
from itertools import zip_longest


def remove_non_alphabetic_characters(word):
    """
    >>> remove_non_alphabetic_characters('hello, world! Ça va ?')
    'helloworldÇava'
    """
    cleaned_word = re.sub(r'[\W\d_]', '', word, flags=re.UNICODE)
    return cleaned_word


def french_word_compare(word1: str, word2: str) -> int:
    num_incorrect = 0
    for ch1, ch2 in zip_longest(word1, word2):
        if ch1 != ch2:
            num_incorrect += 1
    return num_incorrect
