#!/usr/bin/env python3
"""
Author : Zaki Rucker <zakirucker@mac.com>
Date   : 2021-09-06
Purpose: Greet the user"""

import argparse

# --------------------------------------------------
def get_args():
    """parse the arguments"""
    parser = argparse.ArgumentParser(
        description='Greet the user',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', '--name',
                        metavar='name', default='World',
                        help='Name to greet')
    return parser.parse_args()


# -------------------------------------------------
def main():
    """where the magic happens"""
    args = get_args()

    print('Hello, ' + args.name + '!')

if __name__ == '__main__':
    main()
