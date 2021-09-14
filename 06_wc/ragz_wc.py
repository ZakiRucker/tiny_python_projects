#!/usr/bin/env python3
"""
Date   : 2021-09-13
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        help='Input file(s)',
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    num_files = 0
    tot_lines = 0
    tot_words = 0
    tot_bytes = 0
    for file_handle in args.file:
        num_files += 1
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in file_handle:
            num_lines += 1
            words = str.split(line)
            num_words += len(words)
            num_bytes += len(line)
        print('{:8} {:7} {:7} {:2}'.format(num_lines, num_words,
              num_bytes, file_handle.name))
        tot_lines += num_lines
        tot_words += num_words
        tot_bytes += num_bytes

    if num_files > 1:
        print('{:8} {:7} {:7} {:2}'.format(tot_lines, tot_words,
              tot_bytes, 'total'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
