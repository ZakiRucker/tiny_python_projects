#!/usr/bin/env python3
"""
Author : Ragz
Date   : 2021-09-12
Purpose: Howler (upper-case input)
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-case input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("positional", metavar="str",
                        help="A positional argument")

    parser.add_argument(
        "-o", "--outfile", metavar="str",
        help="Output filename ", default=""
    )

    return parser.parse_args()


# --------------------------------------------------
def file_monster(path):
    """open and read file"""

    with open(path) as file_h:
        text = file_h.read()
        file_h.close()
    return text


# --------------------------------------------------
def file_ghost(outfile, text):
    """open and write a file"""

    with open(outfile, "wt") as file_h_o:
        file_h_o.write(text)
        file_h_o.close()


# --------------------------------------------------
def transform(text):
    """capitalize the text"""

    result = text.upper()

    return result


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional

    if os.path.isfile(pos_arg):
        text = file_monster(pos_arg)
    else:
        text = pos_arg

    text = transform(text)

    if args.outfile:
        file_ghost(args.outfile, text)
    #        open(args.outfile, 'wt').write(text)
    else:
        print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
