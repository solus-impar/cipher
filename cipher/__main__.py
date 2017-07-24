"""cipher: A simple cipher."""
import argparse
import json
from os import path
import string
from cipher.encode import shift_text, substitute_text
from cipher.server import start_server
from cipher.tools import find_letter_freq, find_common_words


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
        required=False
    )
    parser.add_argument(
        '-k',
        '--key',
        nargs=2,
        help='Key used for decryption/encryption followed by type of ' \
             '[shift] or [sub]stitution.',
        required=False
    )
    parser.add_argument(
        '-o',
        '--output',
        help='Path to output file.',
        required=False
    )
    parser.add_argument(
        '-s',
        '--server',
        nargs=2,
        help='Startup web server on [host] [port]. Mutually exclusive with ' \
             'other options.',
        required=False
    )
    args = parser.parse_args()

    if args.server:
        if not (args.input or args.key or args.output):
            start_server(args.server[0], args.server[1])
        else:
            parser.error('`server` option mutually exclusive with other ' \
                         'options')

    if path.isfile(args.input):
        infile = open(args.input, 'r')
        text = infile.read()
        infile.close()
    else:
        text = args.input

    if args.key:
        if args.key[1] == 'shift':
            text = shift_text(text, args.key[0])
        elif args.key[1] == 'sub':
            text = substitute_text(text, args.key[0])
        else:
            parser.error('Key type not `shift` or `sub`')

    else:
        text = menu(text)

    if args.output:
        outfile = open(args.output, 'w')
        outfile.write(text)
        outfile.close()

    else:
        print(text)


def menu(text):
    """Command-line menu for `cipher`.

    Args:
        text (str): Input text.

    Returns:
        modified_text (str): Translated `text`.

    Raises:
        None
    """

    english = json.load(open('cipher/static/english.json'))
    key = string.ascii_uppercase
    clear = '\033[1;1H\033[0J'

    while True:
        print(clear, end='')
        modified_text = substitute_text(text, key)

        for i in [modified_text.split()[0:26], key, string.ascii_uppercase]:
            for j in i:
                print(j + ' ', end='')

            print('\n')

        text_letter_freq = find_letter_freq(modified_text)
        text_common_words = find_common_words(modified_text)

        print('Letter frequency      |  Common words')
        print('-' * 22 + '+' + '-' * 14)

        for eng_l, text_l, eng_w, text_w in zip(
                sorted(english['letter_frequency'].items(), key=lambda x: x[1],
                       reverse=True),
                sorted(text_letter_freq.items(), key=lambda x: x[1],
                       reverse=True),
                english['common_words'],
                text_common_words):
            print("{}: {:06.3f}, {}: {:06.3f}  |  {:>4}, {:4}".format(
                eng_l[0], eng_l[1], text_l[0], text_l[1], eng_w, text_w))

        choice = input('> ').upper()
        if choice in ['EXIT', 'QUIT']:
            print(clear, end='')
            return modified_text

        elif choice in list(string.ascii_uppercase):
            new = input("> {} -> ".format(choice)).lower()
            key = key.replace(choice, new)
            key = key.replace(new.upper(), choice)
            key = key.upper()


if __name__ == '__main__':
    cli()
