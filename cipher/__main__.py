"""cipher: A simple cipher."""
import argparse
from itertools import cycle
from os import path
import string


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
            if (j in string.ascii_uppercase and shift > 90) or \
               (j in string.ascii_lowercase and shift > 122):
                shift -= 26

            text[i] = chr(shift)

    text = ''.join(text)

    return text


def cli():
    """Command-line interface for `cipher`.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--input',
        help='Input string or path to input file.',
        required=True
    )
    parser.add_argument(
        '-k',
        '--key',
        help='Key used for decryption/encryption.',
        required=False
    )
    parser.add_argument(
        '-o',
        '--output',
        help='Path to output file.',
        required=False
    )
    args = parser.parse_args()

    if path.isfile(args.input):
        infile = open(args.input, 'r')
        text = infile.read()
        infile.close()

    else:
        text = args.input

    if args.key:
        text = shift_text(text, args.key)

    if args.output:
        outfile = open(args.output, 'w')
        outfile.write(text)
        outfile.close()

    else:
        print(text)


if __name__ == '__main__':
    cli()
