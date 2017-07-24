"""cipher: Analysis functions."""
from collections import Counter
import re
import string


def find_letter_freq(text):
    """Finds frequency of letters in `text`.

    Args:
        text (str): Input text.

    Returns:
        `dict` of letters and relative frequency as percent.

    Raises:
        None
    """

    letters = re.sub('[' + string.punctuation + string.digits + \
                     string.whitespace + ']', '', text.upper())
    count = Counter(list(letters))

    return {i: count[i] / float(len(letters)) * 100.0 for i in count}


def find_common_words(text):
    """Finds common words in `text`.

    Args:
        text (str): Input text.

    Returns:
        Ordered `list` of the 26 most common words in `text`.

    Raises:
        None
    """

    words = re.sub('[' + string.punctuation + string.digits + ']',
                   '', text.upper())

    return [i[0] for i in Counter(words.split()).most_common(26)]


def find_locations(text, word):
    """Finds the frequent distances between occurrences of `word` in `text`.

    Args:
        text (str): Input text.
        word (str): Subject of analysis.

    Returns:
        `Counter` of the 26 most common distances between `word` in `text`.

    Raises:
        None
    """

    text = text.lower().replace(word.lower(), word.upper())
    text = re.sub('[' + string.punctuation + string.digits + \
                  string.whitespace + ']', '', text)
    locs = [i.start() for i in re.finditer(word.upper(), text)]
    diff = [j - i for i, j in zip(locs[:-1], locs[1:])]

    return Counter(diff).most_common(26)


def find_freq_pattern(text, length):
    """Find letter frequency patterns when `text` is broken into chunks of
        size `length`.

    Args:
        text (str): Input text.
        length (int): Size of `text` chunks.

    Returns:
        `list` of letter frequencies at indices of `text` chunks.

    Raises:
        None
    """

    text = re.sub('[' + string.punctuation + string.digits + \
                  string.whitespace + ']', '', text.upper())
    chunks = re.findall('.' * length, text)
    freqs = []
    for i in range(length):
        count = Counter([j[i] for j in chunks]).most_common(5)
        freqs.append(dict(count))

    return freqs
