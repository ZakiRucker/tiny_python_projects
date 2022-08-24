#!/usr/bin/env python3
"""
Author : parallels <parallels@fedora>
Date   : 2022-08-22
Purpose: Sing 99 bottles of beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='How many bottles',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--num "{args.number}" must be greater than 0')

    return parser.parse_args()

# --------------------------------------------------
def verse(bottle):
    """Sing the verse"""

    next_bottle = bottle - 1
    s1 = '' if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    num_next = 'No more' if next_bottle == 0 else next_bottle
    return '\n'.join([f'{bottle} bottle{s1} of beer on the wall,',
          f'{bottle} bottle{s1} of beer,',
          f'Take one down, pass it around,',
          f'{num_next} bottle{s2} of beer on the wall!',])


# --------------------------------------------------
def pu_verse():
    """Sing the penultimate verse"""

    print('2 bottles of beer on the wall,\n'
          '2 bottles of beer,\n'
          'Take one down, pass it around,\n'
          '1 bottle of beer on the wall!\n')


# --------------------------------------------------
def last_verse():
    """Sing the last verse"""

    print('1 bottle of beer on the wall,\n'
          '1 bottle of beer,\n'
          'Take one down, pass it around,\n'
          'No more bottles of beer on the wall!')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num = args.number
    num_bottles = list(range(num, 0, -1))
    print('\n\n'.join(map(verse, range(num, 0, -1))))


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
