#!/usr/bin/env python3
"""
Date   : 2021-09-14
Purpose: Apples and bananas
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        nargs='+',
                        default=[sys.stdin],
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        choices="aeiou",
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    user_input = args.input
    vowel = args.vowel

    string = " ".join(str(i) for i in user_input)
    up_vowel = 'AEIOU'
    low_vowel = 'aeiou'
    output = ''

    if os.path.isfile(string):
        with open(string, 'rt', encoding='UTF-8') as file_h:
            string = file_h.read()
            file_h.close()

    for char in string:
        if char in low_vowel:
            output += vowel.lower()
        elif char in up_vowel:
            output += vowel.upper()
        else:
            output += char
    print(output)


# --------------------------------------------------
if __name__ == '__main__':
    main()
