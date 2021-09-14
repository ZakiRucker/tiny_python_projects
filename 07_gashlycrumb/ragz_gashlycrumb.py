#!/usr/bin/env python3
"""
Date   : 2021-09-13
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.file
    letter = args.letter

    pool = {}

    for line in file_arg:
        pool[line[0]] = line

    for char in letter:
        if char.upper() in pool.keys():
            print(pool[char.upper()], end='')
        else:
            print("I do not know \"{}\".".format(char))


# --------------------------------------------------
if __name__ == '__main__':
    main()
