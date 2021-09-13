#!/usr/bin/env python3
"""
Date   : 2021-09-12
Purpose: encrypt all numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        nargs='+',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def jump(orig):
    """encipher the plain text num"""

    encoding = {'0': '5', '5': '0', '1': '9', '2': '8', '3': '7',
                '4': '6', '6': '4', '7': '3', '8': '2', '9': '1'}
    cipher = encoding[orig]
    return cipher


# --------------------------------------------------
def delist(a_list):
    """turn a list into a string"""

    plain_text = ' '.join([str(elem) for elem in a_list])
    return plain_text


# --------------------------------------------------
def encode(plain_text):
    """iterate the string"""

    enciphered_text = ''
    for i in plain_text:
        if i in '1234567890':
            enciphered_text += jump(i)
        else:
            enciphered_text += i
    return enciphered_text


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    user_str = args.str
    plain_text = ''

    if isinstance(user_str, list):
        plain_text = delist(user_str)

    result = encode(plain_text)

    print(result)


# --------------------------------------------------
if __name__ == '__main__':
    main()
