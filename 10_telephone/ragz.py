#!/usr/bin/env python3
"""
Author : Zaki Rucker <zakirucker@mac.com>
Date   : 2022-08-18
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='float',
                        type=float,
                        default='0.1')

    args = parser.parse_args()

    if args.mutations < 0:
        parser.error ('--mutations "{}" must be between 0 and 1'.format(args.mutations))

    if args.mutations > 1:
        parser.error ('--mutations "{}" must be between 0 and 1'.format(args.mutations))

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    num_mutations = round(len(args.text) * args.mutations)
    print('You said: "{}"\nI heard : "{}"'.format(args.text, args.text))

# --------------------------------------------------
if __name__ == '__main__':
    main()
