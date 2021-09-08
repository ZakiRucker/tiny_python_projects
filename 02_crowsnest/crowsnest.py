#!/usr/bin/env python3
"""
Author : Zaki Rucker <zakirucker@mac.com>
Date   : 2021-09-06
Purpose: learning to work with strings
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def get_article(user_input):
    """Determine which article to use"""

    vowels = ['a', 'e', 'i', 'o', 'u']

    if user_input[0] in vowels:
        solution = "an"
    else:
        solution = "a"

    return solution


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.word

    article = get_article(pos_arg.lower())

    print("Ahoy, Captain, " + article + " " + pos_arg +
          " off the larboard bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
