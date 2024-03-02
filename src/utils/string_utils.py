import re


def remove_non_alphabetic_characters(word):
    """
    >>> remove_non_alphabetic_characters('hello, world! Ça va ?')
    'helloworldÇava'
    """
    cleaned_word = re.sub(r'[\W\d_]', '', word, flags=re.UNICODE)
    return cleaned_word

