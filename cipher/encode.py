"""cipher: Encrypt/Decrypt functions."""
from itertools import cycle
import string


def substitute_text(text, key):
    """Substitutes text's alphabet with key.

    Args:
        text (str): Input text.
        key (str): New alphabet for `text` to be mapped to.

    Returns:
        text (str): Output text.

    Raises:
        ValueError
    """

    if len(key) != 26 or not key.isalpha():
        raise ValueError('`key` not a complete alphabet.')

    return text.translate(str.maketrans(
        string.ascii_letters,
        key.lower() + key
    ))


def shift_text(text, key):
    """Shifts text as a Vigenère or Caesar cipher.

    Args:
        text (str): Input text.
        key (str): Vigenère cipher key or single letter for Caesar cipher key.

    Returns:
        text (str): Output text.

    Raises:
        None
    """

    key = cycle(key.upper())
    text = list(text)

    for i, j in enumerate(text):
        if j in string.ascii_letters:
            shift = ord(j) + ord(next(key)) - 65
            while (j in string.ascii_uppercase and shift > 90) or \
               (j in string.ascii_lowercase and shift > 122):
                shift -= 26

            text[i] = chr(shift)

    text = ''.join(text)

    return text
